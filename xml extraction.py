import xmltodict
import matplotlib.pyplot as plt
with open("C:/Users/ATMH2/Documents/Python codes/Face Detection/annotations.xml") as file:
    file_data = file.read() # read file contents
    
    # parse data using package
    dict_data = xmltodict.parse(file_data)


def crop(dict_data, i):
    filename = "D:/AI project pictures/frames/frame_{}.png".format(int(dict_data["annotations"]["track"]["box"][i]['@frame']))
    image = plt.imread(filename)
    x0 = dict_data["annotations"]["track"]["box"][i]['@xtl']
    x0 = int(float(x0))
    print(x0)
    y0 = dict_data["annotations"]["track"]["box"][i]['@ytl']
    y0 = int(float(y0))
    print(y0)
    width = dict_data["annotations"]["track"]["box"][i]['@xbr']
    width = int(float(width))
    print(width)
    height = dict_data["annotations"]["track"]["box"][i]['@ybr']
    height = int(float(height))
    print(height)
    print("\n")
    return image[y0:height , x0:width, :]

for i in range(0, len(dict_data["annotations"]["track"]["box"])):

    # filename = "hi/images/frame_{:06}.PNG".format(i)
    image = crop(dict_data, i)
    plt.imsave("D:/AI project pictures/annotated faces/pictures/frame_{}.png".format(i), image)
    coordinates = open(f'D:/AI project pictures/annotated faces/coordinates/frame_{i}.txt', 'w')
    pic = dict_data["annotations"]["track"]["box"][i]
    coordinates.write("{}\n{}\n{}\n{}\n".format(pic['@xtl'], pic['@ytl'], pic['@xbr'], pic['@ybr']))
    coordinates.close()
'''xml data is in the form of top left x, top left y, bottom right x, bottom right y'''