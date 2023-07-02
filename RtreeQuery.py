from rtree import index
import face_recognition
import pickle

class RtreeQuery:
    def __init__(self, m):
        p = index.Property()
        p.dimension = 128
        p.buffering_capacity = m
        self.index = index.Index(properties=p)
        self.dict_encoding = pickle.load(open('dict_encoding.pickle', 'rb'))
        self.build_index()

    def build_index(self):
        for i, key in enumerate(self.dict_encoding):
            self.index.insert(i, self.dict_encoding[key], obj=key)

    def knn_query(self, image_path, k):
        image = face_recognition.load_image_file(image_path)
        image_encoding = face_recognition.face_encodings(image)
        if len(image_encoding) > 0:
            image_encoding = image_encoding[0]
            nearest = self.index.nearest(image_encoding, k, objects=True)
            return [obj.object for obj in nearest]
        else:
            return []
        
