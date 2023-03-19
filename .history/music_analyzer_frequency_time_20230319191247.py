import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import datetime

dt = datetime.datetime.now()  # nåværende tidspunkt
dt_with_microsecond = dt + datetime.timedelta(microseconds=1)  
# legg til en mikrosekund

# Sett inn filnavn for lydfilen du vil analysere
filename = "my_audio_file.wav"

# Les inn lydfilen og konverter til numerisk signal
sampling_rate, data = wavfile.read(filename)

# Øk samplingsfrekvensen
new_sampling_rate = 44100
data = np.interp(np.arange(0, len(data), len(data)/new_sampling_rate), np.arange(0, len(data)), data).astype(np.int16)
sampling_rate = new_sampling_rate

# Gjennomfør Fourier-transformasjon for å dekomponere signalet til sinus-bølger
freq_domain = np.fft.fft(data)

# Finn amplituden og frekvensen til hver sinus-bølge
amplitude = np.abs(freq_domain)
frequency = np.fft.fftfreq(len(data), 1/sampling_rate)

# Set the desired time unit and time range
time_unit = 'ms'
start_time_sec = 0.5  # Start time in seconds
end_time_sec = 1.0  # End time in seconds

# Define a dictionary to convert time units to factors
time_unit_factors = {'s': 1, 'ms': 1e3, 'us': 1e6, 'ns': 1e9}

# Get the time unit factor
time_unit_factor = time_unit_factors[time_unit]

# Convert start and end times to samples
start_index = int(start_time_sec * sampling_rate)
end_index = int(end_time_sec * sampling_rate)

# Begrens x-aksen til ønsket tidsperiode
plt.xlim(start_time_sec * time_unit_factor, end_time_sec * time_unit_factor)
plt.ylim(0, 30000)  # Set the y-axis range from 0 to 30000 Hz

# Konverter tid til ønsket enhet
time = np.arange(start_index, end_index) / sampling_rate * time_unit_factor

# Slice the frequency array using the same index
frequency = frequency[start_index:end_index]

# Slice the amplitude array to match the length of the time array
amplitude = amplitude[start_index:end_index]
amplitude_normalized = amplitude / np.max(amplitude)

# Plot resultatene som en sinus-kurve med tidslinje på x-aksen
fig, ax = plt.subplots()
ax.plot(time, amplitude_normalized)
ax.set_xlabel(f"Time ({time_unit})")
ax.set_ylabel("Frequency (Hz)")
ax.set_ylabel("amplitude")
plt.show()
