# R-2R Ladder Digital-to-Analog Converter

## Overview
This project implements and evaluates an R-2R ladder digital-to-analog converter (DAC) designed for audio-band signal conversion. The work emphasizes linearity, quantization behavior, and resistor mismatch sensitivity—key considerations in mixed-signal and IC-adjacent design.

## Architecture
- Binary-weighted R-2R ladder topology
- Passive resistor network driven by digital inputs
- Focus on monotonicity and output accuracy

## Simulation & Analysis
The DAC behavior was analyzed through software simulation to evaluate:
- Ideal vs non-ideal transfer characteristics
- Quantization staircase behavior
- Differential and integral nonlinearity (DNL / INL)
- Impact of resistor mismatch on output accuracy

## Hardware Validation
The R-2R ladder was implemented using discrete resistors and driven with digital inputs to verify real-world conversion behavior. Measured outputs were compared against simulated results to confirm linearity trends and error sources.

## Key Learnings
- Quantization noise and resolution limits in DACs
- Sensitivity of R-2R ladders to resistor mismatch
- Practical tradeoffs in passive DAC implementations
- Reinforced mixed-signal fundamentals relevant to IC design