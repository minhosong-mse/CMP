# =============================================================================
# bcat_1t1c_r7_read_window.cmd
# CMP Run 7 — B0 1T1C independent D0/D1 charge-sharing read-window verification
#
# SWB:
#   AreaFactor = 0.017
#   VSN_INIT   = 0.0 / 0.9481
#
# Fixed in this smoke deck:
#   Ccell = 10 fF, CBL = 45 fF, VBL = 0.5 V
#   WL_OFF = -0.7 V, WL_READ = 3.0 V, Tread = 10 ns
#
# NOTE: independent READ feasibility, not integrated Write->Hold->Read.
# =============================================================================

Device BCAT {
  File { Grid="@tdr@" Plot="@tdrdat@" Current="@plot@" }
  Electrode {
    { Name="source" Voltage=0.0 }
    { Name="drain" Voltage=0.0 }
    { Name="gate" Voltage=0.0 WorkFunction=4.8 }
    { Name="substrate" Voltage=0.0 }
  }
  Physics {
    Temperature=300
    AreaFactor=@AreaFactor@
    Fermi
    EffectiveIntrinsicDensity(OldSlotboom)
    Mobility(DopingDep HighFieldSaturation Enormal)
    Recombination(
      SRH(DopingDep)
      Auger
      Band2Band(Model=NonlocalPath)
    )
  }
}

Math {
  Extrapolate
  RelErrControl
  Digits=6
  Iterations=50
  NotDamped=100
  ErrRef(Electron)=1.0e8
  ErrRef(Hole)=1.0e8
  Transient=BE
  Method=Blocked
  SubMethod=ParDiSo
  ExitOnFailure
}

File { Output="@log@" }

System {
  BCAT cell ("source"=bl "drain"=sn "gate"=wl "substrate"=0)

  Capacitor_pset Ccell (sn 0) { capacitance=1.0e-14 }
  Capacitor_pset Cbl   (bl 0) { capacitance=4.5e-14 }

  Set(sn=@VSN_INIT@)
  Set(bl=0.5)

  Vsource_pset vwl (wl 0) {
    pulse=(-0.7 3.0 1.0e-9 1.0e-10 1.0e-10 1.0e-8 1.0e-6)
  }

  Plot "n@node@_sys_des.plt" (
    time()
    v(bl) v(wl) v(sn)
    i(cell,bl) i(cell,sn)
    i(Cbl,bl) i(Ccell,sn)
  )
}

Solve {
  Coupled(Iterations=100){Poisson Circuit}
  Coupled(Iterations=100){cell.Poisson cell.Electron cell.Hole cell.Contact Circuit}

  Unset(sn)
  Unset(bl)

  NewCurrentFile="R7_READ_"

  Transient(
    InitialTime=0
    FinalTime=1.3e-8
    InitialStep=1.0e-12
    Increment=1.30
    Decrement=2.0
    MinStep=1.0e-15
    MaxStep=2.0e-11
  ){
    Coupled { cell.Poisson cell.Electron cell.Hole cell.Contact Circuit }
    CurrentPlot(
      Time=(
        Range=(0 1.3e-8)
        Intervals=1000
      )
    )
  }
}
