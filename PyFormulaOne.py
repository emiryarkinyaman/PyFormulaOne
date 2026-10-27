import math
import random
from dataclasses import dataclass

import numpy as np
import pandas as pd

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

COUNTRY = "Japan" # Options: Target circuit location by host country.
STINT = "Qualifying" # Options: Free Practice, Qualifying.
SURFACE = "Dry" # Options:  Authentic, Dry, Wet, Extreme Wet.
RUBBER = "Authentic" # Options: Authentic, Soft, Hard, Intermediate, Wet.
TELEMETRY_OUTPUT = True # Options: True, False.
SAFETY_OUTPUT = True # Options: True, False.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@dataclass(frozen=True)
class Physics: # 9
    GF: float
    DT: float

    FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER: float
    FIXED_VELOCITY_TO_RPM_CONVERSION_MULTIPLIER: float
    FIXED_WATT_TO_HP_CONVERSION_MULTIPLIER: float
    FIXED_METER_TO_KILOMETER_CONVERSION_MULTIPLIER: float
    FIXED_LITER_TO_CUBIC_METER_CONVERSION_MULTIPLIER: float

    MIN_VELOCITY_SENSE: float
    MAX_VELOCITY_SENSE: float
PHY = Physics(9.81,0.01,
               3.60,60.00,0.001341,1000.0,1000.0,
               0.001,0.01)

@dataclass(frozen=True)
class Regulations: # 287
    TITLE: str

    ABS_RULE: str
    ACTIVE_AERO_RULE: str
    DRIVER_PROTECTION_RULE: str
    FIXED_CLOSE_COMPETITION_MULTIPLIER: float
    FIXED_CORNERING_LOOKAHEAD_DISTANCE: float
    FIXED_LAP_TIME_ASSUMPTION: float
    FIXED_RADAR_LOOKAHEAD_DISTANCE: float
    FIXED_RADAR_SCAN_FREQ: int
    FIXED_SESSION_DISTANCE: float
    FIXED_STINT_Q: int
    FIXED_TELEMETRY_LOG_FREQ: int
    FIXED_UNRESTRICTED_TARGET_SPEED: float
    FIXED_VERTICAL_G_REFERENCE_MAX_SPEED_ASSUMPTION: float
    FIXED_WET_WEATHER_CLOSE_COMPETITION_MULTIPLIER: float
    IMPACT_TESTING_RULE: str
    LAUNCH_CONTROL_RULE: str
    LEGAL_COCKPIT_GEOMETRY: str
    LEGAL_WHEEL_RETENTION: str
    MAX_STR_SPEED_ASSUMPTION: float
    MIN_STR_SPEED_ASSUMPTION: float
    TRACTION_CONTROL_RULE: str

    FIXED_AMBIENT_WATER_COOLING_RATE: float
    FIXED_AMBIENT_WIND_COOLING_RATE: float
    FIXED_BASE_AMBIENT_TEMP: float
    FIXED_DRYING_VOLATILITY_SCALE: float
    FIXED_INITIAL_WET_TIRE_DIVISOR: float
    FIXED_LETHAL_DRY_TIRE_WET_MULTIPLIER: float
    FIXED_LETHAL_INTER_TIRE_MAX_WET_MULTIPLIER: float
    FIXED_LETHAL_INTER_TIRE_MIN_WET_MULTIPLIER: float
    FIXED_LETHAL_WET_TIRE_MIN_WET_MULTIPLIER: float
    FIXED_TRACK_AMBIENT_TEMP_SCALE: float
    FIXED_TRACK_HEAT_INDEX_MULTIPLIER: float
    FIXED_WEATHER_GEN_MAX_LAP_DURATION: float
    FIXED_WEATHER_GEN_MIN_LAP_DURATION: float
    FIXED_WEATHER_LOOKAHEAD_LAPS: int
    FIXED_WEATHER_MEAN_DRY_VALUE: float
    FIXED_WEATHER_MEAN_EXTREME_WET_VALUE: float
    FIXED_WEATHER_MEAN_WET_VALUE: float
    FIXED_WEATHER_TREND_DIVISOR: float
    FIXED_WETTING_VOLATILITY_SCALE: float
    MIN_BASE_DRYING: float
    MIN_BASE_WETTING: float

    AVG_PIT_STOP_TIME: float
    AVG_WING_REPLACEMENT_TIME: float
    CREW_RATING_RANGE: tuple
    FIXED_FRONT_WING_PIT_THRESHOLD: float
    FIXED_PIT_LIMITER_ACCEL_THROTTLE: float
    FIXED_PIT_LIMITER_BRAKE_INPUT: float
    FIXED_PIT_LIMITER_CRUISE_THROTTLE: float
    FIXED_PIT_SPEED_LIMITER_TOLERANCE: float
    FIXED_PIT_STOP_DISCIPLINE_SCALE_DIVISOR: float
    FIXED_PIT_STOP_RNG_VARIANCE_DIVISOR: float
    MAX_PIT_LANE_SPEED: float
    MAX_PIT_STOP_ERR_PROB: float
    PIT_STOP_ERR_PENALTY_RANGE: tuple

    DRIVER_BRAKING_AGGRESSION_MULTIPLIERS: tuple
    DRIVER_ENTRY_AGGRESSION_MULTIPLIERS: tuple
    DRIVER_ENTRY_TOLERANCE_MULTIPLIERS: tuple
    DRIVER_EXIT_AGGRESSION_MULTIPLIERS: tuple
    DRIVER_RATING_RANGE: tuple
    DRIVER_SHIFTING_MULTIPLIERS: tuple
    DRIVER_SMOOTHNESS_MULTIPLIERS: tuple
    DRIVER_THROTTLE_AGGRESSION_MULTIPLIERS: tuple
    FIXED_COCKPIT_MASS: float
    FIXED_CORNER_APEX_RATIO: float
    FIXED_DRIVER_SMOOTHNESS_TRACTION_DIVISOR: float
    FIXED_TRAIL_BRAKING_DECAY_EXPONENT: float
    FIXED_TRAIL_BRAKING_MAX_LIMIT: float
    MAX_DRIVER_MASS: float

    CHASSIS_CoG_HEIGHT_OPTIONS: tuple
    CHASSIS_FRH_RANGE: tuple
    CHASSIS_LENGTH_RANGE: tuple
    CHASSIS_MASS_RANGE: tuple
    CHASSIS_RATING_RANGE: tuple
    CHASSIS_RELIABILITY_RANGE: tuple
    CHASSIS_RRH_RANGE: tuple
    CHASSIS_SCE_RANGE: tuple
    CHASSIS_TRACK_HEIGHT_RANGE: tuple
    CHASSIS_TRACK_WIDTH_RANGE: tuple
    CHASSIS_WDF_RANGE: tuple
    CHASSIS_WHEELBASE_RANGE: tuple
    CHASSIS_WIDTH_RANGE: tuple
    FIXED_BASE_DAMPING_RATIO: float
    FIXED_BASE_STALL_HEIGHT: float
    FIXED_BROKEN_FRONT_WING_PENALTY_ON_AERO: float
    FIXED_CHASSIS_DAMPING_RATING_SCALE: float
    FIXED_FLOOR_AERO_DEPENDENCY: float
    FIXED_INDUCED_DRAG_MULTIPLIER: float
    FIXED_MATERIAL_QUALITY_RESISTANCE_BODYWORK: float
    FIXED_MATERIAL_QUALITY_RESISTANCE_BODYWORK_FRONT: float
    FIXED_MATERIAL_QUALITY_RESISTANCE_BODYWORK_REAR: float
    FIXED_MATERIAL_QUALITY_RESISTANCE_FLOOR: float
    FIXED_MATERIAL_QUALITY_RESISTANCE_FW: float
    FIXED_MATERIAL_QUALITY_RESISTANCE_RW: float
    FIXED_PORPOISING_RESONANCE_CYCLE: float
    FIXED_PORPOISING_SHOCK_AMPLITUDE_MULTIPLIER: float
    FIXED_PORPOISING_SPATIAL_FREQ_MULTIPLIER: float
    FIXED_PORPOISING_STALL_AMPLITUDE: float
    FIXED_PORPOISING_STALL_BASE_MULTIPLIER: float
    FIXED_RAKE_SENSE: float
    FIXED_REAR_WING_AERO_DEPENDENCY: float
    FIXED_REFERENCE_RAKE_ANGLE: float
    FIXED_SKID_BLOCK_THICKNESS: float
    FIXED_VENTURI_STALL_HEIGHT_RATING_SCALE: float
    MAX_DRY_WEIGHT: float
    MAX_SETUP_BOUNDARY: float
    MIN_DRY_WEIGHT: float
    MIN_PORPOISING_DAMPING_FLOOR: float
    MIN_RAKE_EFF: float
    MIN_SETUP_BOUNDARY: float

    ENGINE_ASPIRATION_RULE: str
    ENGINE_BANK_ANGLE_OPTIONS: tuple
    ENGINE_CONFIGURATION_RULE: str
    ENGINE_MASS_RANGE: tuple
    ENGINE_MECH_EFF_RANGE: tuple
    ENGINE_OPERATION_RULE: str
    ENGINE_RELIABILITY_RANGE: tuple
    ERS_RULE: str
    FIXED_ENGINE_DISPLACEMENT: float
    FIXED_ENGINE_PEAK_RPM_SEARCH_STEP: int
    FIXED_ENGINE_THERMAL_EFF: float
    FIXED_ENGINE_WEAR_POWER_LOSS_BASE: float
    FIXED_ENGINE_WEAR_POWER_LOSS_SCALE: float
    FIXED_IDLE_RPM: float
    FIXED_MAX_RPM: float
    FIXED_TORQUE_CURVE_BASE_MULTIPLIER: float
    FIXED_TORQUE_CURVE_DROP_RATE: float
    FIXED_TORQUE_CURVE_MAX_RPM_MULTIPLIER: float
    FIXED_TORQUE_CURVE_SQUARING_MULTIPLIER: float
    FIXED_TORQUE_DROP_EXPONENT: float
    FIXED_WATT_TO_HP_CONVERSION_MULTIPLIER: float
    MAX_THEORETICAL_ENGINE_TORQUE: float

    AVG_FIRST_GEAR_SPEED: float
    FIXED_CLUTCH_FRICTION_DISC_QUALITY_RATING: float
    FIXED_DRIVETRAIN_INERTIA_MULTIPLIER: float
    FIXED_TRANSMISSION_DOWNSHIFT_DURATION: float
    FIXED_TRANSMISSION_DRIVE_EXPONENT: float
    FIXED_TRANSMISSION_DRIVE_VALUE: float
    FIXED_TRANSMISSION_FINAL_DRIVE_SPEED_MULTIPLIER: float
    FIXED_TRANSMISSION_LEVEL: int
    FIXED_TRANSMISSION_SETUP_BOUNDARY: float
    FIXED_TRANSMISSION_SHIFT_PENALTY_BASE: float
    FIXED_TRANSMISSION_TARGET_RPM_MULTIPLIER: float
    FIXED_TRANSMISSION_TOP_SPEED_BASE_MULTIPLIER: float
    FIXED_TRANSMISSION_UPSHIFT_DURATION: float
    TRANSMISSION_FIRST_DRIVE_RATIO_RANGE: tuple
    TRANSMISSION_LAST_DRIVE_RATIO_RANGE: tuple
    TRANSMISSION_MASS_RANGE: tuple
    TRANSMISSION_MECH_EFF_RANGE: tuple
    TRANSMISSION_RELIABILITY_RANGE: tuple

    FIXED_CALIBRATION_ENGINE_HEALTH: float
    FIXED_CALIBRATION_MEASUREMENT_FUEL_VOLUME: float
    FIXED_CALIBRATION_QUALI_FUEL_VOLUME: float
    FIXED_CALIBRATION_RACE_FUEL_VOLUME: float
    FIXED_CALIBRATION_START_GEAR: int
    FIXED_CALIBRATION_START_SPEED: float
    FIXED_CALIBRATION_TIRE_WEAR_RATIO: float
    FIXED_EMPTY_FUEL_TANK_VOLUME: float
    FIXED_ENERGY_DENSITY: float
    FIXED_FUEL_DENSITY: float
    FIXED_FUEL_RESERVE_BUFFER: float
    FIXED_FUEL_TANK_MASS: float
    FIXED_FUEL_TANK_VOLUME: float
    FIXED_LIFT_AND_COAST_MIN_LAP: int
    FIXED_LIFT_AND_COAST_SEVERITY_MULTIPLIER: float
    FIXED_LIFT_AND_COAST_TIME_MULTIPLIER: float
    FIXED_PRE_NON_QUALI_SESSION_FUEL_ADDITION: float
    FIXED_PRE_QUALI_SESSION_FUEL_ADDITION: float
    FUEL_FLOW_RATE_RULE: str
    FUEL_PRESSURE_GOVERNANCE: str
    FUEL_SPEC_RULE: str
    LEGAL_FUEL_METERING_METHOD: str
    MIN_NON_QUALI_FUEL_SAFETY_MARGIN: float
    OFFICIAL_FUEL_SUPPLIER: str
    POST_SESSION_FUEL_SAMPLE_REQ: str
    REFUELING_RULE: str

    AUXILIARY_BRAKE_PREHEAT: float
    AVG_BRAKING_G: float
    BRAKE_COOLING_EFF_RANGE: tuple
    BRAKE_FRICTION_COEFF_RANGE: tuple
    BRAKE_FRONT_BIAS_RANGE: tuple
    BRAKE_RELIABILITY_RANGE: tuple
    FIXED_BRAKE_AREA: float
    FIXED_BRAKE_BASE_PRESSURE_RATIO: float
    FIXED_BRAKE_CONVECTIVE_COOLING_RATE: float
    FIXED_BRAKE_HEAT_GEN_MULTIPLIER: float
    FIXED_BRAKE_MASS: float
    FIXED_BRAKE_RADIUS: float
    FIXED_BRAKE_THERMAL_FADE_BASE: float
    FIXED_BRAKE_THERMAL_FADE_SLOPE: float
    FIXED_BRAKE_THERMAL_STAGE1_BASE: float
    FIXED_BRAKE_THERMAL_STAGE1_SLOPE: float
    FIXED_BRAKE_THERMAL_STAGE2_BASE: float
    FIXED_BRAKE_THERMAL_STAGE2_SLOPE: float
    FIXED_BRAKE_THERMAL_STAGE3_BASE: float
    FIXED_BRAKE_THERMAL_STAGE3_SLOPE: float
    FIXED_BRAKE_THERMAL_STAGE4_BASE: float
    FIXED_BRAKE_THERMAL_STAGE4_SLOPE: float
    FIXED_BRAKE_WEAR_POWER_LOSS_BASE: float
    FIXED_BRAKE_WEAR_POWER_LOSS_SCALE: float
    FIXED_STEEL_BRAKE_S_H: float
    MAX_BRAKE_LINE_PRESSURE: float
    MAX_BRAKING_DECEL_THRESHOLD: float
    MIN_BRAKE_THERMAL_FADE_FLOOR: float
    PERMITTED_BRAKE_MATERIAL: str
    STEEL_BRAKE_OPERATING_MILESTONES: tuple

    AUXILIARY_TIRE_PREHEAT: float
    FIXED_COMPOUND_AMBIENT_COOLING_RATE: float
    FIXED_COMPOUND_BRAKING_HEAT_GEN_MULTIPLIER: float
    FIXED_COMPOUND_BRAKING_PENALTY: float
    FIXED_COMPOUND_DOWNFORCE_PENALTY: float
    FIXED_COMPOUND_MECHANICAL_PENALTY: float
    FIXED_COMPOUND_SKATING_PENALTY: float
    FIXED_COMPOUND_SLIP_PENALTY: float
    FIXED_COMPOUND_SURFACE_HARSHNESS_SCALE: float
    FIXED_COMPOUND_SURFACE_PENALTY_SCALE: float
    FIXED_COMPOUND_THERMAL_VARIANCE_PENALTY: float
    FIXED_COMPOUND_TURNING_HEAT_GEN_MULTIPLIER: float
    FIXED_COMPOUND_WEAR_MULTIPLIER: float
    FIXED_COMPOUND_WEAR_PENALTY_EXPONENT: float
    FIXED_COMPOUND_WEAR_PENALTY_SCALE: float
    FIXED_COMPOUND_WRONG_TIRE_ON_EXTREME_WET_PENALTY: float
    FIXED_COMPOUND_WRONG_TIRE_ON_WET_PENALTY: float
    FIXED_CORNERING_SPEED_BINARY_SEARCH_ITERATIONS: int
    FIXED_INTER_COMPOUND_PENALTY_ON_DRY_SURFACE: float
    FIXED_KINETIC_FRICTION_FLOOR: float
    FIXED_KINETIC_FRICTION_RANGE: float
    FIXED_NON_SLICK_COMPOUND_DRAINAGE_MULTIPLIER: float
    FIXED_PACEJKA_B: float
    FIXED_PACEJKA_C: float
    FIXED_PACEJKA_E: float
    FIXED_PACEJKA_LOAD_SENSITIVITY_FACTOR: float
    FIXED_PACEJKA_NOMINAL_LOAD: float
    FIXED_PACEJKA_SLIP_ANGLE_DIVISOR: float
    FIXED_SLICK_COMPOUND_DRAINAGE_MULTIPLIER: float
    FIXED_SLICK_WET_PENALTY_MULTIPLIER: float
    FIXED_SLICK_WETNESS_PENALTY_EXPONENT: float
    FIXED_TIRE_BASE_PRESSURE: float
    FIXED_TIRE_BRAKE_HEAT_ACTIVATION_THRESHOLD: float
    FIXED_TIRE_DIAMETER: float
    FIXED_TIRE_DYNAMIC_HEAT_MULTIPLIER: float
    FIXED_TIRE_HIGH_TEMP_COOLING_MULTIPLIER: float
    FIXED_TIRE_LOW_TEMP_COOLING_MULTIPLIER: float
    FIXED_TIRE_MASS: float
    FIXED_TIRE_WEAR_RATE_DIVISOR: float
    FIXED_WET_COMPOUND_PENALTY_ON_DRY_SURFACE: float
    FIXED_WET_COMPOUND_VARIANCE_SCALE: float
    FIXED_WHEEL_RIM_TO_TIRE_RATIO: float
    LEGAL_DRY_COMPOUND_LABEL: tuple
    LEGAL_DRY_COMPOUND_SPEC: str
    LEGAL_WET_COMPOUND_LABEL: tuple
    LEGAL_WET_COMPOUND_SPEC: str
    MAX_COMPOUND_WORKING_BOUNDARY: float
    MAX_TIRE_HEAT_INDEX: float
    MIN_COMPOUND_THERMAL_STATE_MULTIPLIER: float
    MIN_COMPOUND_WORKING_BOUNDARY: float
    MIN_CORNER_RADIUS_THRESHOLD: float
    MIN_CORNERING_SPEED_SEARCH_BOUND: float
    MIN_GRIP_LIMIT_G_SENSE: float
    MIN_INTER_WET_GRIP_FACTOR: float
    MIN_KAMM_CIRCLE_GRIP_FLOOR: float
    MIN_PACEJKA_LATERAL_G_THRESHOLD: float
    MIN_PACEJKA_LOAD_SENSITIVITY: float
    MIN_SLICK_WET_GRIP_FACTOR: float
    MIN_SLICK_WET_WEAR_FACTOR: float
    MIN_TIRE_HEAT_INDEX: float
    MIN_WET_COMPOUND_GRIP_FACTOR: float
    OFFICIAL_TIRE_SUPPLIER: str
    OPTIMUM_COMPOUND_WORKING_WINDOW: tuple
    TIRE_ACTIVATION_RULE: str
    TIRE_WARMING_RULE: str

    FIXED_BRAKE_WEAR_ACTIVATION_THRESHOLD: float
    FIXED_BRAKE_WEAR_MULTIPLIER: float
    FIXED_CHASSIS_DNF_RELIABILITY_SCALE: float
    FIXED_COMPONENT_DEG_RATE_DIVISOR: float
    FIXED_COMPONENT_DNF_HEALTH_SCALE: float
    FIXED_DNF_PROBABILITY_DIVISOR: float
    FIXED_ENGINE_WEAR_MULTIPLIER: float
    FIXED_KINETIC_LOAD_STRESS_MULTIPLIER: float
    FIXED_MATERIAL_BASE_DNF_PROB: float
    FIXED_MATERIAL_WEAR_MULTIPLIER: float
    FIXED_RPM_STRESS_MULTIPLIER: float
    FIXED_TIRE_PUNCTURE_CURVE_EXPONENT: float
    FIXED_TIRE_PUNCTURE_PROB_MULTIPLIER: float
    FIXED_TIRE_PUNCTURE_WEAR_THRESHOLD: float
    FIXED_TRANSMISSION_WEAR_MULTIPLIER: float
REG = Regulations(
    "1976 Custom Regulation Rulebook",
    "STRICTLY PROHIBITED","PROHIBITED (All Aero Components Must Be Rigid)","Head Restraints MANDATORY",0.76,500.00,120.00,270.00,10,270.00,2,1,400.00,283.00,0.023,"High-Strength Steel Wheel Tethers MANDATORY","STRICTLY PROHIBITED (Manual Clutch Release)","Driver Shoulders Must Remain Inside Cockpit","Mandatory Frontal & Lateral CAS Crash Validation",343.00,100.00,"STRICTLY PROHIBITED (Manual Throttle Only)",
    5.00,1.00,25.00,0.70,1.41,0.87,0.97,0.14,0.70,10.00,2.00,23,7,3,0.000,0.767,0.347,1.17,2.70,0.04,0.01,
    14.00,11.00,(49,99),50.00,0.29,0.40,0.1197,0.50,2.00,4.00,70.00,0.83,(2.30,17.60),
    (0.054,0.067,0.083),(0.14,0.23,0.34),(1.10,1.70,2.90),(0.123,0.147,0.164),(49,99),(0.987,1.000,1.019),(2.67,2.23,1.76),(0.31,0.54,0.83),100.00,0.50,10.00,0.767,0.547,83.00,
    (0.231,0.237),(0.034,0.043),(4.10,4.30),(237.00,327.00),(49,99),(49,99),(0.043,0.054),(170000.00,230000.00),(0.90,1.00),(1.60,1.70),(0.40,0.60),(2.70,2.90),(1.90,2.00),0.34,0.017,0.64,0.009834,0.57,0.14,47.00,0.237,0.107,47.00,147.00,147.00,2.00,0.91,8.00,0.47,0.64,0.25,0.67,0.80,0.009,0.000099,740.00,1.04,570.00,0.10,0.30,0.97,
    "Pure Internal Combustion Engine & No Turbo",(60.00,90.00),"3.6L V12 (Naturally Aspirated)",(140.00,200.00),(0.76,0.99),"Unrestricted (Variable Fuel/Ignition Mapping)",(49,99),"STRICTLY PROHIBITED. No Battery, KERS, Or MGU",0.0036,40,0.294,0.96,45.00,4000.00,12000.00,1.37,0.23,0.87,0.23,1.49,0.001341,400.00,
    61.00,34.00,0.0037,0.67,0.70,2.57,20.00,5,0.20,1.04,0.94,100.00,0.34,(4.30,6.70),(1.30,3.10),(30.00,50.00),(0.76,0.99),(49,99),
    82.00,0.050,0.006,0.045,3,150.00,0.45,0.00,47600000.00,760.00,0.0012,10.00,170.00,2,4.00,3.00,0.00,4.00,"UNRESTRICTED (No Flow Limiter Applied)","Mechanical Pump - RPM Dependent","Open Mechanical Injection / Carburetion","High-octane Lead-based Racing Fuel",1.50,"Shell","Minimum 1.0L Scrutineering Sample","Strictly PROHIBITED During Track Sessions",
    140.00,2.00,(14.00,23.00),(0.34,0.43),(0.43,0.54),(49,99),0.0057,1.00,0.23,1.43,5.40,0.17,0.49,0.31,0.64,0.34,1.00,0.11,1.11,0.04,1.04,0.54,0.94,49.9,490.00,4300000.00,-0.10,0.21,"High-Grade Steel Alloy (Homologated Steel)",(170.00,230.00,540.00,760.00),
    -40.0,4.00,3.40,4.00,1.50,0.70,0.50,0.20,0.50,0.34,0.0005,1.70,0.97,2.00,0.15,12.30,10.70,20,0.83,0.87,0.11,3.00,9.40,1.40,-0.76,-0.07,1676.70,0.14,2.00,2.00,0.50,117000.00,0.10,0.67,1.04,0.05,0.10,7.85,1000000.00,0.70,0.50,0.37,("Soft","Hard"),"Slick",("Intermediate","Wet"),"Grooved",87.00,100.00,0.900,50.00,0.10,1.00,0.10,0.50,0.05,0.04,0.76,0.15,0.30,-40.0,0.60,"Goodyear",(70.00,80.00),"Kinetic Friction & Brake Heat Transfer Only","STRICTLY PROHIBITED (No Electric Blankets)",
    0.01,7100.00,50.00,100000.00,80.00,14.00,710.00,1.40,0.00217,0.04130,2.30,16.00,0.70,57.00,4710.00
)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

