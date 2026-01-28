import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure output directory exists
os.makedirs("media", exist_ok=True)

# DAC parameters
N_BITS = 8
V_REF = 1.0

codes = np.arange(2**N_BITS)
v_out = V_REF * codes / (2**N_BITS)

plt.figure(figsize=(8,5))
plt.step(codes, v_out, where='post')
plt.xlabel("Digital Code")
plt.ylabel("Output Voltage (V)")
plt.title("Ideal R-2R DAC Transfer Characteristic")
plt.grid(True)

plt.tight_layout()
plt.savefig("media/transfer_curve.png", dpi=300)
plt.show()
