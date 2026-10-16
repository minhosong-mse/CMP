; CMP / 3D-Sun-SADDLE-V1 / FIVE SWB PARAMETERS, NOMINAL M1 MESH QC
; Historical parent F1 is NOT modified.
; 2026-10-16. Full 3-D SDE candidate: contacts + doping + selectable mesh.
; RfilletFactor is controlled ONLY in the LOWER Si saddle.
; SWB nominal/split inputs (case-sensitive, numeric):
;   ARgate         = 6.0
;   DBCAT_nm       = 36
;   JunctionRatio  = 0.4
;   Wfin_nm        = 17
;   RfilletFactor  = 1.0   <-- NOMINAL, NO SPLIT until QC passes
; SWB 1 nominal point. JunctionRatio drives S/D Gaussian depth.
; Intent: reproduce Sun et al. Micromachines 13(9), 1476 Fig. 2e qualitative geometry.
; Non-paper reconstruction: Hsaddle=0.048 um, Boolean oxide envelope.

; CMP 3D-Sun-SADDLE-V1 FULL SDE -- PROVISIONAL
; Verified preview geometry; new contacts/doping/mesh require Sentaurus QC.
; Existing historical F1_nominal.cmd is preserved unchanged.
; Parent dimensions are inherited; check Fig.1/2 cross-sections against original.
(sde:clear)
(sde:set-process-up-direction "+z")
(sdegeo:set-default-boolean "ABA")
(define Lgate 0.020)
(define ARgate @ARgate@)
(define Drecess (* ARgate Lgate))
(define DBCAT_nm @DBCAT_nm@)
(define DBCAT (* 0.001 DBCAT_nm))   ; nm -> um
(define Tox 0.005)
(define Wfin_nm @Wfin_nm@)
(define Wfin (* 0.001 Wfin_nm))    ; nm -> um
(define Hfin 0.048)
(define Hsaddle 0.048)
(define JunctionRatio @JunctionRatio@)
(define Djunction (* JunctionRatio Drecess)) ; S/D Gaussian junction target
(define RfilletFactor @RfilletFactor@)
(define Xhalf 0.060)
(define Yhalf 0.030)
(define Zbody 0.180)
(define Nbody 1.0e17)
(define NSD 1.0e20)
(define GaussFactor 0.0) ; retain executed F1 reconstruction assumption
(define Rgate (* 0.5 Lgate))
(define Router (+ Rgate Tox))
(define FinHalf (* 0.5 Wfin))
(define Rfin FinHalf)
(define ZgateTop (- DBCAT))
(define ZgateCenter (- Router Drecess))
(define ZfinBottom (- Hfin))
(define ZfinCapCtr (- Rfin))

; Parameter audit: printed values are the SWB-preprocessed case identity.
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
  (position (- Xhalf) (- Rfin) ZfinCapCtr)
  (position Xhalf Rfin ZfinBottom)
  "Silicon" "R.SiFin"))
(define SIFIN_CAP (sdegeo:create-cylinder
  (position (- Xhalf) 0 ZfinCapCtr)
  (position Xhalf 0 ZfinCapCtr)
  Rfin "Silicon" "R.SiFin.Cap"))
(sdegeo:bool-unite (list SIFIN_STEM SIFIN_CAP))

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


;===============================================================================
; SADDLE-V1 GEOMETRY PATCH -- VISUALLY VALIDATED FILLET-ONLY / NO ELECTRICAL VALIDATION
; Added after historical gate/nitride construction, BEFORE contacts and doping.
;
; x = source-drain; y = across-fin / word-line; z = 0 at wafer top.
; Si core crest: ZridgeTop = -Drecess + Hsaddle.
; Raised core is continuous along x; gate oxide envelopes it only inside trench.
;
; This is a reconstruction hypothesis for Fig. 1(b,c), NOT published CAD.
; Wfin, RfilletFactor and Hsaddle are defined above for explicit QA.
;===============================================================================

(define ZridgeTop (+ (- Drecess) Hsaddle))
(define Rridge (* 0.5 Wfin RfilletFactor))
(define ZridgeBase (- (- Drecess) 0.002))  ; 2 nm positive-Si overlap into substrate

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

