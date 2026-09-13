;===============================================================================
; CMP - 3D-Sun-B0
;
; Geometry v05       - FROZEN
; Contacts D1 v01    - FROZEN
; Doping E1 v01      - FROZEN
; Electrical Mesh F1 - v01 NOMINAL
;
; Purpose:
;   Literature-consistent 3D BCAT baseline reconstruction.
;   Build nominal electrical mesh for subsequent SDevice validation.
;
; IMPORTANT:
;   - Geometry / contacts / doping are frozen.
;   - F1 mesh is NOT convergence-frozen yet.
;   - Mesh dimensions are numerical reconstruction settings.
;   - Final acceptance requires Coarse / Nominal / Fine convergence study.
;
; Coordinate convention:
;
;   x : along channel / Source <-> Drain
;       x < 0 : source
;       x > 0 : drain
;
;   y : word-line / across-fin direction
;
;   z : vertical
;       z = 0 : top reference
;       z < 0 : into device
;
; Literature-explicit:
;
;   Lgate    = 0.020 um
;   Drecess  = 0.120 um
;   DBCAT    = 0.036 um
;   Tox      = 0.005 um
;   Wfin     = 0.017 um
;   Hfin     = 0.048 um
;
;   Body Boron       = 1.0e17 cm^-3
;   S/D Arsenic peak = 1.0e20 cm^-3
;   Gaussian doping
;   Djunction        = 0.40 * Drecess = 0.048 um
;
; Reconstruction assumptions:
;
;   Xhalf = 0.060 um
;   Yhalf = 0.030 um
;   Zbody = 0.180 um
;
;   Hfin mapped to fin-to-bulk merge depth.
;
;   Source implant:
;     x = -Xhalf -> -Router
;     y = -Rfin  -> +Rfin
;
;   Drain implant:
;     x = +Router -> +Xhalf
;     y = -Rfin   -> +Rfin
;
;   Gaussian lateral factor = 0.0
;
;===============================================================================


;===============================================================================
; 0. INITIALIZE
;===============================================================================

(sde:clear)

(sde:set-process-up-direction "+z")

(sdegeo:set-default-boolean "ABA")


;===============================================================================
; 1. PRIMARY PARAMETERS
;===============================================================================


;------------------------------------------------------------------------------
; 1-1. LITERATURE GEOMETRY PARAMETERS
;------------------------------------------------------------------------------

(define Lgate
  0.020
)

(define Drecess
  0.120
)

(define DBCAT
  0.036
)

(define Tox
  0.005
)

(define Wfin
  0.017
)

(define Hfin
  0.048
)


;------------------------------------------------------------------------------
; 1-2. RECONSTRUCTION DOMAIN
;------------------------------------------------------------------------------

(define Xhalf
  0.060
)

(define Yhalf
  0.030
)

(define Zbody
  0.180
)


;------------------------------------------------------------------------------
; 1-3. DOPING PARAMETERS
;------------------------------------------------------------------------------

(define Nbody
  1.0e17
)

(define NSD
  1.0e20
)

(define Djunction
  (* 0.40 Drecess)
)

(define GaussFactor
  0.0
)


;===============================================================================
; 2. DERIVED PARAMETERS
;===============================================================================


;------------------------------------------------------------------------------
; 2-1. GATE
;------------------------------------------------------------------------------

(define Rgate
  (* 0.5 Lgate)
)

(define Router
  (+ Rgate Tox)
)


;------------------------------------------------------------------------------
; 2-2. FIN
;------------------------------------------------------------------------------

(define FinHalf
  (* 0.5 Wfin)
)

(define Rfin
  (* 0.5 Wfin)
)


;------------------------------------------------------------------------------
; 2-3. VERTICAL COORDINATES
;------------------------------------------------------------------------------

; W gate top
; = -0.036 um
(define ZgateTop
  (- DBCAT)
)

; Rounded oxide/gate bottom-center
; = 0.015 - 0.120
; = -0.105 um
(define ZgateCenter
  (- Router Drecess)
)

; W gate bottom
; = -0.115 um
(define ZgateBottom
  (- ZgateCenter Rgate)
)

