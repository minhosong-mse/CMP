* CMP 3D-Sun-SADDLE-V1 GaussFactor 5-point pilot (HIGHVD_NEG), archived 2026-10-18.
* Derived from executed M1 single-bias deck; dynamic SWB mesh/output paths, same physics/math.
* Runtime numerical result PROVISIONAL; no field/BTBT or mesh-convergence claim.
File {
  Grid    = "@tdr@"
  Current = "@plot@"
  Plot    = "@tdrdat@"
  Output  = "@log@"
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
  Plot (FilePrefix="n@node@_EQ_0V")
  NewCurrentPrefix="GF_PREP_VD_HIGHVD_NEG_"
  Quasistationary(
    InitialStep=1.0e-3 Increment=1.30 Decrement=2.0
    MinStep=1.0e-6 MaxStep=1.0e-2
    Goal { Name="drain" Voltage=1.2 }
  ) {
    Coupled(Iterations=40) { Poisson Electron Hole }
  }
  Plot (FilePrefix="n@node@_HIGHVD_NEG_VDPREP_3D")
  NewCurrentPrefix="GF_IDVG_HIGHVD_NEG_"
  Quasistationary(
    InitialStep=1.0e-3 Increment=1.30 Decrement=2.0
    MinStep=1.0e-6 MaxStep=5.0e-3
    Goal { Name="gate" Voltage=-1.0 }
  ) {
    Coupled(Iterations=40) { Poisson Electron Hole }
    Plot (FilePrefix="n@node@_HIGHVD_NEG_VG_3D" Time=(0.1; 0.5; 1.0) NoOverwrite)
  }
}

