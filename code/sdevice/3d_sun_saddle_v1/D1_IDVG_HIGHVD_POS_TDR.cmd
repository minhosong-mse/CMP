* CMP 3D-Sun-SADDLE-V1: D1: Vd=1.2V, Vg=0->+2V (first high-Vd validation)
* Experimental: nominal geometry ONLY, W gate via Workfunction=4.8 eV.
* Physical models unchanged versus FAST Quick/P1. M1 changes SDE mesh only.
* Verify expected bias reached, TDR snapshots, and KCL before scientific use.
* T-2022.03 SDevice tested by static audit ONLY; no TCAD runtime test.
File {
  Grid    = "n1_msh.tdr"
  Current = "n8_des.plt"
  Plot    = "n8_des.tdr"
  Output  = "n8_des.log"
}
Electrode {
  { Name="source" Voltage=0.0 }
  { Name="drain" Voltage=0.0 }
  { Name="gate" Voltage=0.0 Workfunction=4.8 }
  { Name="substrate" Voltage=0.0 }
}
Physics { Temperature=300 Fermi }
Physics(Material="Silicon") {
  Mobility(
    PhuMob
    Enormal(Lombardi)
    eHighFieldSaturation(GradQuasiFermi)
    hHighFieldSaturation(GradQuasiFermi)
  )
  Recombination(Band2Band(Hurkx))
}
Plot {
  Potential
  ElectricField/Vector
  eDensity
  hDensity
  Doping
  DonorConcentration
  AcceptorConcentration
  Band2BandGeneration
}
Math {
  NumberOfThreads=8
  Method=ILS
  Extrapolate
  Derivatives
  RelErrControl
  Digits=5
  ErrRef(Electron)=1.0e8
  ErrRef(Hole)=1.0e8
  Iterations=30
  NotDamped=100
  WallClock
  CNormPrint
  -PlotLoadable
}
Solve {
  Coupled(Iterations=100 LineSearchDamping=1.0e-4) { Poisson }
  Coupled(Iterations=100) { Poisson Electron Hole }
  Plot (FilePrefix="n8_QC_EQ_0V")
  NewCurrentPrefix="M1_PREP_VD12_"
  Quasistationary(
    InitialStep=1.0e-3 Increment=1.30 Decrement=2.0
    MinStep=1.0e-6 MaxStep=1.0e-2
    Goal { Name="drain" Voltage=1.2 }
  ) {
    Coupled(Iterations=40) { Poisson Electron Hole }
  }
  Plot (FilePrefix="n8_QC_D1_VD12_VG0")
  NewCurrentPrefix="M1_IDVG_VD12_POS_"
  Quasistationary(
    InitialStep=1.0e-3 Increment=1.30 Decrement=2.0
    MinStep=1.0e-6 MaxStep=1.0e-2
    Goal { Name="gate" Voltage=2.0 }
  ) {
    Coupled(Iterations=40) { Poisson Electron Hole }
    Plot (FilePrefix="n8_QC_D1_HIGHVD_VG" Time=(0.3; 0.6; 1.0) NoOverwrite)
  }
}

