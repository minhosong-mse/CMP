(sde:clear)
(sdegeo:set-default-boolean "ABA")

(define GateCouplingScale 2.300)
(define GateDepthBoost    0.025)

(define MEBDepth  @MEBDepth@)
(define MeshLevel 2)

(define LsdSetback 0.015)
(define GaussFactor 0.0)
(define SDPeakPos   0.0)

(define Lgate 0.020)

(define DrecessPhysical 0.120)
(define Drecess (+ DrecessPhysical GateDepthBoost))

(define ToxPhysical 0.005)
(define Tox (/ ToxPhysical GateCouplingScale))

(define GateTop MEBDepth)

(define Jdepth 0.048)
(define Nbody   1.0e17)
(define NSD     1.0e20)

(define Xdepth 0.300)
(define Ywidth 0.480)

(define Ymid (/ Ywidth 2.0))

(define YgL (- Ymid (/ Lgate 2.0)))
(define YgR (+ Ymid (/ Lgate 2.0)))

(define Router (+ (/ Lgate 2.0) Tox))

(define YoxL (- Ymid Router))
(define YoxR (+ Ymid Router))

(define GateRoundCenter (- Drecess Router))

(define YsR (- YoxL LsdSetback))
(define YdL (+ YoxR LsdSetback))

(sdegeo:create-rectangle
  (position 0.0 0.0 0.0)
  (position Xdepth Ywidth 0.0)
  "Silicon" "R.Body"
)

(let
  (
    (GOX_BOX
      (sdegeo:create-rectangle
        (position 0.0 YoxL 0.0)
        (position GateRoundCenter YoxR 0.0)
        "SiO2" "R.TrenchOx.Box"
      )
    )

    (GOX_CIRC
      (sdegeo:create-circle
        (position GateRoundCenter Ymid 0.0)
        Router
        "SiO2" "R.TrenchOx.Round"
      )
    )
  )

  (sdegeo:bool-unite
    (list GOX_BOX GOX_CIRC)
  )
)

(let
  (
    (WG_BOX
      (sdegeo:create-rectangle
        (position GateTop YgL 0.0)
        (position GateRoundCenter YgR 0.0)
        "Tungsten" "R.Gate.Box"
      )
    )

    (WG_CIRC
      (sdegeo:create-circle
        (position GateRoundCenter Ymid 0.0)
        (/ Lgate 2.0)
        "Tungsten" "R.Gate.Round"
      )
    )
  )

  (sdegeo:bool-unite
    (list WG_BOX WG_CIRC)
  )
)

(sdegeo:create-rectangle
  (position 0.0 YgL 0.0)
  (position GateTop YgR 0.0)
  "Nitride" "R.Cap"
)

(sdedr:define-constant-profile
  "Dop.Body"
  "BoronActiveConcentration"
  Nbody
)

(sdedr:define-constant-profile-region
  "Place.Body"
  "Dop.Body"
  "R.Body"
)

(sdedr:define-refeval-window
  "Base.Source"
  "Line"
  (position 0.0 0.0 0.0)
  (position 0.0 YsR 0.0)
)

(sdedr:define-gaussian-profile
  "Dop.Source.Gauss"
  "ArsenicActiveConcentration"
  "PeakPos" SDPeakPos
  "PeakVal" NSD
  "ValueAtDepth" Nbody
  "Depth" Jdepth
  "Gauss"
  "Factor" GaussFactor
)

(sdedr:define-analytical-profile-placement
  "Place.Source.Gauss"
  "Dop.Source.Gauss"
  "Base.Source"
  "Both"
  "NoReplace"
  "Eval"
)

(sdedr:define-refeval-window
  "Base.Drain"
  "Line"
  (position 0.0 YdL 0.0)
  (position 0.0 Ywidth 0.0)
)

