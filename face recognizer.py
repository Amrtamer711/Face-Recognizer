from deepface import DeepFace
import shutil
import os
person_path = "D:/AI project pictures/comparison pictures/sajid.jpg"
input_folder = "D:/AI project pictures/detected faces"
output_folder = "D:/AI project pictures/matches"
remaining_folder = "D:/AI project pictures/non matches"
folders = os.listdir(input_folder + "/pictures")
for folder in folders:
    faces = os.listdir(input_folder + "/pictures/" + folder)
    for face in faces:
        face_path = input_folder + "/pictures/" + folder + "/" + face
        comparison = DeepFace.verify(img1_path = person_path, img2_path = face_path, model_name = 'ArcFace', detector_backend = 'retinaface', enforce_detection = False)
        if comparison["distance"] < 0.72:
            save_picture_path = output_folder + "/pictures/" + folder + "/" + face
            save_coordinates_path = output_folder + "/coordinates/" + folder + "/" + face.split('.')[0] + ".txt"
            print(save_picture_path)
            coordinates_path = input_folder + "/coordinates/" + folder + "/" + face.split('.')[0] + ".txt"
            try:
                os.makedirs(output_folder + "/pictures/" + folder, exist_ok=True)
            except FileExistsError:
                pass
            try:
                os.makedirs(output_folder + "/coordinates/" + folder, exist_ok=True)
            except FileExistsError:
                pass
            shutil.copy(face_path, save_picture_path)
            shutil.copy(coordinates_path, save_coordinates_path)
        else:
            save_picture_path = remaining_folder + "/pictures/" + folder + "/" + face
            save_coordinates_path = remaining_folder + "/coordinates/" + folder + "/" + face.split('.')[0] + ".txt"
            print(save_picture_path)
            coordinates_path = input_folder + "/coordinates/" + folder + "/" + face.split('.')[0] + ".txt"
            try:
                os.makedirs(remaining_folder + "/pictures/" + folder, exist_ok=True)
            except FileExistsError:
                pass
            try:
                os.makedirs(remaining_folder + "/coordinates/" + folder, exist_ok=True)
            except FileExistsError:
                pass
            shutil.copy(face_path, save_picture_path)
            shutil.copy(coordinates_path, save_coordinates_path)
