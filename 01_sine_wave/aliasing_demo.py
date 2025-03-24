import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# Set parameters
# ---------------------------
true_frequency = 1000  # Hz – the original wave
duration = 0.005       # seconds – short for clean visual

# Sampling rates to compare
sampling_rates = [44000, 4000, 2000, 1000]  # Hz

# ---------------------------
# Plot each one
# ---------------------------
plt.figure(figsize=(12, 8))

for i, sr in enumerate(sampling_rates, 1):
    t = np.linspace(0, duration, int(duration * sr), endpoint=False)
    y = np.sin(2 * np.pi * true_frequency * t)

    plt.subplot(2, 2, i)
    plt.plot(t, y, marker='o')
    plt.title(f"{sr} Hz Sampling Rate")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)

plt.tight_layout()
plt.show()
