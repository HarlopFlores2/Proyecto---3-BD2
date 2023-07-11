from rtree import index
import face_recognition
import pickle
import time

class RtreeQuery:
    def __init__(self, encoded_dataset):
        p = index.Property()
        p.dimension = 128
        self.index = index.Index(properties=p)
        self.dict_encoding = pickle.load(open(encoded_dataset, 'rb'))
        self.build_index()

    def build_index(self):
        for i, key in enumerate(self.dict_encoding):
            self.index.insert(i, self.dict_encoding[key], obj=key)

    def knn_query(self, image_path, k):
        image = face_recognition.load_image_file(image_path)
        image_encoding = face_recognition.face_encodings(image)

        if len(image_encoding) > 0:
            image_encoding = image_encoding[0]
        else:
            raise RuntimeError("No face recognized in given image")
        
        result = []
        start_time = time.time()
        nearest = self.index.nearest(image_encoding, k, objects=True)
        execution_time = time.time() - start_time
        result = [obj.object for obj in nearest]

        return result, execution_time*1000