; Outer rounded dielectric shape: conformal rounded cap approximation.
; This is an intentionally explicit reconstruction, not a process-grown oxide.
(define OX_SADDLE_OUTER
  (cmp:rounded-ridge "R.SaddleDielectricOuter" "Oxide"
    (- Router) Router
    (+ FinHalf Tox)
    (- Drecess) (+ ZridgeTop Tox)
    (+ Rridge Tox)))

; The physical silicon saddle core replaces only the inner portion of oxide/W.
; It connects to the existing source/drain silicon and buried Si substrate.
(define SI_SADDLE
  (cmp:rounded-ridge "R.SiSaddle" "Silicon"
    (- Xhalf) Xhalf
    FinHalf
    ZridgeBase ZridgeTop
    Rridge))

(display "SADDLE geometry QA: Si crest z = ") (display ZridgeTop) (newline)
(display "SADDLE geometry QA: recess floor z = ") (display (- Drecess)) (newline)
(display "SADDLE geometry QA: fin radius = ") (display Rridge) (newline)
(display "SADDLE QA: fillet factor = ") (display RfilletFactor) (newline)
(display "SADDLE QA: Si corner radius [nm] = ") (display (* 1000 Rridge)) (newline)
(display "SADDLE QA: Si flat-crest width [nm] = ") (display (* 1000 (- Wfin (* 2 Rridge)))) (newline)
(display "SADDLE QA: upper source/drain fin cap is unchanged across splits\n")
(display "SADDLE geometry QA: gate-surrounding Si/Oxide intersection at (0,0,zcrest)\n")
(find-body-id (position 0.0 0.0 (- ZridgeTop 0.001)))
(display "SADDLE QA: probe near y=+22 nm; verify W region in SVisual before claiming PASS\n")
(find-body-id (position 0.0 0.022 (* 0.5 (+ ZgateTop ZgateCenter))))
(sdegeo:check-overlap (get-body-list))
;===============================================================================


;===============================================================================
; FULL-SDE CONTINUATION / NOT PART OF THE VISUALIZED GEOMETRY-ONLY CHECK
; Keep historical F1 contacts/doping conventions but update W body probe.
;===============================================================================

; Contact probes are deliberately on EXTERIOR Si faces and a W interior point.
; The gate is a body-contact with "remove" as in historical executed F1.
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
; Snapshot the real W body BEFORE removing it. Geometry visualization ONLY.
; The subsequent SDevice mesh is unaffected by this additional save operation.
(sde:save-model "n@node@_W_VIS")

(sdegeo:set-contact (find-body-id P.GateBody) "gate" "remove")

; Body doping applies to ALL resulting Silicon pieces (including saddle),
; preventing silently undoped Si if 3D Boolean creates new region names.
(sdedr:define-constant-profile
  "Dop.Body" "BoronActiveConcentration" Nbody)
(sdedr:define-constant-profile-material
  "Place.Body.Silicon" "Dop.Body" "Silicon")

; Same 3-D Rectangle z=0 analytic implantation approach as executed F1.
; For all geometry splits, x source/drain windows track Router.
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

; Nominal junction depth is a doping profile TARGET; verify net-doping
; zero-crossing at Source/Drain with an exported 3D TDR after mesh.
(define Zjunction (- Djunction))
(define ZjuncTop (+ Zjunction 0.012))
(define ZjuncBottom (- Zjunction 0.012))

(display "DOPING QA: B[cm^-3]=") (display Nbody) (newline)
(display "DOPING QA: As peak[cm^-3]=") (display NSD) (newline)
(display "DOPING QA: junction z[um]=") (display Zjunction) (newline)
(display "DOPING QA: lateral factor=") (display GaussFactor) (newline)

; Mesh below is M1 candidate; neither numerical mesh convergence nor paper-DC reproduction is established.


;===============================================================================
; M1 MESH: base FAST + local saddle crest/refinement; unexecuted candidate.
; Control A/B versus previous executed FAST. Same nominal geometry/doping.
;===============================================================================
(define MeshPreset 11)

; Bulk and isolation: loose. Small elements confined to the gate/Si areas.
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

