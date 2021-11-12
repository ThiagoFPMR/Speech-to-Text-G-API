from pydub import AudioSegment
from playsound import playsound
import os

source_path = '../audio'

for index, file in enumerate(os.listdir(source_path)):
    sound = AudioSegment.from_file(f'{source_path}/{file}')
    sound = sound.set_channels(1)
    sound.export(f'{source_path}/{file[:-4]}.flac', format='flac')