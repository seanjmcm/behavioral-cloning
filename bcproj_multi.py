import csv
import cv2
import numpy as np

lines = []
with open('D:/SelfDrivingCar/data-2Clockand1antigood/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        lines.append(line)
        
images = []
measurements = []

for line in lines:
    
        source_path = line[i]
	#print(source_path)
	filename=source_path.split('\\')[-1]
	current_path = '..\\data-2Clockand1antigood\\IMG\\' + filename
	image=cv2.imread(current_path)
	images.append(image)
	measurement = float(line[3])
	#flip and append
	measurements.append(measurement)
	image_flip=np.fliplr(image)
	images.append(image_flip)
	measurements.append(-measurement)
	
   
X_train = np.array(images)
y_train = np.array(measurements)

from keras.models import Sequential, Model
from keras.layers import Flatten, Dense, Lambda, Cropping2D #Lambda Wraps arbitrary expression as a Layer object. 
from keras.layers.convolutional import Convolution2D
from keras.layers import MaxPooling2D

model = Sequential()
model.add(Lambda(lambda x:x/255.0 - 0.5, input_shape=(160,320,3))) #((normalise & mean center))
model.add(Cropping2D(cropping=((58,16),(0,0)))) #crop distracting details
model.add(Convolution2D(6,5,5,activation="relu"))
model.add(MaxPooling2D())
model.add(Convolution2D(6,5,5,activation="relu"))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(120))
model.add(Dense(84))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
model.fit(X_train, y_train, validation_split=0.2,shuffle=True, nb_epoch=9)

model.save('model.h5')
print("fin")
