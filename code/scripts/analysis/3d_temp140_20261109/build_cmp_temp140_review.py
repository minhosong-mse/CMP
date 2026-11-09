import os,io,zipfile,hashlib
import numpy as np,pandas as pd,matplotlib.pyplot as plt
from pathlib import Path
Z=Path('/mnt/data/CMP_3D_MEB_TEMP140_PARTIAL_REVIEW.zip'); z=zipfile.ZipFile(Z)
read=lambda fn:pd.read_csv(io.BytesIO(z.read(fn)))
d=read('MEB_5x4_TEMPERATURE_METRICS_PARTIAL.csv');s=read('SPATIAL_ROI_AVAILABLE.csv');cas=read('CASE_QC_140.csv');term=read('TERMINAL_AVAILABLE_QC.csv');m=read('SOURCE_MAPPING_140.csv');
base=Path('/mnt/data');
# Derived GIDL gate versus outer fraction, reliable only where mode5 is endpoint-complete.
g=s[(s.RunMode==5)&s.roi.isin(['GATE_DRAIN','OUTER_DRAIN'])].pivot_table(index=['DBCAT_nm','TempK'],columns='roi',values='qG_positive_A',aggfunc='first')
g['gate_fraction_of_two_roi']=g['GATE_DRAIN']/(g['GATE_DRAIN']+g['OUTER_DRAIN']);g['outer_fraction_of_two_roi']=1-g['gate_fraction_of_two_roi']
g=g.reset_index()
d=d.merge(g[['DBCAT_nm','TempK','gate_fraction_of_two_roi','outer_fraction_of_two_roi']],on=['DBCAT_nm','TempK'],how='left')
cols=['DBCAT_nm','TempK','status','Vth_high_proxy_V','DIBL_proxy_mV_per_V','SS_high_window_1e10_1e8_mV_dec','Ion_Vg1p2_Vd1p2_A','Ioff_Vg0_Vd1p2_A','Hurkx_ON_minus_OFF_A','Emax_GATE_DRAIN_MV_per_cm','Emax_OUTER_DRAIN_MV_per_cm','qGpositive_GATE_DRAIN_A','qGpositive_OUTER_DRAIN_A','gate_fraction_of_two_roi']
d[cols].to_csv(base/'CMP_3D_TEMP140_ANALYSIS_TABLE.csv',index=False)
Tvals=[233,300,340,380]
plt.rcParams.update({'font.size':11,'axes.labelsize':12,'axes.titlesize':13})
def plot(col,title,ylabel,filename,log=False,ylim=None):
 fig,ax=plt.subplots(figsize=(8.0,5.1),layout='constrained')
 for t in Tvals:
  df=d[d.TempK==t].sort_values('DBCAT_nm')
  ax.plot(df.DBCAT_nm,df[col],marker='o',linewidth=2,markersize=6,label=f'{t} K')
 ax.set_xticks([36,41,48,54,60]);ax.set_xlabel('MEB depth (nm)');ax.set_ylabel(ylabel);ax.set_title(title)
 if log: ax.set_yscale('log')
 if ylim: ax.set_ylim(*ylim)
 ax.grid(True,alpha=.3);ax.legend(frameon=True);fig.savefig(base/filename,dpi=210);plt.close(fig)
plot('Hurkx_ON_minus_OFF_A','Hurkx ON − OFF terminal drain current (model-dependent)','I_ON − I_OFF (A)','CMP_TEMP140_HURKX_DEPTH.png',True)
plot('Ion_Vg1p2_Vd1p2_A','On-current versus MEB depth','Id at Vg=1.2 V, Vd=1.2 V (A)','CMP_TEMP140_ION_DEPTH.png')
plot('Ioff_Vg0_Vd1p2_A','Off-current versus MEB depth','Id at Vg=0 V, Vd=1.2 V (A)','CMP_TEMP140_IOFF_DEPTH.png',True)
plot('gate_fraction_of_two_roi','Gate-side contribution within gate/outer BTBT regions','Gate/(Gate + Outer) positive BTBT contribution','CMP_TEMP140_SPATIAL_CROSSOVER.png',False,(0,1))
# tabular report
fmt=lambda x,style='.3g': ('미확보' if pd.isna(x) else format(x,style))
def md_grid(col,scale=1,style='.3f'):
 a=d.pivot(index='DBCAT_nm',columns='TempK',values=col)*scale
 out='| MEB (nm) | 233 K | 300 K | 340 K | 380 K |\n|---:|---:|---:|---:|---:|\n'
 for meb,r in a.iterrows():out+='| '+str(meb)+' | '+' | '.join(fmt(r[t],style) for t in Tvals)+' |\n'
 return out