DNF_list_engine = [
    "Engine (Fuel Pump Failure)",
    "Engine (Fuel Vapor Lock)",
    "Engine (Fuel Injection System Failure)",
    "Engine (Throttle Linkage Stuck)",
    "Engine (Ignition System Failure)",
    "Engine (Distributor Rotor Failure)",
    "Engine (Spark Plug Misfire & Seizure)",
    "Engine (Water Pump Bearing Failure)",
    "Engine (Severe Water Overheating)",
    "Engine (Oil Radiator Puncture)",
    "Engine (Severe Oil Leak)",
    "Engine (Oil Pressure Loss)",
    "Engine (Camshaft Drive Failure)",
    "Engine (Valve Timing Gear Failure)",
    "Engine (Valve Spring Failure)",
    "Engine (Blown Head Gasket)",
    "Engine (Exhaust Manifold Crack)",
    "Engine (Piston Ring Failure)",
    "Engine (Connecting Rod Failure)",
    "Engine (Crankshaft Breakage)",
    "Engine (Cylinder Block Crack)",
    "Engine (Crankcase Explosion)",
    "Engine (Complete Terminal Seizure)"
]
DNF_list_transmission = [
    "Transmission (Clutch Slave Cylinder Failure)",
    "Transmission (Clutch Plate Seizure)",
    "Transmission (Flywheel Bolt Sheared)",
    "Transmission (Gear Linkage Disconnected)",
    "Transmission (Selector Fork Breakage)",
    "Transmission (Synchromesh Hub Failure)",
    "Transmission (Dog Ring Shattered)",
    "Transmission (2nd Gear Stripped)",
    "Transmission (3rd Gear Stripped)",
    "Transmission (4th Gear Stripped)",
    "Transmission (Input Shaft Failure)",
    "Transmission (Lay-shaft Bearing Failure)",
    "Transmission (Thrust Bearing Failure)",
    "Transmission (Crown Wheel & Pinion Failure)",
    "Transmission (Differential Seizure)",
    "Transmission (Half-shaft Breakage)",
    "Transmission (Universal Joint Sheared)",
    "Transmission (Driveshaft CV Joint Failure)",
    "Transmission (Drive-peg Sheared)",
    "Transmission (Gearbox Oil Loss)",
    "Transmission (Severe Gearbox Overheating)",
    "Transmission (Gearbox Casing Crack)",
    "Transmission (Complete Gearbox Jam)"
]
DNF_list_brakes = [
    "Brakes (Brake Pedal Pivot Failure)",
    "Brakes (Master Cylinder Failure)",
    "Brakes (Proportioning Valve Failure)",
    "Brakes (Brake Balance Bar Failure)",
    "Brakes (Brake Line Leak)",
    "Brakes (Hydraulic Pipe Burst)",
    "Brakes (Brake Fluid Leakage To Wheel)",
    "Brakes (Brake Fluid Boiling)",
    "Brakes (Complete Hydraulic Pressure Loss)",
    "Brakes (Brake Duct Debris Blockage)",
    "Brakes (Caliper Mounting Bolt Sheared)",
    "Brakes (Caliper Piston Jammed)",
    "Brakes (Front Caliper Seizure)",
    "Brakes (Rear Caliper Seizure)",
    "Brakes (Pad Backing Plate Sheared)",
    "Brakes (Severe Pad Glazing)",
    "Brakes (Severe Brake Fade & Pad Loss)",
    "Brakes (Disc Warping & Vibration)",
    "Brakes (Front Disc Crack)",
    "Brakes (Rear Disc Crack)",
    "Brakes (Steel Disc Shattered)",
    "Brakes (Overheated Disc Explosion)",
    "Brakes (Complete Terminal Brake Loss)"
]
DNF_list_car = [
    "Chassis (Steering Column Failure)",
    "Chassis (Steering Rack Jammed)",
    "Chassis (Steering Tie-rod Sheared)",
    "Chassis (Track Rod End Failure)",
    "Chassis (Front Wishbone Breakage)",
    "Chassis (Front Upright Failure)",
    "Chassis (Rear Suspension Link Failure)",
    "Chassis (Rear Upright Failure)",
    "Chassis (Rocker Arm Breakage)",
    "Chassis (Radius Rod Sheared)",
    "Chassis (Suspension Pick-up Point Failure)",
    "Chassis (Spring Coil Breakage)",
    "Chassis (Damper Shaft Sheared)",
    "Chassis (Anti-roll Bar Breakage)",
    "Chassis (Wheel Bearing Seizure)",
    "Chassis (Wheel Nut Thread Failure)",
    "Chassis (Wheel Rim Shattered)",
    "Chassis (Ground Effect Skirt Damage)",
    "Chassis (Porpoising Vibration Fatigue)",
    "Chassis (Severe Bottoming Out Damage)",
    "Chassis (Sub-frame Mounting Crack)",
    "Chassis (Monocoque Stress Crack)",
    "Chassis (Complete Structural Collapse)"
]
weather_report_dry = [
    "🌵 Pitwall: Radio check. Track is clear and dry.",
    "🌵 Pitwall: Radio check. Clear skies. We are happy with the setup. Head down, consistency is key here.",
    "🌵 Pitwall: Radio check. No weather threats. Brakes and temps look good. Push where you can.",
    "🌵 Pitwall: Radio check. Dry conditions confirmed for the whole session. Stick to the delta.",
    "🌵 Pitwall: Radio check. Zero risk of rain. Track temps are optimal. Focus on apex speeds and tire management.",
    "🌵 Pitwall: Radio check. Track is perfectly dry. We need three solid push laps. Go.",
    "🌵 Pitwall: Radio check. Bone dry. You have the track to yourself. Execute the run plan."
]
weather_report_wet = [
    "💧 Pitwall: Radio check. Conditions are tricky but stable. Find the grip off the racing line.",
    "💧 Pitwall: Radio check. Constant rain. Focus on smooth inputs. Don't spike the throttle.",
    "💧 Pitwall: Radio check. Consistent rain. Track is greasy.",
    "💧 Pitwall: Radio check. Wet conditions stable. Keep the minimum speeds up, trust the downforce.",
    "💧 Pitwall: Radio check. Rain intensity is holding. Watch the traction zones.",
    "💧 Pitwall: Radio check. Track is wet. Stay off the curbs, they are lethal right now.",
    "💧 Pitwall: Radio check. Wet track. Temps are dropping slightly, lean on the fronts to generate heat."
]
weather_report_extreme_wet = [
    "💧 Pitwall: Radio check. Track is extreme wet.",
    "💧 Pitwall: Radio check. Heavy rain. Visibility is poor. Give us feedback on the puddles.",
    "💧 Pitwall: Radio check. Track is flooded. Drive to the grip limit, do not take any risks.",
    "💧 Pitwall: Radio check. Aquaplaning risk is high. Keep it on the island. Survival mode, mate.",
    "💧 Pitwall: Radio check. Torrential conditions. Watch for rivers crossing the braking zones. Bring it home safely.",
    "💧 Pitwall: Radio check. Massive standing water. Use a higher gear for traction. Keep the car in one piece.",
    "💧 Pitwall: Radio check. Red flag conditions but we are still green. Stay away from the white lines. Just survive."
]
weather_report_authentic_wet = [
    "❓ Pitwall: Radio check. Damp track, but the sun is out. Hunt for the wet patches on the straights to save the treads.",
    "❓ Pitwall: Radio check. Track is wet. Radar shows no further rain. Look for the dry line forming off Turn 1.",
    "❓ Pitwall: Radio check. Wet start, but it's clearing up. Manage the slip, we're boxing for slicks soon.",
    "❓ Pitwall: Radio check. Keep the wets cool. We expect the track to dry rapidly in the next laps.",
    "❓ Pitwall: Radio check. Conditions are improving. Tell us when the crossover point is for slicks.",
    "❓ Pitwall: Radio check. Track is drying. Don't cook the rears. We need these tires to last until the slick window.",
    "❓ Pitwall: Radio check. Rain has stopped. Grip will increase lap by lap. Start shifting your braking points."
]
weather_report_authentic_dry = [
    "❓ Pitwall: Radio check. Radio check. Track is dry for the rollout, but radar shows a heavy cell hitting us mid-stint. Maximize the early laps.",
    "❓ Pitwall: Radio check. Slicks are good for now, but rain is close away. Keep pushing.",
    "❓ Pitwall: Radio check. Track is green, but weather is closing in. Keep the rears alive for when it gets greasy.",
    "❓ Pitwall: Radio check. Radar shows heavy rain towards the end of the stint. Maximize this dry window. Mode Push.",
    "❓ Pitwall: Radio check. Dry conditions, but rain is imminent. Keep the temps up, it's going to get tricky.",
    "❓ Pitwall: Radio check. We see the clouds. Pace is good on the slicks. Tell us when you need the inters.",
    "❓ Pitwall: Radio check. Dry for now. Drops reported at the hairpin. We need to extend this stint before the crossover."
]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # Straight: Type / Distance / Name
# # # # Corner: Type / Angle / Radius / Name
MON_MAP = [
    ["Straight",400,"Start"],
    ["Corner",90,25,"Sainte Dévote"],
    ["Straight",430,"Beau Rivage"],
    ["Corner",45,120,"Massenet"],
    ["Straight",40,"Run to Casino"],
    ["Corner",80,40,"Casino Square"],
    ["Straight",90,"Run to Mirabeau"],
    ["Corner",90,20,"Mirabeau Haute"],
    ["Straight",40,"Run to Hairpin"],
    ["Corner",180,8,"Fairmont Hairpin"],
    ["Straight",40,"Run to Mirabeau Bas"],
    ["Corner",85,22,"Mirabeau Bas"],
    ["Straight",40,"Run to Portier"],
    ["Corner",90,25,"Portier"],
    ["Straight",760,"The Tunnel"],
    ["Corner",90,20,"Nouvelle Chicane Entry"],
    ["Straight",20,"Chicane Mid"],
    ["Corner",90,25,"Nouvelle Chicane Exit"],
    ["Straight",230,"Run to Tabac"],
    ["Corner",50,55,"Tabac"],
    ["Straight",70,"Run to Swimming Pool"],
    ["Corner",60,65,"Louis Chiron Entry"],
    ["Straight",20,"Louis Chiron Mid"],
    ["Corner",60,70,"Louis Chiron Exit"],
    ["Straight",110,"Run to Piscine"],
    ["Corner",80,35,"Piscine Entry"],
    ["Straight",20,"Piscine Mid"],
    ["Corner",85,30,"Piscine Exit"],
    ["Straight",140,"Run to Rascasse"],
    ["Corner",135,15,"La Rascasse"],
    ["Straight",40,"Run to Anthony Noghès"],
    ["Corner",90,20,"Anthony Noghès"],
    ["Straight",109,"Finish"]]
ESP_MAP = [
    ["Straight",700,"Start"],
    ["Corner",85,45,"Elf Entry"],
    ["Straight",20,"Elf Mid"],
    ["Corner",70,55,"Elf Exit"],
    ["Straight",125,"Run to Renault"],
    ["Corner",140,140,"Renault"],
    ["Straight",170,"Run to Repsol"],
    ["Corner",100,60,"Repsol"],
    ["Straight",125,"Run to Seat"],
    ["Corner",110,35,"Seat"],
    ["Straight",230,"Run to Turn 6"],
    ["Corner",25,300,"Turn 6"],
    ["Straight",70,"Run to TV3"],
    ["Corner",60,65,"TV3 Entry"],
    ["Straight",20,"TV3 Mid"],
    ["Corner",50,75,"TV3 Exit"],
    ["Straight",140,"Run to Campsa"],
    ["Corner",75,130,"Campsa"],
    ["Straight",700,"Back Straight"],
    ["Corner",130,22,"La Caixa Hairpin"],
    ["Straight",70,"Run to Turn 11"],
    ["Corner",45,90,"Turn 11"],
    ["Straight",140,"Run to Banc Sabadell"],
    ["Corner",120,50,"Banc Sabadell"],
    ["Straight",70,"Run to Turn 13"],
    ["Corner",90,35,"Europcar"],
    ["Straight",40,"Run to RACC Chicane"],
    ["Corner",80,18,"RACC Chicane Entry"],
    ["Straight",20,"Chicane Mid"],
    ["Corner",85,20,"RACC Chicane Exit"],
    ["Straight",40,"Run to New Catalunya"],
    ["Corner",80,50,"New Catalunya"],
    ["Straight",490,"Finish"]]
USA_MAP = [
    ["Straight",490,"Start"],
    ["Corner",130,22,"Big Red"],
    ["Straight",140,"Run to Turn 2"],
    ["Corner",45,150,"Turn 2"],
    ["Straight",70,"Run to Esses"],
    ["Corner",60,110,"Esses 1"],
    ["Straight",20,"Esses 1-2 Mid"],
    ["Corner",65,100,"Esses 2"],
    ["Straight",20,"Esses 2-3 Mid"],
    ["Corner",70,90,"Esses 3"],
    ["Straight",20,"Esses 3-4 Mid"],
    ["Corner",75,80,"Esses 4"],
    ["Straight",20,"Esses 4-5 Mid"],
    ["Corner",60,90,"Esses 5"],
    ["Straight",40,"Run to Turn 8"],
    ["Corner",55,85,"Turn 8"],
    ["Straight",40,"Run to Turn 9"],
    ["Corner",60,95,"Turn 9"],
    ["Straight",140,"Run to Turn 10"],
    ["Corner",35,220,"Turn 10"],
    ["Straight",170,"Run to Hairpin"],
    ["Corner",145,16,"Hairpin"],
    ["Straight",1640,"Back Straight"],
    ["Corner",120,22,"Turn 12"],
    ["Straight",140,"Stadium Entry"],
    ["Corner",80,45,"Turn 13"],
    ["Straight",40,"Run to Turn 14"],
    ["Corner",80,40,"Turn 14"],
    ["Straight",40,"Run to Turn 15"],
    ["Corner",110,30,"Turn 15"],
    ["Straight",140,"Run to Carousel"],
    ["Corner",50,110,"Turn 16"],
    ["Straight",20,"Carousel Mid 1"],
    ["Corner",90,100,"Carousel"],
    ["Straight",20,"Carousel Mid 2"],
    ["Corner",90,95,"Turn 18"],
    ["Straight",90,"Run to Turn 19"],
    ["Corner",75,85,"Turn 19"],
    ["Straight",140,"Run to Turn 20"],
    ["Corner",95,35,"Turn 20"],
    ["Straight",219,"Finish"]]
CAN_MAP = [
    ["Straight",370,"Start"],
    ["Corner",60,65,"Senna S Entry"],
    ["Straight",25,"Senna S Mid"],
    ["Corner",140,22,"Senna S Hairpin"],
    ["Straight",430,"Run to Chicane 1"],
    ["Corner",65,55,"Chicane 1 Entry"],
    ["Straight",25,"Chicane 1 Mid"],
    ["Corner",60,60,"Chicane 1 Exit"],
    ["Straight",540,"Run to Turn 5"],
    ["Corner",45,120,"Turn 5"],
    ["Straight",25,"Run to Chicane 2"],
    ["Corner",75,45,"Chicane 2 Entry"],
    ["Straight",25,"Chicane 2 Mid"],
    ["Corner",70,50,"Chicane 2 Exit"],
    ["Straight",500,"Run to Turn 8"],
    ["Corner",80,45,"Chicane 3 Entry"],
    ["Straight",25,"Chicane 3 Mid"],
    ["Corner",85,40,"Chicane 3 Exit"],
    ["Straight",270,"Run to Hairpin"],
    ["Corner",180,14,"L'Epingle Hairpin"],
    ["Straight",1099,"Droit du Casino"],
    ["Corner",80,38,"Wall of Champions Entry"],
    ["Straight",25,"Chicane 4 Mid"],
    ["Corner",85,35,"Wall of Champions Exit"],
    ["Straight",270,"Finish"]]
MEX_MAP = [
    ["Straight",834,"Start"],
    ["Corner",90,25,"Turn 1"],
    ["Straight",25,"T1-T2 Mid"],
    ["Corner",45,55,"Turn 2"],
    ["Straight",25,"T2-T3 Mid"],
    ["Corner",50,60,"Turn 3"],
    ["Straight",710,"Run to Turn 4"],
    ["Corner",90,30,"Turn 4"],
    ["Straight",25,"T4-T5 Mid"],
    ["Corner",60,65,"Turn 5"],
    ["Straight",170,"Run to Turn 6"],
    ["Corner",135,18,"Hairpin"],
    ["Straight",140,"Run to Esses"],
    ["Corner",40,140,"Esses Entry"],
    ["Straight",25,"Esses 7-8 Mid"],
    ["Corner",50,130,"Turn 8"],
    ["Straight",25,"Esses 8-9 Mid"],
    ["Corner",55,120,"Turn 9"],
    ["Straight",25,"Esses 9-10 Mid"],
    ["Corner",60,110,"Turn 10"],
    ["Straight",25,"Esses 10-11 Mid"],
    ["Corner",45,125,"Esses Exit"],
    ["Straight",340,"Back Straight"],
    ["Corner",90,25,"Stadium Entry"],
    ["Straight",40,"Run to Foro Sol"],
    ["Corner",90,20,"Foro Sol Entry"],
    ["Straight",40,"Foro Sol Mid 1"],
    ["Corner",85,18,"Turn 14"],
    ["Straight",25,"Foro Sol Mid 2"],
    ["Corner",85,18,"Foro Sol Exit"],
    ["Straight",140,"Run to Peraltada"],
    ["Corner",75,55,"Peraltada Entry"],
    ["Straight",25,"Peraltada Mid"],
    ["Corner",85,65,"Nigel Mansell"],
    ["Straight",540,"Finish"]]
BRA_MAP = [
    ["Straight",376,"Start"],
    ["Corner",90,25,"S do Senna Entry"],
    ["Straight",25,"Senna S Mid"],
    ["Corner",85,35,"S do Senna Exit"],
    ["Straight",70,"Run to Curva do Sol"],
    ["Corner",110,110,"Curva do Sol"],
    ["Straight",780,"Back Straight"],
    ["Corner",90,45,"Descida do Lago Entry"],
    ["Straight",25,"Descida do Lago Mid"],
    ["Corner",45,80,"Descida do Lago Exit"],
    ["Straight",270,"Run to Ferradura"],
    ["Corner",70,60,"Ferradura Entry"],
    ["Straight",25,"Ferradura Mid"],
    ["Corner",50,75,"Ferradura Exit"],
    ["Straight",170,"Run to Laranjinha"],
    ["Corner",80,50,"Laranjinha"],
    ["Straight",40,"Run to Pinheirinho"],
    ["Corner",135,20,"Pinheirinho"],
    ["Straight",100,"Run to Bico de Pato"],
    ["Corner",145,15,"Bico de Pato"],
    ["Straight",140,"Run to Mergulhão"],
    ["Corner",45,130,"Mergulhão"],
    ["Straight",110,"Run to Junção"],
    ["Corner",95,30,"Junção"],
    ["Straight",140,"Subida dos Boxes Approach"],
    ["Corner",35,250,"Subida dos Boxes"],
    ["Straight",140,"Subida dos Boxes Mid"],
    ["Corner",30,300,"Arquibancadas"],
    ["Straight",707,"Finish"]]
GBR_MAP = [
    ["Straight",434,"Start"],
    ["Corner",45,180,"Abbey"],
    ["Straight",40,"Farm Approach"],
    ["Corner",35,200,"Farm Curve"],
    ["Straight",170,"Run to Village"],
    ["Corner",85,45,"Village"],
    ["Straight",40,"Village-Loop Mid"],
    ["Corner",140,25,"The Loop"],
    ["Straight",40,"Loop-Aintree Mid"],
    ["Corner",50,80,"Aintree"],
    ["Straight",830,"Wellington Straight"],
    ["Corner",100,55,"Brooklands"],
    ["Straight",40,"Brooklands-Luffield Mid"],
    ["Corner",160,35,"Luffield"],
    ["Straight",40,"Luffield-Woodcote Mid"],
    ["Corner",40,160,"Woodcote"],
    ["Straight",610,"National Straight"],
    ["Corner",75,140,"Copse"],
    ["Straight",230,"Run to Maggots"],
    ["Corner",40,180,"Maggots Entry"],
    ["Straight",30,"Maggots Mid"],
    ["Corner",50,150,"Maggots Crest"],
    ["Straight",30,"Becketts Approach"],
    ["Corner",65,95,"Becketts Entry"],
    ["Straight",30,"Becketts Mid"],
    ["Corner",70,85,"Becketts Exit"],
    ["Straight",30,"Run to Chapel"],
    ["Corner",45,160,"Chapel"],
    ["Straight",760,"Hangar Straight"],
    ["Corner",85,110,"Stowe"],
    ["Straight",310,"Run to Vale"],
    ["Corner",110,35,"Vale"],
    ["Straight",30,"Vale-Club Mid"],
    ["Corner",100,65,"Club"],
    ["Straight",309,"Finish"]]
NET_MAP = [
    ["Straight",276,"Start"],
    ["Corner",180,22,"Tarzanbocht"],
    ["Straight",140,"Run to Gerarddijk"],
    ["Corner",45,110,"Gerarddijkbocht"],
    ["Straight",40,"Gerarddijk-Hugenholtz Mid"],
    ["Corner",140,28,"Hugenholtzbocht"],
    ["Straight",230,"Hunserug Crest"],
    ["Corner",35,200,"Hunserug"],
    ["Straight",70,"Run to Slotemaker"],
    ["Corner",40,160,"Rob Slotemakerbocht"],
    ["Straight",140,"Approach to Scheivlak"],
    ["Corner",80,105,"Scheivlak"],
    ["Straight",230,"Run to Mastersbocht"],
    ["Corner",65,80,"Mastersbocht"],
    ["Straight",70,"Run to Turn 8"],
    ["Corner",60,75,"Turn 8"],
    ["Straight",230,"Run to Turn 9"],
    ["Corner",70,65,"Turn 9"],
    ["Straight",40,"T9-T10 Mid"],
    ["Corner",80,55,"CM.com Bocht"],
    ["Straight",640,"Back Straight"],
    ["Corner",90,22,"Hans Ernst Chicane Entry"],
    ["Straight",25,"Hans Ernst Chicane Mid"],
    ["Corner",85,25,"Hans Ernst Chicane Exit"],
    ["Straight",170,"Run to Kumho"],
    ["Corner",95,50,"Kumhobocht"],
    ["Straight",70,"Run to Luyendijk"],
    ["Corner",110,210,"Arie Luyendijkbocht"],
    ["Straight",400,"Finish"]]
BEL_MAP = [
    ["Straight",430,"Start"],
    ["Corner",180,15,"La Source"],
    ["Straight",2300,"Eau Rouge to Kemmel"],
    ["Corner",90,60,"Les Combes Entry"],
    ["Straight",20,"Les Combes Mid"],
    ["Corner",95,55,"Les Combes Exit"],
    ["Straight",20,"Run to Malmedy"],
    ["Corner",80,50,"Malmedy"],
    ["Straight",100,"Post-Malmedy"],
    ["Corner",180,45,"Bruxelles"],
    ["Straight",20,"Run to Speaker's"],
    ["Corner",90,65,"Speaker's"],
    ["Straight",500,"Post-Speaker's"],
    ["Corner",80,190,"Pouhon Entry"],
    ["Straight",40,"Pouhon Mid"],
    ["Corner",80,190,"Pouhon Exit"],
    ["Straight",300,"Post-Pouhon"],
    ["Corner",90,75,"Fagnes Entry"],
    ["Straight",20,"Fagnes Mid"],
    ["Corner",90,80,"Fagnes Exit"],
    ["Straight",20,"Run to Stavelot"],
    ["Corner",85,95,"Stavelot"],
    ["Straight",20,"Run to Paul Frère"],
    ["Corner",45,160,"Paul Frère"],
    ["Straight",1400,"Blanchimont"],
    ["Corner",90,20,"Bus-stop Entry"],
    ["Straight",20,"Bus-stop Mid"],
    ["Corner",90,20,"Bus-stop Exit"],
    ["Straight",145,"Finish"]]