; Gate oxide bottom
; = -0.120 um
(define ZoxideBottom
  (- Drecess)
)

; Fin-to-bulk merge
; = -0.048 um
(define ZfinBottom
  (- Hfin)
)

; Rounded fin cap center
; = -0.0085 um
(define ZfinCapCtr
  (- Rfin)
)


;------------------------------------------------------------------------------
; 2-4. JUNCTION COORDINATES
;------------------------------------------------------------------------------

; nominal metallurgical / target junction depth
; = -0.048 um
(define Zjunction
  (- Djunction)
)

; F1 verification/refinement band:
; -0.040 to -0.056 um
(define ZjuncTop
  (+ Zjunction 0.008)
)

(define ZjuncBottom
  (- Zjunction 0.008)
)


;===============================================================================
; 3. TOP ISOLATION
;===============================================================================

(define ISO
  (sdegeo:create-cuboid

    (position
      (- Xhalf)
      (- Yhalf)
      0.0
    )

    (position
      Xhalf
      Yhalf
      ZfinBottom
    )

    "Oxide"
    "R.Isolation"
  )
)


;===============================================================================
; 4. BROAD SILICON SUBSTRATE
;===============================================================================

(define SISUB
  (sdegeo:create-cuboid

    (position
      (- Xhalf)
      (- Yhalf)
      ZfinBottom
    )

    (position
      Xhalf
      Yhalf
      (- Zbody)
    )

    "Silicon"
    "R.SiSubstrate"
  )
)


;===============================================================================
; 5. SADDLE-FIN SILICON
;===============================================================================


;------------------------------------------------------------------------------
; 5-1. FIN STEM
;------------------------------------------------------------------------------

(define SIFIN_STEM
  (sdegeo:create-cuboid

    (position
      (- Xhalf)
      (- Rfin)
      ZfinCapCtr
    )

    (position
      Xhalf
      Rfin
      ZfinBottom
    )

    "Silicon"
    "R.SiFin"
  )
)


;------------------------------------------------------------------------------
; 5-2. ROUNDED FIN CAP
;------------------------------------------------------------------------------

(define SIFIN_CAP
  (sdegeo:create-cylinder

    (position
      (- Xhalf)
      0.0
      ZfinCapCtr
    )

    (position
      Xhalf
      0.0
      ZfinCapCtr
    )

    Rfin

    "Silicon"
    "R.SiFin.Cap"
  )
)


;------------------------------------------------------------------------------
; 5-3. UNITE FIN
;------------------------------------------------------------------------------

(define SIFIN
  (sdegeo:bool-unite
    (list
      SIFIN_STEM
      SIFIN_CAP
    )
  )
)


;===============================================================================
; 6. GATE OXIDE
;===============================================================================


;------------------------------------------------------------------------------
; 6-1. VERTICAL OXIDE BODY
;------------------------------------------------------------------------------

(define GOX_BOX
  (sdegeo:create-cuboid

    (position
      (- Router)
      (- Yhalf)
      0.0
    )

    (position
      Router
      Yhalf
      ZgateCenter
    )

    "Oxide"
    "R.GateOxide"
  )
)


;------------------------------------------------------------------------------
; 6-2. ROUNDED OXIDE BOTTOM
;------------------------------------------------------------------------------

(define GOX_CYL
  (sdegeo:create-cylinder

    (position
      0.0
      (- Yhalf)
      ZgateCenter
    )

    (position
      0.0
      Yhalf
      ZgateCenter
    )

    Router

    "Oxide"
    "R.GateOxide.Bottom"
  )
)


;------------------------------------------------------------------------------
; 6-3. UNITE GATE OXIDE
;------------------------------------------------------------------------------

(define GOX
  (sdegeo:bool-unite
    (list
      GOX_BOX
      GOX_CYL
    )
  )
)


;===============================================================================
; 7. TUNGSTEN BURIED GATE
;===============================================================================


;------------------------------------------------------------------------------
; 7-1. W VERTICAL BODY
;------------------------------------------------------------------------------

