(sde:clear)
(sde:set-process-up-direction "+z")
(sdegeo:set-default-boolean "ABA")
(define Lgate 0.020)
(define ARgate @ARgate@)
(define Drecess (* ARgate Lgate))
(define DBCAT_nm @DBCAT_nm@)
(define DBCAT (* 0.001 DBCAT_nm))
(define Tox 0.005)
(define Wfin_nm @Wfin_nm@)
(define Wfin (* 0.001 Wfin_nm))
(define Hfin 0.048)
(define Hsaddle 0.048)
(define JunctionRatio @JunctionRatio@)
(define Djunction (* JunctionRatio Drecess))
(define RfilletFactor @RfilletFactor@)
(define Xhalf 0.060)
(define Yhalf 0.030)
(define Zbody 0.180)
(define Nbody 1.0e17)
(define NSD 1.0e20)
(define GaussFactor 0.0)
(define MeshCase 0)
(define CadSeamCase 3)
(define CurveGrid @CurveGrid@)
(if (and (>= CurveGrid 0) (<= CurveGrid 2))
    (display "CurveGrid valid 0..2\n")
    (error "Invalid CurveGrid; choose 0 1 or 2"))
(display "CMP GATE-CURVE GRID = ") (display CurveGrid) (newline)
(if (and (>= CadSeamCase 0) (<= CadSeamCase 3))
    (display "CAD-SEAM CASE valid 0..3\n")
    (error "CAD-SEAM CASE invalid; choose 0..3"))
(display "CMP CAD-SEAM A/B: case = ") (display CadSeamCase) (newline)
(display "CMP MESH-ONLY SWEEP: MeshCase = ") (display MeshCase) (newline)
(if (and (>= MeshCase 0) (<= MeshCase 6))
    (display "MeshCase valid (0..6)\n")
    (error "Invalid MeshCase; use integer 0..6"))
(define Rgate (* 0.5 Lgate))
(define Router (+ Rgate Tox))
(define FinHalf (* 0.5 Wfin))
(define Rfin FinHalf)
(define ZgateTop (- DBCAT))
(define ZgateCenter (- Router Drecess))
(define ZfinBottom (- Hfin))
(display "\n=== CMP SADDLE V1 FIVE-PARAMETER CASE ===\n")
(display "ARgate [Drecess/Lgate] = ") (display ARgate) (newline)
(display "Drecess [um] = ") (display Drecess) (newline)
(display "DBCAT_nm [nm] = ") (display DBCAT_nm) (newline)
(display "JunctionRatio [unitless] = ") (display JunctionRatio) (newline)
(display "Djunction [um; Gaussian doping] = ") (display Djunction) (newline)
(display "Wfin_nm [nm] = ") (display Wfin_nm) (newline)
(display "RfilletFactor [unitless] = ") (display RfilletFactor) (newline)
(display "NOTE: full SDE build; JunctionRatio controls source/drain Gaussian depth.\n")
(display "=== END PARAMETER CASE ===\n")
(define ISO (sdegeo:create-cuboid
  (position (- Xhalf) (- Yhalf) 0)
  (position Xhalf Yhalf ZfinBottom)
  "Oxide" "R.Isolation"))
(define SISUB (sdegeo:create-cuboid
  (position (- Xhalf) (- Yhalf) ZfinBottom)
  (position Xhalf Yhalf (- Zbody))
  "Silicon" "R.SiSubstrate"))
(define SIFIN_STEM (sdegeo:create-cuboid
  (position (- Xhalf) (- Rfin) 0.0)
  (position Xhalf Rfin ZfinBottom)
  "Silicon" "R.SiFin"))
(define GOX_BOX (sdegeo:create-cuboid
  (position (- Router) (- Yhalf) 0)
  (position Router Yhalf ZgateCenter)
  "Oxide" "R.GateOxide"))
(define GOX_CYL (sdegeo:create-cylinder
  (position 0 (- Yhalf) ZgateCenter)
  (position 0 Yhalf ZgateCenter)
  Router "Oxide" "R.GateOxide.Bottom"))
(sdegeo:bool-unite (list GOX_BOX GOX_CYL))
(define WG_BOX (sdegeo:create-cuboid
  (position (- Rgate) (- Yhalf) ZgateTop)
  (position Rgate Yhalf ZgateCenter)
  "Tungsten" "R.WGate"))