FRA_MAP = [
    ["Straight",540,"Start"],
    ["Corner",85,45,"S de la Verrerie Entry"],
    ["Straight",40,"Verrerie Mid"],
    ["Corner",70,50,"S de la Verrerie Exit"],
    ["Straight",370,"Run to Hotel"],
    ["Corner",80,55,"Virage de l'Hôtel"],
    ["Straight",70,"Run to Camp"],
    ["Corner",75,45,"Virage du Camp"],
    ["Straight",230,"Run to Turn 5"],
    ["Corner",60,80,"Turn 5"],
    ["Straight",140,"Run to Sainte Baume"],
    ["Corner",65,70,"Sainte Baume Entry"],
    ["Straight",30,"Sainte Baume Mid"],
    ["Corner",50,85,"Sainte Baume Exit"],
    ["Straight",940,"Mistral Straight I"],
    ["Corner",90,30,"Chicane Nord Entry"],
    ["Straight",40,"Chicane Nord Mid"],
    ["Corner",85,35,"Chicane Nord Exit"],
    ["Straight",1040,"Mistral Straight II"],
    ["Corner",40,300,"Virage de Signes"],
    ["Straight",230,"Run to Beausset"],
    ["Corner",150,75,"Double Droite du Beausset"],
    ["Straight",140,"Run to Bendor"],
    ["Corner",90,40,"Virage de Bendor"],
    ["Straight",170,"Run to Garlaban"],
    ["Corner",70,60,"Courbe du Garlaban"],
    ["Straight",90,"Run to Lac"],
    ["Corner",90,30,"Virage du Lac"],
    ["Straight",40,"Run to Virage du Pont"],
    ["Corner",100,25,"Virage du Pont"],
    ["Straight",500,"Finish"]]
GER_MAP = [
    ["Straight",430,"Start"],
    ["Corner",100,85,"Nordkurve"],
    ["Straight",300,"Run to Einfahrt Parabolika"],
    ["Corner",75,50,"Einfahrt Parabolika"],
    ["Straight",1400,"Parabolika Main Straight"],
    ["Corner",180,10,"Spitzkehre Hairpin"],
    ["Straight",470,"Run to Mercedes-Tribüne"],
    ["Corner",90,45,"Mercedes-Tribüne Entry"],
    ["Straight",40,"Mercedes Mid"],
    ["Corner",110,35,"Mercedes-Tribüne Exit"],
    ["Straight",250,"Run to Mobil 1"],
    ["Corner",70,60,"Mobil 1 Kurve"],
    ["Straight",310,"Run to Motodrom"],
    ["Corner",45,90,"Sachs Approach"],
    ["Straight",140,"Stadium Entry"],
    ["Corner",140,25,"Sachs-Kurve"],
    ["Straight",178,"Run to Südkurve"],
    ["Corner",75,55,"Südkurve 1"],
    ["Straight",40,"Südkurve Mid"],
    ["Corner",85,60,"Südkurve 2"],
    ["Straight",267,"Finish"]]
AUT_MAP = [
    ["Straight",501,"Start"],
    ["Corner",85,38,"Niki Lauda Kurve"],
    ["Straight",1140,"Run to Remus"],
    ["Corner",135,15,"Remus Hairpin"],
    ["Straight",700,"Schlossgold Approach Downhill"],
    ["Corner",95,45,"Schlossgold"],
    ["Straight",300,"Run to Turn 5"],
    ["Corner",55,95,"Outer Kink"],
    ["Straight",171,"Run to Rauch"],
    ["Corner",85,60,"Rauch"],
    ["Straight",171,"Run to Wurth"],
    ["Corner",70,65,"Wurth Kurve"],
    ["Straight",171,"Run to Rindt Approach"],
    ["Corner",50,85,"Turn 8"],
    ["Straight",141,"Run to Rindt"],
    ["Corner",80,55,"Rindt Kurve"],
    ["Straight",127,"Run to Cashback"],
    ["Corner",80,48,"Cashback"],
    ["Straight",251,"Finish"]]
ITA_MAP = [
    ["Straight",1317,"Start"],
    ["Corner",90,15,"Variante del Rettifilo Entry"],
    ["Straight",25,"Rettifilo Mid"],
    ["Corner",85,18,"Variante del Rettifilo Exit"],
    ["Straight",1140,"Run to Roggia"],
    ["Corner",80,25,"Variante della Roggia Entry"],
    ["Straight",20,"Roggia Mid"],
    ["Corner",80,28,"Variante della Roggia Exit"],
    ["Straight",170,"Run to Lesmo 1"],
    ["Corner",65,60,"Lesmo 1"],
    ["Straight",170,"Run to Lesmo 2"],
    ["Corner",70,50,"Lesmo 2"],
    ["Straight",699,"Run to Ascari"],
    ["Corner",60,65,"Variante Ascari Entry"],
    ["Straight",25,"Ascari Mid 1"],
    ["Corner",45,80,"Variante Ascari Mid"],
    ["Straight",25,"Ascari Mid 2"],
    ["Corner",60,70,"Variante Ascari Exit"],
    ["Straight",1000,"Run to Parabolica"],
    ["Corner",180,110,"Parabolica"],
    ["Straight",400,"Finish"]]
HUN_MAP = [
    ["Straight",670,"Start"],
    ["Corner",160,18,"Turn 1"],
    ["Straight",390,"Run to Turn 2"],
    ["Corner",170,22,"Turn 2"],
    ["Straight",670,"Run to Turn 4"],
    ["Corner",70,75,"Mansell"],
    ["Straight",230,"Run to Turn 5"],
    ["Corner",110,40,"Turn 5"],
    ["Straight",143,"Run to Chicane"],
    ["Corner",85,20,"Chicane Entry"],
    ["Straight",25,"Chicane Mid"],
    ["Corner",85,25,"Chicane Exit"],
    ["Straight",110,"Run to Turn 8"],
    ["Corner",70,45,"Turn 8"],
    ["Straight",25,"Run to Turn 9"],
    ["Corner",75,45,"Turn 9"],
    ["Straight",140,"Run to Turn 10"],
    ["Corner",35,200,"Turn 10"],
    ["Straight",230,"Run to Turn 11"],
    ["Corner",85,60,"Turn 11"],
    ["Straight",140,"Run to Turn 12"],
    ["Corner",90,25,"Turn 12"],
    ["Straight",170,"Run to Turn 13"],
    ["Corner",170,18,"Turn 13"],
    ["Straight",270,"Run to Turn 14"],
    ["Corner",170,20,"Turn 14"],
    ["Straight",340,"Finish"]]
TUR_MAP = [
    ["Straight",500,"Start"],
    ["Corner",90,50,"Turn 1"],
    ["Straight",40,"Run to Turn 2"],
    ["Corner",90,90,"Turn 2"],
    ["Straight",400,"Run to Turn 3"],
    ["Corner",60,100,"Turn 3"],
    ["Straight",40,"Turn 3-4 Mid"],
    ["Corner",90,40,"Turn 4"],
    ["Straight",40,"Turn 4-5 Mid"],
    ["Corner",70,80,"Turn 5"],
    ["Straight",200,"Run to Turn 6"],
    ["Corner",90,60,"Turn 6"],
    ["Straight",400,"Run to Turn 7"],
    ["Corner",45,150,"Turn 7"],
    ["Straight",40,"Run to Turn 8"],
    ["Corner",200,160,"Turn 8"],
    ["Straight",140,"Run to Turn 9"],
    ["Corner",90,50,"Turn 9"],
    ["Straight",40,"Turn 9-10 Mid"],
    ["Corner",90,50,"Turn 10"],
    ["Straight",1400,"Back Straight"],
    ["Corner",90,30,"Turn 12"],
    ["Straight",40,"Turn 12-13 Mid"],
    ["Corner",90,35,"Turn 13"],
    ["Straight",40,"Turn 13-14 Mid"],
    ["Corner",90,45,"Turn 14"],
    ["Straight",431,"Finish"]]
AZE_MAP = [
    ["Straight",230,"Start"],
    ["Corner",90,25,"Turn 1"],
    ["Straight",340,"Run to Turn 2"],
    ["Corner",90,25,"Turn 2"],
    ["Straight",830,"Run to Turn 3"],
    ["Corner",90,25,"Turn 3"],
    ["Straight",140,"Run to Turn 4"],
    ["Corner",90,25,"Turn 4"],
    ["Straight",110,"Run to Turn 5"],
    ["Corner",80,40,"Chicane Entry"],
    ["Straight",15,"T5-T6 Mid"],
    ["Corner",85,35,"Chicane Exit"],
    ["Straight",140,"Run to Turn 7"],
    ["Corner",90,25,"Turn 7"],
    ["Straight",140,"Run to Castle Section"],
    ["Corner",90,12,"Castle Entry"],
    ["Straight",15,"Castle Mid 1"],
    ["Corner",45,15,"Turn 9"],
    ["Straight",15,"Castle Mid 2"],
    ["Corner",45,15,"Turn 10"],
    ["Straight",15,"Castle Mid 3"],
    ["Corner",80,15,"Turn 11"],
    ["Straight",100,"Run to Turn 12"],
    ["Corner",60,25,"Turn 12"],
    ["Straight",140,"Run to Turn 13"],
    ["Corner",90,20,"Turn 13"],
    ["Straight",70,"Run to Turn 14"],
    ["Corner",45,30,"Turn 14"],
    ["Straight",140,"Run to Turn 15"],
    ["Corner",80,35,"Downhill"],
    ["Straight",270,"Run to Turn 16"],
    ["Corner",90,25,"Turn 16"],
    ["Straight",2757,"Finish"]]
ABU_MAP = [
    ["Straight",541,"Start"],
    ["Corner",85,45,"Turn 1"],
    ["Straight",200,"Run to Turn 2"],
    ["Corner",45,120,"Turn 2"],
    ["Straight",25,"T2-T3 Mid"],
    ["Corner",60,100,"Turn 3"],
    ["Straight",40,"T3-T4 Mid"],
    ["Corner",90,80,"Turn 4"],
    ["Straight",170,"Run to Chicane"],
    ["Corner",90,25,"Chicane Entry"],
    ["Straight",25,"T5-T6 Mid"],
    ["Corner",90,25,"Chicane Exit"],
    ["Straight",40,"Run to Hairpin"],
    ["Corner",180,12,"Hairpin"],
    ["Straight",1710,"Back Straight 1"],
    ["Corner",90,20,"Chicane Entry"],
    ["Straight",25,"T8-T9 Mid"],
    ["Corner",90,20,"Chicane Exit"],
    ["Straight",25,"T9-T10 Mid"],
    ["Corner",30,200,"Sweeper"],
    ["Straight",700,"Back Straight 2"],
    ["Corner",90,25,"Marina Complex Entry"],
    ["Straight",25,"T11-T12 Mid"],
    ["Corner",90,25,"Marina Complex Mid"],
    ["Straight",25,"T12-T13 Mid"],
    ["Corner",60,60,"Marina Complex Exit"],
    ["Straight",70,"Run to Turn 14"],
    ["Corner",90,35,"Turn 14"],
    ["Straight",140,"Run to Turn 15"],
    ["Corner",90,40,"Turn 15"],
    ["Straight",20,"T15-T16 Mid"],
    ["Corner",90,40,"Turn 16"],
    ["Straight",70,"Run to Hotel"],
    ["Corner",90,30,"Hotel Entry"],
    ["Straight",25,"Hotel Mid 1"],
    ["Corner",90,30,"Underpass"],
    ["Straight",25,"Hotel Mid 2"],
    ["Corner",90,30,"Hotel Exit"],
    ["Straight",140,"Run to Turn 20"],
    ["Corner",90,45,"Turn 20"],
    ["Straight",70,"Run to Turn 21"],
    ["Corner",90,40,"Turn 21"],
    ["Straight",171,"Finish"]]
BHR_MAP = [
    ["Straight",830,"Start"],
    ["Corner",120,20,"Michael Schumacher"],
    ["Straight",25,"T1-T2 Mid"],
    ["Corner",65,45,"Turn 2"],
    ["Straight",990,"Run to Turn 4"],
    ["Corner",100,30,"Turn 4"],
    ["Straight",230,"Run to Turn 5"],
    ["Corner",60,110,"Turn 5"],
    ["Straight",25,"T5-T6 Mid"],
    ["Corner",50,100,"Turn 6"],
    ["Straight",25,"T6-T7 Mid"],
    ["Corner",60,90,"Turn 7"],
    ["Straight",170,"Run to Turn 8"],
    ["Corner",150,18,"Hairpin"],
    ["Straight",230,"Run to Turn 9"],
    ["Corner",60,50,"Turn 9"],
    ["Straight",25,"T9-T10 Mid"],
    ["Corner",110,25,"Off-camber"],
    ["Straight",570,"Back Straight 1"],
    ["Corner",80,55,"Turn 11"],
    ["Straight",369,"Back Straight 2"],
    ["Corner",85,45,"Turn 13"],
    ["Straight",570,"Run to Turn 14"],
    ["Corner",85,40,"Turn 14"],
    ["Straight",40,"T14-T15 Mid"],
    ["Corner",45,65,"Turn 15"],
    ["Straight",470,"Finish"]]
AUS_MAP = [
    ["Straight",609,"Start"],
    ["Corner",85,45,"Jones"],
    ["Straight",25,"T1-T2 Mid"],
    ["Corner",75,55,"Brabham"],
    ["Straight",500,"Run to Turn 3"],
    ["Corner",95,25,"Sports Centre"],
    ["Straight",25,"T3-T4 Mid"],
    ["Corner",85,30,"Turn 4"],
    ["Straight",300,"Run to Whiteford"],
    ["Corner",35,180,"Whiteford"],
    ["Straight",300,"Run to Turn 6"],
    ["Corner",85,35,"Turn 6"],
    ["Straight",170,"Run to Turn 7"],
    ["Corner",40,150,"Turn 7"],
    ["Straight",170,"Run to Turn 8"],
    ["Corner",45,130,"Turn 8"],
    ["Straight",300,"Run to Clark Chicane"],
    ["Corner",90,25,"Clark Chicane Entry"],
    ["Straight",25,"T9-T10 Mid"],
    ["Corner",85,30,"Clark Chicane Exit"],
    ["Straight",670,"Lakeside Drive"],
    ["Corner",65,80,"Fast Chicane Entry"],
    ["Straight",25,"T11-T12 Mid"],
    ["Corner",55,95,"Waite"],
    ["Straight",300,"Run to Ascari"],
    ["Corner",90,35,"Ascari"],
    ["Straight",170,"Run to Stewart"],
    ["Corner",65,75,"Stewart"],
    ["Straight",300,"Run to Prost"],
    ["Corner",110,22,"Prost"],
    ["Straight",40,"T15-T16 Mid"],
    ["Corner",85,40,"Turn 16"],
    ["Straight",274,"Finish"]]
SIN_MAP = [
    ["Straight",274,"Start"],
    ["Corner",90,25,"Turn 1"],
    ["Straight",20,"T1-T2 Mid"],
    ["Corner",45,20,"Turn 2"],
    ["Straight",20,"T2-T3 Mid"],
    ["Corner",60,25,"Turn 3"],
    ["Straight",170,"Run to Turn 4"],
    ["Corner",90,20,"Turn 4"],
    ["Straight",270,"Run to Turn 5"],
    ["Corner",90,25,"Turn 5"],
    ["Straight",70,"Run to Turn 6"],
    ["Corner",90,20,"Turn 6"],
    ["Straight",1000,"Raffles Boulevard"],
    ["Corner",90,25,"Turn 7"],
    ["Straight",20,"T7-T8 Mid"],
    ["Corner",90,20,"Turn 8"],
    ["Straight",170,"Run to Turn 9"],
    ["Corner",90,20,"Turn 9"],
    ["Straight",340,"St. Andrew's Road"],
    ["Corner",80,15,"Singapore Sling Entry"],
    ["Straight",20,"Sling Mid 1"],
    ["Corner",85,15,"Singapore Sling Mid"],
    ["Straight",20,"Sling Mid 2"],
    ["Corner",80,15,"Singapore Sling Exit"],
    ["Straight",140,"Run to Turn 11"],
    ["Corner",90,25,"Turn 11"],
    ["Straight",110,"Anderson Bridge"],
    ["Corner",45,30,"Turn 12"],
    ["Straight",70,"Run to Turn 13"],
    ["Corner",180,12,"Hairpin"],
    ["Straight",670,"Esplanade Drive"],
    ["Corner",90,25,"Turn 14"],
    ["Straight",70,"Run to Turn 15"],
    ["Corner",90,20,"Turn 15"],
    ["Straight",70,"Run to Turn 16"],
    ["Corner",90,25,"Turn 16"],
    ["Straight",40,"Run to Turn 17"],
    ["Corner",90,20,"Turn 17"],
    ["Straight",140,"Run to Turn 18"],
    ["Corner",90,20,"Grandstand Entry"],
    ["Straight",20,"T18-T19 Mid"],
    ["Corner",90,20,"Grandstand Exit"],
    ["Straight",40,"Run to Turn 20"],
    ["Corner",90,25,"Turn 20"],
    ["Straight",70,"Run to Turn 21"],
    ["Corner",90,25,"Turn 21"],
    ["Straight",200,"Run to Turn 22"],
    ["Corner",90,25,"Turn 22"],
    ["Straight",70,"Run to Turn 23"],
    ["Corner",90,25,"Turn 23"],
    ["Straight",159,"Finish"]]
MAL_MAP = [
    ["Straight",640,"Pit Straight Start"],
    ["Corner",110,30,"Turn 1"],
    ["Straight",25,"T1-T2 Mid"],
    ["Corner",110,25,"Turn 2"],
    ["Straight",767,"Run to Turn 4"],
    ["Corner",90,45,"Turn 4"],
    ["Straight",230,"Run to Turn 5"],
    ["Corner",65,85,"Turn 5"],
    ["Straight",25,"T5-T6 Mid"],
    ["Corner",65,80,"Turn 6"],
    ["Straight",230,"Run to Turn 7"],
    ["Corner",85,50,"Turn 7"],
    ["Straight",25,"T7-T8 Mid"],
    ["Corner",80,55,"Turn 8"],
    ["Straight",230,"Run to Turn 9"],
    ["Corner",120,20,"Turn 9"],
    ["Straight",140,"Run to Turn 10"],
    ["Corner",45,120,"Turn 10"],
    ["Straight",269,"Run to Turn 11"],
    ["Corner",80,60,"Turn 11"],
    ["Straight",140,"Run to Turn 12"],
    ["Corner",40,110,"Turn 12"],
    ["Straight",25,"T12-T13 Mid"],
    ["Corner",50,110,"Turn 13"],
    ["Straight",340,"Run to Turn 14"],
    ["Corner",100,35,"Turn 14"],
    ["Straight",1083,"Back Straight"],
    ["Corner",180,20,"Hairpin"],
    ["Straight",343,"Pit Straight Finish"]]
CHN_MAP = [
    ["Straight",570,"Start"],
    ["Corner",120,50,"Snail Entry"],
    ["Straight",25,"T1-T2 Mid"],
    ["Corner",100,25,"Turn 2"],
    ["Straight",25,"T2-T3 Mid"],
    ["Corner",80,20,"Turn 3"],
    ["Straight",25,"T3-T4 Mid"],
    ["Corner",90,40,"Snail Exit"],
    ["Straight",230,"Run to Turn 5"],
    ["Corner",60,100,"Turn 5"],
    ["Straight",340,"Run to Turn 6"],
    ["Corner",140,20,"Hairpin"],
    ["Straight",340,"Run to Turn 7"],
    ["Corner",65,140,"Turn 7"],
    ["Straight",25,"T7-T8 Mid"],
    ["Corner",70,120,"Turn 8"],
    ["Straight",140,"Run to Turn 9"],
    ["Corner",90,30,"Turn 9"],
    ["Straight",40,"T9-T10 Mid"],
    ["Corner",60,45,"Turn 10"],
    ["Straight",140,"Run to Turn 11"],
    ["Corner",90,35,"Turn 11"],
    ["Straight",40,"T11-T12 Mid"],
    ["Corner",90,40,"Turn 12"],
    ["Straight",25,"T12-T13 Mid"],
    ["Corner",110,60,"Banked Sweeper"],
    ["Straight",1645,"Back Straight"],
    ["Corner",160,18,"Hairpin"],
    ["Straight",170,"Run to Turn 15"],
    ["Corner",50,60,"Turn 15"],
    ["Straight",140,"Run to Turn 16"],
    ["Corner",90,40,"Turn 16"],
    ["Straight",340,"Finish"]]
JPN_MAP = [
    ["Straight",664,"Start"],
    ["Corner",45,120,"Turn 1"],
    ["Straight",25,"T1-T2 Mid"],
    ["Corner",90,60,"Turn 2"],
    ["Straight",70,"Run to Esses"],
    ["Corner",60,85,"Esses 1"],
    ["Straight",25,"Esses 1-2 Mid"],
    ["Corner",65,80,"Esses 2"],
    ["Straight",25,"Esses 2-3 Mid"],
    ["Corner",60,80,"Esses 3"],
    ["Straight",25,"Esses 3-4 Mid"],
    ["Corner",65,75,"Esses 4"],
    ["Straight",40,"Run to Dunlop"],
    ["Corner",90,110,"Dunlop Curve"],
    ["Straight",270,"Run to Degner"],
    ["Corner",70,70,"Degner 1"],
    ["Straight",25,"Degner Mid"],
    ["Corner",80,45,"Degner 2"],
    ["Straight",400,"Underpass"],
    ["Corner",150,18,"Hairpin"],
    ["Straight",470,"Run to Spoon"],
    ["Corner",80,75,"Spoon Curve Entry"],
    ["Straight",70,"Spoon Mid"],
    ["Corner",90,60,"Spoon Curve Exit"],
    ["Straight",1100,"Crossover"],
    ["Corner",45,250,"130R"],
    ["Straight",270,"Run to Casio Triangle"],
    ["Corner",90,25,"Casio Triangle Entry"],
    ["Straight",25,"Chicane Mid"],
    ["Corner",90,25,"Casio Triangle Exit"],
    ["Straight",430,"Run to Final Corner"],
    ["Corner",45,150,"Final Corner"],
    ["Straight",376,"Finish"]]

class Track:
    def __init__(self,title,GP,city,country,air_density,rain_prob,volatility,abrasiveness,heat_index,theoretical_length,map):
        self.title = title
        self.GP = GP
        self.city = city
        self.country = country
        self.air_density = air_density
        self.rain_prob = rain_prob
        self.volatility = volatility
        self.abrasiveness = abrasiveness
        self.heat_index = heat_index
        self.theoretical_length = theoretical_length
        self.target_lap = math.ceil(REG.FIXED_SESSION_DISTANCE/self.theoretical_length)
        self.map = map
    @property
    def calculated_length(self):
        total = 0.0
        for segment in self.map:
            if segment[0] == "Straight":
                total += segment[1]
            elif segment[0] == "Corner":
                total += 2*math.pi*segment[2]*(segment[1]/360.0)
        return round(total/PHY.FIXED_METER_TO_KILOMETER_CONVERSION_MULTIPLIER,3)

