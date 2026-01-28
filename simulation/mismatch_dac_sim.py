import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure output directory exists
os.makedirs("media", exist_ok=True)

# DAC parameters
N_BITS = 8
V_REF = 1.0
LSB = V_REF / (2**N_BITS)

# Monte Carlo parameters
NUM_RUNS = 200
SIGMA = 0.01  # 1% resistor mismatch

codes = np.arange(2**N_BITS)

def dac_output(code, weights):
    return np.dot(code >> np.arange(N_BITS) & 1, weights)

# Ideal binary weights
ideal_weights = np.array([V_REF / (2**(i+1)) for i in range(N_BITS)])

outputs = []

for _ in range(NUM_RUNS):
    mismatch = np.random.normal(1.0, SIGMA, size=N_BITS)
    weights = ideal_weights * mismatch

    vout = np.array([dac_output(c, weights) for c in codes])
    outputs.append(vout)

outputs = np.array(outputs)
mean_output = np.mean(outputs, axis=0)

# DNL and INL
dnl = np.diff(mean_output) / LSB - 1
inl = (mean_output - codes * LSB) / LSB

# --- Plot DNL ---
plt.figure(figsize=(8,4))
plt.stem(dnl)
plt.xlabel("Code")
plt.ylabel("DNL (LSB)")
plt.title("DNL with 1% Resistor Mismatch")
plt.grid(True)
plt.tight_layout()
plt.savefig("media/dnl.png", dpi=300)
plt.close()

# --- Plot INL ---
plt.figure(figsize=(8,4))
plt.plot(inl)
plt.xlabel("Code")
plt.ylabel("INL (LSB)")
plt.title("INL with 1% Resistor Mismatch")
plt.grid(True)
plt.tight_layout()
plt.savefig("media/inl.png", dpi=300)
plt.close()