(define WG_CYL (sdegeo:create-cylinder
  (position 0 (- Yhalf) ZgateCenter)
  (position 0 Yhalf ZgateCenter)
  Rgate "Tungsten" "R.WGate.Bottom"))
(sdegeo:bool-unite (list WG_BOX WG_CYL))
(define NIT (sdegeo:create-cuboid
  (position (- Rgate) (- Yhalf) 0)
  (position Rgate Yhalf ZgateTop)
  "Nitride" "R.Nitride"))
(define ZridgeTop (+ (- Drecess) Hsaddle))
(define Rridge (* 0.5 Wfin RfilletFactor))
(define ZridgeBase (- (- Drecess) 0.002))
(define (cmp:rounded-ridge name mat xa xb halfwidth zbase ztop rad)
  (let* ((flat (- halfwidth rad))
         (zc (- ztop rad))
         (stem (sdegeo:create-cuboid
                 (position xa (- halfwidth) zbase)
                 (position xb halfwidth zc)
                 mat name))
         (capL (sdegeo:create-cylinder
                 (position xa (- flat) zc)
                 (position xb (- flat) zc)
                 rad mat (string-append name ".CapL"))))
    (if (< flat 0.0000001)
        (sdegeo:bool-unite (list stem capL))
        (let* ((capR (sdegeo:create-cylinder
                       (position xa flat zc)
                       (position xb flat zc)
                       rad mat (string-append name ".CapR")))
               (capFlat (sdegeo:create-cuboid
                          (position xa (- flat) zc)
                          (position xb flat ztop)
                          mat (string-append name ".CapFlat"))))
          (sdegeo:bool-unite (list stem capL capR capFlat))))))
(define OX_SADDLE_OUTER
  (cmp:rounded-ridge "R.SaddleDielectricOuter" "Oxide"
    (- Router) Router
    (+ FinHalf Tox)
    (- Drecess) (+ ZridgeTop Tox)
    (+ Rridge Tox)))
(define SI_SADDLE
  (cmp:rounded-ridge "R.SiSaddle" "Silicon"
    (- Xhalf) Xhalf
    FinHalf
    ZridgeBase ZridgeTop
    Rridge))
(define (cmp:require-one-body pos label)
  (let ((hits (find-body-id pos)))
    (display "CAD-SEAM probe ") (display label)
    (display " count=") (display (length hits)) (newline)
    (if (= (length hits) 1)
        (car hits)
        (error "CAD-SEAM probe did not find EXACTLY one body"))))
(display "CAD-SEAM before unions body count = ")
(display (length (get-body-list))) (newline)
(if (or (= CadSeamCase 1) (= CadSeamCase 3))
    (begin
      (display "CAD-SEAM: Unite Silicon substrate + saddle (first keeps R.SiSubstrate)\n")
      (let* ((cad-si-sub (cmp:require-one-body
                (position 0.040 0.020 -0.090) "R.SiSubstrate"))
             (cad-si-saddle (cmp:require-one-body
                (position 0.040 0.000 -0.090) "R.SiSaddle")))
        (if (sdegeo:bool-unite (list cad-si-sub cad-si-saddle))
            (display "CAD-SEAM Silicon unite returned success\n")
            (error "CAD-SEAM Silicon bool-unite returned false"))))
    (display "CAD-SEAM: Silicon seam unchanged\n"))
(if (or (= CadSeamCase 2) (= CadSeamCase 3))
    (begin
      (display "CAD-SEAM: Unite GateOxide + SaddleDielectricOuter (first keeps R.GateOxide)\n")
      (let* ((cad-gox (cmp:require-one-body
                (position 0.013 0.018 -0.085) "R.GateOxide"))
             (cad-outer-ox (cmp:require-one-body
                (position 0.011 0.010 -0.100) "R.SaddleDielectricOuter")))
        (if (sdegeo:bool-unite (list cad-gox cad-outer-ox))
            (display "CAD-SEAM Oxide unite returned success\n")
            (error "CAD-SEAM Oxide bool-unite returned false"))))
    (display "CAD-SEAM: Oxide seam unchanged\n"))