MON = Track("Monaco Grand Prix","Circuit de Monaco","Monte Carlo","Monaco",1.176,0.17,0.25,-0.67,-0.11,3.337,MON_MAP)
ESP = Track("Spanish Grand Prix","Circuit de Barcelona-Catalunya","Montmeló","Spain",1.203,0.11,0.19,1.11,-0.07,4.657,ESP_MAP)
USA = Track("United States Grand Prix","Circuit of the Americas","Austin","USA",1.154,0.23,0.27,0.47,0.14,5.514,USA_MAP)
CAN = Track("Canadian Grand Prix","Circuit Gilles Villeneuve","Montreal","Canada",1.217,0.23,0.27,-0.57,-0.37,4.361,CAN_MAP)
MEX = Track("Mexican Grand Prix","Autódromo Hermanos Rodríguez","Mexico City","Mexico",0.943,0.07,0.14,-0.64,0.11,4.304,MEX_MAP)
BRA = Track("Brazilian Grand Prix","Autódromo José Carlos Pace","São Paulo","Brazil",1.137,0.11,0.19,0.23,-0.14,4.309,BRA_MAP)
GBR = Track("British Grand Prix","Silverstone Circuit","Silverstone","United Kingdom",1.197,0.21,0.19,0.76,-0.17,5.891,GBR_MAP)
NET = Track("Dutch Grand Prix","Circuit Zandvoort","Zandvoort","Netherlands",1.217,0.21,0.29,0.67,-0.19,4.259,NET_MAP)
BEL = Track("Belgian Grand Prix","Circuit de Spa-Francorchamps","Stavelot","Belgium",1.117,0.17,0.27,0.00,-0.27,7.004,BEL_MAP)
FRA = Track("French Grand Prix","Circuit Paul Ricard","Le Castellet","France",1.143,0.07,0.07,0.43,0.17,5.843,FRA_MAP)
GER = Track("German Grand Prix","Hockenheimring","Hockenheim","Germany",1.176,0.14,0.14,0.07,0.09,4.574,GER_MAP)
AUT = Track("Austrian Grand Prix","Red Bull Ring","Spielberg","Austria",1.143,0.19,0.11,-0.07,-0.01,4.317,AUT_MAP)
ITA = Track("Italian Grand Prix","Autodromo Nazionale Monza","Monza","Italy",1.157,0.09,0.14,-0.23,0.19,5.794,ITA_MAP)
HUN = Track("Hungarian Grand Prix","Hungaroring","Mogyoród","Hungary",1.154,0.09,0.11,0.27,0.23,4.381,HUN_MAP)
TUR = Track("Turkish Grand Prix","Istanbul Park","Istanbul","Türkiye",1.197,0.27,0.17,0.94,0.07,5.337,TUR_MAP)
AZE = Track("Azerbaijan Grand Prix","Baku City Circuit","Baku","Azerbaijan",1.243,0.04,0.07,-0.64,0.01,6.004,AZE_MAP)
ABU = Track("Abu Dhabi Grand Prix","Yas Marina Circuit","Abu Dhabi","UAE",1.157,0.01,0.01,-0.34,0.17,5.554,ABU_MAP)
BHR = Track("Bahrain Grand Prix","Bahrain International Circuit","Sakhir","Bahrain",1.167,0.01,0.01,1.34,0.34,5.412,BHR_MAP)
AUS = Track("Australian Grand Prix","Albert Park Circuit","Melbourne","Australia",1.217,0.14,0.23,-0.54,-0.23,5.304,AUS_MAP)
SIN = Track("Singapore Grand Prix","Marina Bay Street Circuit","Singapore","Singapore",1.171,0.31,0.21,-0.43,0.27,5.074,SIN_MAP)
MAL = Track("Malaysian Grand Prix","Sepang International Circuit","Sepang","Malaysia",1.157,0.34,0.34,1.23,0.37,5.543,MAL_MAP)
CHN = Track("Chinese Grand Prix","Shanghai International Circuit","Shanghai","China",1.237,0.14,0.14,-0.17,-0.41,5.451,CHN_MAP)
JPN = Track("Japanese Grand Prix","Suzuka International Racing Course","Suzuka","Japan",1.243,0.14,0.27,1.01,-0.34,5.807,JPN_MAP)

track_list = [
    MON, ESP, BRA, # April
    MEX, USA, CAN, # May
    GBR, NET, BEL, FRA, # June
    GER, AUT, ITA, HUN, # July
    TUR, AZE, ABU, # September
    BHR, AUS, SIN, # October
    MAL, CHN, JPN # November
]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

DT = PHY.DT
VENUE = None
for track in track_list:
    if track.country == COUNTRY:
        VENUE = track
        break

MODE = STINT
if MODE == "Qualifying":
    LAPS = REG.FIXED_STINT_Q
elif MODE == "Free Practice":
    LAPS = VENUE.target_lap

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def generate_weather_seq(track,total_laps,base_wetness=0.0):
    sequence = []
    current_wetness = base_wetness
    laps_generated = 0
    while laps_generated < total_laps:
        interval = random.randint(REG.FIXED_WEATHER_GEN_MIN_LAP_DURATION,REG.FIXED_WEATHER_GEN_MAX_LAP_DURATION)
        if random.random() < track.rain_prob:
            intensity = random.uniform(REG.MIN_BASE_WETTING,track.volatility*REG.FIXED_WETTING_VOLATILITY_SCALE)
            target_wetness = current_wetness+intensity
        else:
            drying = random.uniform(REG.MIN_BASE_DRYING,track.volatility*REG.FIXED_DRYING_VOLATILITY_SCALE)
            target_wetness = current_wetness-drying
        target_wetness = max(0.0,min(1.0,target_wetness))
        for step in range(1,interval+1):
            if laps_generated >= total_laps:
                break
            progress = step/interval
            interpolated_wetness = current_wetness+(target_wetness-current_wetness)*progress
            sequence.append(round(interpolated_wetness,3))
            laps_generated += 1
        current_wetness = target_wetness
    if SURFACE == "Authentic":
        return sequence
    elif SURFACE == "Dry":
        LLLL = []
        for i in range(1,total_laps+1):
            LLLL.append(REG.FIXED_WEATHER_MEAN_DRY_VALUE)
        return LLLL
    elif SURFACE == "Wet":
        LLLL = []
        for i in range(1,total_laps+1):
            LLLL.append(REG.FIXED_WEATHER_MEAN_WET_VALUE)
        return LLLL
    elif SURFACE == "Extreme Wet":
        LLLL = []
        for i in range(1,total_laps+1):
            LLLL.append(REG.FIXED_WEATHER_MEAN_EXTREME_WET_VALUE)
        return LLLL
WEATHER = generate_weather_seq(VENUE,LAPS)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Fuel:
    def __init__(self,constructor,fuel_density,energy_density):
        self.constructor = constructor
        self.fuel_density = fuel_density
        self.energy_density = energy_density

FUEL = Fuel(REG.OFFICIAL_FUEL_SUPPLIER,REG.FIXED_FUEL_DENSITY,REG.FIXED_ENERGY_DENSITY)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Tire:
    def __init__(self,constructor,design,spec,mass,diameter,base_pressure,load_eff,rolling_res,friction_coeff,heat_rate,durability):
        self.constructor = constructor
        self.design = design
        self.spec = spec
        self.mass = round(mass*4,2)
        self.diameter = diameter
        self.rotational_inertia = round(self.mass*((self.diameter/2)**2+(self.diameter*REG.FIXED_WHEEL_RIM_TO_TIRE_RATIO/2)**2)*0.5,3)
        self.base_pressure = base_pressure
        self.load_eff = load_eff
        self.rolling_res = rolling_res
        self.friction_coeff = friction_coeff
        self.heat_rate = heat_rate
        self.durability = durability
        self.wear_rate = (100-self.durability)/REG.FIXED_TIRE_WEAR_RATE_DIVISOR
        self.wear = 0.0
        self.heat_index = REG.AUXILIARY_TIRE_PREHEAT
        self.temp_state = "Cold"

C1 = Tire(REG.OFFICIAL_TIRE_SUPPLIER,REG.LEGAL_DRY_COMPOUND_SPEC,REG.LEGAL_DRY_COMPOUND_LABEL[0],REG.FIXED_TIRE_MASS,REG.FIXED_TIRE_DIAMETER,REG.FIXED_TIRE_BASE_PRESSURE,1.176,0.0143,1.576,1.00,23)
C2 = Tire(REG.OFFICIAL_TIRE_SUPPLIER,REG.LEGAL_DRY_COMPOUND_SPEC,REG.LEGAL_DRY_COMPOUND_LABEL[1],REG.FIXED_TIRE_MASS,REG.FIXED_TIRE_DIAMETER,REG.FIXED_TIRE_BASE_PRESSURE,1.076,0.0137,1.543,0.76,67)
C3 = Tire(REG.OFFICIAL_TIRE_SUPPLIER,REG.LEGAL_WET_COMPOUND_SPEC,REG.LEGAL_WET_COMPOUND_LABEL[0],REG.FIXED_TIRE_MASS,REG.FIXED_TIRE_DIAMETER,REG.FIXED_TIRE_BASE_PRESSURE,0.876,0.0176,1.367,2.37,76)
C4 = Tire(REG.OFFICIAL_TIRE_SUPPLIER,REG.LEGAL_WET_COMPOUND_SPEC,REG.LEGAL_WET_COMPOUND_LABEL[1],REG.FIXED_TIRE_MASS,REG.FIXED_TIRE_DIAMETER,REG.FIXED_TIRE_BASE_PRESSURE,0.767,0.0183,1.347,2.76,87)
compound_list = [C1,C2,C3,C4]

TIRE = C1
for tire in compound_list:
    if tire.spec == RUBBER:
        TIRE = tire
        break

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Brakes:
    def __init__(self,constructor,spec,material,mass,radius,area,pressure_ratio,front_bias,friction_coeff,cooling_eff,specific_heat,reliability):
        self.constructor = constructor
        self.spec = spec
        self.material = material
        self.mass = round(mass*4,2)
        self.radius = radius
        self.area = area
        self.pressure = round(REG.MAX_BRAKE_LINE_PRESSURE*pressure_ratio,3)
        self.front_bias = front_bias
        self.friction_coeff = friction_coeff
        self.cooling_eff = cooling_eff
        self.specific_heat = specific_heat
        self.reliability = reliability
        self.health = 100.0
        self.deg_rate = (100.0/self.reliability)/REG.FIXED_COMPONENT_DEG_RATE_DIVISOR
        self.temp = REG.AUXILIARY_BRAKE_PREHEAT
class Transmission:
    def __init__(self,constructor,spec,structure,config,alignment,gear_count,mass,mech_eff,reliability):
        self.constructor = constructor
        self.spec = spec
        self.structure = structure
        self.config = config
        self.alignment = alignment
        self.gear_count = gear_count
        self.mass = mass
        self.mech_eff = mech_eff
        self.reliability = reliability
        self.health = 100.0
        self.deg_rate = (100.0/self.reliability)/REG.FIXED_COMPONENT_DEG_RATE_DIVISOR
        if self.config == "Top Speed":
            normalizer = -REG.FIXED_TRANSMISSION_SETUP_BOUNDARY
        elif self.config == "Acceleration":
            normalizer = +REG.FIXED_TRANSMISSION_SETUP_BOUNDARY
        elif self.config == "Balanced":
            normalizer = 0.0
        if self.structure == "Top Speed":
            self.final_drive = REG.FIXED_TRANSMISSION_DRIVE_VALUE-(REG.FIXED_TRANSMISSION_SETUP_BOUNDARY/2)+normalizer
        elif self.structure == "Acceleration":
            self.final_drive = REG.FIXED_TRANSMISSION_DRIVE_VALUE+(REG.FIXED_TRANSMISSION_SETUP_BOUNDARY/2)+normalizer
        elif self.structure == "Balanced":
            self.final_drive = REG.FIXED_TRANSMISSION_DRIVE_VALUE+normalizer
class Engine:
    def __init__(self,constructor,spec,config,displacement,bank_angle,mass,torque,max_RPM,idle_RPM,mech_eff,thermal_eff,reliability):
        self.constructor = constructor
        self.spec = spec
        self.config = config
        self.displacement = displacement
        self.bank_angle = bank_angle
        self.mass = mass
        self.torque = torque
        self.max_RPM = max_RPM
        self.idle_RPM = idle_RPM
        self.mech_eff = mech_eff
        self.thermal_eff = thermal_eff
        self.peak_RPM = self.get_peak_RPM()
        self.reliability = reliability
        self.health = 100.0
        self.deg_rate = (100.0/self.reliability)/REG.FIXED_COMPONENT_DEG_RATE_DIVISOR
    def get_base_torque(self,RPM):
        peak_torque_rpm = self.max_RPM*REG.FIXED_TORQUE_CURVE_MAX_RPM_MULTIPLIER
        x = RPM/peak_torque_rpm
        torque = self.torque*(REG.FIXED_TORQUE_CURVE_BASE_MULTIPLIER*x-REG.FIXED_TORQUE_CURVE_SQUARING_MULTIPLIER*(x**2))
        if RPM > peak_torque_rpm:
            drop = (RPM-peak_torque_rpm)/(self.max_RPM-peak_torque_rpm)
            torque *= (1.0-REG.FIXED_TORQUE_CURVE_DROP_RATE*(drop**REG.FIXED_TORQUE_DROP_EXPONENT))
        return max(torque,0.0)
    def get_peak_RPM(self):
        peak_RPM = self.idle_RPM
        best_power = 0.0
        step = REG.FIXED_ENGINE_PEAK_RPM_SEARCH_STEP
        RPM = self.idle_RPM
        while RPM <= self.max_RPM:
            torque = self.get_base_torque(RPM)*self.mech_eff
            power = torque*RPM*2*math.pi/PHY.FIXED_VELOCITY_TO_RPM_CONVERSION_MULTIPLIER
            if power > best_power:
                best_power = power
                peak_RPM = RPM
            RPM += step
        return peak_RPM
class Tank:
    def __init__(self,constructor,material,fuel,capacity_L,current_volume_L):
        self.constructor = constructor
        self.material = material
        self.fuel = fuel
        self.capacity = round(capacity_L/PHY.FIXED_LITER_TO_CUBIC_METER_CONVERSION_MULTIPLIER,6)
        self.current_volume = round(current_volume_L/PHY.FIXED_LITER_TO_CUBIC_METER_CONVERSION_MULTIPLIER,6)
        self.dry_mass = REG.FIXED_FUEL_TANK_MASS
    @property
    def mass(self):
        return round((self.fuel.fuel_density*self.current_volume)+self.dry_mass,4)
class Chassis:
    def __init__(self,constructor,spec,
                 mass,weight_dist_front,
                 wheelbase,length,width,track_width,track_height,
                 ride_height_front,ride_height_rear,spring_coeff,
                 front_wing,rear_wing,chassis,bodywork,skirts,venturi,
                 reliability):
        self.val_fw = front_wing; self.val_rw = rear_wing; self.val_ch = chassis; self.val_bw = bodywork; self.val_sk = skirts; self.val_ve = venturi
        self.constructor = constructor
        self.spec = spec
        self.mass = mass
        self.weight_dist_front = weight_dist_front
        self.wheelbase = wheelbase
        self.length = length
        self.width = width
        self.track_width = track_width
        self.track_height = track_height
        self.ride_height_front = ride_height_front
        self.ride_height_rear = ride_height_rear
        self.ride_height = round((ride_height_front+ride_height_rear)/2.0,4)
        self.spring_coeff = spring_coeff
        self.static_rake_deg = round(math.degrees(math.atan((self.ride_height_rear-self.ride_height_front)/self.wheelbase)),4)
        self.damping_ratio = round(REG.FIXED_BASE_DAMPING_RATIO+REG.FIXED_CHASSIS_DAMPING_RATING_SCALE*(chassis-REG.CHASSIS_RATING_RANGE[0]),2)
        self.stall_height = round(REG.FIXED_BASE_STALL_HEIGHT-REG.FIXED_VENTURI_STALL_HEIGHT_RATING_SCALE*(venturi-REG.CHASSIS_RATING_RANGE[0]),4)
        self.front_wing_rating = round((REG.FIXED_CLOSE_COMPETITION_MULTIPLIER*(front_wing-REG.CHASSIS_RATING_RANGE[0]))/REG.FIXED_MATERIAL_QUALITY_RESISTANCE_FW,4)
        self.rear_wing_rating = round((REG.FIXED_CLOSE_COMPETITION_MULTIPLIER*(rear_wing-REG.CHASSIS_RATING_RANGE[0]))/REG.FIXED_MATERIAL_QUALITY_RESISTANCE_RW,4)
        self.chassis_rating = REG.FIXED_CLOSE_COMPETITION_MULTIPLIER*(chassis-REG.CHASSIS_RATING_RANGE[0])
        self.bodywork = round((REG.FIXED_CLOSE_COMPETITION_MULTIPLIER*(REG.CHASSIS_RATING_RANGE[1]-bodywork))/REG.FIXED_MATERIAL_QUALITY_RESISTANCE_BODYWORK,4)
        self.ground_effect_rating = round(((REG.FIXED_CLOSE_COMPETITION_MULTIPLIER*(skirts-REG.CHASSIS_RATING_RANGE[0]))+(REG.FIXED_CLOSE_COMPETITION_MULTIPLIER*(venturi-REG.CHASSIS_RATING_RANGE[0])))/REG.FIXED_MATERIAL_QUALITY_RESISTANCE_FLOOR,4)
        self.reliability = reliability
        self.front_wing_health = 100.0
    @property
    def front_wing_downforce(self):
        return round(self.front_wing_rating*(self.front_wing_health/100.0),4)
    @property
    def rear_wing_downforce(self):
        flow_factor = (1-REG.FIXED_REAR_WING_AERO_DEPENDENCY)+(REG.FIXED_REAR_WING_AERO_DEPENDENCY*(self.front_wing_health/100.0))
        return round(self.rear_wing_rating*flow_factor,4)
    @property
    def ground_effect_downforce(self):
        flow_factor = (1-REG.FIXED_FLOOR_AERO_DEPENDENCY)+(REG.FIXED_FLOOR_AERO_DEPENDENCY*(self.front_wing_health/100.0))
        return round(self.ground_effect_rating*flow_factor,4)
    @property
    def chassis_downforce(self):
        return round(self.ground_effect_downforce+self.rear_wing_downforce+self.front_wing_downforce,4)
class Driver:
    def __init__(self,name,age,height,weight,nation,number,
                 wet,
                 shifting,smoothness,
                 entry_aggression,entry_tolerance):
        self.name = name
        self.age = age
        self.height = height
        self.weight = round(max(weight+(REG.FIXED_COCKPIT_MASS-REG.MAX_DRIVER_MASS),REG.FIXED_COCKPIT_MASS),1)
        self.nation = nation
        self.number = number
        # Attrs.
        self.wet = wet
        # General Profile
        self.shifting = shifting # Options: Short-Shifter, Balanced, Rev-Limiter
        self.smoothness = smoothness # Options: Poor, Balanced, Elite
        # Cornering Profile
        self.entry_aggression = entry_aggression # Options: Cautious, Balanced, Aggressive
        self.entry_tolerance = entry_tolerance # Options: Cautious, Balanced, Aggressive
        # Calcs. I
        self.braking_aggression = {"Poor":"Aggressive","Balanced":"Balanced","Elite":"Cautious"}[smoothness]
        self.exit_aggression = {"Poor":"Aggressive","Balanced":"Balanced","Elite":"Cautious"}[smoothness]
        self.throttle_aggression = {"Poor":"Aggressive","Balanced":"Balanced","Elite":"Cautious"}[smoothness]
        # Calcs. II
        self.val_wet = REG.FIXED_WET_WEATHER_CLOSE_COMPETITION_MULTIPLIER*((self.wet-REG.DRIVER_RATING_RANGE[0])/(REG.DRIVER_RATING_RANGE[1]-REG.DRIVER_RATING_RANGE[0]))
        self.val_shifting = {"Short-Shifter":REG.DRIVER_SHIFTING_MULTIPLIERS[0],"Balanced":REG.DRIVER_SHIFTING_MULTIPLIERS[1],"Rev-Limiter":REG.DRIVER_SHIFTING_MULTIPLIERS[2]}[shifting]
        self.val_smoothness = {"Poor":REG.DRIVER_SMOOTHNESS_MULTIPLIERS[0],"Balanced":REG.DRIVER_SMOOTHNESS_MULTIPLIERS[1],"Elite":REG.DRIVER_SMOOTHNESS_MULTIPLIERS[2]}[smoothness]
        self.val_entry_aggression = {"Cautious":REG.DRIVER_ENTRY_AGGRESSION_MULTIPLIERS[0],"Balanced":REG.DRIVER_ENTRY_AGGRESSION_MULTIPLIERS[1],"Aggressive":REG.DRIVER_ENTRY_AGGRESSION_MULTIPLIERS[2]}[entry_aggression]
        self.val_entry_tolerance = {"Cautious":REG.DRIVER_ENTRY_TOLERANCE_MULTIPLIERS[0],"Balanced":REG.DRIVER_ENTRY_TOLERANCE_MULTIPLIERS[1],"Aggressive":REG.DRIVER_ENTRY_TOLERANCE_MULTIPLIERS[2]}[entry_tolerance]
        self.val_braking_aggression = {"Cautious":REG.DRIVER_BRAKING_AGGRESSION_MULTIPLIERS[0],"Balanced":REG.DRIVER_BRAKING_AGGRESSION_MULTIPLIERS[1],"Aggressive":REG.DRIVER_BRAKING_AGGRESSION_MULTIPLIERS[2]}[self.braking_aggression]
        self.val_exit_aggression = {"Cautious":REG.DRIVER_EXIT_AGGRESSION_MULTIPLIERS[0],"Balanced":REG.DRIVER_EXIT_AGGRESSION_MULTIPLIERS[1],"Aggressive":REG.DRIVER_EXIT_AGGRESSION_MULTIPLIERS[2]}[self.exit_aggression]
        self.val_throttle_aggression = {"Cautious":REG.DRIVER_THROTTLE_AGGRESSION_MULTIPLIERS[0],"Balanced":REG.DRIVER_THROTTLE_AGGRESSION_MULTIPLIERS[1],"Aggressive":REG.DRIVER_THROTTLE_AGGRESSION_MULTIPLIERS[2]}[self.throttle_aggression]
class Crew:
    def __init__(self,TP0,TP1,TP2,TP3,TP4,CE0,CE1,CE2,CE3,CE4,CA0,CA1,CA2,CA3,CA4,SD0,SD1,SD2,SD3,SD4):
        self.team_principal_name = TP0
        self.team_principal_leadership = TP1
        self.team_principal_political_clout = TP2
        self.team_principal_financial_acumen = TP3
        self.team_principal_crisis_management = TP4
        self.chief_engineer_name = CE0
        self.chief_engineer_mechanical_ingenuity = CE1
        self.chief_engineer_reliability_focus = CE2
        self.chief_engineer_chassis_rigidity = CE3
        self.chief_engineer_resource_allocation = CE4
        self.chief_aerodynamicist_name = CA0
        self.chief_aerodynamicist_wind_tunnel_mastery = CA1
        self.chief_aerodynamicist_drag_reduction = CA2
        self.chief_aerodynamicist_ground_effect_tuning = CA3
        self.chief_aerodynamicist_cooling_integration = CA4
        self.sporting_director_name = SD0
        self.sporting_director_pit_crew_discipline = SD1
        self.sporting_director_session_strategy = SD2
        self.sporting_director_logistics_efficiency = SD3
        self.sporting_director_regulatory_compliance = SD4
