import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft

# Load wav file
from scipy.io import wavfile
sample_rate, data = wavfile.read('my_audio_file.wav')

# Set time unit and period
time_unit = 1/sample_rate
time_period = 1

# Create time array
time = np.arange(0, len(data)/sample_rate, time_unit)

# Create frequency array using FFT
fft_data = fft(data)
frequency = np.linspace(0, sample_rate/2, len(data)//2)

# Plot time vs. frequency
fig, ax = plt.subplots()
ax.plot(time, np.abs(fft_data[:len(data)//2])) # type: ignore
ax.set_xlabel('Time (s)')
ax.set_ylabel('Frequency (Hz)')

plt.show()
