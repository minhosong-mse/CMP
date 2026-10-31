* CMP competition screening (SEPARATE from core CMP): 3D-Sun-SADDLE-V1 / Flat upper S/D.
* SWB split: DBCAT_nm = 24..48 integer; RunMode = 0..6.
* 0=IDVG_VD005,1=IDVG_VD12,2=IDVD_VG01,3=IDVD_VG06,4=IDVD_VG12,
* 5=GIDL_NEG_ON,6=GIDL_NEG_OFF. T=300 K, Mesh A, WF4.8eV.
* NOTE ON/OFF controls differ ONLY by Recombination(Band2Band(Hurkx)).
File {
  Grid    = "n73_msh.tdr"
  Current = "n236_des.plt"
  Plot    = "n236_des.tdr"
  Output  = "n236_des.log"
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
  Quasistationary(
    InitialStep=1.0e-3 Increment=1.30 Decrement=2.0
    MinStep=1.0e-6 MaxStep=1.0e-2
    Goal { Name="drain" Voltage=1.2 }
  ) {
    Coupled(Iterations=40) { Poisson Electron Hole }
  }
  Quasistationary(
    InitialStep=1.0e-3 Increment=1.30 Decrement=2.0
    MinStep=1.0e-6 MaxStep=1.0e-2
    Goal { Name="gate" Voltage=-0.7 }
  ) {
    Coupled(Iterations=40) { Poisson Electron Hole }
  }
  Plot (FilePrefix="n236_FINAL")
}

