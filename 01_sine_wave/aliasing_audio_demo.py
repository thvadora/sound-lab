import numpy as np
import sounddevice as sd

# ---------------------------
# CHANGE THESE VALUES
# ---------------------------
frequency = 1000        # The frequency to play (Hz)
duration = 2.0          # Seconds
amplitude = 0.5         # Safe volume

# Try these sampling rates to hear aliasing!
sampling_rates = [44100, 8000, 4000, 2000, 1000]

# ---------------------------
# PLAY TONE AT EACH SAMPLING RATE
# ---------------------------
for sr in sampling_rates:
    print(f"\nPlaying {frequency} Hz at {sr} Hz sampling rate...")
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)

    sd.play(wave, samplerate=sr)
    sd.wait()
