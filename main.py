import os
from datetime import datetime
from google.cloud import speech
from transcribe_local import transcribe_local

config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code="en-US",
            audio_channel_count=1,
            enable_automatic_punctuation=True
        )

now = datetime.now()
current_time = now.strftime('%Y-%m-%d-%H-%M-%S')

source_path = 'audio'
destination_path = f'text/{current_time}'
os.makedirs(destination_path)

for index, file in enumerate(os.listdir(source_path)):
    result = transcribe_local(f'{source_path}/{file}', config=config)
    with open(f'{destination_path}/{index}.txt', 'w') as f:
        f.write(result)