class Car:
    def __init__(self,constructor,crew,driver,chassis,tank,engine,transmission,brakes,tire,setup,pit_call,pit_gamble,weather_seq):
        self.constructor = constructor
        self.crew = crew
        self.driver = driver
        self.chassis = chassis
        self.tank = tank
        self.engine = engine
        self.transmission = transmission
        self.brakes = brakes
        self.tire = tire
        self.drag_setup = setup[0]
        self.downforce_setup = setup[1]
        self.pit_threshold = pit_call
        self.pit_call = False
        self.pit_gamble = pit_gamble
        self.weather_seq = weather_seq
        if self.engine.bank_angle == REG.ENGINE_BANK_ANGLE_OPTIONS[1]:
            self.CoG_height = REG.CHASSIS_CoG_HEIGHT_OPTIONS[0]
        elif self.engine.bank_angle == REG.ENGINE_BANK_ANGLE_OPTIONS[0]:
            self.CoG_height = REG.CHASSIS_CoG_HEIGHT_OPTIONS[1]
        self.frontal_area = round(self.chassis.width*self.chassis.track_height,2)
        self.undertray_area = round(self.chassis.wheelbase*self.chassis.track_width,2)
        self.current_lap = 1
        self.current_lap_time = 0.0
        self.current_lap_dist = 0.0
        self.current_gear = 1
        self.gear_ratios, self.shift_RPM = self.optimize_gearbox()
        self.speed = 0.0
        self.status = "Running"
        self.dry_mass = round(self.tire.mass+self.tank.dry_mass+self.brakes.mass+self.transmission.mass+self.engine.mass+self.chassis.mass+self.driver.weight,1)
    @property
    def mass(self):
        return round(self.tire.mass+self.tank.mass+self.brakes.mass+self.transmission.mass+self.engine.mass+self.chassis.mass+self.driver.weight,1)
    @property
    def effective_mass(self):
        WIM = self.tire.rotational_inertia/((self.tire.diameter/2.0)**2.0)
        return round(self.mass+WIM,1)
    def is_porpoising(self,track,V_km_h,Q=None):
        if Q is None:
            velocity = V_km_h/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER
            Q = 0.5*track.air_density*(velocity**2)
        chassis_CL = (self.undertray_area/self.frontal_area)*self.chassis.ground_effect_rating
        total_CL = (chassis_CL+self.chassis.chassis_downforce)*self.downforce_setup
        max_downforce = Q*total_CL
        static_compression = (self.mass*PHY.GF)/(self.chassis.spring_coeff*4.0)
        aero_compression = max_downforce/(self.chassis.spring_coeff*4.0)
        total_compression = static_compression+aero_compression
        estimated_ride_height = self.chassis.ride_height-total_compression
        return estimated_ride_height <= self.chassis.stall_height
    def optimize_gearbox(self):
        circle = math.pi*self.tire.diameter
        target_RPM = self.engine.max_RPM*REG.FIXED_TRANSMISSION_TARGET_RPM_MULTIPLIER
        exponent = REG.FIXED_TRANSMISSION_DRIVE_EXPONENT
        shift_RPM = self.engine.peak_RPM
        target_top_speed = (REG.FIXED_TRANSMISSION_TARGET_RPM_MULTIPLIER*REG.FIXED_TRANSMISSION_TOP_SPEED_BASE_MULTIPLIER)+(REG.FIXED_TRANSMISSION_DRIVE_VALUE-self.transmission.final_drive)*REG.FIXED_TRANSMISSION_FINAL_DRIVE_SPEED_MULTIPLIER
        last_ratio = (target_RPM*circle)/(target_top_speed*PHY.FIXED_VELOCITY_TO_RPM_CONVERSION_MULTIPLIER*self.transmission.final_drive)
        last_ratio = min(max(last_ratio,REG.TRANSMISSION_LAST_DRIVE_RATIO_RANGE[0]),REG.TRANSMISSION_LAST_DRIVE_RATIO_RANGE[1])
        first_ratio = (self.engine.max_RPM*circle)/((REG.AVG_FIRST_GEAR_SPEED/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER)*PHY.FIXED_VELOCITY_TO_RPM_CONVERSION_MULTIPLIER*self.transmission.final_drive)
        first_ratio = min(max(first_ratio,REG.TRANSMISSION_FIRST_DRIVE_RATIO_RANGE[0]),REG.TRANSMISSION_FIRST_DRIVE_RATIO_RANGE[1])
        n = self.transmission.gear_count
        ratios = []
        for i in range(n):
            t = i/(n-1)
            ratio = first_ratio*(last_ratio/first_ratio)**(t**exponent)
            ratios.append(round(ratio,3))
        return ratios,round(shift_RPM,0)
    def get_dynamic_pitch_and_heights(self,track,V_km_h,gear,RPM,throttle,brake,acc=None):
        velocity = V_km_h/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER
        Q = 0.5*track.air_density*(velocity**2)
        base_IGE = self.chassis.ground_effect_rating
        base_df = (((self.undertray_area/self.frontal_area)*base_IGE)+self.chassis.chassis_downforce)*self.downforce_setup*Q
        if acc is None:
            if throttle > 0.0:
                thrust = self.get_thrust(V_km_h,gear,RPM)*throttle
                drag = Q*((self.frontal_area*REG.FIXED_MATERIAL_QUALITY_RESISTANCE_BODYWORK_FRONT)+((self.chassis.length/REG.CHASSIS_LENGTH_RANGE[1])*REG.FIXED_MATERIAL_QUALITY_RESISTANCE_BODYWORK_REAR)+self.chassis.bodywork)*self.drag_setup
                acc = (thrust-drag)/self.effective_mass
            elif brake > 0.0:
                acc = -REG.AVG_BRAKING_G*PHY.GF*brake
            else:
                drag = Q*((self.frontal_area*REG.FIXED_MATERIAL_QUALITY_RESISTANCE_BODYWORK_FRONT)+((self.chassis.length/REG.CHASSIS_LENGTH_RANGE[1])*REG.FIXED_MATERIAL_QUALITY_RESISTANCE_BODYWORK_REAR)+self.chassis.bodywork)*self.drag_setup
                acc = -drag/self.effective_mass
        weight_transfer = round((self.mass*acc*self.CoG_height)/self.chassis.wheelbase,1)
        front_aero_share = self.chassis.weight_dist_front*((self.chassis.front_wing_health/100.0)**REG.FIXED_BROKEN_FRONT_WING_PENALTY_ON_AERO)
        df_front = base_df*front_aero_share
        df_rear = base_df*(1.0-front_aero_share)
        front_compression = (df_front+weight_transfer)/(self.chassis.spring_coeff*2.0)
        rear_compression = (df_rear-weight_transfer)/(self.chassis.spring_coeff*2.0)
        dyn_rh_front = max(self.chassis.ride_height_front-front_compression,REG.FIXED_SKID_BLOCK_THICKNESS)
        dyn_rh_rear = max(self.chassis.ride_height_rear-rear_compression,REG.FIXED_SKID_BLOCK_THICKNESS)
        dyn_rake_rad = math.atan((dyn_rh_rear-dyn_rh_front)/self.chassis.wheelbase)
        dyn_rake_deg = round(math.degrees(dyn_rake_rad),3)
        return dyn_rh_front,dyn_rh_rear,dyn_rake_deg
    def get_ride_height(self,track,V_km_h):
        actual_downforce = self.get_downforce(track,V_km_h)
        compression = actual_downforce/(self.chassis.spring_coeff*4.0)
        estimated_ride_height = self.chassis.ride_height-compression
        estimated_ride_height = max(estimated_ride_height,self.chassis.stall_height)
        return round(estimated_ride_height,4)
    def get_ground_effect(self,track,V_km_h,Q=None):
        velocity = V_km_h/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER
        if Q is None:
            Q = 0.5*track.air_density*(velocity**2)
        base_CL = self.chassis.ground_effect_rating
        gear,rpm = self.get_gear_and_RPM(V_km_h)
        _,_,dyn_rake_deg = self.get_dynamic_pitch_and_heights(track,V_km_h,gear,rpm,0.0,0.0)
        rake_error = abs(dyn_rake_deg-REG.FIXED_REFERENCE_RAKE_ANGLE)
        pitch_efficiency = max(REG.MIN_RAKE_EFF,1.0-(REG.FIXED_RAKE_SENSE*(rake_error**2)))
        if self.is_porpoising(track,V_km_h,Q=Q):
            w_n = math.sqrt(self.chassis.spring_coeff/(self.mass/4.0))
            zeta = self.chassis.damping_ratio
            w_d = w_n*math.sqrt(max(0.0,1.0-(zeta**2)))
            decay = math.exp(-zeta*w_n*(self.current_lap_time%REG.FIXED_PORPOISING_RESONANCE_CYCLE))
            oscillation = math.cos(w_d*self.current_lap_time)*decay
            stall_factor = REG.FIXED_PORPOISING_STALL_BASE_MULTIPLIER+(REG.FIXED_PORPOISING_STALL_AMPLITUDE*oscillation)
            return round(base_CL*pitch_efficiency*stall_factor,3)
        else:
            return round(base_CL*pitch_efficiency,3)
    def get_downforce(self,track,V_km_h):
        velocity = V_km_h/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER
        Q = 0.5*track.air_density*velocity**2
        IGE = self.get_ground_effect(track,V_km_h,Q=Q)
        return round((((self.undertray_area/self.frontal_area)*IGE)+self.chassis.chassis_downforce)*self.downforce_setup*Q,2)
    def get_drag(self,track,V_km_h,df=None):
        velocity = V_km_h/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER
        Q = 0.5*track.air_density*velocity**2
        base_drag = Q*((self.frontal_area*REG.FIXED_MATERIAL_QUALITY_RESISTANCE_BODYWORK_FRONT)+((self.chassis.length/REG.CHASSIS_LENGTH_RANGE[1])*REG.FIXED_MATERIAL_QUALITY_RESISTANCE_BODYWORK_REAR)+self.chassis.bodywork)*self.drag_setup
        base_downforce = df if df is not None else self.get_downforce(track,V_km_h)
        return round(base_drag+(REG.FIXED_INDUCED_DRAG_MULTIPLIER*base_downforce),2)
    def apply_friction_coeff(self):
        temp = self.brakes.temp
        mu_base = self.brakes.friction_coeff
        if temp < REG.STEEL_BRAKE_OPERATING_MILESTONES[0]:
            factor = REG.FIXED_BRAKE_THERMAL_STAGE1_BASE+REG.FIXED_BRAKE_THERMAL_STAGE1_SLOPE*(temp/REG.STEEL_BRAKE_OPERATING_MILESTONES[0])
        elif temp < REG.STEEL_BRAKE_OPERATING_MILESTONES[1]:
            factor = REG.FIXED_BRAKE_THERMAL_STAGE2_BASE+REG.FIXED_BRAKE_THERMAL_STAGE2_SLOPE*((temp-REG.STEEL_BRAKE_OPERATING_MILESTONES[0])/(REG.STEEL_BRAKE_OPERATING_MILESTONES[1]-REG.STEEL_BRAKE_OPERATING_MILESTONES[0]))
        elif temp < REG.STEEL_BRAKE_OPERATING_MILESTONES[2]:
            factor = REG.FIXED_BRAKE_THERMAL_STAGE3_BASE-REG.FIXED_BRAKE_THERMAL_STAGE3_SLOPE*((temp-REG.STEEL_BRAKE_OPERATING_MILESTONES[1])/(REG.STEEL_BRAKE_OPERATING_MILESTONES[2]-REG.STEEL_BRAKE_OPERATING_MILESTONES[1]))
        elif temp < REG.STEEL_BRAKE_OPERATING_MILESTONES[3]:
            factor = REG.FIXED_BRAKE_THERMAL_STAGE4_BASE-REG.FIXED_BRAKE_THERMAL_STAGE4_SLOPE*((temp-REG.STEEL_BRAKE_OPERATING_MILESTONES[2])/(REG.STEEL_BRAKE_OPERATING_MILESTONES[3]-REG.STEEL_BRAKE_OPERATING_MILESTONES[2]))
        else:
            factor = max(REG.MIN_BRAKE_THERMAL_FADE_FLOOR,REG.FIXED_BRAKE_THERMAL_FADE_BASE-REG.FIXED_BRAKE_THERMAL_FADE_SLOPE*((temp-REG.STEEL_BRAKE_OPERATING_MILESTONES[3])/(REG.STEEL_BRAKE_OPERATING_MILESTONES[3]-REG.STEEL_BRAKE_OPERATING_MILESTONES[2])))
        health_factor = REG.FIXED_BRAKE_WEAR_POWER_LOSS_BASE**((100.0-self.brakes.health)/REG.FIXED_BRAKE_WEAR_POWER_LOSS_SCALE)
        return round(mu_base*factor*health_factor,4)
    def apply_brakes(self,V_km_h,brake):
        mu = self.apply_friction_coeff()
        velocity = V_km_h/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER
        clamping_F_N = self.brakes.pressure*brake*self.brakes.area
        total_torque_Nm = clamping_F_N*self.brakes.radius*mu*2
        front_torque_Nm = total_torque_Nm*self.brakes.front_bias
        rear_torque_Nm = total_torque_Nm*(1.0-self.brakes.front_bias)
        if velocity > PHY.MIN_VELOCITY_SENSE:
            wheel_ang_vel = velocity/(self.tire.diameter/2)
            heat_input_W = (total_torque_Nm*wheel_ang_vel)*REG.FIXED_BRAKE_HEAT_GEN_MULTIPLIER
        else:
            heat_input_W = 0.0
        delta_T = self.brakes.temp-REG.AUXILIARY_BRAKE_PREHEAT
        cooling_W = self.brakes.cooling_eff*delta_T*(1.0+(velocity*REG.FIXED_BRAKE_CONVECTIVE_COOLING_RATE))
        net_energy_J = (heat_input_W-cooling_W)*DT
        delta_temp = net_energy_J/(self.brakes.mass*self.brakes.specific_heat)
        self.brakes.temp = round(max(self.brakes.temp+delta_temp,REG.AUXILIARY_BRAKE_PREHEAT),2)
        return round(front_torque_Nm,1),round(rear_torque_Nm,1),self.brakes.temp
    def get_torque(self,RPM):
        RPM = max(min(RPM,self.engine.max_RPM),self.engine.idle_RPM)
        base_torque = self.engine.get_base_torque(RPM)
        health_factor = REG.FIXED_ENGINE_WEAR_POWER_LOSS_BASE**((100.0-self.engine.health)/REG.FIXED_ENGINE_WEAR_POWER_LOSS_SCALE)
        return round(base_torque*self.engine.mech_eff*health_factor,1)
    def get_power(self,RPM):
        return round(self.get_torque(RPM)*RPM*2*math.pi/PHY.FIXED_VELOCITY_TO_RPM_CONVERSION_MULTIPLIER,1)
    def get_HP(self,RPM):
        return round(self.get_power(RPM)*PHY.FIXED_WATT_TO_HP_CONVERSION_MULTIPLIER,1)
    def get_gear_and_RPM(self,V_km_h):
        V = max(V_km_h,PHY.MIN_VELOCITY_SENSE)/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER
        if not hasattr(self,"shift_timer"):
            self.shift_timer = 0.0
        wheel_RPM = (V*PHY.FIXED_VELOCITY_TO_RPM_CONVERSION_MULTIPLIER)/(math.pi*self.tire.diameter)
        engine_RPM = wheel_RPM*self.gear_ratios[self.current_gear-1]*self.transmission.final_drive
        actual_RPM = max(min(engine_RPM,self.engine.max_RPM),self.engine.idle_RPM)
        return self.current_gear,round(actual_RPM,0)
    def get_thrust(self,V_km_h,gear,RPM):
        if hasattr(self,"shift_timer") and self.shift_timer > 0:
            return 0.0
        torque = self.get_torque(RPM)
        ratio = self.gear_ratios[gear-1]*self.transmission.final_drive
        radius = self.tire.diameter*0.5
        raw_thrust = (torque*ratio*self.transmission.mech_eff)/radius
        inertia_factor = 1.0+(REG.FIXED_DRIVETRAIN_INERTIA_MULTIPLIER*(ratio**2))
        effective_thrust = raw_thrust/inertia_factor
        return round(max(effective_thrust,0.0),0)
    def get_acceleration(self,track,V_km_h,gear,RPM,throttle,brake):
        T_PEDAL = throttle
        B_PEDAL = brake
        if T_PEDAL > 0.0 and B_PEDAL > 0.0:
            if T_PEDAL > B_PEDAL:
                T_PEDAL = T_PEDAL-B_PEDAL
                B_PEDAL = 0.0
                situation = "Accelerating"
            elif T_PEDAL < B_PEDAL:
                B_PEDAL = B_PEDAL-T_PEDAL
                T_PEDAL = 0.0
                situation = "Braking"
            else:
                T_PEDAL = 0.0
                B_PEDAL = 0.0
                situation = "Lift-off"
        elif T_PEDAL > 0.0:
            situation = "Accelerating"
        elif B_PEDAL > 0.0:
            situation = "Braking"
        else:
            situation = "Lift-off"
        f_brakes,r_brakes,_ = self.apply_brakes(V_km_h,B_PEDAL)
        raw_brake_force = (f_brakes+r_brakes)/(self.tire.diameter/2.0)
        df = self.get_downforce(track,V_km_h)
        drag = self.get_drag(track,V_km_h,df=df)
        rolling_res = self.tire.rolling_res*self.mass*PHY.GF if V_km_h > PHY.MIN_VELOCITY_SENSE else 0.0
        if situation == "Accelerating":
            _,rear_load,_ = self.get_dynamic_wheel_load(track,V_km_h,gear,RPM,T_PEDAL,0.0,acc=0.0)
            mu = self.get_effective_friction_coeff()
            max_traction = rear_load*mu
            raw_force = self.get_thrust(V_km_h,gear,RPM)*T_PEDAL
            if raw_force > max_traction:
                actual_force = max_traction*(REG.FIXED_KINETIC_FRICTION_FLOOR+REG.FIXED_KINETIC_FRICTION_RANGE*(max_traction/max(raw_force,1.0)))
            else:
                actual_force = raw_force
            return round((actual_force-(drag+rolling_res))/self.effective_mass,3)
        elif situation == "Braking":
            total_vertical_load = (self.mass*PHY.GF)+df
            max_braking_grip = total_vertical_load*self.get_effective_friction_coeff()
            actual_brake_force = min(raw_brake_force,max_braking_grip)
            net_force = -actual_brake_force-(drag+rolling_res)
            return round(net_force/self.effective_mass,3)
        elif situation == "Lift-off":
            net_force = -(drag+rolling_res)
            return round(net_force/self.effective_mass,3)
    def get_dynamic_wheel_load(self,track,V_km_h,gear,RPM,throttle,brake,acc=None):
        if acc is None:
            acc = self.get_acceleration(track,V_km_h,gear,RPM,throttle,brake)
        static_front = self.mass*PHY.GF*self.chassis.weight_dist_front
        static_rear = self.mass*PHY.GF*(1-self.chassis.weight_dist_front)
        weight_transfer = round((self.mass*acc*self.CoG_height)/self.chassis.wheelbase,1)
        dynamic_front = static_front-weight_transfer
        dynamic_rear = static_rear+weight_transfer
        total_df = self.get_downforce(track,V_km_h)
        front_aero_share = self.chassis.weight_dist_front*((self.chassis.front_wing_health/100.0)**REG.FIXED_BROKEN_FRONT_WING_PENALTY_ON_AERO)
        df_front = total_df*front_aero_share
        df_rear = total_df*(1.0-front_aero_share)
        front_load = round(dynamic_front+df_front,2)
        rear_load = round(dynamic_rear+df_rear,2)
        return front_load,rear_load,weight_transfer
    def get_grip(self,track,V_km_h,gear,RPM,throttle,brake,corner_radius):
        velocity = V_km_h/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER
        front_load,rear_load,_ = self.get_dynamic_wheel_load(track,V_km_h,gear,RPM,throttle,brake)
        static_front_mass = self.mass*self.chassis.weight_dist_front
        static_rear_mass = self.mass*(1.0-self.chassis.weight_dist_front)
        lateral_acc_ms2 = ((velocity**2)/corner_radius) if corner_radius > REG.MIN_CORNER_RADIUS_THRESHOLD else 0.0
        lateral_g = lateral_acc_ms2/PHY.GF
        thrust_N = self.get_thrust(V_km_h,gear,RPM)*throttle
        acc_g_rear = thrust_N/(static_rear_mass*PHY.GF)
        brake_mu = self.apply_friction_coeff()
        clamping_F_N = self.brakes.pressure*brake*self.brakes.area
        total_brake_force_N = (clamping_F_N*self.brakes.radius*brake_mu*2.0)/(self.tire.diameter/2.0)
        front_brake_force_N = total_brake_force_N*self.brakes.front_bias
        rear_brake_force_N = total_brake_force_N*(1.0-self.brakes.front_bias)
        brake_g_front = front_brake_force_N/(static_front_mass*PHY.GF)
        brake_g_rear = rear_brake_force_N/(static_rear_mass*PHY.GF)
        front_stress_g = math.sqrt((lateral_g**2)+(brake_g_front**2))
        long_rear_stress_g = max(acc_g_rear,brake_g_rear)
        rear_stress_g = math.sqrt((lateral_g**2)+(long_rear_stress_g**2))
        mu_eff = self.get_effective_friction_coeff()
        front_lat_g = lateral_g*(static_front_mass/(static_front_mass+static_rear_mass))*2.0
        rear_lat_g = lateral_g*(static_rear_mass/(static_front_mass+static_rear_mass))*2.0
        total_lat_transfer_N = (self.mass*lateral_acc_ms2*self.CoG_height)/self.chassis.track_width
        front_lat_transfer = total_lat_transfer_N*self.chassis.weight_dist_front
        rear_lat_transfer = total_lat_transfer_N*(1.0-self.chassis.weight_dist_front)
        front_outer_load = (front_load/2.0)+front_lat_transfer
        front_inner_load = max((front_load/2.0)-front_lat_transfer,0.0)
        rear_outer_load = (rear_load/2.0)+rear_lat_transfer
        rear_inner_load = max((rear_load/2.0)-rear_lat_transfer,0.0)
        mu_f_outer,_ = self.get_pacejka_lateral_mu(front_lat_g,front_outer_load,mu_eff)
        mu_f_inner,_ = self.get_pacejka_lateral_mu(front_lat_g,front_inner_load,mu_eff)
        mu_r_outer,_ = self.get_pacejka_lateral_mu(rear_lat_g,rear_outer_load,mu_eff)
        mu_r_inner,_ = self.get_pacejka_lateral_mu(rear_lat_g,rear_inner_load,mu_eff)
        front_grip_force_N = (front_outer_load*mu_f_outer+front_inner_load*mu_f_inner)*self.tire.load_eff
        rear_grip_force_N = (rear_outer_load*mu_r_outer+rear_inner_load*mu_r_inner)*self.tire.load_eff
        current_front_limit_g = front_grip_force_N/(static_front_mass*PHY.GF)
        current_rear_limit_g = rear_grip_force_N/(static_rear_mass*PHY.GF)
        long_g_f = abs(brake_g_front)
        long_g_r = max(abs(acc_g_rear),abs(brake_g_rear))
        kamm_f = math.sqrt(max(REG.MIN_KAMM_CIRCLE_GRIP_FLOOR,1.0-(long_g_f/max(REG.MIN_GRIP_LIMIT_G_SENSE,current_front_limit_g))**2.0))
        kamm_r = math.sqrt(max(REG.MIN_KAMM_CIRCLE_GRIP_FLOOR,1.0-(long_g_r/max(REG.MIN_GRIP_LIMIT_G_SENSE,current_rear_limit_g))**2.0))
        current_front_limit_g = round(current_front_limit_g*kamm_f,4)
        current_rear_limit_g = round(current_rear_limit_g*kamm_r,4)
        front_grip_usage = round(front_stress_g/max(REG.MIN_GRIP_LIMIT_G_SENSE,current_front_limit_g),3)
        rear_grip_usage = round(rear_stress_g/max(REG.MIN_GRIP_LIMIT_G_SENSE,current_rear_limit_g),3)
        return front_grip_usage,rear_grip_usage
    def get_effective_friction_coeff(self):
        scaled_wear = self.tire.wear*REG.FIXED_COMPOUND_WEAR_MULTIPLIER
        penalty = (scaled_wear**REG.FIXED_COMPOUND_WEAR_PENALTY_EXPONENT)*REG.FIXED_COMPOUND_WEAR_PENALTY_SCALE
        base_mu = self.tire.friction_coeff*(1.0-penalty)
        heat = self.tire.heat_index
        lower_bound = REG.OPTIMUM_COMPOUND_WORKING_WINDOW[0]
        upper_bound = REG.OPTIMUM_COMPOUND_WORKING_WINDOW[1]
        if lower_bound <= heat <= upper_bound:
            state_multiplier = 1.000
        elif heat < lower_bound:
            heat_variance = lower_bound-heat
            state_multiplier = 1.000-(REG.FIXED_COMPOUND_THERMAL_VARIANCE_PENALTY*(heat_variance**2))
        else:
            heat_variance = heat-upper_bound
            state_multiplier = 1.000-(REG.FIXED_COMPOUND_THERMAL_VARIANCE_PENALTY*(heat_variance**2))
        state_multiplier = max(state_multiplier,REG.MIN_COMPOUND_THERMAL_STATE_MULTIPLIER)
        current_wetness = self.weather_seq[self.current_lap-1]
        wet_grip_factor = 1.00
        if self.tire.spec in ["Soft","Hard"]:
            water_penalty = current_wetness**REG.FIXED_SLICK_WETNESS_PENALTY_EXPONENT
            wet_grip_factor = max(REG.MIN_SLICK_WET_GRIP_FACTOR,1.00-(water_penalty*REG.FIXED_SLICK_WET_PENALTY_MULTIPLIER))
        elif self.tire.spec == "Intermediate":
            if current_wetness < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_DRY_VALUE)/4):
                wet_grip_factor = REG.FIXED_INTER_COMPOUND_PENALTY_ON_DRY_SURFACE
            else:
                variance = abs(current_wetness-REG.FIXED_WEATHER_MEAN_WET_VALUE)
                wet_grip_factor = max(REG.MIN_INTER_WET_GRIP_FACTOR,1.00-variance)
        elif self.tire.spec == "Wet":
            if current_wetness < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_DRY_VALUE)/2):
                wet_grip_factor = REG.FIXED_WET_COMPOUND_PENALTY_ON_DRY_SURFACE
            else:
                variance = abs(current_wetness-REG.FIXED_WEATHER_MEAN_EXTREME_WET_VALUE)
                wet_grip_factor = max(REG.MIN_WET_COMPOUND_GRIP_FACTOR,1.00-(variance*REG.FIXED_WET_COMPOUND_VARIANCE_SCALE))
        mastery_multiplier = 1.00+(self.driver.val_wet*current_wetness)
        final_mu = base_mu*state_multiplier*wet_grip_factor*mastery_multiplier
        return round(final_mu,3)
    def get_throttle_limit(self,track,V_km_h,gear,RPM):
        rear_aero_share = 1.0-(self.chassis.weight_dist_front*((self.chassis.front_wing_health/100.0)**REG.FIXED_BROKEN_FRONT_WING_PENALTY_ON_AERO))
        rear_load = (self.mass*PHY.GF*(1.0-self.chassis.weight_dist_front))+(self.get_downforce(track,V_km_h)*rear_aero_share)
        traction_limit = rear_load*self.get_effective_friction_coeff()
        return min(1.0,(traction_limit/max(1.0,self.get_thrust(V_km_h,gear,RPM)))*(1.0+(self.driver.val_smoothness/REG.FIXED_DRIVER_SMOOTHNESS_TRACTION_DIVISOR)))
    def get_braking_distance(self,track,V_i,gear,RPM,V_target):
        if V_i <= V_target:
            return 0.0
        real_temp = self.brakes.temp
        V_mid = (V_i+V_target)/2.0
        acc_initial = self.get_acceleration(track,V_i,gear,RPM,0.0,1.0)
        self.brakes.temp = real_temp
        acc_mid = self.get_acceleration(track,V_mid,gear,RPM,0.0,1.0)
        self.brakes.temp = real_temp
        acc_target = self.get_acceleration(track,V_target,gear,RPM,0.0,1.0)
        self.brakes.temp = real_temp
        avg_acc = (acc_initial+4.0*acc_mid+acc_target)/6.0
        if avg_acc >= REG.MAX_BRAKING_DECEL_THRESHOLD:
            avg_acc = -PHY.GF
        v_i_ms = V_i/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER
        v_t_ms = V_target/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER
        distance = (v_i_ms**2-v_t_ms**2)/(2.0*abs(avg_acc))
        return round(distance,1)
    def get_pacejka_lateral_mu(self,lateral_g,F_z_load,mu_eff):
        alpha_deg = abs(lateral_g)/REG.FIXED_PACEJKA_SLIP_ANGLE_DIVISOR
        alpha_rad = math.radians(alpha_deg)
        C = REG.FIXED_PACEJKA_C
        B = REG.FIXED_PACEJKA_B
        E = REG.FIXED_PACEJKA_E
        F_z0 = REG.FIXED_PACEJKA_NOMINAL_LOAD
        df_z = REG.FIXED_PACEJKA_LOAD_SENSITIVITY_FACTOR
        load_shift = (F_z_load-F_z0)/F_z0
        load_sensitivity = max(REG.MIN_PACEJKA_LOAD_SENSITIVITY,1.0+(df_z*load_shift))
        D = mu_eff*load_sensitivity
        phi = B*alpha_rad
        mu_lateral = D*math.sin(C*math.atan(phi-E*(phi-math.atan(phi))))
        if lateral_g < REG.MIN_PACEJKA_LATERAL_G_THRESHOLD:
            return mu_eff,0.0
        return round(abs(mu_lateral),4),round(alpha_deg,2)
    def get_max_cornering_speed(self,track,corner_radius):
        low_v = REG.MIN_CORNERING_SPEED_SEARCH_BOUND
        high_v = REG.MAX_STR_SPEED_ASSUMPTION
        max_v = REG.MIN_CORNERING_SPEED_SEARCH_BOUND
        real_temp = self.brakes.temp
        for _ in range(REG.FIXED_CORNERING_SPEED_BINARY_SEARCH_ITERATIONS):
            mid_v = (low_v+high_v)/2.0
            gear,RPM = self.estimate_gear_and_RPM(mid_v)
            front_usage,rear_usage = self.get_grip(track,mid_v,gear,RPM,0.0,0.0,corner_radius)
            self.brakes.temp = real_temp
            if max(front_usage,rear_usage) > 1.0:
                high_v = mid_v
            else:
                max_v = mid_v
                low_v = mid_v
        return round(max_v,1)
    def estimate_RK4(self,track,gear,RPM,throttle,brake):
        dt = DT
        v0_ms = self.speed/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER
        x0 = self.current_lap_dist
        initial_brake_temp = self.brakes.temp
        acc_k1 = self.get_acceleration(track,v0_ms*PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER,gear,RPM,throttle,brake)
        k1_brake_temp = self.brakes.temp
        self.brakes.temp = initial_brake_temp
        v_mid1 = v0_ms+0.5*acc_k1*dt
        acc_k2 = self.get_acceleration(track,v_mid1*PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER,gear,RPM,throttle,brake)
        self.brakes.temp = initial_brake_temp
        v_mid2 = v0_ms+0.5*acc_k2*dt
        acc_k3 = self.get_acceleration(track,v_mid2*PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER,gear,RPM,throttle,brake)
        self.brakes.temp = initial_brake_temp
        v_end = v0_ms+acc_k3*dt
        acc_k4 = self.get_acceleration(track,v_end*PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER,gear,RPM,throttle,brake)
        self.brakes.temp = k1_brake_temp
        final_v_ms = max(v0_ms+(dt/6.0)*(acc_k1+2*acc_k2+2*acc_k3+acc_k4),0.0)
        final_x = x0+(dt/6.0)*(v0_ms+2*v_mid1+2*v_mid2+v_end)
        self.speed = final_v_ms*PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER
        self.current_lap_dist = final_x
        self.current_lap_time += dt
        effective_acc = (final_v_ms-v0_ms)/dt if dt > 0 else acc_k1
        return round(effective_acc,3)
    def update_gearbox(self,V_km_h):
        V = max(V_km_h,PHY.MIN_VELOCITY_SENSE)/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER
        if not hasattr(self,"shift_timer"):
            self.shift_timer = 0.0
        if self.shift_timer > 0:
            self.shift_timer -= DT
            return
        wheel_RPM = (V*PHY.FIXED_VELOCITY_TO_RPM_CONVERSION_MULTIPLIER)/(math.pi*self.tire.diameter)
        engine_RPM = wheel_RPM*self.gear_ratios[self.current_gear-1]*self.transmission.final_drive
        shift_penalty = REG.FIXED_TRANSMISSION_SHIFT_PENALTY_BASE**((100.0-self.transmission.health)/REG.FIXED_CLUTCH_FRICTION_DISC_QUALITY_RATING)
        driver_shift_RPM = min(self.shift_RPM*self.driver.val_shifting,self.engine.max_RPM)
        if self.current_gear > 1:
            current_ratio = self.gear_ratios[self.current_gear-1]
            lower_ratio = self.gear_ratios[self.current_gear-2]
            downshift_RPM = driver_shift_RPM*(current_ratio/lower_ratio)*REG.FIXED_TRANSMISSION_TARGET_RPM_MULTIPLIER
            downshift_RPM = max(downshift_RPM,self.engine.idle_RPM)
        else:
            downshift_RPM = self.engine.idle_RPM
        if engine_RPM >= driver_shift_RPM and self.current_gear < self.transmission.gear_count:
            self.current_gear += 1
            self.shift_timer = REG.FIXED_TRANSMISSION_UPSHIFT_DURATION*shift_penalty
        elif engine_RPM < downshift_RPM and self.current_gear > 1:
            self.current_gear -= 1
            self.shift_timer = REG.FIXED_TRANSMISSION_DOWNSHIFT_DURATION*shift_penalty
    def estimate_gear_and_RPM(self,V_km_h):
        V = max(V_km_h,PHY.MIN_VELOCITY_SENSE)/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER
        wheel_RPM = (V*PHY.FIXED_VELOCITY_TO_RPM_CONVERSION_MULTIPLIER)/(math.pi*self.tire.diameter)
        estimated_gear = 1
        driver_shift_RPM = min(self.shift_RPM*self.driver.val_shifting,self.engine.max_RPM)
        for i in range(self.transmission.gear_count):
            rpm = wheel_RPM*self.gear_ratios[i]*self.transmission.final_drive
            if rpm < driver_shift_RPM:
                estimated_gear = i+1
                break
        else:
            estimated_gear = self.transmission.gear_count
        engine_RPM = wheel_RPM*self.gear_ratios[estimated_gear-1]*self.transmission.final_drive
        actual_RPM = max(min(engine_RPM,self.engine.max_RPM),self.engine.idle_RPM)
        return estimated_gear,round(actual_RPM,0)
    def load_fuel(self,track,mode,laps):
        orig_tire = self.tire
        orig_theat = self.tire.heat_index
        orig_twear = self.tire.wear
        orig_tstate = self.tire.temp_state
        orig_w0 = self.weather_seq[0]
        orig_speed = self.speed
        orig_gear = self.current_gear
        orig_shift = getattr(self,"shift_timer",0.0)
        orig_dist = self.current_lap_dist
        orig_time = self.current_lap_time
        orig_lap = self.current_lap
        orig_btemp = self.brakes.temp
        orig_ehealth = self.engine.health
        self.calibrating = True
        w_avg = sum(self.weather_seq[:laps])/max(1,laps)
        self.weather_seq[0] = w_avg
        if RUBBER == "Authentic":
            if w_avg < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_DRY_VALUE)/4):
                self.tire = C1
            elif w_avg < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_EXTREME_WET_VALUE)/2):
                self.tire = C3
            else:
                self.tire = C4
        self.tank.current_volume = REG.FIXED_CALIBRATION_RACE_FUEL_VOLUME if mode != "Qualifying" else REG.FIXED_CALIBRATION_QUALI_FUEL_VOLUME
        self.tire.heat_index = ((REG.OPTIMUM_COMPOUND_WORKING_WINDOW[0]+REG.OPTIMUM_COMPOUND_WORKING_WINDOW[1])/2.0) if mode != "Qualifying" else REG.AUXILIARY_TIRE_PREHEAT
        self.tire.wear = (((1.0-self.pit_threshold)*REG.FIXED_CALIBRATION_TIRE_WEAR_RATIO)/REG.FIXED_COMPOUND_WEAR_MULTIPLIER) if mode != "Qualifying" else 0.0
        self.brakes.temp = REG.STEEL_BRAKE_OPERATING_MILESTONES[1]
        self.engine.health = REG.FIXED_CALIBRATION_ENGINE_HEALTH if mode != "Qualifying" else 100.0
        self.current_lap = 1
        self.current_gear = REG.FIXED_CALIBRATION_START_GEAR
        self.shift_timer = 0.0
        self.speed = REG.FIXED_CALIBRATION_START_SPEED
        self.current_lap_dist = 0.0
        self.current_lap_time = 0.0
        last_seg = self.parse_segment(track.map[-1])
        first_seg = self.parse_segment(track.map[0])
        warmup_dist_next = first_seg["Length"] if first_seg["Type"] == "Straight" else 0.0
        look_seg = self.parse_segment(track.map[1 % len(track.map)])
        warmup_target = self.get_max_cornering_speed(track,first_seg["Radius"]) if first_seg["Type"] == "Corner" else (self.get_max_cornering_speed(track,look_seg["Radius"]) if look_seg["Type"] == "Corner" else REG.FIXED_UNRESTRICTED_TARGET_SPEED)
        if last_seg["Type"] == "Straight":
            self.run_straight(track,last_seg["Length"],warmup_target,last_seg["Name"],dist_to_next=warmup_dist_next)
        else:
            c_spd = self.get_max_cornering_speed(track,last_seg["Radius"])
            self.run_corner(track,last_seg["Length"],c_spd,last_seg["Name"],last_seg["Radius"],next_target_speed=warmup_target,dist_to_next=warmup_dist_next)
        start_vol = REG.FIXED_CALIBRATION_MEASUREMENT_FUEL_VOLUME
        self.tank.current_volume = start_vol
        self.current_lap_dist = 0.0
        self.current_lap_time = 0.0
        for i,raw_segment in enumerate(track.map):
            segment = self.parse_segment(raw_segment)
            target_speed = REG.FIXED_UNRESTRICTED_TARGET_SPEED
            dist_to_next = 0.0
            next_raw = track.map[i+1] if i+1 < len(track.map) else track.map[0]
            next_seg = self.parse_segment(next_raw)
            if next_seg["Type"] == "Corner":
                target_speed = self.get_max_cornering_speed(track,next_seg["Radius"])
            else:
                dist_to_next = next_seg["Length"]
                look_idx = (i+2)%len(track.map)
                look_seg = self.parse_segment(track.map[look_idx])
                if look_seg["Type"] == "Corner":
                    target_speed = self.get_max_cornering_speed(track,look_seg["Radius"])
                else:
                    target_speed = REG.FIXED_UNRESTRICTED_TARGET_SPEED
            if segment["Type"] == "Straight":
                self.run_straight(track,segment["Length"],target_speed,segment["Name"],dist_to_next=dist_to_next)
            elif segment["Type"] == "Corner":
                actual_corner_speed = self.get_max_cornering_speed(track,segment["Radius"])
                self.run_corner(track,segment["Length"],actual_corner_speed,segment["Name"],segment["Radius"],next_target_speed=target_speed,dist_to_next=dist_to_next)
        est_fuel_m3_lap = start_vol-self.tank.current_volume
        self.calibrated_lap_dist = self.current_lap_dist
        self.calibrating = False
        self.tire.heat_index = REG.AUXILIARY_TIRE_PREHEAT
        self.tire.wear = 0.0
        self.tire.temp_state = "Cold"
        self.tire = orig_tire
        self.tire.heat_index = orig_theat
        self.tire.wear = orig_twear
        self.tire.temp_state = orig_tstate
        self.weather_seq[0] = orig_w0
        self.speed = orig_speed
        self.current_gear = orig_gear
        self.shift_timer = orig_shift
        self.current_lap_dist = orig_dist
        self.current_lap_time = orig_time
        self.current_lap = orig_lap
        self.brakes.temp = orig_btemp
        self.engine.health = orig_ehealth
        safety_margin = REG.FIXED_PRE_QUALI_SESSION_FUEL_ADDITION if mode == "Qualifying" else max(REG.MIN_NON_QUALI_FUEL_SAFETY_MARGIN,REG.FIXED_PRE_NON_QUALI_SESSION_FUEL_ADDITION)
        optimal_load_L = math.ceil((est_fuel_m3_lap*PHY.FIXED_LITER_TO_CUBIC_METER_CONVERSION_MULTIPLIER*laps)+safety_margin)
        self.tank.current_volume = min(REG.FIXED_FUEL_TANK_VOLUME,optimal_load_L)/PHY.FIXED_LITER_TO_CUBIC_METER_CONVERSION_MULTIPLIER
        self.starting_fuel = self.tank.current_volume
        self.total_race_dist = laps*self.calibrated_lap_dist
        print(f"⛽ Pitwall: Loaded {int(round(self.tank.current_volume*PHY.FIXED_LITER_TO_CUBIC_METER_CONVERSION_MULTIPLIER,1))}L For {laps} Laps")
    def consume_fuel(self,RPM,throttle):
        consumed = round((self.get_power(RPM)*throttle)/(self.tank.fuel.energy_density*self.engine.thermal_eff)*DT,6)
        self.tank.current_volume -= consumed/self.tank.fuel.fuel_density
        if self.tank.current_volume <= 0.0:
            self.tank.current_volume = 0.0
            self.status = f"🔧 Lap {int(self.current_lap):02d} | {self.driver.name!s}. DNF: Out Of Fuel (Empty Tank)"
        return consumed
    def wear_tires(self,track,V_km_h,gear,RPM,throttle,brake,is_corner=False,acc=None):
        front_load,rear_load,_ = self.get_dynamic_wheel_load(track,V_km_h,gear,RPM,throttle,brake,acc=acc)
        load_factor = ((front_load+rear_load)/(self.mass*PHY.GF))**REG.FIXED_COMPOUND_DOWNFORCE_PENALTY
        slip_factor = REG.FIXED_COMPOUND_SLIP_PENALTY+(throttle**2)*REG.FIXED_COMPOUND_SKATING_PENALTY+(brake**2)*REG.FIXED_COMPOUND_BRAKING_PENALTY
        speed_factor = PHY.MIN_VELOCITY_SENSE+(V_km_h/REG.MAX_STR_SPEED_ASSUMPTION)
        heat_factor = REG.FIXED_COMPOUND_MECHANICAL_PENALTY+max(0.0,(self.brakes.temp-REG.STEEL_BRAKE_OPERATING_MILESTONES[2])/REG.STEEL_BRAKE_OPERATING_MILESTONES[3])
        current_wetness = self.weather_seq[self.current_lap-1]
        wet_wear_factor = 1.0
        if self.tire.spec in ["Soft","Hard"]:
            wet_wear_factor = max(REG.MIN_SLICK_WET_WEAR_FACTOR,1.0-current_wetness)
        elif self.tire.spec == "Intermediate" and current_wetness < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_DRY_VALUE)/4):
            wet_wear_factor = REG.FIXED_COMPOUND_WRONG_TIRE_ON_WET_PENALTY
        elif self.tire.spec == "Wet" and current_wetness < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_DRY_VALUE)/2):
            wet_wear_factor = REG.FIXED_COMPOUND_WRONG_TIRE_ON_EXTREME_WET_PENALTY
        surface_multiplier = max(REG.FIXED_COMPOUND_SURFACE_HARSHNESS_SCALE,1.0+(track.abrasiveness*REG.FIXED_COMPOUND_SURFACE_PENALTY_SCALE))
        self.tire.wear += load_factor*slip_factor*speed_factor*heat_factor*self.tire.wear_rate*wet_wear_factor*surface_multiplier*self.driver.val_smoothness*DT
        dynamic_heat = speed_factor*max(1.0,slip_factor)*REG.FIXED_TIRE_DYNAMIC_HEAT_MULTIPLIER
        if brake > REG.FIXED_TIRE_BRAKE_HEAT_ACTIVATION_THRESHOLD:
            self.tire.heat_index += (REG.FIXED_COMPOUND_BRAKING_HEAT_GEN_MULTIPLIER+(track.heat_index*REG.FIXED_TRACK_HEAT_INDEX_MULTIPLIER))*self.tire.heat_rate*dynamic_heat*DT
        elif is_corner:
            self.tire.heat_index += (REG.FIXED_COMPOUND_TURNING_HEAT_GEN_MULTIPLIER+(track.heat_index*REG.FIXED_TRACK_HEAT_INDEX_MULTIPLIER))*self.tire.heat_rate*dynamic_heat*DT
        else:
            wind_chill = max(REG.FIXED_AMBIENT_WIND_COOLING_RATE,V_km_h/REG.MIN_STR_SPEED_ASSUMPTION)
            water_chill = REG.FIXED_AMBIENT_WIND_COOLING_RATE+(current_wetness*REG.FIXED_AMBIENT_WATER_COOLING_RATE)
            ambient_temp = REG.FIXED_BASE_AMBIENT_TEMP+(track.heat_index*REG.FIXED_TRACK_AMBIENT_TEMP_SCALE)
            if self.tire.heat_index > ambient_temp:
                if self.tire.heat_index > ((REG.OPTIMUM_COMPOUND_WORKING_WINDOW[0]+REG.OPTIMUM_COMPOUND_WORKING_WINDOW[1])/2):
                    cooling_rate = (self.tire.heat_index-((REG.OPTIMUM_COMPOUND_WORKING_WINDOW[0]+REG.OPTIMUM_COMPOUND_WORKING_WINDOW[1])/2))*wind_chill*water_chill
                    self.tire.heat_index -= (cooling_rate*REG.FIXED_TIRE_HIGH_TEMP_COOLING_MULTIPLIER)*DT
                else:
                    self.tire.heat_index -= (REG.FIXED_COMPOUND_AMBIENT_COOLING_RATE*REG.FIXED_TIRE_LOW_TEMP_COOLING_MULTIPLIER)*water_chill*DT
        water_drain = current_wetness*REG.FIXED_NON_SLICK_COMPOUND_DRAINAGE_MULTIPLIER
        if self.tire.spec in ["Soft","Hard"]:
            water_drain *= REG.FIXED_SLICK_COMPOUND_DRAINAGE_MULTIPLIER
        self.tire.heat_index -= water_drain*DT
        self.tire.heat_index = max(REG.AUXILIARY_TIRE_PREHEAT,min(self.tire.heat_index,REG.MAX_TIRE_HEAT_INDEX))
        if self.tire.heat_index < REG.OPTIMUM_COMPOUND_WORKING_WINDOW[0]:
            self.tire.temp_state = "Cold"
        elif self.tire.heat_index <= REG.OPTIMUM_COMPOUND_WORKING_WINDOW[1]:
            self.tire.temp_state = "Optimal"
        elif self.tire.heat_index < REG.MAX_COMPOUND_WORKING_BOUNDARY:
            self.tire.temp_state = "Hot"
        else:
            self.tire.temp_state = "Very Hot"
        return self.tire.wear*REG.FIXED_COMPOUND_WEAR_MULTIPLIER
    def wear_mechanics(self,track,V_km_h,gear,RPM,throttle,brake):
        dt = DT
        rpm_stress = (RPM/self.engine.max_RPM)**REG.FIXED_RPM_STRESS_MULTIPLIER
        thermal_load = (100.0/(self.engine.thermal_eff*100.0))
        engine_drop = rpm_stress*throttle*self.engine.deg_rate*thermal_load*dt*REG.FIXED_ENGINE_WEAR_MULTIPLIER
        self.engine.health = max(0.0,self.engine.health-engine_drop)
        if hasattr(self,"shift_timer") and self.shift_timer > 0:
            torque_impact = (self.get_torque(RPM)/max(1.0,self.engine.torque))
            trans_drop = torque_impact*self.transmission.deg_rate*dt*REG.FIXED_TRANSMISSION_WEAR_MULTIPLIER
            self.transmission.health = max(0.0,self.transmission.health-trans_drop)
        if brake > REG.FIXED_BRAKE_WEAR_ACTIVATION_THRESHOLD:
            kinetic_load = (V_km_h/REG.MAX_STR_SPEED_ASSUMPTION)**REG.FIXED_KINETIC_LOAD_STRESS_MULTIPLIER
            thermal_penalty = 1.0+max(0.0,((self.brakes.temp-REG.STEEL_BRAKE_OPERATING_MILESTONES[2])/REG.STEEL_BRAKE_OPERATING_MILESTONES[0])**2.0)
            brake_drop = brake*kinetic_load*self.brakes.deg_rate*thermal_penalty*dt*REG.FIXED_BRAKE_WEAR_MULTIPLIER
            self.brakes.health = max(0.0,self.brakes.health-brake_drop)
        chassis_prob = ((REG.FIXED_MATERIAL_BASE_DNF_PROB+REG.FIXED_MATERIAL_WEAR_MULTIPLIER*((100.0-self.chassis.reliability)/REG.FIXED_CHASSIS_DNF_RELIABILITY_SCALE)**2.0)*(dt/REG.FIXED_LAP_TIME_ASSUMPTION))/REG.FIXED_DNF_PROBABILITY_DIVISOR
        engine_prob = ((REG.FIXED_MATERIAL_BASE_DNF_PROB+REG.FIXED_MATERIAL_WEAR_MULTIPLIER*((100.0-self.engine.health)/REG.FIXED_COMPONENT_DNF_HEALTH_SCALE)**2.0)*(dt/REG.FIXED_LAP_TIME_ASSUMPTION))/REG.FIXED_DNF_PROBABILITY_DIVISOR
        trans_prob = ((REG.FIXED_MATERIAL_BASE_DNF_PROB+REG.FIXED_MATERIAL_WEAR_MULTIPLIER*((100.0-self.transmission.health)/REG.FIXED_COMPONENT_DNF_HEALTH_SCALE)**2.0)*(dt/REG.FIXED_LAP_TIME_ASSUMPTION))/REG.FIXED_DNF_PROBABILITY_DIVISOR
        brake_prob = ((REG.FIXED_MATERIAL_BASE_DNF_PROB+REG.FIXED_MATERIAL_WEAR_MULTIPLIER*((100.0-self.brakes.health)/REG.FIXED_COMPONENT_DNF_HEALTH_SCALE)**2.0)*(dt/REG.FIXED_LAP_TIME_ASSUMPTION))/REG.FIXED_DNF_PROBABILITY_DIVISOR
        tire_left = 100.0*(1.0-(self.tire.wear*REG.FIXED_COMPOUND_WEAR_MULTIPLIER))
        tire_prob = 0.0
        if tire_left <= 0.0:
            tire_prob = 1.0
        elif tire_left <= REG.FIXED_TIRE_PUNCTURE_WEAR_THRESHOLD:
            tire_prob = (((REG.FIXED_TIRE_PUNCTURE_WEAR_THRESHOLD-tire_left)/REG.FIXED_TIRE_PUNCTURE_WEAR_THRESHOLD)**REG.FIXED_TIRE_PUNCTURE_CURVE_EXPONENT)*dt*REG.FIXED_TIRE_PUNCTURE_PROB_MULTIPLIER
        if random.random() < engine_prob or self.engine.health <= 0.0:
            self.status = f"🔧 Lap {int(self.current_lap):02d} | {self.driver.name!s}. DNF: {random.choice(DNF_list_engine)}"
        elif random.random() < trans_prob or self.transmission.health <= 0.0:
            self.status = f"🔧 Lap {int(self.current_lap):02d} | {self.driver.name!s}. DNF: {random.choice(DNF_list_transmission)}"
        elif random.random() < brake_prob or self.brakes.health <= 0.0:
            self.status = f"🔧 Lap {int(self.current_lap):02d} | {self.driver.name!s}. DNF: {random.choice(DNF_list_brakes)}"
        elif random.random() < chassis_prob:
            self.status = f"🔧 Lap {int(self.current_lap):02d} | {self.driver.name!s}. DNF: {random.choice(DNF_list_car)}"
        elif random.random() < tire_prob:
            self.status = f"🔧 Lap {int(self.current_lap):02d} | {self.driver.name!s}. DNF: Tire Blowout (Puncture)"
        return self.engine.health,self.transmission.health,self.brakes.health
    def perform_pit_stop(self):
        discipline = self.crew.sporting_director_pit_crew_discipline
        old_spec = self.tire.spec
        current_wetness = self.weather_seq[self.current_lap-1]
        if current_wetness < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_DRY_VALUE)/4):
            if self.tire.spec == "Soft":
                target_spec = "Hard"
            else:
                target_spec = "Soft"
        elif current_wetness < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_EXTREME_WET_VALUE)/2):
            target_spec = "Intermediate"
        else:
            target_spec = "Wet"
        for comp in compound_list:
            if comp.spec == target_spec:
                self.tire = comp
                break
        self.tire.wear = 0.0
        self.tire.heat_index = REG.AUXILIARY_TIRE_PREHEAT
        self.tire.temp_state = "Cold"
        base_time = REG.AVG_PIT_STOP_TIME+(((REG.CREW_RATING_RANGE[1]+1)-discipline)/(REG.CREW_RATING_RANGE[1]+1))*(REG.AVG_PIT_STOP_TIME/REG.FIXED_PIT_STOP_DISCIPLINE_SCALE_DIVISOR)
        rng_time = random.uniform(-(REG.AVG_PIT_STOP_TIME/REG.FIXED_PIT_STOP_RNG_VARIANCE_DIVISOR),+(REG.AVG_PIT_STOP_TIME/REG.FIXED_PIT_STOP_RNG_VARIANCE_DIVISOR))
        action_time = base_time+rng_time
        error_prob = (((REG.CREW_RATING_RANGE[1]+1)-discipline)/(REG.CREW_RATING_RANGE[1]+1))*REG.MAX_PIT_STOP_ERR_PROB
        blunder_msg = ""
        if random.random() < error_prob:
            penalty = random.uniform(REG.PIT_STOP_ERR_PENALTY_RANGE[0],REG.PIT_STOP_ERR_PENALTY_RANGE[1])
            action_time += penalty
            reasons = [
                "Wheel Gun Jammed",
                "Stripped Wheel Nut",
                "Mechanic Dropped The Wheel",
                "Front Jack Slipped"
            ]
            blunder_msg = f" & Err: {random.choice(reasons)} +{round(penalty,1)} s."
        wing_msg = ""
        if self.chassis.front_wing_health < 100.0:
            wing_time = REG.AVG_WING_REPLACEMENT_TIME+(((REG.CREW_RATING_RANGE[1]+1)-discipline)/(REG.CREW_RATING_RANGE[1]+1))*REG.AVG_WING_REPLACEMENT_TIME+random.uniform(-REG.AVG_WING_REPLACEMENT_TIME,+REG.AVG_WING_REPLACEMENT_TIME)
            action_time += wing_time
            self.chassis.front_wing_health = 100.0
            wing_msg = " & Wing Replacement"
        action_time = round(action_time,1)
        self.current_lap_time += action_time
        print(f"🧤 Lap {int(self.current_lap):02d} | {old_spec} To {self.tire.spec}{wing_msg} In {action_time} s{blunder_msg}")
    def parse_segment(self,segment):
        if segment[0] == "Straight":
            return {"Type":"Straight","Length":segment[1],"Name":segment[2]}
        elif segment[0] == "Corner":
            radian = math.radians(segment[1])
            length = segment[2]*radian
            return {"Type":"Corner","Angle":segment[1],"Radius":segment[2],"Length":round(length,1),"Name":segment[3]}
    def record_telemetry(self,track,sector_name,gear,rpm,throttle,brake,acc,consume,wear,thrust,corner_radius=0.0):
        front_load,rear_load,_ = self.get_dynamic_wheel_load(track,self.speed,gear,rpm,throttle,brake,acc=acc)
        long_g = acc/PHY.GF
        if corner_radius > 0.1:
            velocity = self.speed/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER
            raw_lat_g = (velocity**2/corner_radius)/PHY.GF
            mu_eff = self.get_effective_friction_coeff()
            total_load = (front_load+rear_load)/(self.mass*PHY.GF)
            max_grip_g = mu_eff*total_load
            rem_lat_g = math.sqrt(max(PHY.MIN_VELOCITY_SENSE,(max_grip_g**2)-(long_g**2))) if abs(long_g) < max_grip_g else 0.0
            lat_g = round(min(raw_lat_g,rem_lat_g),3)
        else:
            lat_g = 0.0
        neck_g = round(math.sqrt(long_g**2+lat_g**2),2)
        if self.is_porpoising(track,self.speed):
            w_n = math.sqrt(self.chassis.spring_coeff/(self.mass/4.0))
            zeta = self.chassis.damping_ratio
            decay = math.exp(-zeta*w_n*(self.current_lap_time%REG.FIXED_PORPOISING_RESONANCE_CYCLE))
            shock_amp = ((self.speed/REG.FIXED_VERTICAL_G_REFERENCE_MAX_SPEED_ASSUMPTION)**2)*(1.0/max(zeta,REG.MIN_PORPOISING_DAMPING_FLOOR))*REG.FIXED_PORPOISING_SHOCK_AMPLITUDE_MULTIPLIER
            vertical_g = round(1.0+(shock_amp*abs(math.sin(self.current_lap_dist*REG.FIXED_PORPOISING_SPATIAL_FREQ_MULTIPLIER))*decay),2)
        else:
            vertical_g = 1.00
        if self.log_idx >= self.max_rows:
            self.max_rows *= 2
            self.telemetry_matrix = np.pad(self.telemetry_matrix,((0,self.max_rows-self.log_idx),(0,0)),mode='constant')
            self.log_sector.extend([None]*(self.max_rows-self.log_idx))
            self.log_tire_compound.extend([None]*(self.max_rows-self.log_idx))
            self.log_tire_state.extend([None]*(self.max_rows-self.log_idx))
        idx = self.log_idx
        self.telemetry_matrix[idx,0] = int(self.current_lap)
        self.telemetry_matrix[idx,1] = round(self.weather_seq[self.current_lap-1],3)
        self.telemetry_matrix[idx,2] = round(self.current_lap_dist,2)
        self.telemetry_matrix[idx,3] = round(self.current_lap_time,2)
        self.telemetry_matrix[idx,4] = int(self.speed)
        self.telemetry_matrix[idx,5] = int(rpm)
        self.telemetry_matrix[idx,6] = int(gear)
        self.telemetry_matrix[idx,7] = round(acc,3)
        self.telemetry_matrix[idx,8] = int(thrust)
        self.telemetry_matrix[idx,9] = int(self.get_drag(track,self.speed))
        self.telemetry_matrix[idx,10] = int(self.get_downforce(track,self.speed))
        self.telemetry_matrix[idx,11] = int(front_load)
        self.telemetry_matrix[idx,12] = int(rear_load)
        self.telemetry_matrix[idx,13] = round(self.get_ride_height(track,self.speed),7)
        self.telemetry_matrix[idx,14] = int(self.mass)
        self.telemetry_matrix[idx,15] = round(consume,9)
        self.telemetry_matrix[idx,16] = round(self.tank.current_volume*PHY.FIXED_LITER_TO_CUBIC_METER_CONVERSION_MULTIPLIER,3)
        self.telemetry_matrix[idx,17] = wear
        self.telemetry_matrix[idx,18] = int(self.brakes.temp)
        self.telemetry_matrix[idx,19] = brake
        self.telemetry_matrix[idx,20] = throttle
        self.telemetry_matrix[idx,21] = round(neck_g,3)
        self.telemetry_matrix[idx,22] = round(vertical_g,3)
        self.telemetry_matrix[idx,23] = self.chassis.front_wing_health
        self.telemetry_matrix[idx,24] = self.transmission.health
        self.telemetry_matrix[idx,25] = self.engine.health
        self.telemetry_matrix[idx,26] = self.brakes.health
        self.log_sector[idx] = str(sector_name)
        self.log_tire_compound[idx] = str(self.tire.spec)
        self.log_tire_state[idx] = str(self.tire.temp_state)
        self.log_idx += 1
    def record_time(self,raw_time):
        raw_time += random.choice([0,1,2,3,4,5,6,7,8,9])/1000
        total_ms = round(raw_time*1000)
        minutes = total_ms//60000
        seconds = (total_ms%60000)//1000
        milliseconds = total_ms%1000
        return f"{minutes}:{seconds:02d}.{milliseconds:03d}"
    def run_stint(self,track,mode,laps):
        EARLY_WET_AVG = sum(self.weather_seq[:min(REG.FIXED_WEATHER_LOOKAHEAD_LAPS,laps)])/min(REG.FIXED_WEATHER_LOOKAHEAD_LAPS,laps)
        WS,WMAX,WMIN = self.weather_seq[0],max(self.weather_seq),min(self.weather_seq)
        if RUBBER == "Authentic":
            if WS >= ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_EXTREME_WET_VALUE)/2): target_spec = "Wet"
            elif WS >= (REG.FIXED_WEATHER_MEAN_WET_VALUE/REG.FIXED_INITIAL_WET_TIRE_DIVISOR): target_spec = "Soft" if EARLY_WET_AVG < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_DRY_VALUE)/2) else "Intermediate"
            else: target_spec = "Intermediate" if EARLY_WET_AVG > (REG.FIXED_WEATHER_MEAN_WET_VALUE/REG.FIXED_WEATHER_TREND_DIVISOR) else "Soft"
        else: target_spec = RUBBER
        for comp in compound_list:
            if comp.spec == target_spec:
                self.tire = comp
                break
        self.tire.wear = 0.0; self.tire.heat_index = REG.AUXILIARY_TIRE_PREHEAT
        self.load_fuel(track,mode,laps)
        if WMAX-WS > (REG.FIXED_WEATHER_MEAN_WET_VALUE/REG.FIXED_WEATHER_TREND_DIVISOR): W_MSG = random.choice(weather_report_authentic_dry)
        elif WS-WMIN > (REG.FIXED_WEATHER_MEAN_WET_VALUE/REG.FIXED_WEATHER_TREND_DIVISOR): W_MSG = random.choice(weather_report_authentic_wet)
        elif WMAX < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_DRY_VALUE)/2): W_MSG = random.choice(weather_report_dry)
        elif WMAX < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_EXTREME_WET_VALUE)/2): W_MSG = random.choice(weather_report_wet)
        else: W_MSG = random.choice(weather_report_extreme_wet)
        TEL_MSG = "📡 Pitwall: Telemetry (Excel Output) Active" if TELEMETRY_OUTPUT else "📡 Pitwall: Telemetry (Excel Output) Disabled"
        print(TEL_MSG)
        print(W_MSG)
        print(f"🏁 {laps} Laps Of {mode} Stint In {track.GP}")
        print(f"🏁 {self.driver.name} {self.driver.number} ({self.constructor})")
        log_freq = max(1,int((1.0/DT)/REG.FIXED_TELEMETRY_LOG_FREQ))
        self.max_rows = int(laps*180*log_freq)+1000
        self.log_idx = 0
        self.telemetry_matrix = np.zeros((self.max_rows,27),dtype=np.float64)
        self.log_sector = [None]*self.max_rows
        self.log_tire_compound = [None]*self.max_rows
        self.log_tire_state = [None]*self.max_rows
        lap_times = {}
        for lap in range(1,laps+1):
            self.current_lap = lap
            self.current_lap_dist = 0.0
            self.current_lap_time = 0.0
            current_wetness = self.weather_seq[self.current_lap-1]
            if current_wetness < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_DRY_VALUE)/4):
                optimal_tire = "Dry"
            elif current_wetness < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_EXTREME_WET_VALUE)/2):
                optimal_tire = "Intermediate"
            else:
                optimal_tire = "Wet"
            current_tire_cat = "Dry" if self.tire.spec in ["Soft","Hard"] else self.tire.spec
            wrong_weather_tire = optimal_tire != current_tire_cat
            if wrong_weather_tire:
                lethal_condition = (
                    (current_tire_cat == "Dry" and current_wetness > (REG.FIXED_WEATHER_MEAN_WET_VALUE*REG.FIXED_LETHAL_DRY_TIRE_WET_MULTIPLIER)) or
                    (current_tire_cat == "Intermediate" and (current_wetness > (REG.FIXED_WEATHER_MEAN_EXTREME_WET_VALUE*REG.FIXED_LETHAL_INTER_TIRE_MAX_WET_MULTIPLIER) or current_wetness < (REG.FIXED_WEATHER_MEAN_WET_VALUE*REG.FIXED_LETHAL_INTER_TIRE_MIN_WET_MULTIPLIER))) or
                    (current_tire_cat == "Wet" and current_wetness < (REG.FIXED_WEATHER_MEAN_WET_VALUE*REG.FIXED_LETHAL_WET_TIRE_MIN_WET_MULTIPLIER))
                )
                if not lethal_condition:
                    lookahead_limit = min(self.current_lap+REG.FIXED_WEATHER_LOOKAHEAD_LAPS,len(self.weather_seq))
                    for future_idx in range(self.current_lap,lookahead_limit):
                        future_wet = self.weather_seq[future_idx]
                        if future_wet < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_DRY_VALUE)/4):
                            future_optimal = "Dry"
                        elif future_wet < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_EXTREME_WET_VALUE)/2):
                            future_optimal = "Intermediate"
                        else:
                            future_optimal = "Wet"
                        if future_optimal == current_tire_cat:
                            wrong_weather_tire = False
                            break
            worn_tire = (1.0-(self.tire.wear*REG.FIXED_COMPOUND_WEAR_MULTIPLIER)) < self.pit_threshold
            if (laps-self.current_lap) <= self.pit_gamble:
                worn_tire = False
            if worn_tire:
                lookahead_limit = min(self.current_lap+REG.FIXED_WEATHER_LOOKAHEAD_LAPS,len(self.weather_seq))
                for future_idx in range(self.current_lap,lookahead_limit):
                    future_wet = self.weather_seq[future_idx]
                    if future_wet < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_DRY_VALUE)/4):
                        future_optimal = "Dry"
                    elif future_wet < ((REG.FIXED_WEATHER_MEAN_WET_VALUE+REG.FIXED_WEATHER_MEAN_EXTREME_WET_VALUE)/2):
                        future_optimal = "Intermediate"
                    else:
                        future_optimal = "Wet"
                    if future_optimal != current_tire_cat:
                        worn_tire = False
                        break
            broken_wing = self.chassis.front_wing_health <= REG.FIXED_FRONT_WING_PIT_THRESHOLD
            self.pit_call = (worn_tire or broken_wing or wrong_weather_tire)
            for i,raw_segment in enumerate(track.map):
                segment = self.parse_segment(raw_segment)
                target_speed = REG.FIXED_UNRESTRICTED_TARGET_SPEED
                dist_to_next = 0.0
                if i+1 < len(track.map):
                    next_raw = track.map[i+1]
                else:
                    next_raw = track.map[0]
                next_seg = self.parse_segment(next_raw)
                if next_seg["Type"] == "Corner":
                    target_speed = self.get_max_cornering_speed(track,next_seg["Radius"])
                else:
                    dist_to_next = next_seg["Length"]
                    look_idx = (i+2)%len(track.map)
                    look_seg = self.parse_segment(track.map[look_idx])
                    if look_seg["Type"] == "Corner":
                        target_speed = self.get_max_cornering_speed(track,look_seg["Radius"])
                    else:
                        target_speed = REG.FIXED_UNRESTRICTED_TARGET_SPEED
                if i == 0 and self.pit_call:
                    target_speed = REG.MAX_PIT_LANE_SPEED
                    segment["Name"] = "Pit Lane"
                    self.run_straight(track,segment["Length"],target_speed,segment["Name"],is_pit=True)
                    self.perform_pit_stop()
                    self.pit_call = False
                    continue
                if segment["Type"] == "Straight":
                    self.run_straight(track,segment["Length"],target_speed,segment["Name"],dist_to_next=dist_to_next)
                elif segment["Type"] == "Corner":
                    actual_corner_speed = self.get_max_cornering_speed(track,segment["Radius"])
                    self.run_corner(track,segment["Length"],actual_corner_speed,segment["Name"],segment["Radius"],next_target_speed=target_speed,dist_to_next=dist_to_next)
                if self.status != "Running":
                    break
            if self.status != "Running":
                print(self.status)
                break
            lap_formatted_time = self.record_time(self.current_lap_time)
            lap_times[lap] = lap_formatted_time
            if mode in ["Qualifying","Free Practice"]:
                CWP = int(self.weather_seq[self.current_lap-1]*100)
                TLP = int(max(0,int(100*(1.0-(self.tire.wear*REG.FIXED_COMPOUND_WEAR_MULTIPLIER)))))
                print(f"🏁 Lap {lap:02d} | Laptime: {lap_formatted_time} | Track Wetness: %{CWP:02d} | Compound: {self.tire.spec[0]} | Compound Left: %{TLP:02d} | Fuel Left: {round(self.tank.current_volume*1000,2):.2f}L")
        idx = self.log_idx
        mat = self.telemetry_matrix[:idx]
        self.telemetry = {
            "Lap": [int(val) for val in mat[:,0]],
            "Circuit": [str(track.city)]*idx,
            "Sector": self.log_sector[:idx],
            "Track Wetness (%)": [f"%{round(val*100,1)}" for val in mat[:,1]],
            "Driver": [str(self.driver.name)]*idx,
            "Constructor": [str(self.constructor)]*idx,
            "Engine": [str(self.engine.constructor)]*idx,
            "Lap Distance (m)": mat[:,2],
            "Lap Time (s)": mat[:,3],
            "Velocity (km/h)": [int(val) for val in mat[:,4]],
            "RPM": [int(val) for val in mat[:,5]],
            "Gear": [int(val) for val in mat[:,6]],
            "Acc. (m/s^2)": mat[:,7],
            "Thrust (N)": [int(val) for val in mat[:,8]],
            "Drag (N)": [int(val) for val in mat[:,9]],
            "Downforce (N)": [int(val) for val in mat[:,10]],
            "Front Load (N)": [int(val) for val in mat[:,11]],
            "Rear Load (N)": [int(val) for val in mat[:,12]],
            "Ride Height (m)": mat[:,13],
            "Vehicle Mass (kg.)": mat[:,14],
            "Fuel Spent (kg.)": mat[:,15],
            "Fuel Left (L)": mat[:,16],
            "Tire Left (%)": [f"%{int(100*(1.0-val))}" for val in mat[:,17]],
            "Tire Compound": self.log_tire_compound[:idx],
            "Tire State": self.log_tire_state[:idx],
            "Brake Temp. (°C)": [int(val) for val in mat[:,18]],
            "Brake Pedal (%)": [f"%{int(val*100)}" for val in mat[:,19]],
            "Gas Pedal (%)": [f"%{int(val*100)}" for val in mat[:,20]],
            "Neck G": mat[:,21],
            "Vertical G": mat[:,22],
            "Front Wing Health (%)": [f"%{int(val)}" for val in mat[:,23]],
            "Transmission Health (%)": [f"%{int(val)}" for val in mat[:,24]],
            "Engine Health (%)": [f"%{int(val)}" for val in mat[:,25]],
            "Brake Health (%)": [f"%{int(val)}" for val in mat[:,26]]
        }
        self.lap_chart = {
            "Lap": [],"Circuit": [],"Track Wetness (%)": [],
            "Driver": [],"Constructor": [],"Engine": [],
            "Lap Time (s)": [],
            "Avg. Velocity (km/h)": [],"Avg. RPM": [],"Avg. Acc. (m/s^2)": [],
            "Avg. Thrust (N)": [],"Avg. Drag (N)": [],"Avg. Downforce (N)": [],
            "Vehicle Mass (kg.)": [],
            "Fuel Left (L)": [],
            "Tire Left (%)": [],"Tire Compound": [],
            "Avg. Brake Pedal (%)": [],"Avg. Gas Pedal (%)": [],
            "Avg. Neck G": [],"Avg. Vertical G": [],
            "Front Wing Health (%)": [],"Transmission Health (%)": [],"Engine Health (%)": [],"Brake Health (%)": []
        }
        unique_laps = np.unique(mat[:,0]).astype(int)
        for lap_num in unique_laps:
            lap_indices = np.where(mat[:,0] == lap_num)[0]
            if len(lap_indices) == 0:
                continue
            lap_mat = mat[lap_indices]
            last_idx = lap_indices[-1]
            self.lap_chart["Lap"].append(int(lap_num))
            self.lap_chart["Circuit"].append(str(track.city))
            self.lap_chart["Track Wetness (%)"].append(f"%{round(lap_mat[:,1].mean()*100,1)}")
            self.lap_chart["Driver"].append(str(self.driver.name))
            self.lap_chart["Constructor"].append(str(self.constructor))
            self.lap_chart["Engine"].append(str(self.engine.constructor))
            self.lap_chart["Lap Time (s)"].append(lap_times.get(lap_num,self.record_time(lap_mat[:,3][-1])))
            self.lap_chart["Avg. Velocity (km/h)"].append(int(lap_mat[:,4].mean()))
            self.lap_chart["Avg. RPM"].append(int(lap_mat[:,5].mean()))
            self.lap_chart["Avg. Acc. (m/s^2)"].append(round(lap_mat[:,7].mean(),3))
            self.lap_chart["Avg. Thrust (N)"].append(int(lap_mat[:,8].mean()))
            self.lap_chart["Avg. Drag (N)"].append(int(lap_mat[:,9].mean()))
            self.lap_chart["Avg. Downforce (N)"].append(int(lap_mat[:,10].mean()))
            self.lap_chart["Vehicle Mass (kg.)"].append(lap_mat[:,14][-1])
            self.lap_chart["Fuel Left (L)"].append(round(lap_mat[:,16][-1],3))
            self.lap_chart["Tire Left (%)"].append(f"%{int(100*(1.0-lap_mat[:,17][-1]))}")
            self.lap_chart["Tire Compound"].append(str(self.log_tire_compound[last_idx]))
            self.lap_chart["Avg. Brake Pedal (%)"].append(f"%{int(lap_mat[:,19].mean()*100)}")
            self.lap_chart["Avg. Gas Pedal (%)"].append(f"%{int(lap_mat[:,20].mean()*100)}")
            self.lap_chart["Avg. Neck G"].append(round(lap_mat[:,21].mean(),3))
            self.lap_chart["Avg. Vertical G"].append(round(lap_mat[:,22].mean(),3))
            self.lap_chart["Front Wing Health (%)"].append(f"%{int(lap_mat[:,23][-1])}")
            self.lap_chart["Transmission Health (%)"].append(f"%{int(lap_mat[:,24][-1])}")
            self.lap_chart["Engine Health (%)"].append(f"%{int(lap_mat[:,25][-1])}")
            self.lap_chart["Brake Health (%)"].append(f"%{int(lap_mat[:,26][-1])}")
        if mode == "Free Practice":
            SESCO = "FP"
            if idx > 0 and SAFETY_OUTPUT == True:
                print(f"📡 Pitwall: Max. Speed Detected: {int(mat[:,4].max()):03d} km/h\n📡 Pitwall: Max. Downforce Detected: {int(mat[:,10].max()):05d} N\n📡 Pitwall: Max. Neck G Detected: {mat[:,21].max():.1f}G\n📡 Pitwall: Max. Vertical G Detected: {mat[:,22].max():.1f}G")
        elif mode == "Qualifying":
            SESCO = "Q"
            if idx > 0 and SAFETY_OUTPUT == True:
                print(f"📡 Pitwall: Max. Speed Detected: {int(mat[:,4].max()):03d} km/h\n📡 Pitwall: Max. Downforce Detected: {int(mat[:,10].max()):05d} N\n📡 Pitwall: Max. Neck G Detected: {mat[:,21].max():.1f}G\n📡 Pitwall: Max. Vertical G Detected: {mat[:,22].max():.1f}G")
        table_telemetry = pd.DataFrame(self.telemetry)
        table_lap_chart = pd.DataFrame(self.lap_chart)
        if TELEMETRY_OUTPUT == True:
            table_telemetry.to_excel(f"Telemetry. {laps}L Of {SESCO} In {track.city}. {self.constructor} {self.driver.number}.xlsx",index=False)
            table_lap_chart.to_excel(f"Chart. {laps}L Of {SESCO} In {track.city}. {self.constructor} {self.driver.number}.xlsx",index=False)
    def run_straight(self,track,length,target_speed,sector_name,is_pit=False,dist_to_next=0.0):
        start_dist = self.current_lap_dist
        brake_dist = 0.0
        coast_dist = 0.0
        coast_flag = False
        ticks = 0
        is_cal = getattr(self,"calibrating",False)
        log_freq = max(1,int((1.0/DT)/REG.FIXED_TELEMETRY_LOG_FREQ))
        scan_freq = max(1,int((1.0/DT)/REG.FIXED_RADAR_SCAN_FREQ))
        if not is_cal and not hasattr(self,"starting_fuel"):
            self.starting_fuel = self.tank.current_volume
            self.total_race_dist = LAPS*getattr(self,"calibrated_lap_dist",track.calculated_length*1000.0)
        while (self.current_lap_dist-start_dist) < length:
            remaining_distance = length-(self.current_lap_dist-start_dist)
            self.update_gearbox(self.speed)
            gear,rpm = self.get_gear_and_RPM(self.speed)
            if is_pit:
                if self.speed > target_speed+REG.FIXED_PIT_SPEED_LIMITER_TOLERANCE:
                    throttle,brake = 0.0,REG.FIXED_PIT_LIMITER_BRAKE_INPUT
                elif self.speed < target_speed-REG.FIXED_PIT_SPEED_LIMITER_TOLERANCE:
                    throttle,brake = REG.FIXED_PIT_LIMITER_ACCEL_THROTTLE,0.0
                else:
                    throttle,brake = REG.FIXED_PIT_LIMITER_CRUISE_THROTTLE,0.0
            else:
                if self.speed > target_speed:
                    if remaining_distance+dist_to_next <= max((length+dist_to_next)*REG.FIXED_CORNER_APEX_RATIO,REG.FIXED_RADAR_LOOKAHEAD_DISTANCE) and (ticks%scan_freq == 0 or brake_dist == 0.0):
                        brake_dist = self.get_braking_distance(track,self.speed,gear,rpm,target_speed)
                        if not is_cal and self.current_lap >= REG.FIXED_LIFT_AND_COAST_MIN_LAP and MODE != "Qualifying":
                            lap_d = getattr(self,"calibrated_lap_dist",track.calculated_length*1000.0)
                            current_overall_dist = ((self.current_lap-1)*lap_d)+self.current_lap_dist
                            rem_overall_dist = max(1.0,self.total_race_dist-current_overall_dist)
                            consumed_fuel = self.starting_fuel-self.tank.current_volume
                            proj_req = (consumed_fuel/current_overall_dist)*rem_overall_dist
                            avail_fuel = max(0.0,self.tank.current_volume-REG.FIXED_FUEL_RESERVE_BUFFER)
                            if proj_req > avail_fuel:
                                severity = min(1.0,((proj_req-avail_fuel)/max(PHY.MIN_VELOCITY_SENSE,avail_fuel))*REG.FIXED_LIFT_AND_COAST_SEVERITY_MULTIPLIER)
                                coast_dist = (self.speed/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER)*REG.FIXED_LIFT_AND_COAST_TIME_MULTIPLIER*severity
                            else:
                                coast_dist = 0.0
                else:
                    brake_dist = 0.0
                    coast_dist = 0.0
                if remaining_distance+dist_to_next <= brake_dist and self.speed > target_speed:
                    throttle,brake = 0.0,1.0
                elif remaining_distance+dist_to_next <= (brake_dist+coast_dist) and self.speed > target_speed:
                    throttle,brake = 0.0,0.0
                    if not coast_flag:
                        # print(f"🔋 Lap {int(self.current_lap):02d} | {self.driver.name!s} | Lift & Coast Activated In {sector_name}")
                        coast_flag = True
                else:
                    throttle,brake = self.get_throttle_limit(track,self.speed,gear,rpm),0.0
            thrust = self.get_thrust(self.speed,gear,rpm)*throttle
            acc = self.estimate_RK4(track,gear,rpm,throttle,brake)
            consume = self.consume_fuel(rpm,throttle)
            if not is_cal:
                wear = self.wear_tires(track,self.speed,gear,rpm,throttle,brake,is_corner=False,acc=acc)
                self.wear_mechanics(track,self.speed,gear,rpm,throttle,brake)
                if self.status != "Running":
                    break
                if ticks%log_freq == 0:
                    self.record_telemetry(track,sector_name,gear,rpm,throttle,brake,acc,consume,wear,thrust)
            ticks += 1
    def run_corner(self,track,length,corner_speed,sector_name,corner_radius,next_target_speed=REG.FIXED_UNRESTRICTED_TARGET_SPEED,dist_to_next=0.0):
        start_dist = self.current_lap_dist
        apex_dist = length*REG.FIXED_CORNER_APEX_RATIO
        ticks = 0
        brake_dist = 0.0
        coast_dist = 0.0
        coast_flag = False
        is_cal = getattr(self,"calibrating",False)
        log_freq = max(1,int((1.0/DT)/REG.FIXED_TELEMETRY_LOG_FREQ))
        scan_freq = max(1,int((1.0/DT)/REG.FIXED_RADAR_SCAN_FREQ))
        if not is_cal and not hasattr(self,"starting_fuel"):
            self.starting_fuel = self.tank.current_volume
            self.total_race_dist = LAPS*getattr(self,"calibrated_lap_dist",track.calculated_length*1000.0)
        while (self.current_lap_dist-start_dist) < length:
            distance_in_corner = self.current_lap_dist-start_dist
            self.update_gearbox(self.speed)
            gear,rpm = self.get_gear_and_RPM(self.speed)
            if distance_in_corner < apex_dist:
                progress = distance_in_corner/max(apex_dist,PHY.MIN_VELOCITY_SENSE)
                error = corner_speed-self.speed
                if error > 0:
                    throttle = min(max(error*self.driver.val_entry_aggression,0.0),self.get_throttle_limit(track,self.speed,gear,rpm))
                    brake = 0.0
                else:
                    throttle = 0.0
                    excess_speed = -error
                    if excess_speed < self.driver.val_entry_tolerance:
                        brake = 0.0
                    else:
                        trail_limit = max(0.0,REG.FIXED_TRAIL_BRAKING_MAX_LIMIT*(1.0-(progress**REG.FIXED_TRAIL_BRAKING_DECAY_EXPONENT)))
                        brake_demand = (excess_speed-self.driver.val_entry_tolerance)*self.driver.val_braking_aggression
                        brake = min(max(brake_demand,0.0),trail_limit)
            else:
                progress = (distance_in_corner-apex_dist)/(length-apex_dist)
                exit_target_speed = corner_speed*(1.0+(self.driver.val_exit_aggression*progress))
                rem_dist = (length-distance_in_corner)+dist_to_next
                if self.speed > next_target_speed and rem_dist <= REG.FIXED_CORNERING_LOOKAHEAD_DISTANCE and (ticks%scan_freq == 0 or brake_dist == 0.0):
                    brake_dist = self.get_braking_distance(track,self.speed,gear,rpm,next_target_speed)
                    if not is_cal and self.current_lap >= REG.FIXED_LIFT_AND_COAST_MIN_LAP and MODE != "Qualifying":
                        lap_d = getattr(self,"calibrated_lap_dist",track.calculated_length*1000.0)
                        current_overall_dist = ((self.current_lap-1)*lap_d)+self.current_lap_dist
                        rem_overall_dist = max(1.0,self.total_race_dist-current_overall_dist)
                        consumed_fuel = self.starting_fuel-self.tank.current_volume
                        proj_req = (consumed_fuel/current_overall_dist)*rem_overall_dist
                        avail_fuel = max(0.0,self.tank.current_volume-REG.FIXED_FUEL_RESERVE_BUFFER)
                        if proj_req > avail_fuel:
                            severity = min(1.0,((proj_req-avail_fuel)/max(PHY.MIN_VELOCITY_SENSE,avail_fuel))*REG.FIXED_LIFT_AND_COAST_SEVERITY_MULTIPLIER)
                            coast_dist = (self.speed/PHY.FIXED_VELOCITY_UNIT_CONVERSION_MULTIPLIER)*REG.FIXED_LIFT_AND_COAST_TIME_MULTIPLIER*severity
                        else:
                            coast_dist = 0.0
                if rem_dist <= brake_dist and self.speed > next_target_speed:
                    throttle = 0.0
                    brake = 1.0
                elif rem_dist <= (brake_dist+coast_dist) and self.speed > next_target_speed:
                    throttle = 0.0
                    brake = 0.0
                    if not coast_flag:
                        # print(f"🔋 Lap {int(self.current_lap):02d} | {self.driver.name!s} | Lift & Coast Activated Towards Next Target")
                        coast_flag = True
                else:
                    error = exit_target_speed-self.speed
                    if error > 0:
                        throttle = min(max(error*self.driver.val_throttle_aggression,0.0),self.get_throttle_limit(track,self.speed,gear,rpm))
                        brake = 0.0
                    else:
                        throttle = 0.0
                        brake = 0.0
            thrust = self.get_thrust(self.speed,gear,rpm)*throttle
            acc = self.estimate_RK4(track,gear,rpm,throttle,brake)
            consume = self.consume_fuel(rpm,throttle)
            if not is_cal:
                wear = self.wear_tires(track,self.speed,gear,rpm,throttle,brake,is_corner=True,acc=acc)
                self.wear_mechanics(track,self.speed,gear,rpm,throttle,brake)
                if self.status != "Running":
                    break
                if ticks%log_freq == 0:
                    self.record_telemetry(track,sector_name,gear,rpm,throttle,brake,acc,consume,wear,thrust,corner_radius)
            ticks += 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

