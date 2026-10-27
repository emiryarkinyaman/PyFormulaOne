# 🏎️ PyFormulaOne — Open-Wheel Motorsport Physics Engine & Regulatory Sandbox

![Status](https://img.shields.io/badge/Status-In_Development_-FFB800?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Physics](https://img.shields.io/badge/Solver-RK4_-00A86B?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

**PyFormulaOne** is a fan-made, high-fidelity, deterministic-meets-stochastic open-wheel motorsport physics engine and regulatory sandbox written in Python.

The core multi-variable physics engine has been perfected and locked in—featuring **100 Hz 4th-Order Runge-Kutta (RK4)** numerical integration, **Pacejka "Magic Formula"** tire dynamics, **underbody Venturi ground-effect aerodynamics**, **harmonic porpoising resonance**, **5-stage steel brake thermal fade**, **Virtual Dyno fuel calibration**, and **real-time Lift & Coast telemetry projection**. With the mathematical foundation complete, the project is now transitioning into its **gamification and full-grid expansion phase**.

---

## 🛠️ The Ultimate Regulatory Sandbox (1976 to 2022 & Beyond)

Zero "magic numbers" are hardcoded into the simulation loop. Every physical law, aerodynamic dependency, mechanical wear rate, and sporting rule is governed by two immutable dataclasses at the top of the engine:

* **`Physics` (`PHY`)**: 9 fundamental physical constants and unit conversion scalars (`DT = 0.01s`, gravitational acceleration, etc.).
* **`Regulations` (`REG`)**: **287 granular technical and simulation parameters** acting as master sliders for the entire motorsport universe.

### Default Era: 1976–1983 Ground Effect Golden Age

Out of the box, `REG` is calibrated to simulate an authentic late-1970s / early-1980s **Ground Effect** specification:

* **Power Unit:** 3.6L Naturally Aspirated V12 (`12,000 RPM` redline, `400 Nm` max torque, 60° or 90° bank angle, mechanical fuel injection, zero hybrid/ERS assistance).
* **Aerodynamics:** Sliding underbody skirts, Venturi diffuser tunnels, dynamic pitch/rake sensitivity (`0.80°` optimal rake), and violent high-speed aerodynamic stall (**porpoising**).
* **Drivetrain & Aids:** 5-speed manual dog-ring transaxle. ABS, Traction Control, Launch Control, and Active Aero are strictly prohibited.
* **Brakes & Tires:** Homologated high-grade steel alloy rotors (peaking between `230°C` and `540°C`, fading severely past `760°C`) paired with unheated Goodyear Slick (`Soft`, `Hard`) and Grooved (`Intermediate`, `Wet`) compounds.

### Build Your Own Era (Community Playground)

Because the entire physics engine is dynamically bound to the `Regulations` dataclass, **PyFormulaOne is a complete motorsport sandbox**:

* **Replicate 2022+ Modern Ground Effect Cars:** Increase minimum dry weight (`MIN_DRY_WEIGHT` / `MAX_DRY_WEIGHT`), raise spring stiffness (`CHASSIS_SCE_RANGE`), adjust Venturi stall heights (`FIXED_BASE_STALL_HEIGHT`), and recalibrate tire diameters and brake line pressures to mimic modern ground-effect machinery.
* **Invent Custom Eras:** Strip out underbody ground effect entirely, crank the engine redline to `19,000 RPM` to simulate 2000s V10 screamers, alter gearbox speed counts (`FIXED_TRANSMISSION_LEVEL`), or tweak tire thermal degradation multipliers to test extreme endurance regulations.

---

## ⚙️ Core Physics & Engineering Architecture

1. **100 Hz RK4 Numerical Kinematics (`estimate_RK4`)**
   Evaluates longitudinal acceleration, aerodynamic drag, rolling resistance, and mechanical thrust four times per `0.01s` timestep using Simpson's rule braking lookahead and dynamic longitudinal weight transfer.
2. **Dynamic Pitch, Rake & Porpoising Resonance (`get_ground_effect` & `is_porpoising`)**
   Calculates real-time front and rear suspension compression down to the `9 mm` skid block (`FIXED_SKID_BLOCK_THICKNESS`). If aerodynamic downforce compresses the chassis below its Venturi stall height, the car enters a damped harmonic oscillation cycle—shedding downforce rhythmically and subjecting the driver to severe vertical G-loads.
3. **Pacejka Lateral Tire Physics & Kamm Friction Circle (`get_grip` & `get_pacejka_lateral_mu`)**
   Models lateral load transfer across inner and outer tires, non-linear vertical load sensitivity ($df_z$), and Kamm circle vector coupling between longitudinal braking/traction and lateral cornering G-forces.
4. **4-State Tire Thermodynamics & Exponential Puncture Hazard (`wear_tires` & `wear_mechanics`)**
   Simulates kinetic friction heating, radiated brake heat transfer, straight-line wind chill, and standing water drainage across `Cold`, `Optimal` (`70°C–80°C`), `Hot`, and `Very Hot` states. Dropping below `57%` remaining compound life triggers a steep 16th-power exponential probability curve for sudden tire blowouts.
5. **1-Lap "Virtual Dyno" Fuel Calibration & Lift-and-Coast AI (`load_fuel`)**
   Before a session begins, the pitwall runs a silent, sub-millisecond flying lap using the car's exact RK4 physics, weather forecast, and gear ratios to meter fuel consumption down to the milliliter. From Lap 2 onward, onboard telemetry projects remaining race distance against real-time fuel burn, automatically triggering proportional **Lift & Coast** zones prior to braking points if a deficit is detected.
6. **49-Point Pre-Session Scrutineering (`SCRUTINEERING`)**
   Every entry is inspected against 49 dimensional, mass, setup, and component rating boundaries prior to track clearance. Any infraction results in immediate disqualification (`DSQ`).

---

## 🚦 Current State vs. Development Roadmap

Currently, the simulation operates in **Single-Car Time Trial / Stint Mode**. The active entry (`PROTOTYPE`) is crewed and driven by a maxed-out (`99/99` rated) "omniscient" benchmark AI crew and driver to validate pure mechanical and aerodynamic limits across 23 circuits.

### Roadmap to v1.0

- [X] **Phase 1: Core Physics Engine & Regulatory Sandbox** *(Completed)*
  - 100 Hz RK4 solver, Pacejka tire model, Ground Effect & Porpoising, Virtual Dyno fueling, Lift & Coast telemetry, 287-parameter `Regulations` architecture, and 23-track calendar.
- [ ] **Phase 2: Organic Driver & Crew AI Intelligence** *(Up Next)*
  - Transitioning away from the maxed-out "omniscient" prototype AI. Introducing human-like driver errors, imperfect weather reads, personalities, setup miscalculations, and dynamic crew strategy adaptation.
- [ ] **Phase 3: Full-Grid Free Practice (FP) & Qualifying (Q) Sessions**
  - Expanding `ENTRY_LIST` to a full multi-constructor grid competing simultaneously in 4-hour Friday Free Practice and 30-minute Saturday "Rush Hour" Qualifying sessions.
- [ ] **Phase 4: Full-Grid Grand Prix Race (R) & Gamification Loop**
  - Wheel-to-wheel multi-car race craft, dirty air / slipstream interactions, championship points tracking, R&D upgrades, and financial/contractual team management.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.10+ installed along with `numpy`, `pandas`, and `openpyxl` (required for Excel telemetry exports):

```bash
pip install numpy pandas openpyxl
```

### Running a Session

Open the script and configure the session switches at the top of the file:

```python
COUNTRY = "Japan"          # Target circuit host country (23 circuits available, e.g., "Monaco", "Belgium", "Italy", "United Kingdom")
STINT = "Qualifying"       # Options: "Free Practice", "Qualifying"
SURFACE = "Dry"            # Options: "Authentic" (dynamic weather), "Dry", "Wet", "Extreme Wet"
RUBBER = "Authentic"       # Options: "Authentic" (auto-select), "Soft", "Hard", "Intermediate", "Wet"
TELEMETRY_OUTPUT = True    # Exports high-frequency Telemetry & Lap Chart .xlsx files
SAFETY_OUTPUT = True       # Prints post-session peak Speed, Downforce, Neck G, and Vertical G reports
```

Run the simulation from your terminal:

```bash
python PyFormulaOne.py
```

### Sample Console Output

```text
✅ Scrutineering (Passed): Prototype #1 (Prototype)
⛽ Pitwall: Loaded 9L For 2 Laps
📡 Pitwall: Telemetry (Excel Output) Active
🌵 Pitwall: Radio check. Track is clear and dry.
🏁 2 Laps Of Qualifying Stint In Japanese Grand Prix
🏁 Prototype #1 (Prototype)
🏁 Lap 01 | Laptime: 1:41.284 | Track Wetness: %00 | Compound: S | Compound Left: %96 | Fuel Left: 5.14L
🏁 Lap 02 | Laptime: 1:36.812 | Track Wetness: %00 | Compound: S | Compound Left: %92 | Fuel Left: 1.42L
📡 Pitwall: Max. Speed Detected: 312 km/h
📡 Pitwall: Max. Downforce Detected: 14820 N
📡 Pitwall: Max. Neck G Detected: 4.1G
📡 Pitwall: Max. Vertical G Detected: 1.9G
```

When `TELEMETRY_OUTPUT = True`, the engine automatically generates two detailed spreadsheets in your working directory:

1. `Telemetry. <Laps>L Of <Session> In <City>. <Constructor> <Number>.xlsx` — 27-column second-by-second vehicle state log (Velocity, RPM, Gear, Thrust, Drag, Downforce, Wheel Loads, Ride Height, Brake Temp, Neck G, Vertical G, and Component Healths).
2. `Chart. <Laps>L Of <Session> In <City>. <Constructor> <Number>.xlsx` — Lap-by-lap aggregated summary chart.

---

## 🗺️ Included Circuits (23 Grand Prix Venues)

| Round | Grand Prix               | Circuit                            | Host Country (`COUNTRY`) |
| :---- | :----------------------- | :--------------------------------- | :------------------------- |
| 01    | Monaco Grand Prix        | Circuit de Monaco                  | `"Monaco"`               |
| 02    | Spanish Grand Prix       | Circuit de Barcelona-Catalunya     | `"Spain"`                |
| 03    | Brazilian Grand Prix     | Autódromo José Carlos Pace       | `"Brazil"`               |
| 04    | Mexican Grand Prix       | Autódromo Hermanos Rodríguez     | `"Mexico"`               |
| 05    | United States Grand Prix | Circuit of the Americas            | `"USA"`                  |
| 06    | Canadian Grand Prix      | Circuit Gilles Villeneuve          | `"Canada"`               |
| 07    | British Grand Prix       | Silverstone Circuit                | `"United Kingdom"`       |
| 08    | Dutch Grand Prix         | Circuit Zandvoort                  | `"Netherlands"`          |
| 09    | Belgian Grand Prix       | Circuit de Spa-Francorchamps       | `"Belgium"`              |
| 10    | French Grand Prix        | Circuit Paul Ricard                | `"France"`               |
| 11    | German Grand Prix        | Hockenheimring                     | `"Germany"`              |
| 12    | Austrian Grand Prix      | Red Bull Ring                      | `"Austria"`              |
| 13    | Italian Grand Prix       | Autodromo Nazionale Monza          | `"Italy"`                |
| 14    | Hungarian Grand Prix     | Hungaroring                        | `"Hungary"`              |
| 15    | Turkish Grand Prix       | Istanbul Park                      | `"Türkiye"`             |
| 16    | Azerbaijan Grand Prix    | Baku City Circuit                  | `"Azerbaijan"`           |
| 17    | Abu Dhabi Grand Prix     | Yas Marina Circuit                 | `"UAE"`                  |
| 18    | Bahrain Grand Prix       | Bahrain International Circuit      | `"Bahrain"`              |
| 19    | Australian Grand Prix    | Albert Park Circuit                | `"Australia"`            |
| 20    | Singapore Grand Prix     | Marina Bay Street Circuit          | `"Singapore"`            |
| 21    | Malaysian Grand Prix     | Sepang International Circuit       | `"Malaysia"`             |
| 22    | Chinese Grand Prix       | Shanghai International Circuit     | `"China"`                |
| 23    | Japanese Grand Prix      | Suzuka International Racing Course | `"Japan"`                |

---

## 📄 License

This project is licensed under the **MIT License**.

```text
MIT License

Copyright (c) 2026 Emir Yarkın Yaman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📬 Contact & Contributions

Have questions, feedback, or custom `Regulations` presets for different motorsport eras? Feel free to reach out:

* **Developer:** Emir Yarkın Yaman
* **Email:** [emiryarkinyaman@hacettepe.edu.tr](mailto:emiryarkinyaman@hacettepe.edu.tr)

*Disclaimer: This is an independent, fan-made simulation project and is not affiliated with, endorsed by, or connected to Formula 1, the FIA, or any of their subsidiaries.*