(display "CAD-SEAM after unions body count = ")
(display (length (get-body-list))) (newline)
(display "CAD-SEAM after union: overlap QA (empty report is not sufficient for topology acceptance)\n")
(sdegeo:check-overlap (get-body-list))
(display "SADDLE geometry QA: Si crest z = ") (display ZridgeTop) (newline)
(display "SADDLE geometry QA: recess floor z = ") (display (- Drecess)) (newline)
(display "SADDLE geometry QA: fin radius = ") (display Rridge) (newline)
(display "SADDLE QA: fillet factor = ") (display RfilletFactor) (newline)
(display "SADDLE QA: Si corner radius [nm] = ") (display (* 1000 Rridge)) (newline)
(display "SADDLE QA: Si flat-crest width [nm] = ") (display (* 1000 (- Wfin (* 2 Rridge)))) (newline)
(display "SADDLE QA: upper S/D Si = FLAT TOP (NO SiFin.Cap), W [nm] = ")
(display Wfin_nm)
(display "; z top [um] = 0; z bottom [um] = ")
(display ZfinBottom)
(newline)
(display "SADDLE geometry QA: gate-surrounding Si/Oxide intersection at (0,0,zcrest)\n")
(find-body-id (position 0.0 0.0 (- ZridgeTop 0.001)))
(display "SADDLE QA: probe near y=+22 nm; verify W region in SVisual before claiming PASS\n")
(find-body-id (position 0.0 0.022 (* 0.5 (+ ZgateTop ZgateCenter))))
(sdegeo:check-overlap (get-body-list))
(define P.Source (position (- Xhalf) 0.0 -0.025))
(define P.Drain (position Xhalf 0.0 -0.025))
(define P.Substrate (position 0.0 0.0 (- Zbody)))
(define P.GateBody (position 0.0 0.022 (* 0.5 (+ ZgateTop ZgateCenter))))
(display "CONTACT QA - source face ID: ") (display (find-face-id P.Source)) (newline)
(display "CONTACT QA - drain face ID: ") (display (find-face-id P.Drain)) (newline)
(display "CONTACT QA - substrate face ID: ") (display (find-face-id P.Substrate)) (newline)
(display "CONTACT QA - gate W body ID: ") (display (find-body-id P.GateBody)) (newline)
(sdegeo:define-contact-set "source" 4 (color:rgb 1 0 0) "##")
(sdegeo:define-contact-set "drain" 4 (color:rgb 0 0 1) "##")
(sdegeo:define-contact-set "gate" 4 (color:rgb 1 0 1) "##")
(sdegeo:define-contact-set "substrate" 4 (color:rgb 0 1 0) "##")
(sdegeo:set-contact (find-face-id P.Source) "source")
(sdegeo:set-contact (find-face-id P.Drain) "drain")
(sdegeo:set-contact (find-face-id P.Substrate) "substrate")
(sde:save-model "n1_W_VIS")
(sdegeo:set-contact (find-body-id P.GateBody) "gate" "remove")
(sdedr:define-constant-profile
  "Dop.Body" "BoronActiveConcentration" Nbody)
(sdedr:define-constant-profile-material
  "Place.Body.Silicon" "Dop.Body" "Silicon")
(sdedr:define-refeval-window "Base.Source" "Rectangle"
  (position (- Xhalf) (- Rfin) 0.0)
  (position (- Router) Rfin 0.0))
(sdedr:define-refeval-window "Base.Drain" "Rectangle"
  (position Router (- Rfin) 0.0)
  (position Xhalf Rfin 0.0))
(sdedr:define-gaussian-profile
  "Dop.Source.Gauss" "ArsenicActiveConcentration"
  "PeakPos" 0.0 "PeakVal" NSD
  "ValueAtDepth" Nbody "Depth" Djunction
  "Gauss" "Factor" GaussFactor)
(sdedr:define-gaussian-profile
  "Dop.Drain.Gauss" "ArsenicActiveConcentration"
  "PeakPos" 0.0 "PeakVal" NSD
  "ValueAtDepth" Nbody "Depth" Djunction
  "Gauss" "Factor" GaussFactor)
(sdedr:define-analytical-profile-placement
  "Place.Source.Gauss" "Dop.Source.Gauss" "Base.Source"
  "Both" "NoReplace" "Eval")