; Active Si fin and shoulder: width and crest follow Wfin, Hfin, Drecess.
(sdedr:define-refeval-window "Fast.Win.Active" "Cuboid"
  (position (- Xhalf) (- (+ FinHalf 0.009)) (- (+ Drecess 0.016)))
  (position Xhalf (+ FinHalf 0.009) 0.0))
(sdedr:define-refinement-size "Fast.Def.Active"
  0.0065 0.0040 0.0055
  0.0018 0.0012 0.0012)
(sdedr:define-refinement-placement "Fast.Place.Active"
  "Fast.Def.Active" "Fast.Win.Active")

; Core Si/Oxide interface: ~1.0 nm first interface spacing vs F1 0.3 nm;
; check that 5 nm oxide retains enough layers for DC feasibility.
(sdedr:define-refeval-window "Fast.Win.Gate" "Cuboid"
  (position (- (+ Router 0.007)) (- (+ FinHalf Tox 0.007)) (- (+ Drecess 0.007)))
  (position (+ Router 0.007) (+ FinHalf Tox 0.007) (+ ZgateTop 0.007)))
(sdedr:define-refinement-size "Fast.Def.Gate"
  0.0035 0.0025 0.0035
  0.0009 0.00075 0.0008)
(sdedr:define-refinement-function "Fast.Def.Gate"
  "MaxLenInt" "Silicon" "Oxide" 0.00085 1.5 "DoubleSide")
(sdedr:define-refinement-placement "Fast.Place.Gate"
  "Fast.Def.Gate" "Fast.Win.Gate")

; Junction strips, moderate compared to historical F1's 0.25 nm z minimum.
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
(sdedr:define-refinement-placement "Fast.Place.JS"
  "Fast.Def.Junction" "Fast.Win.JS")
(sdedr:define-refinement-placement "Fast.Place.JD"
  "Fast.Def.Junction" "Fast.Win.JD")


; M1 ADDITION: 3D Si-saddle crest refinement along the entire S/D direction.
; Previous n8 high-Vd Newton hotspot: x=+0.045 um,
; y= +/-0.004216 um, z=-0.073125 um, outside prior Fast.Win.Gate.
; This refines a LOCAL crest slab without altering physical geometry.
; At nominal: x=[-0.060,+0.060], y=[-0.0175,+0.0175],
; z=[ZridgeTop-0.020, ZridgeTop+0.006]=[-0.092,-0.066] um.
(sdedr:define-refeval-window "M1.Win.SaddleCrest" "Cuboid"
  (position (- Xhalf) (- (+ FinHalf Tox 0.004)) (- ZridgeTop 0.020))
  (position Xhalf (+ FinHalf Tox 0.004) (+ ZridgeTop 0.006)))
(sdedr:define-refinement-size "M1.Def.SaddleCrest"
  0.0045 0.0020 0.0025
  0.0012 0.0007 0.0008)
(sdedr:define-refinement-function "M1.Def.SaddleCrest"
  "MaxLenInt" "Silicon" "Oxide" 0.0008 1.5 "DoubleSide")
(sdedr:define-refinement-placement "M1.Place.SaddleCrest"
  "M1.Def.SaddleCrest" "M1.Win.SaddleCrest")

;===============================================================================
; GEOMETRY / CONTACTS / PROFILE PRE-MESH REPORT
;===============================================================================
(display "\n==== 3D SADDLE FULL-SDE PRE-MESH QA ====\n")
(display "MeshPreset = ") (display MeshPreset) (newline)
(display "All geometry parameters above are case-specific.\n")
(display "Expected contact names: source,drain,gate,substrate\n")
(display "Overlap query below is diagnostic and does not alone validate topology.\n")
(sdegeo:check-overlap (get-body-list))

; Save model BEFORE mesh for geometry/contact inspection.
(sde:save-model "n@node@")

; Standalone WORKBENCH mesh, matched to existing executed 3D F1 convention.
(sde:build-mesh "snmesh" "" "n@node@")
(display "3D SADDLE: n@node@_bnd.tdr / n@node@_msh.tdr expected.\n")
(display "STATUS: mesh/device validation not yet executed on user server.\n")