(define WG_BOX
  (sdegeo:create-cuboid

    (position
      (- Rgate)
      (- Yhalf)
      ZgateTop
    )

    (position
      Rgate
      Yhalf
      ZgateCenter
    )

    "Tungsten"
    "R.WGate"
  )
)


;------------------------------------------------------------------------------
; 7-2. W ROUNDED BOTTOM
;------------------------------------------------------------------------------

(define WG_CYL
  (sdegeo:create-cylinder

    (position
      0.0
      (- Yhalf)
      ZgateCenter
    )

    (position
      0.0
      Yhalf
      ZgateCenter
    )

    Rgate

    "Tungsten"
    "R.WGate.Bottom"
  )
)


;------------------------------------------------------------------------------
; 7-3. UNITE W GATE
;------------------------------------------------------------------------------

(define WGATE
  (sdegeo:bool-unite
    (list
      WG_BOX
      WG_CYL
    )
  )
)


;===============================================================================
; 8. NITRIDE ABOVE W GATE
;===============================================================================

(define NIT
  (sdegeo:create-cuboid

    (position
      (- Rgate)
      (- Yhalf)
      0.0
    )

    (position
      Rgate
      Yhalf
      ZgateTop
    )

    "Nitride"
    "R.Nitride"
  )
)


;===============================================================================
; 9. CONTACT PROBE POSITIONS
;===============================================================================


;------------------------------------------------------------------------------
; 9-1. SOURCE
;------------------------------------------------------------------------------

(define P.Source
  (position
    (- Xhalf)
    0.0
    -0.025
  )
)


;------------------------------------------------------------------------------
; 9-2. DRAIN
;------------------------------------------------------------------------------

(define P.Drain
  (position
    Xhalf
    0.0
    -0.025
  )
)


;------------------------------------------------------------------------------
; 9-3. GATE BODY
;------------------------------------------------------------------------------

(define P.GateBody
  (position
    0.0
    0.0
    -0.070
  )
)


;------------------------------------------------------------------------------
; 9-4. SUBSTRATE
;------------------------------------------------------------------------------

(define P.Substrate
  (position
    0.0
    0.0
    (- Zbody)
  )
)


;===============================================================================
; 10. PRE-CONTACT QA
;===============================================================================

(display "\n")
(display "============================================================\n")
(display "=== PRE-CONTACT QA =========================================\n")
(display "============================================================\n")

(display "Source candidate:\n")
(find-face-id P.Source)

(display "Drain candidate:\n")
(find-face-id P.Drain)

(display "Gate body candidate:\n")
(find-body-id P.GateBody)

(display "Substrate candidate:\n")
(find-face-id P.Substrate)

(display "Geometry overlap before contacts:\n")
(sdegeo:check-overlap (get-body-list))

(display "============================================================\n")


;===============================================================================
; 11. CONTACT SET DEFINITIONS
;===============================================================================


;------------------------------------------------------------------------------
; 11-1. SOURCE
;------------------------------------------------------------------------------

(sdegeo:define-contact-set
  "source"
  4
  (color:rgb 1 0 0)
  "##"
)


;------------------------------------------------------------------------------
; 11-2. DRAIN
;------------------------------------------------------------------------------

(sdegeo:define-contact-set
  "drain"
  4
  (color:rgb 0 0 1)
  "##"
)


;------------------------------------------------------------------------------
; 11-3. GATE
;------------------------------------------------------------------------------

(sdegeo:define-contact-set
  "gate"
  4
  (color:rgb 1 0 1)
  "##"
)


;------------------------------------------------------------------------------
; 11-4. SUBSTRATE
;------------------------------------------------------------------------------

(sdegeo:define-contact-set
  "substrate"
  4
  (color:rgb 0 1 0)
  "##"
)


;===============================================================================
; 12. CONTACT ASSIGNMENT
;===============================================================================


;------------------------------------------------------------------------------
; 12-1. SOURCE
;------------------------------------------------------------------------------

(sdegeo:set-contact
  (find-face-id P.Source)
  "source"
)


;------------------------------------------------------------------------------
; 12-2. DRAIN
;------------------------------------------------------------------------------