(sdedr:define-analytical-profile-placement
  "Place.Drain.Gauss" "Dop.Drain.Gauss" "Base.Drain"
  "Both" "NoReplace" "Eval")
(define Zjunction (- Djunction))
(define ZjuncTop (+ Zjunction 0.012))
(define ZjuncBottom (- Zjunction 0.012))
(display "DOPING QA: B[cm^-3]=") (display Nbody) (newline)
(display "DOPING QA: As peak[cm^-3]=") (display NSD) (newline)
(display "DOPING QA: junction z[um]=") (display Zjunction) (newline)
(display "DOPING QA: lateral factor=") (display GaussFactor) (newline)
(define MeshPreset 11)
(sdedr:define-refeval-window "Fast.Win.Global" "Cuboid"
  (position (- Xhalf) (- Yhalf) (- Zbody))
  (position Xhalf Yhalf 0.0))
(sdedr:define-refinement-size "Fast.Def.Global"
  0.022 0.016 0.023
  0.004 0.004 0.004)
(sdedr:define-refinement-function "Fast.Def.Global"
  "DopingConcentration" "MaxTransDiff" 1.25)
(sdedr:define-refinement-placement "Fast.Place.Global"
  "Fast.Def.Global" "Fast.Win.Global")
(sdedr:define-refeval-window "Fast.Win.Active" "Cuboid"
  (position (- Xhalf) (- (+ FinHalf 0.009)) (- (+ Drecess 0.016)))
  (position Xhalf (+ FinHalf 0.009) 0.0))
(sdedr:define-refinement-size "Fast.Def.Active"
  0.0065 0.0040 0.0055
  0.0018 0.0012 0.0012)
(if (or (= MeshCase 3) (= MeshCase 6))
    (display "SKIP: Active refinement placement\n")
    (sdedr:define-refinement-placement "Fast.Place.Active"
      "Fast.Def.Active" "Fast.Win.Active"))
(sdedr:define-refeval-window "Fast.Win.Gate" "Cuboid"
  (position (- (+ Router 0.007)) (- (+ FinHalf Tox 0.007)) (- (+ Drecess 0.007)))
  (position (+ Router 0.007) (+ FinHalf Tox 0.007) (+ ZgateTop 0.007)))
(if (= MeshCase 4)
    (sdedr:define-refinement-size "Fast.Def.Gate"
      0.0035 0.0025 0.0035
      0.0018 0.0015 0.0016)
    (sdedr:define-refinement-size "Fast.Def.Gate"
      0.0035 0.0025 0.0035
      0.0009 0.00075 0.0008))
(display "M2B GATE MaxLenInt disabled; geometry/contact/doping unchanged.\n")
(if (or (= MeshCase 2) (= MeshCase 6))
    (display "SKIP: Gate refinement placement\n")
    (sdedr:define-refinement-placement "Fast.Place.Gate"
      "Fast.Def.Gate" "Fast.Win.Gate"))
(sdedr:define-refeval-window "Fast.Win.JS" "Cuboid"
  (position (- Xhalf) (- (+ FinHalf 0.005)) ZjuncBottom)
  (position (- Router) (+ FinHalf 0.005) ZjuncTop))
(sdedr:define-refeval-window "Fast.Win.JD" "Cuboid"
  (position Router (- (+ FinHalf 0.005)) ZjuncBottom)
  (position Xhalf (+ FinHalf 0.005) ZjuncTop))
(sdedr:define-refinement-size "Fast.Def.Junction"
  0.004 0.004 0.003
  0.0012 0.0012 0.0010)
(sdedr:define-refinement-function "Fast.Def.Junction"
  "DopingConcentration" "MaxTransDiff" 0.75)
(if (= MeshCase 6)
    (display "SKIP: Junction placements, coarse-only control\n")
    (begin
      (sdedr:define-refinement-placement "Fast.Place.JS"
        "Fast.Def.Junction" "Fast.Win.JS")
      (sdedr:define-refinement-placement "Fast.Place.JD"
        "Fast.Def.Junction" "Fast.Win.JD")))
(sdedr:define-refeval-window "M1.Win.SaddleCrest" "Cuboid"
  (position (- Xhalf) (- (+ FinHalf Tox 0.004)) (- ZridgeTop 0.020))
  (position Xhalf (+ FinHalf Tox 0.004) (+ ZridgeTop 0.006)))
