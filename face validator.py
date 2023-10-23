import os
import shutil
true_positives = {}
false_positives = {}
true_negatives = {}
false_negatives = {}
matched_coordinates_folder = "D:/AI project pictures/matches/coordinates"
non_matched_coordinates_folder = "D:/AI project pictures/non matches/coordinates"
annotation_coordinates_folder = "D:/AI project pictures/annotated faces/coordinates"
frames = os.listdir(matched_coordinates_folder)
for frame in frames:
    faces = os.listdir(matched_coordinates_folder + f'/{frame}')
    with open(annotation_coordinates_folder + f'/{frame}.txt', "r") as annotated_coordinates_file: 
        annotated_coordinates = annotated_coordinates_file.readlines()
    for face in faces:
        with open(matched_coordinates_folder + f'/{frame}/{face}', "r") as matched_coordinates_file: 
            matched_coordinates = matched_coordinates_file.readlines()
        difference_xtl = abs(int(matched_coordinates[0].split('\n')[0]) - int(float(annotated_coordinates[0].split('\n')[0])))
        difference_ytl = abs(int(matched_coordinates[1].split('\n')[0]) - int(float(annotated_coordinates[1].split('\n')[0])))
        difference_xbr = abs(int(matched_coordinates[2].split('\n')[0]) - int(float(annotated_coordinates[2].split('\n')[0])))
        difference_ybr = abs(int(matched_coordinates[3].split('\n')[0]) - int(float(annotated_coordinates[3].split('\n')[0])))
        if (difference_xtl < 200 and difference_xbr < 200 and difference_ytl < 200 and difference_ybr < 200):
            if frame in true_positives:
                true_positives[frame].append(face.split('.')[0])
            else:
                true_positives[frame] = [face.split('.')[0]]
        else:
            if frame in false_positives:
                false_positives[frame].append(face.split('.')[0])
            else:
                false_positives[frame] = [face.split('.')[0]]
frames = os.listdir(non_matched_coordinates_folder)
for frame in frames:
    faces = os.listdir(non_matched_coordinates_folder + f'/{frame}')
    with open(annotation_coordinates_folder + f'/{frame}.txt', "r") as annotated_coordinates_file: 
        annotated_coordinates = annotated_coordinates_file.readlines()
    for face in faces:
        with open(non_matched_coordinates_folder + f'/{frame}/{face}', "r") as non_matched_coordinates_file: 
            non_matched_coordinates = non_matched_coordinates_file.readlines()
        difference_xtl = abs(int(non_matched_coordinates[0].split('\n')[0]) - int(float(annotated_coordinates[0].split('\n')[0])))
        difference_ytl = abs(int(non_matched_coordinates[1].split('\n')[0]) - int(float(annotated_coordinates[1].split('\n')[0])))
        difference_xbr = abs(int(non_matched_coordinates[2].split('\n')[0]) - int(float(annotated_coordinates[2].split('\n')[0])))
        difference_ybr = abs(int(non_matched_coordinates[3].split('\n')[0]) - int(float(annotated_coordinates[3].split('\n')[0])))
        if (difference_xtl > 200 or difference_xbr > 200 or difference_ytl > 200 or difference_ybr > 200):
            if frame in true_negatives:
                true_negatives[frame].append(face.split('.')[0])
            else:
                true_negatives[frame] = [face.split('.')[0]]
        else:
            if frame in false_negatives:
                false_negatives[frame].append(face.split('.')[0])
            else:
                false_negatives[frame] = [face.split('.')[0]]
