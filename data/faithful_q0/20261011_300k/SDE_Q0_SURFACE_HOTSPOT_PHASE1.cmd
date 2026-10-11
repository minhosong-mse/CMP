; ================================================================
; CMP B0-2D-FAITHFUL-Q0 / GIDL 300 K / MEB5
; STATUS: PHASE-1 REFINEMENT PREPARED / NOT YET EXECUTED. Sentaurus T-2022.03 SWB CMD.
; Parent: completed PAPER-CAL Atlas 300 K L2 SDE (from user ZIP).
; SWB parameter MEBDepth (um): 0.031 / 0.036 / 0.041 / 0.048 / 0.051
; Lgate=0.020 um; ToxPhysical=0.005 um; DrecessPhysical=0.120 um;
; Jdepth=0.048 um; gate WF=4.8 eV (in SDevice).
; Qf is not set in SDE. Q0 assumes no extra FixedCharge in SDevice.
; 2D longitudinal reconstruction, NOT an exact 3D paper deck.
; MeshLevel 2 inherited POLICY; convergence is unverified here.
; ================================================================

(sde:clear)
(sdegeo:set-default-boolean "ABA")

; =============================================================================
; 0. FROZEN CALIBRATION / SWB PARAMETERS
; =============================================================================

(define GateCouplingScale 1.000)
(define GateDepthBoost    0.000)

(define MEBDepth  @MEBDepth@)
(define MeshLevel 2)

(define LsdSetback 0.015)
(define GaussFactor 0.0)
(define SDPeakPos   0.0)

; =============================================================================
; 1. PAPER-EXPLICIT PHYSICAL BASELINE + FROZEN EFFECTIVE-2D COORDINATES
; =============================================================================

(define Lgate 0.020)

(define DrecessPhysical 0.120)
(define Drecess (+ DrecessPhysical GateDepthBoost))

(define ToxPhysical 0.005)
(define Tox (/ ToxPhysical GateCouplingScale))

(define GateTop MEBDepth)

(define Jdepth 0.048)
(define Nbody   1.0e17)
(define NSD     1.0e20)

; =============================================================================
; 2. FROZEN NUMERICAL DOMAIN
; =============================================================================

(define Xdepth 0.300)
(define Ywidth 0.480)

; =============================================================================
; 3. DERIVED GEOMETRY
; =============================================================================

; X = vertical depth
; Y = source -> drain direction

(define Ymid (/ Ywidth 2.0))

(define YgL (- Ymid (/ Lgate 2.0)))
(define YgR (+ Ymid (/ Lgate 2.0)))

(define Router (+ (/ Lgate 2.0) Tox))

(define YoxL (- Ymid Router))
(define YoxR (+ Ymid Router))

(define GateRoundCenter (- Drecess Router))

(define YsR (- YoxL LsdSetback))
(define YdL (+ YoxR LsdSetback))

; =============================================================================
; 4. SILICON BODY
; =============================================================================

(sdegeo:create-rectangle
  (position 0.0 0.0 0.0)
  (position Xdepth Ywidth 0.0)
  "Silicon" "R.Body"
)

; =============================================================================
; 5. ROUNDED GATE OXIDE — FROZEN
; =============================================================================

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

; =============================================================================
; 6. ROUNDED TUNGSTEN BURIED GATE — FROZEN
; =============================================================================

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

; =============================================================================
; 7. NITRIDE CAP
; =============================================================================

(sdegeo:create-rectangle
  (position 0.0 YgL 0.0)
  (position GateTop YgR 0.0)
  "Nitride" "R.Cap"
)

; =============================================================================
; 8. BODY DOPING — FROZEN
; =============================================================================

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

; =============================================================================
; 9. GAUSSIAN SOURCE / DRAIN — FROZEN
; =============================================================================

; SOURCE
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

; DRAIN
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

; =============================================================================
; 10. CONTACTS — FROZEN
; =============================================================================

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

; =============================================================================
; 11. MESH FAMILY
; =============================================================================
;
; Units below are um.
;
; Level 0:
;   Global + gate/interface + compact S/D shoulder refinement.
;   No dedicated GIDL nested windows.
;
; Level 1:
;   Level 0 + three-stage nested drain refinement.
;   This is NEW-OPT-v1.
;
; Level 2:
;   Same topology as Level 1, but tighter only in drain-side BTBT-critical ROI.
;   This is NEW-REF-v1 for convergence.
;
; Level 3:
;   Same topology and SAME minimum sizes as Level 2.
;   Only the maximum element sizes in GIDL Outer/Mid/Core are reduced:
;     Outer max = 1.5 x 0.9 nm
;     Mid   max = 0.9 x 0.5 nm
;     Core  max = 0.55 x 0.35 nm
;   This is NEW-REF-v2 and is intended only as the final L2->L3 reference.
;
; The global mesh, gate/interface mesh, and S/D shoulder mesh are intentionally
; NOT tightened from Level 1 to Level 2 or Level 3. This keeps convergence local
; and limits runtime growth.
; =============================================================================

; -----------------------------------------------------------------------------
; 11-1. GLOBAL
; -----------------------------------------------------------------------------

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

; Preserve adaptive Gaussian-junction tracking without using a full-width
; fixed fine band.
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

; -----------------------------------------------------------------------------
; 11-2. GATE / Si-SiO2 INTERFACE
; -----------------------------------------------------------------------------

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

; Interface-following refinement. Factor gives a graded expansion away from
; the interface instead of forcing a wide uniformly fine rectangle.
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

; -----------------------------------------------------------------------------
; 11-3. COMPACT SOURCE-SIDE JUNCTION / SHOULDER
; -----------------------------------------------------------------------------

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

