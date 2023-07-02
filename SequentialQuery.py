import pickle
import face_recognition
import numpy as np
import heapq

class SequentialQuery:
    def __init__(self):
        self.dict_encoding = pickle.load(open('dict_encoding.pickle', 'rb'))

    def range_query(self, image_path, r):
        image = face_recognition.load_image_file(image_path)
        image_encoding = face_recognition.face_encodings(image)
        if len(image_encoding) > 0:
            image_encoding = image_encoding[0]
            result = []
            for key in self.dict_encoding:
                distance = np.linalg.norm(image_encoding - self.dict_encoding[key])
                if distance <= r:
                    result.append(key)
            return sorted(result)
        else:
            return []
        
    def knn_query(self, image_path, k):
        image = face_recognition.load_image_file(image_path)
        image_encoding = face_recognition.face_encodings(image)
        if len(image_encoding) > 0:
            image_encoding = image_encoding[0]
            result = []
            for key in self.dict_encoding:
                distance = np.linalg.norm(image_encoding - self.dict_encoding[key])
                if len(result) < k:
                    heapq.heappush(result, (-distance, key))
                else:
                    heapq.heappushpop(result, (-distance, key))
            return [key for _, key in sorted(result)]
        else:
            return []