(sdegeo:set-contact
  (find-face-id P.Drain)
  "drain"
)


;------------------------------------------------------------------------------
; 12-3. SUBSTRATE
;------------------------------------------------------------------------------

(sdegeo:set-contact
  (find-face-id P.Substrate)
  "substrate"
)


;------------------------------------------------------------------------------
; 12-4. GATE
;
; Entire W body converted into electrical gate boundary.
;------------------------------------------------------------------------------

(sdegeo:set-contact
  (find-body-id P.GateBody)
  "gate"
  "remove"
)


;===============================================================================
; 13. POST-CONTACT QA
;===============================================================================

(display "\n")
(display "============================================================\n")
(display "=== CONTACT QA =============================================\n")
(display "============================================================\n")

(display "Source contact probe:\n")
(find-face-id P.Source)

(display "Drain contact probe:\n")
(find-face-id P.Drain)

(display "Substrate contact probe:\n")
(find-face-id P.Substrate)

(display "Overlap after contacts:\n")
(sdegeo:check-overlap (get-body-list))

(display "============================================================\n")


;===============================================================================
; 14. BODY BORON BACKGROUND
;===============================================================================


;------------------------------------------------------------------------------
; 14-1. PROFILE
;------------------------------------------------------------------------------

(sdedr:define-constant-profile
  "Dop.Body"
  "BoronActiveConcentration"
  Nbody
)


;------------------------------------------------------------------------------
; 14-2. FIN / CHANNEL
;------------------------------------------------------------------------------

(sdedr:define-constant-profile-region
  "Place.Body.Fin"
  "Dop.Body"
  "R.SiFin"
)


;------------------------------------------------------------------------------
; 14-3. BULK SUBSTRATE
;------------------------------------------------------------------------------

(sdedr:define-constant-profile-region
  "Place.Body.Substrate"
  "Dop.Body"
  "R.SiSubstrate"
)


;===============================================================================
; 15. SOURCE GAUSSIAN ARSENIC
;===============================================================================


;------------------------------------------------------------------------------
; 15-1. SOURCE REFERENCE WINDOW
;------------------------------------------------------------------------------

(sdedr:define-refeval-window
  "Base.Source"
  "Rectangle"

  (position
    (- Xhalf)
    (- Rfin)
    0.0
  )

  (position
    (- Router)
    Rfin
    0.0
  )
)


;------------------------------------------------------------------------------
; 15-2. SOURCE PROFILE
;------------------------------------------------------------------------------

(sdedr:define-gaussian-profile
  "Dop.Source.Gauss"
  "ArsenicActiveConcentration"

  "PeakPos"
  0.0

  "PeakVal"
  NSD

  "ValueAtDepth"
  Nbody

  "Depth"
  Djunction

  "Gauss"

  "Factor"
  GaussFactor
)


;------------------------------------------------------------------------------
; 15-3. SOURCE PROFILE PLACEMENT
;------------------------------------------------------------------------------

(sdedr:define-analytical-profile-placement
  "Place.Source.Gauss"
  "Dop.Source.Gauss"
  "Base.Source"
  "Both"
  "NoReplace"
  "Eval"
)


;===============================================================================
; 16. DRAIN GAUSSIAN ARSENIC
;===============================================================================


;------------------------------------------------------------------------------
; 16-1. DRAIN REFERENCE WINDOW
;------------------------------------------------------------------------------

(sdedr:define-refeval-window
  "Base.Drain"
  "Rectangle"

  (position
    Router
    (- Rfin)
    0.0
  )

  (position
    Xhalf
    Rfin
    0.0
  )
)


;------------------------------------------------------------------------------
; 16-2. DRAIN PROFILE
;------------------------------------------------------------------------------

(sdedr:define-gaussian-profile
  "Dop.Drain.Gauss"
  "ArsenicActiveConcentration"

  "PeakPos"
  0.0

  "PeakVal"
  NSD

  "ValueAtDepth"
  Nbody

  "Depth"
  Djunction

  "Gauss"

  "Factor"
  GaussFactor
)


