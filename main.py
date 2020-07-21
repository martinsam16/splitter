from splitter.AudioSplitter import AudioSplitter
from splitter.ImageSplitter import ImageSplitter
from splitter.VideoSplitter import VideoSplitter

path_video = './video.mp4'

# split video range (minutes, seconds)
start_video = (0, 0)
end_video = (6, 12)

# split per n minutes
minutes_per_split_audio = 2
seconds_per_split_video = 30

# percent of similarity between images for delete
min_similarity_images = 0.90

# paths save
path_audio_save = 'audio.wav'
folder_audio_splitted = './audio_splitted/'
folder_images = './images/'
path_text_save = './text.txt'

video_splitter = VideoSplitter(path_video=path_video, start=start_video, end=end_video)
video_splitter.split_images(path_folder_save=folder_images, seconds_per_split=seconds_per_split_video)
video_splitter.extract_audio(path_file_save=path_audio_save)

audio_splitter = AudioSplitter(path_audio=path_audio_save, path_folder_split=folder_audio_splitted)
audio_splitter.multiple_split(min_per_split=minutes_per_split_audio)

image_splitter = ImageSplitter()
image_splitter.delete_image_similarity(path_folder_images=folder_images, min_similarity=min_similarity_images)

AudioSplitter.extract_text_from_folder(path_folder=folder_audio_splitted, path_txt=path_text_save)
