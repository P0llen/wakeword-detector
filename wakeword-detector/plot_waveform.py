import matplotlib.pyplot as plt
import numpy as np
import librosa

file_path = "test_sample.wav"

y, sr = librosa.load(file_path, sr=16000)

plt.figure(figsize=(10, 4))
plt.plot(np.linspace(0, len(y) / sr, num=len(y)), y)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Recorded Audio Waveform")
plt.show()

