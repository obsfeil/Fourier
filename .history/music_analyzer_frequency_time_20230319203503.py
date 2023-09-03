import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

# Load the .wav file
filename = 'my_audio_file.wav'
samplerate, data = wav.read(filename)

# Define the time scale in seconds, milliseconds, and microseconds
time_sec = np.arange(0, len(data)/samplerate, 1/samplerate)
time_ms = np.arange(0, len(data)/samplerate*1000, 1/samplerate*1000)
time_us = np.arange(0, len(data)/samplerate*1000000, 1/samplerate*1000000)

# Define the frequency domain of the signal using Fourier transform
freq_domain = np.fft.fft(data)
freq = np.fft.fftfreq(len(data), 1/samplerate)

# Define the start and end times for the plot
start_time = int(input("Enter start time in seconds: "))
end_time = int(input("Enter end time in seconds: "))
time_period = float(input("Enter time period: "))
time_units = input("Enter time units (s, ms, us): ")
samplerate = 48000



if time_units == 's':
    time_period *= 1
elif time_units == 'ms':
    time_period *= 0.001
elif time_units == 'us':
    time_period *= 0.000001
else:
    print("Invalid time units. Please enter s, ms, or us.")

# Plot the signal in the specified time period and units
fig, ax = plt.subplots()
for i in range(start_time * samplerate, end_time * samplerate, int(time_period * samplerate)):
    ax.plot(freq, np.abs(freq_domain[i:i+int(time_period*samplerate)]))

# Set axis labels and show the plot
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Amplitude")

plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.show()
