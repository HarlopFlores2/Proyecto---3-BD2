import pickle
import time

import face_recognition
import scipy


class KDTree:
    def __init__(self, faces_dict):
        if isinstance(faces_dict, str):
            with open(faces_dict, 'rb') as fp:
                faces_dict = pickle.load(fp)

        self.faces_files = list(faces_dict.keys())
        self.faces_encodings = list(faces_dict.values())

        self.kdt = scipy.spatial.KDTree(self.faces_encodings)

    def knn_query(self, image_file, k=5):
        image = face_recognition.load_image_file(image_file)
        image_encoding = face_recognition.face_encodings(image)

        if len(image_encoding) > 0:
            image_encoding = image_encoding[0]
        else:
            raise RuntimeError("No face recognized in given image")

        start = time.time()
        distances, indexes = self.kdt.query(image_encoding, k)
        end = time.time()

        distances = distances.tolist()
        return distances, [self.faces_files[i] for i in indexes], (end - start)*1000 
