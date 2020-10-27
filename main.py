import os

from splitter.AudioSplitter import AudioSplitter
from splitter.ImageSplitter import ImageSplitter
from splitter.VideoSplitter import VideoSplitter

from ui import *


class MainWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButtonOk.clicked.connect(self.process)

    def process(self):
        # paths save
        folder_save = self.inptOutputFolder.toPlainText()
        if not os.path.exists(folder_save):
            os.mkdir(folder_save)
        path_audio_save = os.path.join(folder_save, 'audio.wav')
        folder_audio_splitted = os.path.join(folder_save, 'audio_splitted')
        folder_images = os.path.join(folder_save, 'images')
        path_text_save = os.path.join(folder_save, 'text.txt')

        # split video range (minutes, seconds)
        path_video = self.inptPathVideo.toPlainText()
        start_video = (self.spinMinStart.value(), self.spinSecStart.value())
        end_video = (self.spinMinEnd.value(), self.spinSecEnd.value())

        # split per n minutes
        minutes_per_split_audio = 2
        seconds_per_split_video = self.spinSecSplit.value()

        # percent of similarity between images for delete
        min_similarity_images = self.doubleSpinSimilarity.value()

        video_splitter = VideoSplitter(path_video=path_video, start=start_video, end=end_video)
        video_splitter.split_images(path_folder_save=folder_images, seconds_per_split=seconds_per_split_video)

        image_splitter = ImageSplitter()
        image_splitter.delete_image_similarity(path_folder_images=folder_images, min_similarity=min_similarity_images)

        # Extract speech
        if self.checkBoxSpeechRecognition.isChecked():
            video_splitter.extract_audio(path_file_save=path_audio_save)
            audio_splitter = AudioSplitter(path_audio=path_audio_save, path_folder_split=folder_audio_splitted)
            audio_splitter.multiple_split(min_per_split=minutes_per_split_audio)
            AudioSplitter.extract_text_from_folder(path_folder=folder_audio_splitted, path_txt=path_text_save)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
