import pyaudio
import wave

# Parameters
CHUNK = 1024  
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1  # Number of audio channels
RATE = 44100  # Sampling rate (samples per second)
# DEVICE_INDEX = 1
OUTPUT_FILENAME = "song.wav"

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("Recording... Press Ctrl+C to stop.")

try:
    # Record audio
    audio_frames = []
    while True:
        data = stream.read(CHUNK)
        audio_frames.append(data)

except KeyboardInterrupt:
    # Stop recording on Ctrl+C
    print("Recording stopped.")

# Close the stream
stream.stop_stream()
stream.close()
p.terminate()

# Save the recorded audio to a WAV file
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(audio_frames))

print(f"Audio saved as {OUTPUT_FILENAME}")
