import csv, math, json, zipfile, hashlib, argparse
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
parser = argparse.ArgumentParser(description='Plot CMP 300 K MEB Atlas evidence')
parser.add_argument('--archive', default='CMP_MEB_ATLAS_300K_EVIDENCE_PUBLIC.zip')
parser.add_argument('--out', default='CMP_300K_ATLAS_ANALYSIS')
args=parser.parse_args()
OUT=Path(args.out)
raw=list(csv.DictReader((OUT/'CMP_300K_MEB_ATLAS_MASTER_VALIDATED.csv').open()))
D=[{k:(float(v) if k!='MEB_nm' else int(v)) for k,v in r.items()} for r in raw]
m=[r['MEB_nm'] for r in D]
chartdir=OUT/'figures'; chartdir.mkdir(exist_ok=True)

# Each visual is intentionally a separate single-panel chart.
def plot(name,yseries,title,ylabel,logy=False,percent=False):
 fig,ax=plt.subplots(figsize=(8.8,4.5))
 for key,label in yseries:
  ax.plot(m,[r[key] for r in D],marker='o',markersize=4,linewidth=1.7,label=label)
 if logy:ax.set_yscale('log')
 ax.set_xticks(m);ax.tick_params(axis='x',labelrotation=45,labelsize=8)
 ax.set_xlabel('MEB depth (nm)'); ax.set_ylabel(ylabel);ax.set_title(title,fontweight='bold',fontsize=12)
 ax.axvline(48,linestyle=':',linewidth=1.1,alpha=.5,label='GateTop = Jdepth (48 nm)')
 ax.grid(axis='y',alpha=.2)
 ax.legend(loc='best',fontsize=8,ncol=2)
 fig.tight_layout()
 fig.savefig(chartdir/(name+'.png'),dpi=180)
 fig.savefig(chartdir/(name+'.svg'))
 plt.close(fig)

plot('01_terminal_current_components', [('Id_ON_signed_A_per_um','Total drain leakage (Hurkx ON)'),('Id_OFF_signed_A_per_um','Residual drain leakage (BTBT OFF)'),('Hurkx_delta_A_per_um','ON−OFF (Hurkx-sensitive)'),('qG_BTBT_A_per_um','q∫BTBT dA')], 'Leakage decomposition (300 K)', 'Drain current per width (A/um)', logy=True)
plot('02_hurkx_sensitive_fraction',[('Hurkx_sensitive_pct','ON−OFF / ON')], 'Hurkx sensitivity vs MEB', 'Hurkx-sensitive fraction (%)')
plot('03_cgd_coupling',[('Cgd_abs','|c(g,d)| @ 1 MHz')], 'Gate–drain AC matrix coupling', 'Cgd raw matrix value (F, model-internal)')
plot('04_btbt_spatial',[('BTBT_int2D_s_inv_um_inv','Integrated BTBT generation')], 'Spatial BTBT integral (300 K)', '2D integral (s^-1 um^-1)')
plot('05_btbt_active_area',[('BTBT20_area_um2','20% active-area measure')], '20%-threshold BTBT active area', 'Area (um^2)')
plot('06_dc_ion',[('Ion_12_Vg1p2_A_per_um','Ion Vg=1.2 V'),('Ion_12_Vg2_A_per_um','Ion Vg=2.0 V')], 'DC current guardrail (Vd=1.2 V)', 'Id (A/um)')
plot('07_dc_dibl',[('DIBL_mV_per_V','DIBL')], 'DC DIBL guardrail', 'DIBL (mV/V)')
plot('08_peak_btbt',[('BTBTmax_cm3s','BTBT peak')], 'BTBT peak vs MEB (nonmonotonic)', 'Generation peak (cm^-3 s^-1)')
plot('09_ehot',[('Ehot_at_BTBT_V_cm','E @ BTBT hotspot')], 'Electric field at BTBT hotspot', 'Electric field (V/cm)')

# 5 selected common fixed-cut profiles: must beware cut not representative of shallow hotspot.
z=zipfile.ZipFile(args.archive)
fig,ax=plt.subplots(figsize=(8.8,4.5))
for meb in (31,36,39,48,51):
 j=m.index(meb); node=2 if j==0 else 3*(j+1)
 fn=f'curves/MEB_GIDL/n{node}_p2_fixedcut.csv'
 dd=list(csv.DictReader(z.read(fn).decode().splitlines()))
 if dd:
  ax.plot([float(x['X_um'])*1e3 for x in dd], [max(float(x['Band2BandGeneration_cm-3s-1']),0) for x in dd], label=f'{meb} nm',linewidth=1.7)
ax.set_yscale('log');ax.set_xlim(20,65);ax.set_ylim(1e9,1e25)
ax.set_xlabel('X (nm)');ax.set_ylabel('BTBT generation along fixed Y (cm^-3 s^-1)')
ax.set_title('Common fixed-cut: Y=0.252174 um (shallow point under-samples hotspot)',fontweight='bold',fontsize=11)
ax.grid(alpha=.2);ax.legend()
fig.tight_layout();fig.savefig(chartdir/'10_selected_fixedcut_profiles.png',dpi=180);fig.savefig(chartdir/'10_selected_fixedcut_profiles.svg');plt.close(fig)

