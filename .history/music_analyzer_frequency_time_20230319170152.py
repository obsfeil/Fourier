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

# Velg tidsintervall å plotte (her fra 0 til varigheten av lydfilen)
start_time = 0  # sekunder
end_time = len(data) / sampling_rate  # sekunder

# Sett ønsket enhet for tidsaksen
time_unit = 'us'
# 's', 'ms' eller 'us'

# Konverter tid til ønsket enhet
if time_unit == 's':
    start_time_ms = start_time * 1000
    end_time_ms = end_time * 1000
    time_scale = 1
elif time_unit == 'ms':
    start_time_ms = start_time * 1000
    end_time_ms = end_time * 1000
    time_scale = 1000
else:
    start_time_ms = start_time * 1000000
    end_time_ms = end_time * 1000000
    time_scale = 1000000

start_index = int(start_time_ms * sampling_rate / 1000)
end_index = int(end_time_ms * sampling_rate / 1000)


# Begrens x-aksen til ønsket tidsperiode
plt.xlim(start_time_ms, end_time_ms)



time = np.arange(start_index, end_index) / sampling_rate * time_scale


# Slice the amplitude array to match the length of the time array
amplitude = amplitude[start_index:end_index]

# Plot resultatene som en sinus-kurve med tidslinje på x-aksen
fig, ax = plt.subplots()
ax.plot(time, amplitude)
ax.set_xlabel(f"Time ({time_unit})")
ax.set_ylabel("Frequency (Hz)")

plt.show()
