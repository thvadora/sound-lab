import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# PARAMETERS YOU CAN CHANGE
# ---------------------------
frequency = 440        # Frequency in Hz (440 = A4 note)
duration = 0.01        # Duration in seconds (short for clean plot)
amplitude = 1.0        # Volume (1.0 = max, 0.5 = half volume)
sampling_rate = 44100  # Samples per second (CD quality)

# ---------------------------
# GENERATE TIME ARRAY
# ---------------------------
# Create an array of time points, evenly spaced
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# ---------------------------
# CREATE SINE WAVE
# ---------------------------
# Apply the formula: y(t) = A * sin(2πft)
y = amplitude * np.sin(2 * np.pi * frequency * t)

# ---------------------------
# PLOT THE WAVE
# ---------------------------
plt.figure(figsize=(10, 4))
plt.plot(t, y)
plt.title(f"Sine Wave: {frequency} Hz")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()
