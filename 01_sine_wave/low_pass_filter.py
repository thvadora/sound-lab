import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# ---------------------------
# PARAMETERS
# ---------------------------
duration = 2.0        # seconds
sampling_rate = 44100 # Hz
amplitude = 0.5

# Frequencies in the mix
low_freq = 440     # A4 (hearable tone)
high_freq = 8000   # High, bright tone

# ---------------------------
# Generate mixed signal
# ---------------------------
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Mixed wave: low tone + high tone
signal = amplitude * (np.sin(2 * np.pi * low_freq * t) +
                      np.sin(2 * np.pi * high_freq * t))

# ---------------------------
# Low-pass filter: moving average
# ---------------------------
def low_pass_filter(data, window_size=20):
    return np.convolve(data, np.ones(window_size)/window_size, mode='same')

# Apply filter
filtered_signal = low_pass_filter(signal, window_size=50)

# ---------------------------
# Plot original vs filtered
# ---------------------------
plt.figure(figsize=(12, 5))
plt.plot(t[:1000], signal[:1000], label='Original Signal', alpha=0.5)
plt.plot(t[:1000], filtered_signal[:1000], label='Filtered Signal', linewidth=2)
plt.title("Low-Pass Filter Effect (Zoomed In)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------------------------
# Listen to results
# ---------------------------
print("Playing original signal...")
sd.play(signal, samplerate=sampling_rate)
sd.wait()

print("Playing filtered signal (high frequencies removed)...")
sd.play(filtered_signal, samplerate=sampling_rate)
sd.wait()
