import numpy as np

# Parameters
sampling_rate = 8000   # 8 kHz
duration = 1.0         # 1 second
freq = 440             # A4 tone

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate a 440 Hz sine wave
signal = np.sin(2 * np.pi * freq * t)

# FFT
N = len(signal)
fft_data = np.fft.fft(signal)
fft_freqs = np.fft.fftfreq(N, 1 / sampling_rate)

# Normalize for readable magnitude
magnitude = np.abs(fft_data) * 2 / N

# Show first 20 positive frequency bins
for i in range(20):
    print(f"Freq: {fft_freqs[i]:>1.1f} Hz → Mag: {magnitude[i]:.5f}")