;------------------------------------------------------------------------------
; 16-3. DRAIN PROFILE PLACEMENT
;------------------------------------------------------------------------------

(sdedr:define-analytical-profile-placement
  "Place.Drain.Gauss"
  "Dop.Drain.Gauss"
  "Base.Drain"
  "Both"
  "NoReplace"
  "Eval"
)


;===============================================================================
; 17. DOPING QA
;===============================================================================

(display "\n")
(display "============================================================\n")
(display "=== DOPING QA ==============================================\n")
(display "============================================================\n")

(display "Body Boron [cm^-3]       = ")
(display Nbody)
(newline)

(display "S/D As peak [cm^-3]      = ")
(display NSD)
(newline)

(display "Djunction [um]           = ")
(display Djunction)
(newline)

(display "Djunction / Drecess      = ")
(display (/ Djunction Drecess))
(newline)

(display "Gaussian lateral factor  = ")
(display GaussFactor)
(newline)

(display "Source X range [um]       = ")
(display (- Xhalf))
(display " to ")
(display (- Router))
(newline)

(display "Drain X range [um]        = ")
(display Router)
(display " to ")
(display Xhalf)
(newline)

(display "S/D Y range [um]          = ")
(display (- Rfin))
(display " to ")
(display Rfin)
(newline)

(display "============================================================\n")


;===============================================================================
; 18. PHASE F1 - ELECTRICAL MESH v01
;
; STATUS:
;   NOMINAL / CANDIDATE
;
; Mesh values are numerical reconstruction settings.
;
; Goals:
;   - manage total 3D element count
;   - preserve channel electrostatics
;   - resolve 5 nm oxide surroundings
;   - resolve S/D junction gradients
;   - resolve source/drain-side gate-edge electric fields
;
;===============================================================================


;===============================================================================
; 18-1. GLOBAL DOMAIN
;
; Max: 12 / 12 / 12 nm
; Min:  3 /  3 /  3 nm
;===============================================================================

(sdedr:define-refeval-window
  "F1.Win.Global"
  "Cuboid"

  (position
    (- Xhalf)
    (- Yhalf)
    (- Zbody)
  )

  (position
    Xhalf
    Yhalf
    0.0
  )
)


(sdedr:define-refinement-size
  "F1.Def.Global"

  0.012
  0.012
  0.012

  0.003
  0.003
  0.003
)


; Adaptive doping-gradient refinement
(sdedr:define-refinement-function
  "F1.Def.Global"
  "DopingConcentration"
  "MaxTransDiff"
  1.0
)


(sdedr:define-refinement-placement
  "F1.Place.Global"
  "F1.Def.Global"
  "F1.Win.Global"
)


;===============================================================================
; 18-2. ACTIVE FIN / CHANNEL REGION
;
; x : full active length
; y : +/-14 nm
; z : 0 -> -130 nm
;
; Max:
;   dx = 3 nm
;   dy = 2 nm
;   dz = 2 nm
;
; Min:
;   dx = 1 nm
;   dy = 0.5 nm
;   dz = 0.5 nm
;===============================================================================

(sdedr:define-refeval-window
  "F1.Win.Active"
  "Cuboid"

  (position
    (- Xhalf)
    -0.014
    -0.130
  )

  (position
    Xhalf
    0.014
    0.0
  )
)


(sdedr:define-refinement-size
  "F1.Def.Active"

  0.003
  0.002
  0.002

  0.001
  0.0005
  0.0005
)


(sdedr:define-refinement-function
  "F1.Def.Active"
  "DopingConcentration"
  "MaxTransDiff"
  0.5
)


(sdedr:define-refinement-placement
  "F1.Place.Active"
  "F1.Def.Active"
  "F1.Win.Active"
)


;===============================================================================
; 18-3. GATE / Si-OXIDE INTERFACE
;
; Covers central gate-channel electrostatic region.
;
; Max:
;   1.5 nm isotropic
;
; Min:
;   0.3 nm isotropic
;===============================================================================

