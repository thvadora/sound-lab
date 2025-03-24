# Sine Wave Generator & Visualizer

This is a simple Python script that generates and plots a sine wave — the basic building block of all sound.

## 🔊 What is a Sine Wave?

A sine wave is a smooth, periodic oscillation. It's the simplest form of a sound wave, and it represents a **pure tone**. Musical notes can be modeled as combinations of sine waves.

### Formula:

y(t) = A * sin(2*pi*f*t)

Where:
- **A** = Amplitude (volume)
- **f** = Frequency in Hertz (pitch)
- **t** = Time (in seconds)

## ⚙️ Parameters

In `sine_wave_plot.py`, you can change:
- `frequency` – try 440Hz (A4), 880Hz (A5), 100Hz (bass)
- `amplitude` – range: 0.0 (silent) to 1.0 (max)
- `duration` – how long the wave lasts
- `sampling_rate` – how many samples per second (CD audio is 44100 Hz)

## 📈 Output

The script generates a time array and computes the sine wave, then uses `matplotlib` to display the waveform.

## ✅ Requirements

Install with pip:

'''pip install matplotlib
pip install numpy'''




