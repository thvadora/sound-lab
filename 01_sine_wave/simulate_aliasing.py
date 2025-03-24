import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# Simulation Parameters
# ---------------------------
true_freq = 3000          # Hz – frequency of the "real" analog wave
duration = 0.005          # seconds – short duration for clean visual
amplitude = 1.0

# "Analog" reference wave – sampled at a very high rate
high_sr = 100000  # 100kHz sampling rate = virtually continuous
t_high = np.linspace(0, duration, int(high_sr * duration), endpoint=False)
analog_wave = amplitude * np.sin(2 * np.pi * true_freq * t_high)

# Sampling rates that will cause aliasing
sampling_rates = [8000, 4000, 2000, 1000]

# ---------------------------
# Plotting
# ---------------------------
plt.figure(figsize=(12, 8))

for i, sr in enumerate(sampling_rates, 1):
    t_sampled = np.linspace(0, duration, int(sr * duration), endpoint=False)
    sampled_wave = amplitude * np.sin(2 * np.pi * true_freq * t_sampled)

    plt.subplot(2, 2, i)
    plt.plot(t_high, analog_wave, label="Original (Analog)", alpha=0.5)
    plt.stem(t_sampled, sampled_wave, linefmt='r-', markerfmt='ro', basefmt='k-',
             label=f"Sampled at {sr} Hz")
    plt.title(f"Sampling {true_freq} Hz at {sr} Hz")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()

plt.tight_layout()
plt.show()