A=D[0]; N=D[2]; X=D[-1]; R39=D[3]; R41=D[4]; R48=D[11]
fmt=lambda x:f'{x:.4g}'
report=['# B0-2D-PAPER-CAL — 300 K 15-point MEB Atlas: Interim Evidence Review',
'> **Status: DATA-VALIDATED / MODEL-LINEAGE BRIDGE OPEN. Not a final physical optimum or retention conclusion.**',
'> Date: 2026-10-08. Source: user-exported `CMP_MEB_ATLAS_300K_EVIDENCE.zip` (immutable raw archive).',
'',
'## 1. Provenance and scope',
'',
'- Target main lineage: `B0-2D-PAPER-CAL / C7_4 / B_QF_HALF`, 2D simplified BCAT. Current series is a **post-freeze production-mesh branch** (Level 2).',
'- Frozen calibration inputs: `GateCouplingScale=2.300`, `GateDepthBoost=25 nm`, `Qf_Int=2.55e12 cm^-2`, `WF=4.8 eV`; no retuning in this analysis.',
'- The exact executed original 2026-10-05 FZ-C parent is **not yet recovered/bridged**. The GitHub `b0_2d_production_revalidation_plan.md` and `b0_2d_paper_cal_mesh_revalidation_20261007.md` preserve this restriction. This 15-point set establishes **within-branch** trends, not proof of mesh-only identity to the historical freeze.',
'- Biases: GIDL `Vd=1.2 V`, `Vg=-0.7 V`, 300 K, Hurkx ON/OFF; Cgd `1 MHz`, `Vd=1.2 V`, `Vg=-0.7 V`, BTBT OFF; DC `Vd=0.05/1.2 V`.',
'- MEB: `31/33/36/39/41/42/43/44/45/46/47/48/49/50/51 nm`.',
'- Imported source summary CSVs: 6 branches × 15 = 90; source curve CSVs: 105 (unchanged archive); independent check count: 1036, all passed.',
'- `GIDL_End` is **total signed drain leakage at GIDL bias**, not a pure measured BTBT component; `Cgd_abs` is a **project-internal raw AC capacitance-matrix metric**, not a calibrated production-cell overlap capacitance.',
'- 2D ∫BTBT is per-unit-width model metric. No 3D equivalence, process optimum, physical retention time, or refresh claim is supported.',
'',
'## 2. Data QC and numerical controls',
'',
'- All 90 summary files present; exact 15-point MEB coverage for each branch; no duplicates.',
'- DC endpoints and constant-current Vth reached; GIDL ON/OFF endpoints and signed currents present; AC point bias and 1 MHz verified.',
'- DC-low summary has no explicit MeshLevel column; mesh Level 2 is supported by SWB/deck lineage and all other extraction branches, not a row-wise assertion from the DC-low CSV itself.',
'- ON/OFF terminal KCL checked; max relative residual: `'+fmt(max(max(x['KCL_ON_rel'],x['KCL_OFF_rel']) for x in D))+'`.',
'- Max Cgd `|c(g,d)|` vs `|c(d,g)|` reciprocity discrepancy: `'+fmt(max(x['Cgd_reciprocity_pct'] for x in D))+'%`.',
'- Relative mismatch of signed ON−OFF vs `q*∫BTBT`: maximum `'+fmt(max(abs(x['Delta_vs_qG_err_pct']) for x in D))+'%` at 31 nm; 36–51 nm well below 0.01%. This is a **consistency/transport diagnostic** under the tested settings, not an identity guaranteed for other configurations.',
'',
'## 3. Selected data points (full 15-point values in validated master CSV)',
'',
'| MEB (nm) | Total Id ON (A/um) | Residual Id OFF (A/um) | ON−OFF (A/um) | q∫BTBT (A/um) | Hurkx-sensitive fraction | Cgd raw | Ion @ Vg=1.2 (A/um) |',
'|---:|---:|---:|---:|---:|---:|---:|---:|']
for r in D:
 report.append(f"| {r['MEB_nm']} | {r['Id_ON_signed_A_per_um']:.4e} | {r['Id_OFF_signed_A_per_um']:.4e} | {r['Hurkx_delta_A_per_um']:.4e} | {r['qG_BTBT_A_per_um']:.4e} | {r['Hurkx_sensitive_pct']:.2f}% | {r['Cgd_abs']:.4e} | {r['Ion_12_Vg1p2_A_per_um']:.4e} |")
