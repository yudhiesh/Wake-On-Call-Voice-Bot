import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np

FILE = "Audio/sample.wav"


# Waveform -> Time Domain
signal, sr = librosa.load(path=FILE, sr=22050)  # sr * T -> 22050 * 30
librosa.display.waveplot(signal, sr)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Waveform")
plt.savefig("Audio/waveform.png")
plt.show()

# Time domain to frequency domain -> Fast Fourier Transform
# fast_fourier_transform -> as many numbers of samples as the waveform 600_000
# at each of the values there are complex values
# GOAL: Move from complex numbers and get the magnitude of the values
fast_fourier_transform = np.fft.fft(signal)

# Absolute value on the complex values
# Magnitude shows the contribution of each frequency to the overall sound
magnitude = np.abs(fast_fourier_transform)
# 0Hz -> sr range of values
frequency = np.linspace(0, sr, len(magnitude))
plt.plot(frequency, magnitude)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("Power Spectrum")
plt.savefig("Audio/powerspectrum.png")
plt.show()

# We do not need the whole plot as the plot is symmetrical
# The only part of the plot that is bringing novel information is the left most
# plot
frequency = np.linspace(0, sr, len(magnitude))
left_frequency = frequency[: int(len(frequency) // 2)]
left_magnitude = magnitude[: int(len(magnitude) // 2)]
plt.plot(left_frequency, left_magnitude)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("Power Spectrum(half of sample rate)")
plt.savefig("Audio/half_powerspectrum.png")
plt.show()

# Short Time Fourier Transform -> produces a spectrogram
n_fft = 2048  # Sample rate of each interval
hop_length = 512  # How much the values are shifted to the right
short_time_fourier_transform = librosa.core.stft(
    signal, n_fft=n_fft, hop_length=hop_length
)
spectrogram = np.abs(short_time_fourier_transform)
# Take the log of the spectrogram as the values of loudness are not linearlly
# observed and instead they are log-like
log_spectrogram = librosa.amplitude_to_db(spectrogram)
librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.title("Log Spectrogram")
plt.colorbar()
plt.savefig("Audio/spectrogram.png")
plt.show()

mfccs = librosa.feature.mfcc(signal, n_fft=n_fft, hop_length=hop_length, n_mfcc=13)
librosa.display.specshow(mfccs, sr=sr, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("MFCC Coefficients")
plt.title("MFCC")
plt.colorbar()
plt.savefig("Audio/mfcc.png")
plt.show()
