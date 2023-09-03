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
start_time = 0
end_time = len(data)/samplerate

# Ask user for time period and units to display on x-axis
time_period = float(input("Enter time period: "))
time_units = input("Enter time units (s, ms, us): ")

if time_units == "s":
    time_scale = time_sec
    xlabel = "Time (s)"
elif time_units == "ms":
    time_scale = time_ms
    xlabel = "Time (ms)"
elif time_units == "us":
    time_scale = time_us
    xlabel = "Time (us)"
else:
    print("Invalid time unit. Please enter s, ms, or us.")
    exit()

# Plot the signal in the specified time period and units
fig, ax = plt.subplots()
for i in range(start_time, end_time, int(time_period*samplerate)):
    ax.plot(time_scale[i:i+int(time_period*samplerate)], np.abs(freq_domain[i:i+int(time_period*samplerate)]))

# Set axis labels and show the plot
ax.set_xlabel(xlabel)
ax.set_ylabel("Frequency (Hz)")
plt.show()
