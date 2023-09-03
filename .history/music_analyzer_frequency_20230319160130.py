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

# Velg en starttid og slutttid for plottet
# start_time = 2.0  # sekunder
# end_time = 2.001    # sekunder


# Øk samplingsfrekvensen
new_sampling_rate = 44100
data = np.interp(np.arange(0, len(data), len(data)/new_sampling_rate), np.arange(0, len(data)), data).astype(np.int16)
sampling_rate = new_sampling_rate

# Gjennomfør Fourier-transformasjon for å dekomponere signalet til sinus-bølger
freq_domain = np.fft.fft(data)

# Finn amplituden og frekvensen til hver sinus-bølge
amplitude = np.abs(freq_domain)
frequency = np.fft.fftfreq(len(data), 1/sampling_rate)

# Velg tidsintervall å plotte (her fra 0 til 1000 millisekunder)
start_time_ms = 0
end_time_ms = 1
start_index = int(start_time_ms * sampling_rate / 1000)
end_index = int(end_time_ms * sampling_rate / 1000)


# Begrens x-aksen til ønsket tidsperiode
# plt.xlim(start_time, end_time)

# Gjør om tid til millisekunder
# evt mindre med ekstra 
time_ms = np.arange(start_index, end_index) / sampling_rate * 1000



# Plot resultatene som en sinus-kurve med tidslinje på x-aksen
fig, ax = plt.subplots()
ax.plot(np.arange(0, len(data)/sampling_rate, 1/sampling_rate), amplitude)
ax.set_xlabel("Time (ms)")
ax.set_ylabel("Frequency (Hz)")

# Begrens tidslinjen til mikrosekunder
# plt.xlim(0, len(data)/sampling_rate * 1e6)

plt.show()
