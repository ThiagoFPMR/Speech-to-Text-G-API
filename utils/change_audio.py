from pydub import AudioSegment
sound = AudioSegment.from_wav("test_file.wav")
sound = sound.set_channels(1)
sound.export("path.wav", format="wav")