CREW = Crew("Prototype",99,99,99,99,"Prototype",99,99,99,99,"Prototype",99,99,99,99,"Prototype",99,99,99,99)
DRIVER = Driver("Prototype",23,1.76,67.6,"Prototype","#1",
                99,
                "Balanced","Balanced",
                "Balanced","Balanced")
CHASSIS = Chassis("Prototype","PRO-C.001-1976",237.0,0.40,2.7,4.3,2.0,1.7,0.9,0.034,0.043,170000.0,99,99,99,99,99,99,99)
TANK = Tank("Prototype","Rubber",FUEL,REG.FIXED_FUEL_TANK_VOLUME,REG.FIXED_EMPTY_FUEL_TANK_VOLUME)
ENGINE = Engine("Prototype","PRO-ICE.001-1976","V12",REG.FIXED_ENGINE_DISPLACEMENT,60.0,140.0,400.0,REG.FIXED_MAX_RPM,REG.FIXED_IDLE_RPM,0.99,REG.FIXED_ENGINE_THERMAL_EFF,99)
TRANSMISSION = Transmission("Prototype","PRO-T.001-1976","Balanced","Balanced","Manual",REG.FIXED_TRANSMISSION_LEVEL,30.0,0.99,99)
BRAKES = Brakes("Prototype","PRO-B.001-1976","Steel",REG.FIXED_BRAKE_MASS,REG.FIXED_BRAKE_RADIUS,REG.FIXED_BRAKE_AREA,REG.FIXED_BRAKE_BASE_PRESSURE_RATIO,0.43,0.43,23.0,REG.FIXED_STEEL_BRAKE_S_H,99)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

