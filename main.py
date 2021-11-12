import os
from datetime import datetime
from google.cloud import speech
from transcribe_local import transcribe_local

# Defining all important variables

bucket_name = 'name-of-your-bucket'

config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
            sample_rate_hertz=48000,
            language_code="pt-BR",
            audio_channel_count=1,
            enable_automatic_punctuation=True,
            enable_spoken_punctuation=False,
            model="phone_call",
            use_enhanced=True
        )

source_path = 'audio'
destination_path = 'text'

# Running the transcriber

now = datetime.now()
current_time = now.strftime('%Y-%m-%d-%H-%M-%S')

transcriptions_folder = f'{destination_path}/{current_time}'
os.makedirs(transcriptions_folder)

print(transcriptions_folder)
print('Initializing transcriptions...')

for file in os.listdir(source_path):
    results = transcribe_local(f'{source_path}/{file}', bucket_name=bucket_name, config=config)
    with open(f'{transcriptions_folder}/{file[:-4]}.txt', 'w') as f:
        for result in results:
            f.write(result.alternatives[0].transcript + ' ')

