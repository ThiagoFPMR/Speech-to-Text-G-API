import os
from datetime import datetime
from google.cloud import speech
from transcribe_local import transcribe_local

# Defining all important variables

bucket_name = 'name-of-your-bucket'

config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code="en-US",
            audio_channel_count=1,
            enable_automatic_punctuation=True
        )

source_path = 'audio'
destination_path = 'text'

# Running the transcriber

now = datetime.now()
current_time = now.strftime('%Y-%m-%d-%H-%M-%S')

transcriptions_folder = f'{destination_path}/{current_time}'
os.makedirs(transcriptions_folder)

for index, file in enumerate(os.listdir(source_path)):
    result = transcribe_local(f'{source_path}/{file}', bucket_name=bucket_name, config=config)
    with open(f'{transcriptions_folder}/{index}.txt', 'w') as f:
        f.write(result)

