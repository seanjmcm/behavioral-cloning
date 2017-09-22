import csv
import cv2
import numpy as np

lines = []
with open('D:/selfdrive/2clockwise-1antismoothrec-rwbbbrbc/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        lines.append(line)
        
images = []
measurements = []
tick = 0

for line in lines:
	for i in range(3):
		if tick ==0:
                    print("Ind : " +str(i))
                    
		if i==0:
			correction=0
		elif i==1:
			correction=0.04
		elif i==2:
			correction=+0.04
		source_path = line[i]
		#print(source_path)
		filename=source_path.split('\\')[-1]
		current_path = '..\\..\\2clockwise-1antismoothrec-rwbbbrbc\\IMG\\' + filename
		image=cv2.imread(current_path)
		images.append(image)
		measurement = float(line[3])+correction
		#flip and append
		measurements.append(measurement)
		image_flip=np.fliplr(image)
		images.append(image_flip)
		measurements.append(-measurement)
	tick=tick+1
	
   
X_train = np.array(images)
y_train = np.array(measurements)

from keras.models import Sequential, Model
from keras.layers import Flatten, Dense, Lambda, Cropping2D #Lambda Wraps arbitrary expression as a Layer object. 
from keras.layers.convolutional import Convolution2D
from keras.layers import MaxPooling2D

model = Sequential()
model.add(Lambda(lambda x:x/255.0 - 0.5, input_shape=(160,320,3))) #((normalise & mean center))
model.add(Cropping2D(cropping=((58,20),(0,0)))) #crop distracting details increas to 20 to focus further out
model.add(Convolution2D(24,5,5,subsample=(2,2),activation="relu")) #Convolution2D(nb_filter, nb_row, nb_col, init='glorot_uniform', activation=None, weights=None, border_mode='valid', subsample=(1, 1), dim_ordering='default', W_regularizer=None, b_regularizer=None, activity_regularizer=None, W_constraint=None, b_constraint=None, bias=True)
model.add(Convolution2D(36,5,5,subsample=(2,2),activation="relu"))
model.add(Convolution2D(48,5,5,subsample=(2,2),activation="relu"))
model.add(Convolution2D(64,3,3,activation="relu"))
model.add(Convolution2D(64,3,3,activation="relu"))
model.add(Flatten())
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
model.fit(X_train, y_train, validation_split=0.2,shuffle=True, nb_epoch=5)

model.save('modelvpt04bbbrbc.h5')
print("fin")