(sdedr:define-refeval-window
  "F1.Win.GateInterface"
  "Cuboid"

  (position
    -0.020
    -0.014
    -0.125
  )

  (position
    0.020
    0.014
    0.0
  )
)


(sdedr:define-refinement-size
  "F1.Def.GateInterface"

  0.0015
  0.0015
  0.0015

  0.0003
  0.0003
  0.0003
)


; Explicit Si/Oxide interface refinement
(sdedr:define-refinement-function
  "F1.Def.GateInterface"
  "MaxLenInt"
  "Silicon"
  "Oxide"
  0.0003
  1.5
  "DoubleSide"
)


(sdedr:define-refinement-placement
  "F1.Place.GateInterface"
  "F1.Def.GateInterface"
  "F1.Win.GateInterface"
)


;===============================================================================
; 18-4. SOURCE JUNCTION
;
; nominal z_junction = -0.048 um
;
; window:
;   -0.040 to -0.056 um
;
; Max:
;   dx = 1.5 nm
;   dy = 1.5 nm
;   dz = 0.5 nm
;
; Min:
;   dx = 0.5 nm
;   dy = 0.5 nm
;   dz = 0.25 nm
;===============================================================================

(sdedr:define-refeval-window
  "F1.Win.Junction.Source"
  "Cuboid"

  (position
    (- Xhalf)
    -0.011
    ZjuncBottom
  )

  (position
    (- Router)
    0.011
    ZjuncTop
  )
)


(sdedr:define-refinement-size
  "F1.Def.Junction.Source"

  0.0015
  0.0015
  0.0005

  0.0005
  0.0005
  0.00025
)


(sdedr:define-refinement-placement
  "F1.Place.Junction.Source"
  "F1.Def.Junction.Source"
  "F1.Win.Junction.Source"
)


;===============================================================================
; 18-5. DRAIN JUNCTION
;===============================================================================

(sdedr:define-refeval-window
  "F1.Win.Junction.Drain"
  "Cuboid"

  (position
    Router
    -0.011
    ZjuncBottom
  )

  (position
    Xhalf
    0.011
    ZjuncTop
  )
)


(sdedr:define-refinement-size
  "F1.Def.Junction.Drain"

  0.0015
  0.0015
  0.0005

  0.0005
  0.0005
  0.00025
)


(sdedr:define-refinement-placement
  "F1.Place.Junction.Drain"
  "F1.Def.Junction.Drain"
  "F1.Win.Junction.Drain"
)


;===============================================================================
; 18-6. SOURCE-SIDE GATE EDGE
;
; Symmetric refinement retained in the nominal baseline.
;
; Max:
;   dx = 1.0 nm
;   dy = 1.0 nm
;   dz = 0.5 nm
;
; Min:
;   dx = 0.3 nm
;   dy = 0.3 nm
;   dz = 0.2 nm
;===============================================================================

(sdedr:define-refeval-window
  "F1.Win.Edge.Source"
  "Cuboid"

  (position
    -0.025
    -0.012
    -0.060
  )

  (position
    -0.007
    0.012
    -0.025
  )
)


(sdedr:define-refinement-size
  "F1.Def.Edge.Source"

  0.001
  0.001
  0.0005

  0.0003
  0.0003
  0.0002
)


(sdedr:define-refinement-placement
  "F1.Place.Edge.Source"
  "F1.Def.Edge.Source"
  "F1.Win.Edge.Source"
)


;===============================================================================
; 18-7. DRAIN-SIDE GATE EDGE
;
; Critical future electric-field / leakage region.
;
; Same resolution as source edge for the nominal symmetric baseline.
;===============================================================================

(sdedr:define-refeval-window
  "F1.Win.Edge.Drain"
  "Cuboid"

  (position
    0.007
    -0.012
    -0.060
  )

  (position
    0.025
    0.012
    -0.025
  )
)


(sdedr:define-refinement-size
  "F1.Def.Edge.Drain"

  0.001
  0.001
  0.0005

  0.0003
  0.0003
  0.0002
)


(sdedr:define-refinement-placement
  "F1.Place.Edge.Drain"
  "F1.Def.Edge.Drain"
  "F1.Win.Edge.Drain"
)


