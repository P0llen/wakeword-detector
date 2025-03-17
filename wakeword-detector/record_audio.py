import sounddevice as sd
import numpy as np
import wave

fs = 16000  # Sample rate
duration = 3  # Increase recording duration to 3 seconds
filename = "test_sample.wav"

print("Recording... Speak now!")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()  # Wait until recording is finished
print("Recording complete!")

# Save as WAV file
wavefile = wave.open(filename, 'wb')
wavefile.setnchannels(1)
wavefile.setsampwidth(2)
wavefile.setframerate(fs)
wavefile.writeframes(recording.tobytes())
wavefile.close()

print(f"Saved recording as {filename}")

