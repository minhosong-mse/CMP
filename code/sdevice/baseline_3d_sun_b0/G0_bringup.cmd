File {
  Grid    = "@tdr@"
  Current = "@plot@"
  Plot    = "@tdrdat@"
  Output  = "@log@"
}

Electrode {
  { Name="source"    Voltage=0.0 }
  { Name="drain"     Voltage=0.0 }
  { Name="gate"      Voltage=0.0 Workfunction=4.8 }
  { Name="substrate" Voltage=0.0 }
}

Physics {
  Temperature=300
  Fermi
}

Physics(Material="Silicon") {
  Mobility(
    PhuMob
    Enormal(
      Lombardi
    )
    eHighFieldSaturation(
      GradQuasiFermi
    )
    hHighFieldSaturation(
      GradQuasiFermi
    )
  )

  Recombination(
    Band2Band(
      Hurkx
    )
  )
}

Plot {
  Potential
  ElectricField/Vector
  eDensity
  hDensity
  eCurrent/Vector
  hCurrent/Vector
  eMobility
  hMobility
  Doping
  DonorConcentration
  AcceptorConcentration
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
  -PlotLoadable
}

Solve {
  Coupled(
    Iterations=100
    LineSearchDamping=1.0e-4
  ) {
    Poisson
  }

  Coupled(
    Iterations=100
  ) {
    Poisson
    Electron
    Hole
  }

  NewCurrentPrefix="DrainRamp_"

  Quasistationary(
    InitialStep=1.0e-3
    Increment=1.35
    Decrement=2.0
    MinStep=1.0e-6
    MaxStep=1.0e-2
    Goal {
      Name="drain"
      Voltage=0.05
    }
  ) {
    Coupled(
      Iterations=40
    ) {
      Poisson
      Electron
      Hole
    }
  }

  NewCurrentPrefix="IdVg_LowVd_"

  Quasistationary(
    InitialStep=1.0e-3
    Increment=1.30
    Decrement=2.0
    MinStep=1.0e-6
    MaxStep=2.0e-2
    Goal {
      Name="gate"
      Voltage=1.20
    }
  ) {
    Coupled(
      Iterations=40
    ) {
      Poisson
      Electron
      Hole
    }
  }
}
