import pickle
import face_recognition
import numpy as np
import heapq
import time

class SequentialQuery:
    def __init__(self, encoded_dataset):
        self.dict_encoding = pickle.load(open(encoded_dataset, 'rb'))

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
        else:
            raise RuntimeError("No face recognized in given image")

        result = []
        start_time = time.time()
        for key in self.dict_encoding:
            distance = np.linalg.norm(image_encoding - self.dict_encoding[key])
            if len(result) < k:
                heapq.heappush(result, (-distance, key))
            else:
                heapq.heappushpop(result, (-distance, key))
        execution_time = time.time() - start_time
        result = [(np.abs(distance), key) for distance, key in sorted(result, reverse=True)]
        distances = [np.abs(distance).tolist() for distance, _ in result]
        result = [key for _, key in result]

        return distances, result, execution_time*1000
