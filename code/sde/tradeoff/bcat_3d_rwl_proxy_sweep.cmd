;===============================================================================
; CMP - 3D RWL PROXY SWEEP
;
; Purpose:
;   Geometry-only trade-off study derived from frozen 3D-Sun-B0 Geometry v05.
;   Sweep MEB-related gate-top / DBCAT depth and calculate a normalized
;   word-line-resistance proxy from the remaining tungsten x-z cross-section.
;
; IMPORTANT:
;   - No SDevice electrical simulation.
;   - No doping or electrical mesh required.
;   - This deck does not claim absolute production RWL or RC delay.
;   - Metric: RWL_proxy(d) = A_W(36 nm) / A_W(d), using R ~ rho*L/A.
;===============================================================================

(sde:clear)
(sde:set-process-up-direction "+z")
(sdegeo:set-default-boolean "ABA")

;-------------------------------------------------------------------------------
; Primary geometry parameters
;-------------------------------------------------------------------------------
(define Lgate 0.020)
(define Drecess 0.120)
(define DBCAT @GateTopDepth@)
(define Tox 0.005)
(define Wfin 0.017)
(define Hfin 0.048)

(define Xhalf 0.060)
(define Yhalf 0.030)
(define Zbody 0.180)

;-------------------------------------------------------------------------------
; Derived parameters
;-------------------------------------------------------------------------------
(define Rgate (* 0.5 Lgate))
(define Router (+ Rgate Tox))
(define FinHalf (* 0.5 Wfin))
(define Rfin (* 0.5 Wfin))

(define ZgateTop (- DBCAT))
(define ZgateCenter (- Router Drecess))
(define ZgateBottom (- ZgateCenter Rgate))
(define ZoxideBottom (- Drecess))
(define ZfinBottom (- Hfin))
(define ZfinCapCtr (- Rfin))

;-------------------------------------------------------------------------------
; Top isolation
;-------------------------------------------------------------------------------
(define ISO
  (sdegeo:create-cuboid
    (position (- Xhalf) (- Yhalf) 0.0)
    (position Xhalf Yhalf ZfinBottom)
    "Oxide"
    "R.Isolation"
  )
)

;-------------------------------------------------------------------------------
; Broad silicon substrate
;-------------------------------------------------------------------------------
(define SISUB
  (sdegeo:create-cuboid
    (position (- Xhalf) (- Yhalf) ZfinBottom)
    (position Xhalf Yhalf (- Zbody))
    "Silicon"
    "R.SiSubstrate"
  )
)

;-------------------------------------------------------------------------------
; Saddle-fin silicon
;-------------------------------------------------------------------------------
(define SIFIN_STEM
  (sdegeo:create-cuboid
    (position (- Xhalf) (- Rfin) ZfinCapCtr)
    (position Xhalf Rfin ZfinBottom)
    "Silicon"
    "R.SiFin"
  )
)

(define SIFIN_CAP
  (sdegeo:create-cylinder
    (position (- Xhalf) 0.0 ZfinCapCtr)
    (position Xhalf 0.0 ZfinCapCtr)
    Rfin
    "Silicon"
    "R.SiFin.Cap"
  )
)

(define SIFIN
  (sdegeo:bool-unite
    (list SIFIN_STEM SIFIN_CAP)
  )
)

;-------------------------------------------------------------------------------
; Gate oxide
;-------------------------------------------------------------------------------
(define GOX_BOX
  (sdegeo:create-cuboid
    (position (- Router) (- Yhalf) 0.0)
    (position Router Yhalf ZgateCenter)
    "Oxide"
    "R.GateOxide"
  )
)

(define GOX_CYL
  (sdegeo:create-cylinder
    (position 0.0 (- Yhalf) ZgateCenter)
    (position 0.0 Yhalf ZgateCenter)
    Router
    "Oxide"
    "R.GateOxide.Bottom"
  )
)

