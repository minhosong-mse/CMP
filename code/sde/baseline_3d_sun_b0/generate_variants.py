from pathlib import Path

BASE = Path(__file__).with_name("F1_nominal.cmd")
TEXT = BASE.read_text(encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"{label}: expected source block not found")
    return text.replace(old, new, 1)


def make_h1(text: str) -> str:
    t = text
    t = t.replace(
        "; Geometry v05       - FROZEN\n; Contacts D1 v01    - FROZEN\n; Doping E1 v01      - FROZEN\n; Electrical Mesh F1 - v01 NOMINAL",
        "; Geometry v05 baseline reference\n; H1 Lgate mapping   - SENSITIVITY B / NOT FROZEN\n; Contacts D1 v01    - unchanged\n; Doping E1 v01      - unchanged except gate-edge-following window location\n; Electrical Mesh F1 - same policy / candidate",
    )
    t = t.replace(
        "; Purpose:\n;   Literature-consistent 3D BCAT baseline reconstruction.\n;   Build nominal electrical mesh for subsequent SDevice validation.",
        "; Purpose:\n;   Controlled H1 sensitivity test for the interpretation of literature Lgate.\n;   Alternative B assumes Lgate=20 nm spans the oxide-outer recess width,\n;   so W-metal width = Lgate - 2*Tox = 10 nm.\n;   All other literature inputs and the F1 mesh policy are retained.",
    )
    old = """(define Rgate
  (* 0.5 Lgate)
)

(define Router
  (+ Rgate Tox)
)"""
    new = """; H1 sensitivity interpretation B:
;   Lgate = oxide-outer recess width = 20 nm
;   Router = Lgate/2 = 10 nm
;   Rgate  = Router - Tox = 5 nm
(define Router
  (* 0.5 Lgate)
)

(define Rgate
  (- Router Tox)
)"""
    t = replace_once(t, old, new, "H1 gate mapping")
    return t


def make_h2(text: str) -> str:
    t = text
    t = t.replace(
        "; Geometry v05       - FROZEN\n; Contacts D1 v01    - FROZEN\n; Doping E1 v01      - FROZEN\n; Electrical Mesh F1 - v01 NOMINAL",
        "; Geometry v05       - baseline mapping retained\n; Contacts D1 v01    - retained\n; Doping H2          - lateral Gaussian sensitivity / NOT FROZEN\n; Electrical Mesh F1 - same policy / candidate",
    )
    t = t.replace(
        "; Purpose:\n;   Literature-consistent 3D BCAT baseline reconstruction.\n;   Build nominal electrical mesh for subsequent SDevice validation.",
        "; Purpose:\n;   H2 controlled sensitivity test for the unpublished lateral S/D Gaussian spread.\n;   Geometry, contacts, vertical junction target, peak doping, and mesh policy are retained.\n;   Only Gaussian lateral Factor is changed from 0.0 to 0.8.",
    )
    t = replace_once(
        t,
        "(define GaussFactor\n  0.0\n)",
        "(define GaussFactor\n  0.8\n)",
        "H2 GaussFactor",
    )
    return t


def apply_mesh_blocks(text: str, variant: str) -> str:
    if variant == "coarse":
        repls = {
            "  0.012\n  0.012\n  0.012\n\n  0.003\n  0.003\n  0.003": "  0.015\n  0.015\n  0.015\n\n  0.00375\n  0.00375\n  0.00375",
            "  0.003\n  0.002\n  0.002\n\n  0.001\n  0.0005\n  0.0005": "  0.00375\n  0.0025\n  0.0025\n\n  0.00125\n  0.000625\n  0.000625",
            "  0.0015\n  0.0015\n  0.0015\n\n  0.0003\n  0.0003\n  0.0003": "  0.001875\n  0.001875\n  0.001875\n\n  0.000375\n  0.000375\n  0.000375",
            '  "Oxide"\n  0.0003\n  1.5': '  "Oxide"\n  0.000375\n  1.5',
            "  0.0015\n  0.0015\n  0.0005\n\n  0.0005\n  0.0005\n  0.00025": "  0.001875\n  0.001875\n  0.000625\n\n  0.000625\n  0.000625\n  0.0003125",
            "  0.001\n  0.001\n  0.0005\n\n  0.0003\n  0.0003\n  0.0002": "  0.00125\n  0.00125\n  0.000625\n\n  0.000375\n  0.000375\n  0.00025",
        }
    elif variant == "fine":
        repls = {
            "  0.012\n  0.012\n  0.012\n\n  0.003\n  0.003\n  0.003": "  0.0096\n  0.0096\n  0.0096\n\n  0.0024\n  0.0024\n  0.0024",
            "  0.003\n  0.002\n  0.002\n\n  0.001\n  0.0005\n  0.0005": "  0.0024\n  0.0016\n  0.0016\n\n  0.0008\n  0.0004\n  0.0004",
            "  0.0015\n  0.0015\n  0.0015\n\n  0.0003\n  0.0003\n  0.0003": "  0.0012\n  0.0012\n  0.0012\n\n  0.00024\n  0.00024\n  0.00024",
            '  "Oxide"\n  0.0003\n  1.5': '  "Oxide"\n  0.00024\n  1.5',
            "  0.0015\n  0.0015\n  0.0005\n\n  0.0005\n  0.0005\n  0.00025": "  0.0012\n  0.0012\n  0.0004\n\n  0.0004\n  0.0004\n  0.0002",
            "  0.001\n  0.001\n  0.0005\n\n  0.0003\n  0.0003\n  0.0002": "  0.0008\n  0.0008\n  0.0004\n\n  0.00024\n  0.00024\n  0.00016",
        }
    else:
        raise ValueError(variant)

    t = text
    for old, new in repls.items():
        if old not in t:
            raise RuntimeError(f"{variant}: expected mesh block not found")
        t = t.replace(old, new)
    return t


def write(name: str, text: str) -> None:
    Path(__file__).with_name(name).write_text(text, encoding="utf-8")
    print(name)


write("H1_Lgate_outer20nm_sensitivity.cmd", make_h1(TEXT))
write("H2_GaussFactor_0p8_sensitivity.cmd", make_h2(TEXT))
write("F1C_coarse_mesh.cmd", apply_mesh_blocks(TEXT, "coarse"))
write("F1F_fine_mesh.cmd", apply_mesh_blocks(TEXT, "fine"))