(sdedr:define-gaussian-profile
  "Dop.Drain.Gauss"
  "ArsenicActiveConcentration"
  "PeakPos" SDPeakPos
  "PeakVal" NSD
  "ValueAtDepth" Nbody
  "Depth" Jdepth
  "Gauss"
  "Factor" GaussFactor
)

(sdedr:define-analytical-profile-placement
  "Place.Drain.Gauss"
  "Dop.Drain.Gauss"
  "Base.Drain"
  "Both"
  "NoReplace"
  "Eval"
)

(sdegeo:define-contact-set "source" 4 (color:rgb 1 0 0) "##")
(sdegeo:set-current-contact-set "source")
(sdegeo:define-2d-contact
  (find-edge-id (position 0.0 (/ YsR 2.0) 0.0))
  "source"
)

(sdegeo:define-contact-set "drain" 4 (color:rgb 0 0 1) "##")
(sdegeo:set-current-contact-set "drain")
(sdegeo:define-2d-contact
  (find-edge-id (position 0.0 (/ (+ YdL Ywidth) 2.0) 0.0))
  "drain"
)

(sdegeo:define-contact-set "substrate" 4 (color:rgb 0 1 0) "##")
(sdegeo:set-current-contact-set "substrate")
(sdegeo:define-2d-contact
  (find-edge-id (position Xdepth Ymid 0.0))
  "substrate"
)

(sdegeo:define-contact-set "gate" 4 (color:rgb 1 0 1) "##")
(sdegeo:set-current-contact-set "gate")
(sdegeo:set-contact
  (find-body-id
    (position (/ (+ GateTop GateRoundCenter) 2.0) Ymid 0.0)
  )
  "gate"
  "remove"
)

(sdedr:define-refeval-window
  "RefWin.Global"
  "Rectangle"
  (position 0.0 0.0 0.0)
  (position Xdepth Ywidth 0.0)
)

(sdedr:define-refinement-size
  "RefDef.Global"
  0.010 0.010
  0.002 0.002
)

(sdedr:define-refinement-function
  "RefDef.Global"
  "DopingConcentration"
  "MaxTransDiff"
  1.0
)

(sdedr:define-refinement-placement
  "Place.Global"
  "RefDef.Global"
  "RefWin.Global"
)

(sdedr:define-refeval-window
  "RefWin.Gate"
  "Rectangle"
  (position 0.0 (- YoxL 0.012) 0.0)
  (position (+ Drecess 0.012) (+ YoxR 0.012) 0.0)
)

(sdedr:define-refinement-size
  "RefDef.Gate"
  0.0030 0.0030
  0.0005 0.0005
)

(sdedr:define-refinement-function
  "RefDef.Gate"
  "MaxLenInt"
  "Silicon"
  "SiO2"
  0.0004
  1.5
  "DoubleSide"
)

(sdedr:define-refinement-placement
  "Place.Gate"
  "RefDef.Gate"
  "RefWin.Gate"
)

(sdedr:define-refeval-window
  "RefWin.SourceJunction"
  "Rectangle"
  (position 0.028 (- YsR 0.006) 0.0)
  (position 0.064 (+ YoxL 0.006) 0.0)
)

(sdedr:define-refinement-size
  "RefDef.SourceJunction"
  0.0030 0.0020
  0.0007 0.0005
)

(sdedr:define-refinement-placement
  "Place.SourceJunction"
  "RefDef.SourceJunction"
  "RefWin.SourceJunction"
)

(sdedr:define-refeval-window
  "RefWin.DrainJunction"
  "Rectangle"
  (position 0.028 (- YoxR 0.006) 0.0)
  (position 0.064 (+ YdL 0.006) 0.0)
)

(sdedr:define-refinement-size
  "RefDef.DrainJunction"
  0.0030 0.0020
  0.0007 0.0005
)

(sdedr:define-refinement-placement
  "Place.DrainJunction"
  "RefDef.DrainJunction"
  "RefWin.DrainJunction"
)

