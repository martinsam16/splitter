import os
import shutil

from moviepy.editor import VideoFileClip


class VideoSplitter:

    def __init__(self, path_video: str, start: tuple, end: tuple):
        self._clip = self._extract_clip(path_video, start, end)

    def _extract_clip(self, path_video: str, start: tuple, end: tuple):
        clip = VideoFileClip(path_video)
        clip = clip.subclip(t_start=start, t_end=end)
        return clip

    def extract_audio(self, path_file_save: str):
        self._clip.audio.write_audiofile(path_file_save, ffmpeg_params=["-ac", "1"])

    def get_duration(self):
        return self._clip.duration

    def split_images(self, path_folder_save: str, seconds_per_split: int):
        duration = int(self.get_duration())
        if os.path.exists(path_folder_save):
            shutil.rmtree(path_folder_save)
        os.mkdir(path_folder_save)
        for i in range(0, duration, seconds_per_split):
            num_file = '0' * (len(str(duration)) - len(str(i))) + str(i)
            name_file = os.path.join(path_folder_save, str(num_file) + '.jpg')
            self._clip.save_frame(name_file, i)
            print(f'image saved: {name_file}')
