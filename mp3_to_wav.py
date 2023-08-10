import os
from pathlib import Path
from pydub import AudioSegment

files_to_convert = ["record_1.mp3", "record_3.mp3", "record_4.mp3", "record_5.mp3"]
AudioSegment.ffmpeg = os.getcwd()+"\\ffmpeg.exe"
print(AudioSegment.ffmpeg)


for file in files_to_convert:
    print(Path(file).is_file())
    sound = AudioSegment.from_mp3(file)
    sound.export(f"{file.split('.')[0]}.wav", format="wav")