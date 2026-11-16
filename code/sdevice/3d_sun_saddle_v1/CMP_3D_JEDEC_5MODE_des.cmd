* CMP 3D-Sun-SADDLE-V1 / Flat upper S/D: JEDEC-reference 5-temperature DOE
* PLANNED: source reconstructed from executed 3D DC RunModes 0/1/5/6 and
* Nov-13 IVSN pp873_des.cmd; no geometry, physics or solver changes.
* SWB: DBCAT_nm=36..60, TempK=233.15 300 340 358.15 368.15
* RunMode=0 1 5 6 7 ONLY. 0=low-Vd IdVg, 1=high-Vd IdVg,
* 5=negative gate Hurkx ON, 6=Hurkx OFF, 7=SN IVSN (Hurkx ON).
* Mode 1 additionally saves transport fields at Vg=1.2, Vd=1.2 (t=0.6).
* Preprocess all five mode branches and check pp decks before queuing.
* Unsupported modes produce no Device/Solve block; do not use 2/3/4.
#if @RunMode@ == 7
Device BCAT {
  File { Grid="@tdr@" Plot="@tdrdat@" Current="@plot@" }
  Electrode {
    { Name="source" Voltage=0.0 }
    { Name="drain" Voltage=0.0 }
    { Name="gate" Voltage=0.0 Workfunction=4.8 }
    { Name="substrate" Voltage=0.0 }
  }
  Physics { Temperature=@TempK@ Fermi }
  Physics(Material="Silicon") {
    Mobility(
      PhuMob
      Enormal(Lombardi)
      eHighFieldSaturation(GradQuasiFermi)
      hHighFieldSaturation(GradQuasiFermi)
    )
    Recombination(Band2Band(Hurkx))
  }
  Plot { Potential ElectricField/Vector eDensity hDensity Band2BandGeneration }
}

File { Output="@log@" }
Math {
  NumberOfThreads=8
  Method=Blocked SubMethod=ILS
  Extrapolate Derivatives RelErrControl
  Digits=7 Iterations=50 NotDamped=100
  ErrRef(Electron)=1.0e8 ErrRef(Hole)=1.0e8
  ExitOnFailure
}

System {
  BCAT cell ("source"=bl "drain"=sn "gate"=wl "substrate"=0)
  Capacitor_pset Ccell (sn 0) { capacitance=1e-14 }
  Vsource_pset vbl (bl 0) { dc=0.0 }
  Vsource_pset vwl (wl 0) { dc=-0.7 }
  Vsource_pset vsn (sn 0) { dc=0.0 }
  Plot "n@node@_ivsn_sys.plt" (v(sn) v(bl) v(wl) i(cell,sn) i(cell,bl) i(vsn,sn))
}

Solve {
  Coupled(Iterations=100) { Poisson Circuit }
  Coupled(Iterations=100) { cell.Poisson cell.Electron cell.Hole cell.Contact Circuit }
  NewCurrentPrefix="PRE_IVSN_"
  Quasistationary(
    InitialStep=1e-4 Increment=1.2 Decrement=2
    MinStep=1e-10 MaxStep=0.01
    Goal { Parameter=vsn.dc Value=0.8 }
  ) { Coupled { cell.Poisson cell.Electron cell.Hole cell.Contact Circuit } }

  NewCurrentPrefix="IVSN_0P8_TO_1P0_"
  Quasistationary(
    InitialStep=1e-3 Increment=1.2 Decrement=2
    MinStep=1e-10 MaxStep=0.01
    Goal { Parameter=vsn.dc Value=1.0 }
  ) {
    Coupled { cell.Poisson cell.Electron cell.Hole cell.Contact Circuit }
    CurrentPlot(Time=(Range=(0 1) Intervals=100))
  }
}
#elif @RunMode@ == 0 || @RunMode@ == 1 || @RunMode@ == 5 || @RunMode@ == 6
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
Physics { Temperature=@TempK@ Fermi }
Physics(Material="Silicon") {
  Mobility(
    PhuMob
    Enormal(Lombardi)
    eHighFieldSaturation(GradQuasiFermi)
    hHighFieldSaturation(GradQuasiFermi)
  )
#if @RunMode@ != 6
  Recombination(Band2Band(Hurkx))
#endif
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
#if @RunMode@ == 1
  eMobility
  eCurrent/Vector
#endif
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
#if @RunMode@ == 0
    Goal { Name="drain" Voltage=0.05 }
#else
    Goal { Name="drain" Voltage=1.2 }
#endif
  ) {
    Coupled(Iterations=40) { Poisson Electron Hole }
  }
  Quasistationary(
    InitialStep=1.0e-3 Increment=1.30 Decrement=2.0
    MinStep=1.0e-6 MaxStep=1.0e-2
#if @RunMode@ == 0
    Goal { Name="gate" Voltage=1.5 }
#elif @RunMode@ == 1
    Goal { Name="gate" Voltage=2.0 }
#else
    Goal { Name="gate" Voltage=-0.7 }
#endif
  ) {
    Coupled(Iterations=40) { Poisson Electron Hole }
#if @RunMode@ == 1
    Plot (FilePrefix="n@node@_ION_VG1P2" Time=(0.6) NoOverwrite)
#endif
  }
  Plot (FilePrefix="n@node@_FINAL")
}
#endif