report+=['',
'## 4. Main within-branch observations',
'',
f'- **Total current:** 31→51 nm falls {A["Id_ON_signed_A_per_um"]/X["Id_ON_signed_A_per_um"]:.1f}×; nominal 36→51 nm falls {N["Id_ON_signed_A_per_um"]/X["Id_ON_signed_A_per_um"]:.2f}×. All 15 ON currents decrease monotonically.',
f'- **Cgd:** 31→51 nm decreases {100*(1-X["Cgd_abs"]/A["Cgd_abs"]):.2f}% without sharp break at 48 nm. This indicates global coupling reduction, not direct local-field causality.',
f'- **DC penalty:** Id @Vg1.2 decreases {100*(1-X["Ion_12_Vg1p2_A_per_um"]/A["Ion_12_Vg1p2_A_per_um"]):.2f}%; Id @Vg2.0 decreases {100*(1-X["Ion_12_Vg2_A_per_um"]/A["Ion_12_Vg2_A_per_um"]):.2f}%. DIBL rises {X["DIBL_mV_per_V"]-A["DIBL_mV_per_V"]:.3f} mV/V and SSquick@Vd1.2 rises {X["SSquick_12_mV_dec"]-A["SSquick_12_mV_dec"]:.3f} mV/dec.',
'- **Peak/spatial split:** E@BTBT peaks at 39 nm; BTBTmax at 41 nm; ∫BTBT peaks at 39 nm, whereas terminal leakage falls throughout. The 20%-threshold active area decreases strongly. Peak or spatial area alone therefore cannot explain terminal leakage across all MEB.',
'- **Hurkx activation:** shallow 31–33 nm current is mostly BTBT-OFF residual; the ON−OFF fraction increases through 36 nm (16.94%), 39 nm (74.10%), 41 nm (91.19%), and 51 nm (99.81%). These fractions are *sensitivity to enabling the model*, not a decomposition proven independent of self-consistent electrostatics.',
'- **Conversion check:** ON−OFF ≈ `q∫G_BTBT dA` across all 15 points, within max 0.62% (worst 31 nm: subtraction of nearly equal currents).',
'- **48-nm model boundary:** 47→48 reduction 13.4%, 48→49 17.3%, 49→50 17.6%, 50→51 17.7%. No positive evidence of an electrical knee at 48 from terminal leakage or Cgd. `GateTop≈Jdepth=48 nm` remains a geometry/model-internal marker.',
'- **Fixed Y-cut caution:** Y=0.252174 um captures only ~5.9% of global peak at 31 nm, ~16.6% at 33 nm, and ~62.6% at 36 nm. It becomes representative for the deep side. Use the 2D silicon integral and threshold area to compare all points; fixed cut is a common location descriptor, not universal hotspot-following measure.',
'',
'## 5. Figures (one chart per file)',
'',
'1. `figures/01_terminal_current_components`: semilog total, residual, ON−OFF and q∫BTBT.',
'2. `figures/02_hurkx_sensitive_fraction`: fraction vs MEB.',
'3. `figures/03_cgd_coupling`: raw AC coupling.',
'4. `figures/04_btbt_spatial`: integrated BTBT nonmonotonicity.',
'5. `figures/05_btbt_active_area`: 20%-active area.',
'6. `figures/06_dc_ion`, `07_dc_dibl`: DC guardrails.',
'7. `figures/08_peak_btbt`, `09_ehot`: spatial peaks.',
'8. `figures/10_selected_fixedcut_profiles`: 31/36/39/48/51 nm profiles (shallow cut limitation).',
'',
'## 6. Unresolved gate before interpreting this as official PAPER-CAL replacement',
'',
'1. Reconcile 2026-10-05 executed C7_4/FZ-C parent SDE/device/extraction with current working mesh branch. Old documents explicitly classify this bridge as open. **Do not rewrite the old FZ-C freeze**.',
'2. Compare nominal (36 nm) low/high Vth, GIDL and spatial E against frozen reference under identical decks; avoid treating any absolute differences as mesh-only effects until controlled.',
'3. Residual OFF leakage at shallow MEB still lacks mechanism-resolved spatial current evidence; the ON/OFF diagnostic identifies the residual current, not its microscopic mechanism.',
'4. The current series ends at 51 nm with continued total leakage improvement; no globally optimal depth, robust window, or local 0.5/0.1 nm sweep decision is established.',
'5. Temperature and new PAPER-CAL 1T1C Write/Hold/Read/retention have not been performed on this branch. Decide selected temperature points **after** documentation/lineage gate is addressed.',
'',
'## 7. Evidence/close-out status',
'',
'- **DATA:** completed and independently QC-validated; raw user ZIP is immutable source with SHA256 manifest.',
'- **WITHIN-BRANCH MECHANISM:** strong terminal–spatial numerical consistency; separate ON vs OFF diagnostic; global Cgd correlation not asserted causal.',
'- **FZ-C EXACT-PARENT IDENTITY:** not demonstrated; explicitly open.',
'- **NEXT:** synchronize derived evidence to GitHub with this caveat; keep historical freeze unchanged; then plan temperature and 1T1C under an explicitly approved numerical lineage.',
'']
(OUT/'CMP_300K_MEB_ATLAS_INTERIM_RESEARCH_REPORT.md').write_text('\n'.join(report),encoding='utf-8')
print('Figures:',len(list(chartdir.glob('*.png'))),'PNGs +',len(list(chartdir.glob('*.svg'))),'SVGs')
print('Report:',OUT/'CMP_300K_MEB_ATLAS_INTERIM_RESEARCH_REPORT.md')
