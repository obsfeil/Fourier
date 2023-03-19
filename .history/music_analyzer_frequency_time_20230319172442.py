import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import math
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

# Velg tidsintervall å plotte (her fra 0 til varigheten av lydfilen i ønsket tidsenhet)
start_time = 0
end_time = len(data) / sampling_rate
time_interval = 0.1  # tidsintervall i sekunder, endres etter behov

if time_interval >= 1:
    start_index = int(start_time * sampling_rate)
    end_index = int(end_time * sampling_rate)
    time_unit = 's'
    time_scale = 1
elif time_interval >= 1e-3:
    start_index = int(start_time * sampling_rate / 1000)
    end_index = int(end_time * sampling_rate / 1000)
    time_unit = 'ms'
    time_scale = 1000
else:
    start_index = int(start_time * sampling_rate / 1e6)
    end_index = int(end_time * sampling_rate / 1e6)
    time_unit = 'us'
    time_scale = 1e6

# Begrens x-aksen til ønsket tidsperiode
plt.xlim(start_time * time_scale, end_time * time_scale)

# Konverter tid til ønsket enhet
time = np.arange(start_index, end_index) / sampling_rate * time_scale



# Slice the frequency array using the same index
frequecy= frequency[start_index:end_index]


# Slice the amplitude array to match the length of the time array
# amplitude = amplitude[start_index:end_index]

# Plot resultatene som en sinus-kurve med tidslinje på x-aksen
fig, ax = plt.subplots()
ax.plot(time, amplitude)
ax.set_xlabel(f"Time ({time_unit})")
ax.set_ylabel("Frequency (Hz)")

plt.show()