;===============================================================================
; 19. FINAL QA BEFORE MESH
;===============================================================================

(display "\n")
(display "============================================================\n")
(display "=== PHASE F1 ELECTRICAL MESH v01 ===========================\n")
(display "============================================================\n")

(display "Geometry status : FROZEN\n")
(display "Contacts status : FROZEN\n")
(display "Doping status   : FROZEN\n")
(display "F1 mesh status  : NOMINAL / CANDIDATE\n")

(display "------------------------------------------------------------\n")

(display "Lgate [um]               = ")
(display Lgate)
(newline)

(display "Drecess [um]             = ")
(display Drecess)
(newline)

(display "DBCAT [um]               = ")
(display DBCAT)
(newline)

(display "Tox [um]                 = ")
(display Tox)
(newline)

(display "Wfin [um]                = ")
(display Wfin)
(newline)

(display "Hfin [um]                = ")
(display Hfin)
(newline)

(display "------------------------------------------------------------\n")

(display "Body Boron [cm^-3]       = ")
(display Nbody)
(newline)

(display "S/D As peak [cm^-3]      = ")
(display NSD)
(newline)

(display "Djunction [um]           = ")
(display Djunction)
(newline)

(display "Zjunction [um]           = ")
(display Zjunction)
(newline)

(display "Junction window top      = ")
(display ZjuncTop)
(newline)

(display "Junction window bottom   = ")
(display ZjuncBottom)
(newline)

(display "------------------------------------------------------------\n")

(display "F1 Global:\n")
(display "  max = 12 / 12 / 12 nm\n")
(display "  min =  3 /  3 /  3 nm\n")

(display "F1 Active:\n")
(display "  max = 3 / 2 / 2 nm\n")
(display "  min = 1 / 0.5 / 0.5 nm\n")

(display "F1 Gate Interface:\n")
(display "  max = 1.5 / 1.5 / 1.5 nm\n")
(display "  min = 0.3 / 0.3 / 0.3 nm\n")
(display "  Si/Oxide MaxLenInt = 0.3 nm\n")

(display "F1 Junction:\n")
(display "  max = 1.5 / 1.5 / 0.5 nm\n")
(display "  min = 0.5 / 0.5 / 0.25 nm\n")

(display "F1 Gate Edge:\n")
(display "  max = 1.0 / 1.0 / 0.5 nm\n")
(display "  min = 0.3 / 0.3 / 0.2 nm\n")

(display "------------------------------------------------------------\n")

(display "Overlap result before mesh follows:\n")

(sdegeo:check-overlap
  (get-body-list)
)

(display "============================================================\n")


;===============================================================================
; 20. SAVE MODEL
;===============================================================================

(sde:save-model
  "n@node@"
)


;===============================================================================
; 21. BUILD F1 NOMINAL MESH
;===============================================================================

(display "\n")
(display "============================================================\n")
(display "=== BUILDING F1 NOMINAL ELECTRICAL MESH ====================\n")
(display "============================================================\n")

(sde:build-mesh
  "snmesh"
  ""
  "n@node@"
)


;===============================================================================
; 22. FINAL MESSAGE
;===============================================================================

(display "\n")
(display "============================================================\n")
(display "=== CMP 3D-Sun-B0 ==========================================\n")
(display "=== Geometry v05       : FROZEN ============================\n")
(display "=== Contacts D1        : FROZEN ============================\n")
(display "=== Doping E1          : FROZEN ============================\n")
(display "=== Electrical Mesh F1 : NOMINAL / CANDIDATE ==============\n")
(display "============================================================\n")

(display "Expected output:\n")
(display "  n@node@_bnd.tdr\n")
(display "  n@node@_msh.tdr\n")

(display "Next validation:\n")
(display "  1) mesh build success\n")
(display "  2) Elements / Points\n")
(display "  3) local mesh visual QA\n")
(display "  4) proceed to SDevice baseline\n")
(display "  5) later Coarse/Nominal/Fine convergence study\n")

(display "============================================================\n")
(display "=== END F1 =================================================\n")
(display "============================================================\n")