; -----------------------------------------------------------------------------
; 11-4. COMPACT DRAIN-SIDE JUNCTION / SHOULDER
; -----------------------------------------------------------------------------

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

; -----------------------------------------------------------------------------
; 11-5. GIDL OUTER / MID / CORE WINDOWS
;
; Nominal frozen FZ-C hotspot was near:
;   X ~ 0.0349 um
;   Y ~ 0.252174 um ~= YoxR
;
; Later debug runs showed Xhot moving with MEB.
; Therefore the windows below follow GateTop instead of using one absolute box.
; -----------------------------------------------------------------------------

(if (> MeshLevel 0)
  (begin

    ; -----------------------------
    ; OUTER
    ; -----------------------------
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

    ; -----------------------------
    ; MID
    ; -----------------------------
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

    ; -----------------------------
    ; CORE
    ; -----------------------------
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

; =============================================================================
; 11-6. FAITHFUL-Q0 SURFACE BTBT HOTSPOT REFINEMENT — PHASE 1
; =============================================================================
;
; REASON (independent 300 K Atlas-L2 audit, 2026-10-11):
;   MEB 33..51 nm: measured global Si-BTBT hotspot is near
;     Xhot = 0.002343750 um, Yhot = 0.266250014 um.
;   Existing MEB-following GIDL Core targets X ~ GateTop (0.031..0.051 um),
;   thus the near-surface hotspot does not lie inside that finest ROI.
;
; EXPERIMENT: preserve all geometry, material, doping, contacts, all existing
;   mesh refinements, physics, bias, solver, and SVisual measurements.
;   ADD ONLY two small rectangular refinement placements near the drain-side
;   top silicon surface. Both windows are tied to YdL (drain baseline edge).
;
; SurfaceRefineLevel = 1: first targeted-refinement run (DEFAULT).
; SurfaceRefineLevel = 2: optional tighter confirmation run. Change ONLY this
;                         numeric constant, in a copied SWB project.
; SurfaceRefineLevel = 0: no extra surface refinements (original policy).
;
; CAUTION: MaxElementSize > MinElementSize; sizes are in um.
; SDE mesh refinement DOES NOT locate/track hotspots dynamically.
; It targets a measured hotspot from prior runs; if it moves after remeshing,
; compare the new position and assess window coverage anew.
;
; Reference geometry for Faithful-Q0:
;   YoxR = 0.255 um; YdL = 0.270 um.
;   Stage-1 OUTER window: X=[0,0.015], Y=[0.258,0.276] um.
;   Stage-1 CORE  window: X=[0,0.008], Y=[0.263,0.270] um.
;
(define SurfaceRefineLevel 1)

(if (> SurfaceRefineLevel 0)
  (begin
    ; OUTER - include top-Si/drain shoulder and spatial integration tail.
    (sdedr:define-refeval-window
      "RefWin.Q0SurfaceOuter"
      "Rectangle"
      (position 0.000 (- YdL 0.012) 0.0)
      (position 0.015 (+ YdL 0.006) 0.0)
    )

    (sdedr:define-refinement-size
      "RefDef.Q0SurfaceOuter"
      (if (= SurfaceRefineLevel 2) 0.0012 0.0015)
      (if (= SurfaceRefineLevel 2) 0.0008 0.0010)
      (if (= SurfaceRefineLevel 2) 0.00030 0.00035)
      (if (= SurfaceRefineLevel 2) 0.00020 0.00025)
    )

    (sdedr:define-refinement-placement
      "Place.Q0SurfaceOuter"
      "RefDef.Q0SurfaceOuter"
      "RefWin.Q0SurfaceOuter"
    )

    ; CORE - includes measured BTBTmax at X=0.00234, Y=0.26625 um.
    ; Fine sizes are comparable to the existing GateTop GIDL Core sizes.
    (sdedr:define-refeval-window
      "RefWin.Q0SurfaceCore"
      "Rectangle"
      (position 0.000 (- YdL 0.007) 0.0)
      (position 0.008 YdL 0.0)
    )

    (sdedr:define-refinement-size
      "RefDef.Q0SurfaceCore"
      (if (= SurfaceRefineLevel 2) 0.00055 0.00065)
      (if (= SurfaceRefineLevel 2) 0.00035 0.00040)
      (if (= SurfaceRefineLevel 2) 0.00018 0.00018)
      (if (= SurfaceRefineLevel 2) 0.00012 0.00012)
    )

    (sdedr:define-refinement-placement
      "Place.Q0SurfaceCore"
      "RefDef.Q0SurfaceCore"
      "RefWin.Q0SurfaceCore"
    )
  )
  0
)

; =============================================================================
; 12. QA PRINT
; =============================================================================

(display "\n")
(display "============================================================\n")
(display "CMP B0-2D-FAITHFUL-Q0 / Atlas-L2 mesh policy\n")
(display "============================================================\n")

(display "MEBDepth / GateTop [um] = ")
(display GateTop)
(newline)

(display "MeshLevel               = ")
(display MeshLevel)
(newline)
(display "SurfaceRefineLevel       = ")
(display SurfaceRefineLevel)
(newline)

(display "Surface Outer X [um]    = 0.000 / 0.015; Y near drain [um] = ")
(display (- YdL 0.012))
(display " / ")
(display (+ YdL 0.006))
(newline)

(display "Surface Core X [um]     = 0.000 / 0.008; Y near drain [um] = ")
(display (- YdL 0.007))
(display " / ")
(display YdL)
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

(display "NOTE: no interface FixedCharge included in Q0 GIDL SDevice decks.\n")
(display "============================================================\n")

; =============================================================================
; 13. BUILD MESH
; =============================================================================

(sde:build-mesh
  "snmesh"
  ""
  "n@node@"
)