base36=d[(d.DBCAT_nm==36)].set_index('TempK'); v233=base36.loc[233,'Hurkx_ON_minus_OFF_A'];v300=base36.loc[300,'Hurkx_ON_minus_OFF_A']
assert len(cas)==140 and len(term)==138 and len(s)==552
mismatched=[]
import re
for dep in [36,41,48,54,60]:
 for mode in range(7):
  cm=None
  for temp in Tvals:
   n=int(m[(m.DBCAT_nm==dep)&(m.TempK==temp)&(m.RunMode==mode)].SDevice_node.iloc[0])
   p=z.read(f'PP_DECKS/DBCAT_{dep}_T{temp}_mode{mode}_n{n}_pp_des.cmd').decode()
   p=re.sub(r'\bTemperature\s*=\s*\d+','Temperature=TEMP',p)
   p=re.sub(r'\bn\d+_','nNODE_',p)
   if cm is None:cm=p
   elif p!=cm:mismatched.append((dep,mode,temp))
assert not mismatched
lines=[
'# CMP 3D MEB × Temperature 분석 — 2026-11-09',
'',
'> 입력: `CMP_3D_MEB_TEMP140_PARTIAL_REVIEW.zip` (사용자 제공). 범위: `3D-Sun-SADDLE-V1 / Flat upper S/D` 작업 베이스라인; 5 MEB × 4 T × 7 모드. 본 문서는 제공된 ZIP만으로 도출한 **내부 모델 비교**이며 실제 retention/제조 최적화 근거가 아니다.',
'',
'## 1. QC 및 출처',
'',
'- 140/140 전처리 매핑, 138/140 목표 전압 endpoint 통과, 공간 ROI 552행, Cutline 552개, 정규 터미널 QC 138개.',
'- 미완료: 36 nm / 380 K / Mode5 / n1979 / 목표 Vg −0.7 V 대비 실제 −0.66372928 V; 54 nm / 340 K / Mode1 / n1686 / 목표 Vg +2.0 V 대비 실제 +0.108366 V.',
'- 이 두 케이스는 목표 전압의 지표로 사용할 수 없으며 곡선 파일은 참고용 원시 증거로만 유지.',
'- ZIP 내부의 해당 5개 MEB 모든 온도 쌍에 대해 SDE 전처리 SHA-256 동일함. SDevice 전처리 파일도 5깊이×7모드×3비교=105 쌍에 대해 온도 숫자와 SWB 노드 출력 파일명만 제거하면 텍스트 동일(정규화 비교). 이는 비교 신뢰도를 높이지만 실제 메시 TDR의 해시 동일성/메시 수렴 검증을 대체하지 않는다.',
'- KCL_relative_max 최댓값 '+fmt(term.KCL_relative_max.max(),'.3e')+' (추출기 정의의 상대 잔차). Spatial BTBT signed=positive+negative 잔차는 `SPATIAL_ROI_AVAILABLE.csv`에 보존.',
'',
'## 2. Hurkx ON−OFF terminal drain difference (fA, Vg −0.7 V, Vd 1.2 V)',
'',
md_grid('Hurkx_ON_minus_OFF_A',1e15,'.3f'),
'',
'**해석**: 모든 비교 가능한 온도에서 MEB 깊이가 증가할수록 Hurkx-모델의 ON−OFF excess가 낮아진다. 36 nm 233 K 대비 300 K excess 증가 약 '+fmt(v300/v233,'.1f')+'배. 단 이는 순수 수집 GIDL/Retention current가 아니다.',
'',
'## 3. Ion (µA, Vg 1.2 V, Vd 1.2 V)',
'',
md_grid('Ion_Vg1p2_Vd1p2_A',1e6,'.3f'),
'',
'36→60 nm 변화: 233 K '+fmt(100*(d[(d.DBCAT_nm==60)&(d.TempK==233)].Ion_Vg1p2_Vd1p2_A.iloc[0]/d[(d.DBCAT_nm==36)&(d.TempK==233)].Ion_Vg1p2_Vd1p2_A.iloc[0]-1),'.2f')+'%, 300 K '+fmt(100*(d[(d.DBCAT_nm==60)&(d.TempK==300)].Ion_Vg1p2_Vd1p2_A.iloc[0]/d[(d.DBCAT_nm==36)&(d.TempK==300)].Ion_Vg1p2_Vd1p2_A.iloc[0]-1),'.2f')+'%.',
'',
'## 4. Ioff (fA, Vg 0 V, Vd 1.2 V)',
'',
md_grid('Ioff_Vg0_Vd1p2_A',1e15,'.3f'),
'',
'고온 380 K에서 MEB 36→60 nm 변화가 약 −4.75%에 그친다. MEB에 약하게 의존하는 off-state 배경이 고온에서 매우 커지는 경향으로 기술 가능하지만 유일한 물리 경로를 특정할 근거는 아니다.',
'',
'## 5. High-Vd subthreshold slope (mV/dec; 1e−10–1e−8 A 창 정의)',
'',
md_grid('SS_high_window_1e10_1e8_mV_dec',1,'.2f'),
'',
'**주의**: 본 SS는 추출기에서 설정한 두 전류 decade의 window SS이며 논문 원자료 또는 이전 CMP의 다른 정의와 무조건 동일시하지 않는다.',
'',
'## 6. DIBL proxy (mV/V)',
'',
md_grid('DIBL_proxy_mV_per_V',1,'.2f'),
'',
'MEB 깊이가 깊어질수록 DIBL 지표가 악화한다. 233 K의 절대 DIBL은 300–380 K보다 전반적으로 높으며, 저온에서 모든 성능 지표가 좋아진다는 식의 단정은 불가.',
'',
'## 7. 온도별 공간 BTBT 생성 기여',
'',
'정의: Mode5의 `qGpositive_GATE_DRAIN_A / (qGpositive_GATE_DRAIN_A + qGpositive_OUTER_DRAIN_A)`; 이 두 영역 간 상대 비율이며 실제 접촉 수집 분율이 아니다.',
'',
md_grid('gate_fraction_of_two_roi',100,'.1f'),
'',
'- 300 K: 41 nm 약 49.4%로 Gate/Outer crossover.',
'- 233 K: 48 nm 약 61.6%, 54 nm 약 41.1%이므로 crossover 48–54 nm 사이.',
'- 340 K: 36 nm 약 63.1%, 41 nm 약 26.2%이므로 crossover 36–41 nm 사이.',
'- 380 K: 36 nm ON 미완료로 crossover 위치 확정 불가; 41 nm에서도 Gate 기여 12.5%.',
'- Outer Emax의 x 위치가 반복적으로 x≈0.060 µm 경계에 있으므로 물리적 GIDL path로 확정하지 말고 접촉 Face91/경계·메시 감도를 검토해야 한다.',
'',
'## 8. 현재 판단과 후속 작업',
'',
'1. **재실행 우선**: n1686(54 nm/340 K/Mode1: +0.108 V에서 중단) 및 n1979(36 nm/380 K/Mode5: −0.6637 V에서 중단). 원 덱의 bias continuation/Newton/MinStep 로그를 비교하고 최소 변경으로 수렴 검증. 다른 138개는 보존.',
'2. 온도별 절대 비교의 게이트: 동일 Grid 실제 mesh SHA/mesh policy 확인, 233 K 도핑 불완전 이온화 등 모델 적용 타당성 별도 검토, 외측 드레인 경계 영역 Attribution QC 및 대표점 mesh sensitivity.',
'3. GIDL ON−OFF와 공간 BTBT는 모델 내부 비교 지표이고 1T1C SN 순누설이 아니다. 1 V→0.8 V Retention Time 주장 전에 SN 전류–전압 + C_eff 적분을 실제 3D 회로에서 검증.',
'4. 36/41/48/54/60 모두 유지하여 Trade-off/온도별 후보 범위를 비교. 아직 단일 최적 깊이 또는 물리 retention optimum 선택 불가.',
'',
'## 생성 그래프',
'',
'- `CMP_TEMP140_HURKX_DEPTH.png`: 온도별 Hurkx terminal excess (로그 축)',
'- `CMP_TEMP140_ION_DEPTH.png`: Ion 대 MEB 깊이',
'- `CMP_TEMP140_IOFF_DEPTH.png`: Vg=0 off-state 전류 (로그 축)',
'- `CMP_TEMP140_SPATIAL_CROSSOVER.png`: Gate/Outer positive BTBT 상대 분율',
'',
'## 재현 출처',
'',
'- ZIP sha256: `'+hashlib.sha256(Z.read_bytes()).hexdigest()+'`',
'- 원본 CSV: `MEB_5x4_TEMPERATURE_METRICS_PARTIAL.csv`, `SPATIAL_ROI_AVAILABLE.csv`, `HURKX_SPATIAL_ON_OFF_DELTA_PARTIAL.csv`, `TERMINAL_AVAILABLE_QC.csv`, `CASE_QC_140.csv`, `INCOMPLETE_CASES.csv`.',
'- 모든 표는 제공 ZIP의 값을 재표시한 것이며 유효점 누락은 `미확보`로 표시함.',
]
(base/'CMP_3D_TEMP140_ANALYSIS.md').write_text('\n'.join(lines),encoding='utf-8')
print('saved')
for x in ['CMP_3D_TEMP140_ANALYSIS.md','CMP_3D_TEMP140_ANALYSIS_TABLE.csv','CMP_TEMP140_HURKX_DEPTH.png','CMP_TEMP140_ION_DEPTH.png','CMP_TEMP140_IOFF_DEPTH.png','CMP_TEMP140_SPATIAL_CROSSOVER.png']:
 p=base/x;print(p, p.stat().st_size)
