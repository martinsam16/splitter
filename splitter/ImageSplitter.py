import os
import cv2

from skimage.measure import compare_ssim


class ImageSplitter:

    def delete_image_similarity(self, path_folder_images: str, min_similarity: float = 0.90):
        images = os.listdir(path_folder_images)
        images.sort()
        try:
            for indice in range(len(images)):
                path_image1 = os.path.join(path_folder_images, images[indice])
                path_image2 = os.path.join(path_folder_images, images[indice + 1])
                if self.image_similarity(path_image1, path_image2) >= min_similarity:
                    os.remove(path_image1)
                    print(f'similar image deleted: ' + path_image1)
        except Exception:
            pass

    def image_similarity(self, path_image1: str, path_image2: str):
        imagen1_bw = cv2.cvtColor(cv2.imread(path_image1), cv2.COLOR_BGR2GRAY)
        imagen2_bw = cv2.cvtColor(cv2.imread(path_image2), cv2.COLOR_BGR2GRAY)
        (score, diff) = compare_ssim(imagen1_bw, imagen2_bw, full=True)
        print(f'score {score}')
        return score
