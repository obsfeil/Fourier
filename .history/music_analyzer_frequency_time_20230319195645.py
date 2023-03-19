import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Set the filename for the WAV file to analyze
filename = "my_audio_file.wav"

# Read in the WAV file and convert to numerical signal
sampling_rate, data = wavfile.read(filename)

# Set the time unit (in seconds)
time_unit = 1.0

# Calculate the number of samples in the chosen time period
num_samples = int(sampling_rate * time_unit)

# Set the starting time for the chosen time period (in seconds)
start_time = 0.0

# Extract the desired portion of the signal
start_sample = int(start_time * sampling_rate)
end_sample = start_sample + num_samples
data = data[start_sample:end_sample]

# Perform Fourier transform to decompose the signal into sinusoidal waves
freq_domain = np.fft.fft(data)

# Calculate the amplitude and frequency of each sinusoidal wave
amplitude = np.abs(freq_domain)
frequency = np.fft.fftfreq(len(data), 1/sampling_rate)

# Create a time array based on the chosen time unit
time = np.linspace(start_time, start_time + time_unit, num_samples)

# Plot the frequency content as a function of time
fig, ax = plt.subplots()
ax.plot(time, frequency[:len(time)], linewidth=1)
ax.set_xlim(start_time, start_time + time_unit)
ax.set_xlabel("Time (" + str(time_unit) + " s)")
ax.set_ylabel("Frequency (Hz)")
plt.show()