(define GOX
  (sdegeo:bool-unite
    (list GOX_BOX GOX_CYL)
  )
)

;-------------------------------------------------------------------------------
; Tungsten buried gate
;-------------------------------------------------------------------------------
(define WG_BOX
  (sdegeo:create-cuboid
    (position (- Rgate) (- Yhalf) ZgateTop)
    (position Rgate Yhalf ZgateCenter)
    "Tungsten"
    "R.WGate"
  )
)

(define WG_CYL
  (sdegeo:create-cylinder
    (position 0.0 (- Yhalf) ZgateCenter)
    (position 0.0 Yhalf ZgateCenter)
    Rgate
    "Tungsten"
    "R.WGate.Bottom"
  )
)

(define WGATE
  (sdegeo:bool-unite
    (list WG_BOX WG_CYL)
  )
)

;-------------------------------------------------------------------------------
; Nitride above W gate
;-------------------------------------------------------------------------------
(define NIT
  (sdegeo:create-cuboid
    (position (- Rgate) (- Yhalf) 0.0)
    (position Rgate Yhalf ZgateTop)
    "Nitride"
    "R.Nitride"
  )
)

;-------------------------------------------------------------------------------
; Geometry-derived W cross-section / RWL proxy
;-------------------------------------------------------------------------------
(define PI 3.141592653589793)

; y is word-line direction, so use x-z conducting cross-section.
(define WArea_Rect
  (* (* 2.0 Rgate) (- ZgateTop ZgateCenter))
)

(define WArea_Rounded
  (* 0.5 PI Rgate Rgate)
)

(define WArea
  (+ WArea_Rect WArea_Rounded)
)

; 36 nm reference
(define DBCAT_REF 0.036)
(define ZgateTop_REF (- DBCAT_REF))

(define WArea_REF_Rect
  (* (* 2.0 Rgate) (- ZgateTop_REF ZgateCenter))
)

(define WArea_REF_Rounded
  (* 0.5 PI Rgate Rgate)
)

(define WArea_REF
  (+ WArea_REF_Rect WArea_REF_Rounded)
)

(define RWL_PROXY (/ WArea_REF WArea))
(define WArea_RATIO (/ WArea WArea_REF))
(define WArea_LOSS_FRAC (- 1.0 WArea_RATIO))
(define RWL_PENALTY_FRAC (- RWL_PROXY 1.0))

;-------------------------------------------------------------------------------
; QA / output
;-------------------------------------------------------------------------------
(display "\n")
(display "============================================================\n")
(display "=== CMP 3D RWL PROXY SWEEP ================================\n")
(display "============================================================\n")

(display "GateTopDepth / DBCAT [um] = ")
(display DBCAT)
(newline)

(display "GateTop z [um]            = ")
(display ZgateTop)
(newline)

(display "Gate center z [um]         = ")
(display ZgateCenter)
(newline)

(display "Gate bottom z [um]         = ")
(display ZgateBottom)
(newline)

(display "W rectangular area [um^2]  = ")
(display WArea_Rect)
(newline)

(display "W rounded area [um^2]      = ")
(display WArea_Rounded)
(newline)

(display "W total area [um^2]        = ")
(display WArea)
(newline)

(display "36nm reference area [um^2] = ")
(display WArea_REF)
(newline)

(display "W area ratio               = ")
(display WArea_RATIO)
(newline)

(display "W area loss fraction       = ")
(display WArea_LOSS_FRAC)
(newline)

(display "Normalized RWL proxy       = ")
(display RWL_PROXY)
(newline)

(display "RWL penalty fraction       = ")
(display RWL_PENALTY_FRAC)
(newline)

(display "Geometry overlap check:\n")
(sdegeo:check-overlap (get-body-list))

(sde:save-model "n@node@")

(display "============================================================\n")
(display "=== CMP 3D RWL PROXY : COMPLETE ===========================\n")
(display "No mesh / SDevice required for this phase.\n")
(display "============================================================\n")
