import numpy as np
import sounddevice as sd

# ---------------------------
# PARAMETERS
# ---------------------------
frequency = 116        # A4 note
duration = 4.0         # 2 seconds of sound
amplitude = 0.5        # 0.5 = safe volume (not too loud)
sampling_rate = 44100  # CD quality

# ---------------------------
# GENERATE TIME ARRAY
# ---------------------------
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# ---------------------------
# GENERATE SINE WAVE
# ---------------------------
wave = amplitude * np.sin(2 * np.pi * frequency * t)

# ---------------------------
# PLAY AUDIO
# ---------------------------
print(f"Playing {frequency} Hz for {duration} seconds...")
sd.play(wave, samplerate=sampling_rate)
sd.wait()  # Wait until playback is done
print("Done.")