for frame in true_positives.keys():
    faces = true_positives[frame]
    for face in faces:
        picture = f'D:/AI project pictures/matches/pictures/{frame}/{face}.png'
        coordinates = f'D:/AI project pictures/matches/coordinates/{frame}/{face}.txt'
        save_picture_path = f'D:/AI project pictures/true positives/pictures/{frame}/{face}.png'
        save_coordinates_path = f'D:/AI project pictures/true positives/coordinates/{frame}/{face}.txt'
        try:
            os.makedirs(f'D:/AI project pictures/true positives/pictures/{frame}', exist_ok=True)
        except FileExistsError:
            pass
        try:
            os.makedirs(f'D:/AI project pictures/true positives/coordinates/{frame}', exist_ok=True)
        except FileExistsError:
            pass
        shutil.copy(picture, save_picture_path)
        shutil.copy(coordinates, save_coordinates_path)
for frame in false_positives.keys():
    faces = false_positives[frame]
    for face in faces:
        picture = f'D:/AI project pictures/matches/pictures/{frame}/{face}.png'
        coordinates = f'D:/AI project pictures/matches/coordinates/{frame}/{face}.txt'
        save_picture_path = f'D:/AI project pictures/false positives/pictures/{frame}/{face}.png'
        save_coordinates_path = f'D:/AI project pictures/false positives/coordinates/{frame}/{face}.txt'
        try:
            os.makedirs(f'D:/AI project pictures/false positives/pictures/{frame}', exist_ok=True)
        except FileExistsError:
            pass
        try:
            os.makedirs(f'D:/AI project pictures/false positives/coordinates/{frame}', exist_ok=True)
        except FileExistsError:
            pass
        shutil.copy(picture, save_picture_path)
        shutil.copy(coordinates, save_coordinates_path)
for frame in true_negatives.keys():
    faces = true_negatives[frame]
    for face in faces:
        picture = f'D:/AI project pictures/non matches/pictures/{frame}/{face}.png'
        coordinates = f'D:/AI project pictures/non matches/coordinates/{frame}/{face}.txt'
        save_picture_path = f'D:/AI project pictures/true negatives/pictures/{frame}/{face}.png'
        save_coordinates_path = f'D:/AI project pictures/true negatives/coordinates/{frame}/{face}.txt'
        try:
            os.makedirs(f'D:/AI project pictures/true negatives/pictures/{frame}', exist_ok=True)
        except FileExistsError:
            pass
        try:
            os.makedirs(f'D:/AI project pictures/true negatives/coordinates/{frame}', exist_ok=True)
        except FileExistsError:
            pass
        shutil.copy(picture, save_picture_path)
        shutil.copy(coordinates, save_coordinates_path)
for frame in false_negatives.keys():
    faces = false_negatives[frame]
    for face in faces:
        picture = f'D:/AI project pictures/non matches/pictures/{frame}/{face}.png'
        coordinates = f'D:/AI project pictures/non matches/coordinates/{frame}/{face}.txt'
        save_picture_path = f'D:/AI project pictures/false negatives/pictures/{frame}/{face}.png'
        save_coordinates_path = f'D:/AI project pictures/false negatives/coordinates/{frame}/{face}.txt'
        try:
            os.makedirs(f'D:/AI project pictures/false negatives/pictures/{frame}', exist_ok=True)
        except FileExistsError:
            pass
        try:
            os.makedirs(f'D:/AI project pictures/false negatives/coordinates/{frame}', exist_ok=True)
        except FileExistsError:
            pass
        shutil.copy(picture, save_picture_path)
        shutil.copy(coordinates, save_coordinates_path)
print(f'There were {len(true_positives)} faces that the algoirthm correctly matched to the target.\nThere were {len(false_positives)} faces that the algoirthm incorrectly matched to the target.\nThere were {len(true_negatives)} faces that the algoirthm correctly differentiated from the target.\nThere were {len(false_negatives)} faces that the algoirthm failed to match the target.')
matching_accuracy = round(len(true_positives) / (len(true_positives) + len(false_negatives)) * 100, 1)
differentating_accuracy = round(len(true_negatives) / (len(true_negatives) + len(false_positives)) * 100, 1)
print(f'The algorithm in this test had a matching accuracy of {matching_accuracy}% and differentating accuracy of {differentating_accuracy}')