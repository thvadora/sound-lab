import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# ---------------------------
# Signal Parameters
# ---------------------------
sampling_rate = 44100  # Hz
duration = 1.0         # seconds
amplitude = 0.5

# Frequencies to include
freqs = [440, 8000, 120, 382]

# ---------------------------
# Time and signal generation
# ---------------------------
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
signal = sum([np.sin(2 * np.pi * f * t) for f in freqs])
signal *= amplitude
signal /= np.max(np.abs(signal))  # Normalize

# ---------------------------
# Play the signal (optional)
# ---------------------------
print("Playing signal...")
sd.play(signal, samplerate=sampling_rate)
sd.wait()

# ---------------------------
# FFT Analysis
# ---------------------------
N = len(signal)
fft_data = np.fft.fft(signal)
fft_freqs = np.fft.fftfreq(N, 1/sampling_rate)

# Only keep the positive half of the FFT
positive_freqs = fft_freqs[:N//2]
magnitude = np.abs(fft_data[:N//2]) * 2 / N  # Normalize

# ---------------------------
# Plot the Frequency Spectrum
# ---------------------------
plt.figure(figsize=(12, 6))
plt.plot(positive_freqs, magnitude)
plt.title("Frequency Spectrum (FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0, 10000)  # Zoom in to see our frequencies clearly
plt.grid(True)
plt.tight_layout()
plt.show()
