* CMP MEB=53 nm ONLY / numerical recovery R1 candidate
* Source lineage: 3D-Sun-SADDLE-V1 / Flat upper S/D.
* Original project: CMP_3D_Temp_49-60_Copy_Copy (MAIN account).
* Run only: (TempK,RunMode) = (358.15,1), (358.15,5), (368.15,7).
* Original failed device nodes: 3182 / 3183 / 3191; original mesh grid: 3166.
* MEB is selected by the inherited SWB SDE geometry / @tdr@; never replace it.
* Recovery method: exact GitHub CMP_3D_JEDEC_RECOVERY_R1_des.cmd core;
* only comment header was changed. No physical/bias/WF/mesh changes.
* R1 source was previously successful on 11 separate recovery cases;
* this specific 53 nm recovery has NOT been executed/validated yet.
* Edit the SDevice SOURCE in a COPIED SWB project, not ppNN_des.cmd.
* DO NOT queue any other MEB, temperatures, or modes with this dedicated copy.

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
  NumberOfThreads=32
  Method=Blocked SubMethod=ILS
  Extrapolate Derivatives RelErrControl
  Digits=7 Iterations=80 NotDamped=100
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
    InitialStep=1e-4 Increment=1.1 Decrement=2
    MinStep=1e-12 MaxStep=0.005
    Extrapolate(MinStep=1e-6)
    Goal { Parameter=vsn.dc Value=0.8 }
  ) { Coupled { cell.Poisson cell.Electron cell.Hole cell.Contact Circuit } }

  NewCurrentPrefix="IVSN_0P8_TO_1P0_"
  Quasistationary(
    InitialStep=2.5e-4 Increment=1.1 Decrement=2
    MinStep=1e-12 MaxStep=0.005
    Extrapolate(MinStep=1e-6)
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
  NumberOfThreads=32
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
#if @RunMode@ == 1 || @RunMode@ == 5
  ExitOnFailure
#endif
}
Solve {
  Coupled(Iterations=100 LineSearchDamping=1.0e-4) { Poisson }
  Coupled(Iterations=100) { Poisson Electron Hole }
  Quasistationary(
#if @RunMode@ == 1 || @RunMode@ == 5
    InitialStep=1.0e-4 Increment=1.15 Decrement=2.0
    MinStep=1.0e-9 MaxStep=5.0e-3
    Extrapolate(MinStep=1.0e-5)
#else
    InitialStep=1.0e-3 Increment=1.30 Decrement=2.0
    MinStep=1.0e-6 MaxStep=1.0e-2
#endif
#if @RunMode@ == 0
    Goal { Name="drain" Voltage=0.05 }
#else
    Goal { Name="drain" Voltage=1.2 }
#endif
  ) {
#if @RunMode@ == 1 || @RunMode@ == 5
    Coupled(Iterations=80) { Poisson Electron Hole }
#else
    Coupled(Iterations=40) { Poisson Electron Hole }
#endif
  }
  Quasistationary(
#if @RunMode@ == 1 || @RunMode@ == 5
    InitialStep=1.0e-4 Increment=1.15 Decrement=2.0
    MinStep=1.0e-9 MaxStep=5.0e-3
    Extrapolate(MinStep=1.0e-5)
#else
    InitialStep=1.0e-3 Increment=1.30 Decrement=2.0
    MinStep=1.0e-6 MaxStep=1.0e-2
#endif
#if @RunMode@ == 0
    Goal { Name="gate" Voltage=1.5 }
#elif @RunMode@ == 1
    Goal { Name="gate" Voltage=2.0 }
#else
    Goal { Name="gate" Voltage=-0.7 }
#endif
  ) {
#if @RunMode@ == 1 || @RunMode@ == 5
    Coupled(Iterations=80) { Poisson Electron Hole }
#else
    Coupled(Iterations=40) { Poisson Electron Hole }
#endif
#if @RunMode@ == 1
    Plot (FilePrefix="n@node@_ION_VG1P2" Time=(0.6) NoOverwrite)
#endif
  }
  Plot (FilePrefix="n@node@_FINAL")
}
#endif
