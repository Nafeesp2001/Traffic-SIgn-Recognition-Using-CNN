import numpy as np
import cv2
import pickle
import gradio as gr
from gtts import gTTS
import os
img = cv2.imread("/traffic-sign/bumpy.png")
threshold = 0.5# PROBABLITY THRESHOLD
pickle_in = open("/traffic-sign/model_trained3.p", "rb")  ## rb = READ BYTE
model = pickle.load(pickle_in)


def grayscale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    return img


def equalize(img):
    img = cv2.equalizeHist(img)


    return img


def preprocessing(img):
    img = grayscale(img)


    img = equalize(img)
    img = img / 255
    return img


def getCalssName(classNo):
    if classNo == 0:

        return 'Speed Limit 20 km/h'
    elif classNo == 1:
        return 'Speed Limit 30 km/h'
    elif classNo == 2:
        return 'Speed Limit 50 km/h'
    elif classNo == 3:
        return 'Speed Limit 60 km/h'
    elif classNo == 4:
        return 'Speed Limit 70 km/h'
    elif classNo == 5:
        return 'Speed Limit 80 km/h'
    elif classNo == 6:
        return 'End of Speed Limit 80 km/h'
    elif classNo == 7:
        return 'Speed Limit 100 km/h'
    elif classNo == 8:
        return 'Speed Limit 120 km/h'
    elif classNo == 9:
        return 'No passing'
    elif classNo == 10:
        return 'No passing for vechiles over 3.5 metric tons'
    elif classNo == 11:
        return 'Right-of-way at the next intersection'
    elif classNo == 12:
        return 'Priority road'
    elif classNo == 13:
        return 'Yield'
    elif classNo == 14:
        return 'Stop'
    elif classNo == 15:
        return 'No vechiles'
    elif classNo == 16:
        return 'Vechiles over 3.5 metric tons prohibited'
    elif classNo == 17:
        return 'No entry'
    elif classNo == 18:
        return 'General caution'
    elif classNo == 19:
        return 'Dangerous curve to the left'
    elif classNo == 20:
        return 'Dangerous curve to the right'
    elif classNo == 21:
        return 'Double curve'
    elif classNo == 22:
        return 'Bumpy road'
    elif classNo == 23:
        return 'Slippery road'
    elif classNo == 24:
        return 'Road narrows on the right'
    elif classNo == 25:
        return 'Road work'
    elif classNo == 26:
        return 'Traffic signals'
    elif classNo == 27:
        return 'Pedestrians'
    elif classNo == 28:
        return 'Children crossing'
    elif classNo == 29:
        return 'Bicycles crossing'
    elif classNo == 30:
        return 'Beware of ice/snow'
    elif classNo == 31:
        return 'Wild animals crossing'
    elif classNo == 32:
        return 'End of all speed and passing limits'
    elif classNo == 33:
        return 'Turn right ahead'
    elif classNo == 34:
        return 'Turn left ahead'
    elif classNo == 35:
        return 'Ahead only'
    elif classNo == 36:
        return 'Go straight or right'
    elif classNo == 37:
        return 'Go straight or left'
    elif classNo == 38:
        return 'Keep right'
    elif classNo == 39:
        return 'Keep left'
    elif classNo == 40:
        return 'Roundabout mandatory'
    elif classNo == 41:
        return 'End of no passing'
    elif classNo == 42:
        return 'End of no passing by vechiles over 3.5 metric tons'

def classify_image(img):

    img = np.asarray(img)
    img = cv2.resize(img, (32, 32))
    img = preprocessing(img)
    img = img.reshape(1, 32, 32, 1)
    while True:
        predictions = model.predict(img)
            #classIndex = model.predict_classes(img)
        predict_x=model.predict(img)
        classIndex=np.argmax(predict_x,axis=1)
            #classIndex = (model.predict(img) > 0.5)*1
            #classIndex = (model.predict(img) > 0.5)*1


        probabilityValue = np.amax(predictions)
        print(probabilityValue)
        return str(getCalssName(classIndex))
        break

                # print(getCalssName(classIndex))
                #print(str(classIndex) )
                #print(str(getCalssName(classIndex)))

image = gr.inputs.Image(shape=(32,32))
label = gr.outputs.Label(num_top_classes=3)
gr.Interface(fn=classify_image, inputs=image,outputs=label,css=".gradio-container {background-color: red}").launch(share=True)


