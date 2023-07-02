import face_recognition
import os
from os import listdir
import pickle


path_project = os.getcwd()
path_dir_images = os.path.join(path_project, 'lfw')
dir_list = listdir(path_dir_images)
dict_encoding = {}
for dir_imagename in dir_list:
    path_dir_imagename = os.path.join(path_dir_images, dir_imagename)
    if os.path.isdir(path_dir_imagename):
        imagename_list = listdir(path_dir_imagename)
        for imagename in imagename_list:
            path_imagename = os.path.join(path_dir_imagename, imagename)
            image = face_recognition.load_image_file(path_imagename)
            image_encoding = face_recognition.face_encodings(image)
            if len(image_encoding) > 0:
                image_encoding = image_encoding[0]
                dict_encoding[path_imagename] = image_encoding
 
pickle.dump(dict_encoding, open('dict_encoding.pickle', 'wb'))

                