(sdedr:define-refinement-size "M1.Def.SaddleCrest"
  0.0045 0.0020 0.0025
  0.0012 0.0007 0.0008)
(define M2A.GateRefX (+ Router 0.007))
(sdedr:define-refeval-window "M2A.Win.CrestSourceOuter" "Cuboid"
  (position (- Xhalf) (- (+ FinHalf Tox 0.004)) (- ZridgeTop 0.020))
  (position (- M2A.GateRefX) (+ FinHalf Tox 0.004) (+ ZridgeTop 0.006)))
(sdedr:define-refeval-window "M2A.Win.CrestDrainOuter" "Cuboid"
  (position M2A.GateRefX (- (+ FinHalf Tox 0.004)) (- ZridgeTop 0.020))
  (position Xhalf (+ FinHalf Tox 0.004) (+ ZridgeTop 0.006)))
(if (= MeshCase 5)
    (sdedr:define-refinement-size "M2A.Def.OuterCrestInterface"
      0.0045 0.0020 0.0025
      0.0024 0.0014 0.0016)
    (sdedr:define-refinement-size "M2A.Def.OuterCrestInterface"
      0.0045 0.0020 0.0025
      0.0012 0.0007 0.0008))
(if (or (= MeshCase 1) (= MeshCase 6))
    (display "SKIP: both OuterCrest refinement placements\n")
    (begin
      (sdedr:define-refinement-placement "M2A.Place.CrestSourceOuter"
        "M2A.Def.OuterCrestInterface" "M2A.Win.CrestSourceOuter")
      (sdedr:define-refinement-placement "M2A.Place.CrestDrainOuter"
        "M2A.Def.OuterCrestInterface" "M2A.Win.CrestDrainOuter")))
(display "M2A geometry unchanged; mesh-only gate-interface de-duplication; gate-ref x=+/-")
(display M2A.GateRefX) (newline)
(display "M2A status: candidate, run SDE and audit min edge & R/H before SDevice DC.\n")
(if (= CurveGrid 0)
    (display "GATE-CURVE: baseline n44 placements, no extra local window\n")
    (begin
      (sdedr:define-refeval-window "QC.Win.GateCurve" "Cuboid"
        (position (- (+ Router 0.005)) (- (+ FinHalf Tox 0.004)) (- ZridgeTop 0.022))
        (position (+ Router 0.005) (+ FinHalf Tox 0.004) (+ ZridgeTop 0.009)))
      (if (= CurveGrid 1)
          (sdedr:define-refinement-size "QC.Def.GateCurve"
            0.0022 0.0018 0.0022
            0.0007 0.0006 0.0007)
          (sdedr:define-refinement-size "QC.Def.GateCurve"
            0.0015 0.0012 0.0015
            0.0005 0.0004 0.0005))
      (sdedr:define-refinement-placement "QC.Place.GateCurve"
        "QC.Def.GateCurve" "QC.Win.GateCurve")
      (display "GATE-CURVE: local size placement enabled, CurveGrid = ")
      (display CurveGrid) (newline)))
(display "\n==== 3D SADDLE FULL-SDE PRE-MESH QA ====\n")
(display "MeshPreset = ") (display MeshPreset) (newline)
(display "All geometry parameters above are case-specific.\n")
(display "Expected contact names: source,drain,gate,substrate\n")
(display "Overlap query below is diagnostic and does not alone validate topology.\n")
(sdegeo:check-overlap (get-body-list))
(sde:save-model "n1")
(sde:build-mesh "snmesh" "" "n@node@")
(display "3D SADDLE: n1_bnd.tdr / n1_msh.tdr expected.\n")
(display "STATUS: mesh/device validation not yet executed on user server.\n")
(display "M2D diagnostic: Gate and crest MaxLenInt OFF, outer crest size placement retained; geometry unchanged. SDE ONLY.\n")
(display "FINAL DIAGNOSTIC MeshCase = ") (display MeshCase) (newline)
(display "FINAL DIAGNOSTIC CadSeamCase = ") (display CadSeamCase) (newline)
(display "FINAL GATE-CURVE DIAGNOSTIC CurveGrid = ") (display CurveGrid) (newline)
