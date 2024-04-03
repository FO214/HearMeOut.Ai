import pyaudio
import wave

def record_audio(filename, duration):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    audio = pyaudio.PyAudio()

    stream = audio.open(format = FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("recording started...")

    frames = []
    seconds = duration + 1
    for i in range(0, int(RATE/CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("recording stopped...")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    audioFile = wave.open(filename, 'wb')
    audioFile.setnchannels(CHANNELS)
    audioFile.setsampwidth(audio.get_sample_size(FORMAT))
    audioFile.setframerate(RATE)
    audioFile.writeframes(b''.join(frames))
    audioFile.close()

    return filename #make it return the file path 