import os
import io
import math
import shutil

import speech_recognition as sr
from pydub import AudioSegment


class AudioSplitter:

    def __init__(self, path_audio: str, path_folder_split: str):
        self.path_folder_split = path_folder_split
        self.path_audio = path_audio
        self.audio = AudioSegment.from_wav(self.path_audio)

    @classmethod
    def extract_text_from_file(cls, path_audio: str, language: str = 'ES'):
        recognizer = sr.Recognizer()
        audio_file = sr.AudioFile(path_audio)
        with audio_file as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio_data=audio, language=language)
        except Exception:
            return ''

    @classmethod
    def extract_text_from_folder(cls, path_folder: str, path_txt: str, language: str = 'ES'):
        if os.path.exists(path_txt):
            os.remove(path_txt)
        audios = os.listdir(path_folder)
        audios.sort()
        for audio in audios:
            path_audio = os.path.join(path_folder, audio)
            print(f'extracting text from: {path_audio}')
            text = cls.extract_text_from_file(path_audio, language) + ' '
            with io.open(path_txt, 'a', encoding='utf8') as text_file:
                text_file.write(text)
            print(f'text extracted from: {path_audio}')

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_min, to_min, split_filename):
        start = from_min * 60 * 1000
        end = to_min * 60 * 1000
        split_audio = self.audio[start:end]
        split_audio.export(os.path.join(self.path_folder_split, split_filename), format="wav")

    def multiple_split(self, min_per_split: int):
        if os.path.exists(self.path_folder_split):
            shutil.rmtree(self.path_folder_split)
        os.mkdir(self.path_folder_split)
        min_total = math.ceil(self.get_duration() / 60)
        for i in range(0, min_total, min_per_split):
            num_file = '0' * (len(str(min_total)) - len(str(i))) + str(i)
            name_file = str(num_file) + '.wav'
            self.single_split(i, i + min_per_split, name_file)