PROTOTYPE = Car("Prototype",CREW,DRIVER,CHASSIS,TANK,ENGINE,TRANSMISSION,BRAKES,TIRE,[1.00,1.00],0.5,7.0,WEATHER)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

ENTRY_LIST = [PROTOTYPE]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def SCRUTINEERING(LIST): # 49
    CLEARED_ENTRY = []
    for CAR in LIST:
        INFRACTIONS = []
        if not (REG.MIN_SETUP_BOUNDARY <= CAR.drag_setup <= REG.MAX_SETUP_BOUNDARY): INFRACTIONS.append(f"Illegal Drag Setup: {CAR.drag_setup}")
        if not (REG.MIN_SETUP_BOUNDARY <= CAR.downforce_setup <= REG.MAX_SETUP_BOUNDARY): INFRACTIONS.append(f"Illegal Downforce Setup: {CAR.downforce_setup}")
        if not (REG.BRAKE_FRONT_BIAS_RANGE[0] <= CAR.brakes.front_bias <= REG.BRAKE_FRONT_BIAS_RANGE[1]): INFRACTIONS.append(f"Illegal Brake Front Bias: {CAR.brakes.front_bias}")
        if not (REG.BRAKE_FRICTION_COEFF_RANGE[0] <= CAR.brakes.friction_coeff <= REG.BRAKE_FRICTION_COEFF_RANGE[1]): INFRACTIONS.append(f"Illegal Brake Friction Coeff: {CAR.brakes.friction_coeff}")
        if not (REG.BRAKE_COOLING_EFF_RANGE[0] <= CAR.brakes.cooling_eff <= REG.BRAKE_COOLING_EFF_RANGE[1]): INFRACTIONS.append(f"Illegal Brake Cooling Eff: {CAR.brakes.cooling_eff}")
        if not (REG.BRAKE_RELIABILITY_RANGE[0] <= CAR.brakes.reliability <= REG.BRAKE_RELIABILITY_RANGE[1]): INFRACTIONS.append(f"Illegal Brake Reliability: {CAR.brakes.reliability}")
        if not (REG.TRANSMISSION_MASS_RANGE[0] <= CAR.transmission.mass <= REG.TRANSMISSION_MASS_RANGE[1]): INFRACTIONS.append(f"Illegal Transmission Mass: {CAR.transmission.mass}")
        if not (REG.TRANSMISSION_MECH_EFF_RANGE[0] <= CAR.transmission.mech_eff <= REG.TRANSMISSION_MECH_EFF_RANGE[1]): INFRACTIONS.append(f"Illegal Transmission Mech Eff: {CAR.transmission.mech_eff}")
        if not (REG.TRANSMISSION_RELIABILITY_RANGE[0] <= CAR.transmission.reliability <= REG.TRANSMISSION_RELIABILITY_RANGE[1]): INFRACTIONS.append(f"Illegal Transmission Reliability: {CAR.transmission.reliability}")
        if CAR.engine.bank_angle not in REG.ENGINE_BANK_ANGLE_OPTIONS: INFRACTIONS.append(f"Illegal Engine Bank Angle: {CAR.engine.bank_angle}")
        if CAR.engine.torque > REG.MAX_THEORETICAL_ENGINE_TORQUE: INFRACTIONS.append(f"Illegal Engine Torque: {CAR.engine.torque}")
        if not (REG.ENGINE_MASS_RANGE[0] <= CAR.engine.mass <= REG.ENGINE_MASS_RANGE[1]): INFRACTIONS.append(f"Illegal Engine Mass: {CAR.engine.mass}")
        if not (REG.ENGINE_MECH_EFF_RANGE[0] <= CAR.engine.mech_eff <= REG.ENGINE_MECH_EFF_RANGE[1]): INFRACTIONS.append(f"Illegal Engine Mech Eff: {CAR.engine.mech_eff}")
        if not (REG.ENGINE_RELIABILITY_RANGE[0] <= CAR.engine.reliability <= REG.ENGINE_RELIABILITY_RANGE[1]): INFRACTIONS.append(f"Illegal Engine Reliability: {CAR.engine.reliability}")
        if CAR.driver.weight < REG.FIXED_COCKPIT_MASS: INFRACTIONS.append(f"Illegal Driver Mass: {CAR.driver.weight}")
        if not (REG.CREW_RATING_RANGE[0] <= CAR.crew.team_principal_leadership <= REG.CREW_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal TP Leadership Rating: {CAR.crew.team_principal_leadership}")
        if not (REG.CREW_RATING_RANGE[0] <= CAR.crew.team_principal_political_clout <= REG.CREW_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal TP Political Rating: {CAR.crew.team_principal_political_clout}")
        if not (REG.CREW_RATING_RANGE[0] <= CAR.crew.team_principal_financial_acumen <= REG.CREW_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal TP Financial Rating: {CAR.crew.team_principal_financial_acumen}")
        if not (REG.CREW_RATING_RANGE[0] <= CAR.crew.team_principal_crisis_management <= REG.CREW_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal TP Crisis Rating: {CAR.crew.team_principal_crisis_management}")
        if not (REG.CREW_RATING_RANGE[0] <= CAR.crew.chief_engineer_mechanical_ingenuity <= REG.CREW_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal CE Mechanical Rating: {CAR.crew.chief_engineer_mechanical_ingenuity}")
        if not (REG.CREW_RATING_RANGE[0] <= CAR.crew.chief_engineer_reliability_focus <= REG.CREW_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal CE Reliability Rating: {CAR.crew.chief_engineer_reliability_focus}")
        if not (REG.CREW_RATING_RANGE[0] <= CAR.crew.chief_engineer_chassis_rigidity <= REG.CREW_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal CE Chassis Rating: {CAR.crew.chief_engineer_chassis_rigidity}")
        if not (REG.CREW_RATING_RANGE[0] <= CAR.crew.chief_engineer_resource_allocation <= REG.CREW_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal CE Resource Rating: {CAR.crew.chief_engineer_resource_allocation}")
        if not (REG.CREW_RATING_RANGE[0] <= CAR.crew.chief_aerodynamicist_wind_tunnel_mastery <= REG.CREW_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal CA Wind Tunnel Rating: {CAR.crew.chief_aerodynamicist_wind_tunnel_mastery}")
        if not (REG.CREW_RATING_RANGE[0] <= CAR.crew.chief_aerodynamicist_drag_reduction <= REG.CREW_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal CA Drag Rating: {CAR.crew.chief_aerodynamicist_drag_reduction}")
        if not (REG.CREW_RATING_RANGE[0] <= CAR.crew.chief_aerodynamicist_ground_effect_tuning <= REG.CREW_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal CA Ground Effect Rating: {CAR.crew.chief_aerodynamicist_ground_effect_tuning}")
        if not (REG.CREW_RATING_RANGE[0] <= CAR.crew.chief_aerodynamicist_cooling_integration <= REG.CREW_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal CA Cooling Rating: {CAR.crew.chief_aerodynamicist_cooling_integration}")
        if not (REG.CREW_RATING_RANGE[0] <= CAR.crew.sporting_director_pit_crew_discipline <= REG.CREW_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal SD Pit Crew Rating: {CAR.crew.sporting_director_pit_crew_discipline}")
        if not (REG.CREW_RATING_RANGE[0] <= CAR.crew.sporting_director_session_strategy <= REG.CREW_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal SD Strategy Rating: {CAR.crew.sporting_director_session_strategy}")
        if not (REG.CREW_RATING_RANGE[0] <= CAR.crew.sporting_director_logistics_efficiency <= REG.CREW_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal SD Logistics Rating: {CAR.crew.sporting_director_logistics_efficiency}")
        if not (REG.CREW_RATING_RANGE[0] <= CAR.crew.sporting_director_regulatory_compliance <= REG.CREW_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal SD Compliance Rating: {CAR.crew.sporting_director_regulatory_compliance}")
        if not (REG.CHASSIS_MASS_RANGE[0] <= CAR.chassis.mass <= REG.CHASSIS_MASS_RANGE[1]): INFRACTIONS.append(f"Illegal Chassis Mass: {CAR.chassis.mass}")
        if not (REG.CHASSIS_WDF_RANGE[0] <= CAR.chassis.weight_dist_front <= REG.CHASSIS_WDF_RANGE[1]): INFRACTIONS.append(f"Illegal Front Weight Dist: {CAR.chassis.weight_dist_front}")
        if not (REG.CHASSIS_WHEELBASE_RANGE[0] <= CAR.chassis.wheelbase <= REG.CHASSIS_WHEELBASE_RANGE[1]): INFRACTIONS.append(f"Illegal Wheelbase: {CAR.chassis.wheelbase}")
        if not (REG.CHASSIS_LENGTH_RANGE[0] <= CAR.chassis.length <= REG.CHASSIS_LENGTH_RANGE[1]): INFRACTIONS.append(f"Illegal Car Length: {CAR.chassis.length}")
        if not (REG.CHASSIS_WIDTH_RANGE[0] <= CAR.chassis.width <= REG.CHASSIS_WIDTH_RANGE[1]): INFRACTIONS.append(f"Illegal Car Width: {CAR.chassis.width}")
        if not (REG.CHASSIS_TRACK_WIDTH_RANGE[0] <= CAR.chassis.track_width <= REG.CHASSIS_TRACK_WIDTH_RANGE[1]): INFRACTIONS.append(f"Illegal Track Width: {CAR.chassis.track_width}")
        if not (REG.CHASSIS_TRACK_HEIGHT_RANGE[0] <= CAR.chassis.track_height <= REG.CHASSIS_TRACK_HEIGHT_RANGE[1]): INFRACTIONS.append(f"Illegal Track Height: {CAR.chassis.track_height}")
        if not (REG.CHASSIS_FRH_RANGE[0] <= CAR.chassis.ride_height_front <= REG.CHASSIS_FRH_RANGE[1]): INFRACTIONS.append(f"Illegal Front Ride Height: {CAR.chassis.ride_height_front}")
        if not (REG.CHASSIS_RRH_RANGE[0] <= CAR.chassis.ride_height_rear <= REG.CHASSIS_RRH_RANGE[1]): INFRACTIONS.append(f"Illegal Rear Ride Height: {CAR.chassis.ride_height_rear}")
        if not (REG.CHASSIS_SCE_RANGE[0] <= CAR.chassis.spring_coeff <= REG.CHASSIS_SCE_RANGE[1]): INFRACTIONS.append(f"Illegal Spring Coeff: {CAR.chassis.spring_coeff}")
        if not (REG.CHASSIS_RATING_RANGE[0] <= CAR.chassis.val_fw <= REG.CHASSIS_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal Front Wing Rating: {CAR.chassis.val_fw}")
        if not (REG.CHASSIS_RATING_RANGE[0] <= CAR.chassis.val_rw <= REG.CHASSIS_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal Rear Wing Rating: {CAR.chassis.val_rw}")
        if not (REG.CHASSIS_RATING_RANGE[0] <= CAR.chassis.val_ch <= REG.CHASSIS_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal Chassis Rating: {CAR.chassis.val_ch}")
        if not (REG.CHASSIS_RATING_RANGE[0] <= CAR.chassis.val_bw <= REG.CHASSIS_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal Bodywork Rating: {CAR.chassis.val_bw}")
        if not (REG.CHASSIS_RATING_RANGE[0] <= CAR.chassis.val_sk <= REG.CHASSIS_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal Skirts Rating: {CAR.chassis.val_sk}")
        if not (REG.CHASSIS_RATING_RANGE[0] <= CAR.chassis.val_ve <= REG.CHASSIS_RATING_RANGE[1]): INFRACTIONS.append(f"Illegal Venturi Rating: {CAR.chassis.val_ve}")
        if not (REG.CHASSIS_RELIABILITY_RANGE[0] <= CAR.chassis.reliability <= REG.CHASSIS_RELIABILITY_RANGE[1]): INFRACTIONS.append(f"Illegal Chassis Reliability: {CAR.chassis.reliability}")
        if not (REG.MIN_DRY_WEIGHT <= CAR.dry_mass <= REG.MAX_DRY_WEIGHT): INFRACTIONS.append(f"Illegal Dry Car Mass: {CAR.dry_mass}")
        if len(INFRACTIONS) == 0:
            print(f"✅ Scrutineering (Passed): {CAR.driver.name} {CAR.driver.number} ({CAR.constructor})")
            CLEARED_ENTRY.append(CAR)
        else:
            print(f"❌ Scrutineering (Disqualified): {CAR.constructor} | {CAR.driver.name}")
            for INF in INFRACTIONS: print(f"{INF}")
    return CLEARED_ENTRY

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

for ENTRY in SCRUTINEERING(ENTRY_LIST):
    ENTRY.run_stint(VENUE,MODE,LAPS)