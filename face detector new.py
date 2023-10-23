import matplotlib.pyplot as plt
from retinaface import RetinaFace
import cv2
import os
input_folder = "D:/AI project pictures/frames"
output_folder = "D:/AI project pictures/detected faces"
frames = os.listdir(input_folder)
for frame in frames:
    frame_number = frame.split('.')[0]
    img_path = input_folder + "/" + frame
    boxes = RetinaFace.detect_faces(img_path)
    picture = cv2.imread(img_path)
    if type(boxes) == dict:
        count = 1
        for key in boxes.keys():
            identity = boxes[key]
            box = identity["facial_area"]
            output_picture_folder = output_folder + "/pictures/" + img_path.split('/')[-1].split('.')[0]
            output_coordinates_folder = output_folder + "/coordinates/" + img_path.split('/')[-1].split('.')[0]
            face = picture[box[1]:box[3], box[0]:box[2]]
            try:
                os.makedirs(output_picture_folder, exist_ok=True)
            except FileExistsError:
                pass
            try:
                os.makedirs(output_coordinates_folder, exist_ok=True)
            except FileExistsError:
                pass
            save_path = output_folder + f'/pictures/{frame_number}/face_' + str(count) + '.png'
            print(save_path)
            cv2.imwrite(save_path, face)
            coordinates = open(f'{output_folder}/coordinates/{frame_number}/face_{count}.txt', 'w')
            coordinates.write(f'{box[0]}\n{box[1]}\n{box[2]}\n{box[3]}\n')
            coordinates.close()
            cv2.rectangle(picture, (box[2], box[3]), (box[0], box[1]), (255, 255, 255), 1)
            count += 1
        plt.figure(figsize = (20, 20))
        plt.imshow(picture[:, :, : :-1])
        plt.show()
            
            
            
            
            
            