(if (> MeshLevel 0)
  (begin

    (sdedr:define-refeval-window
      "RefWin.GIDLOuter"
      "Rectangle"
      (position (- GateTop 0.015) (- YgR 0.006) 0.0)
      (position (+ Jdepth 0.015) (+ YoxR 0.010) 0.0)
    )

    (sdedr:define-refinement-size
      "RefDef.GIDLOuter"
      (if (= MeshLevel 3) 0.0015
          (if (= MeshLevel 2) 0.0020 0.0025))
      (if (= MeshLevel 3) 0.0009
          (if (= MeshLevel 2) 0.0012 0.0015))
      (if (> MeshLevel 1) 0.0005 0.0006)
      (if (> MeshLevel 1) 0.0003 0.0004)
    )

    (sdedr:define-refinement-placement
      "Place.GIDLOuter"
      "RefDef.GIDLOuter"
      "RefWin.GIDLOuter"
    )

    (sdedr:define-refeval-window
      "RefWin.GIDLMid"
      "Rectangle"
      (position (- GateTop 0.008) (- YgR 0.003) 0.0)
      (position (+ GateTop 0.014) (+ YoxR 0.006) 0.0)
    )

    (sdedr:define-refinement-size
      "RefDef.GIDLMid"
      (if (= MeshLevel 3) 0.0009
          (if (= MeshLevel 2) 0.0012 0.0015))
      (if (= MeshLevel 3) 0.0005
          (if (= MeshLevel 2) 0.0007 0.0009))
      (if (> MeshLevel 1) 0.0003 0.0004)
      (if (> MeshLevel 1) 0.00018 0.00025)
    )

    (sdedr:define-refinement-placement
      "Place.GIDLMid"
      "RefDef.GIDLMid"
      "RefWin.GIDLMid"
    )

    (sdedr:define-refeval-window
      "RefWin.GIDLCore"
      "Rectangle"
      (position (- GateTop 0.004) (- YgR 0.0015) 0.0)
      (position (+ GateTop 0.008) (+ YoxR 0.0035) 0.0)
    )

    (sdedr:define-refinement-size
      "RefDef.GIDLCore"
      (if (= MeshLevel 3) 0.00055
          (if (= MeshLevel 2) 0.00065 0.00090))
      (if (= MeshLevel 3) 0.00035
          (if (= MeshLevel 2) 0.00040 0.00060))
      (if (> MeshLevel 1) 0.00018 0.00025)
      (if (> MeshLevel 1) 0.00012 0.00018)
    )

    (sdedr:define-refinement-placement
      "Place.GIDLCore"
      "RefDef.GIDLCore"
      "RefWin.GIDLCore"
    )
  )
  0
)

(display "\n")
(display "============================================================\n")
(display "CMP B0-2D-PAPER-CAL NEW MESH FAMILY v1\n")
(display "============================================================\n")

(display "MEBDepth / GateTop [um] = ")
(display GateTop)
(newline)

(display "MeshLevel               = ")
(display MeshLevel)
(newline)

(display "Domain X / Y [um]       = ")
(display Xdepth)
(display " / ")
(display Ywidth)
(newline)

(display "GateCouplingScale       = ")
(display GateCouplingScale)
(newline)

(display "GateDepthBoost [um]     = ")
(display GateDepthBoost)
(newline)

(display "Physical Tox [um]       = ")
(display ToxPhysical)
(newline)

(display "Effective Tox [um]      = ")
(display Tox)
(newline)

(display "Physical Drecess [um]   = ")
(display DrecessPhysical)
(newline)

(display "Effective Drecess [um]  = ")
(display Drecess)
(newline)

(display "YgR / YoxR [um]         = ")
(display YgR)
(display " / ")
(display YoxR)
(newline)

(display "Jdepth [um]             = ")
(display Jdepth)
(newline)

(display "NOTE: Qf_Int is frozen in SDevice, not in this SDE deck.\n")
(display "============================================================\n")

(sde:build-mesh
  "snmesh"
  ""
  "n@node@"
)
