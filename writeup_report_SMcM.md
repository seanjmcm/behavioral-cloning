#**Behavioral Cloning** 

##Writeup Template

###You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.

---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./examples/placeholder.png "Model Visualization"
[image2]: ./examples/center.jpg "center lane driving"
[image3]: ./examples/rec1.jpg "Recovery Image"
[image4]: ./examples/rec2.jpg "Recovery Image"
[image5]: ./examples/rec3.jpg "Recovery Image"
[image6]: ./examples/normal.jpg "Normal Image"
[image7]: ./examples/flipped.jpg "Flipped Image"

## Rubric Points
###Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
###Files Submitted & Code Quality

####1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* writeup_report.md summarizing the results

####2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py modelvpt04bbbrbc.h5
```

####3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

###Model Architecture and Training Strategy

####1. An appropriate model architecture has been employed

My model is based on the NVidia model architecture.  It first consists of a convolution neural network with 5x5 convolutions and filter of 24, 36, 48, 64 & 64 using a RELU (rectified linear unit) activation.  The data is then flattened and passed to four fully connected layers of sizes 100, 50, 10 & 1. 

The data is normalized in the model using a Keras lambda layer (code line 50) and then cropped.  The top 58 pixels are removed and the bottom 20 are also removed.  The bottom crop was increased slightly to focus on future position rather than current position in addition to the cropping od the wheel.

####2. Attempts to reduce overfitting in the model

In order to reduce overfitting, the track was driven anticlockwise and various recovery samples were added.

The model was trained and then validated on 20% of the data.  To ensure that the model was not overfitting (code line 64), the data was shuffled before running each epoch. The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

####3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually (model.py line 64).

####4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I used a combination of center lane driving, recovering from the left and right sides of the road, an anti clockwise lap, smooth driving around corner and recovery additions specific to the bridge, chicane and red/white left strip beside water.

For details about how I created the training data, see the next section. 

###Model Architecture and Training Strategy

####1. Solution Design Approach

The overall strategy for deriving a model architecture was to first gather sufficient and appropriate training data on which to run the model. 

My first step was to use a convolution neural network model similar to the the LeNet model.  This actually worked and I drove the vehicle successfully around the course, however the vehicle was hugging the corners and I tried to improve the model by adding data.  After approximately 10 hours of further testing, my extra features served only to make the model worse and I could not return it to its 'good' state.  

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set. I found that my first model had a low mean squared error on the training set but a high mean squared error on the validation set. This implied that the model was overfitting.  In retrospect, the keras documentation revealed that the validation data unlike the training data was not shuffled.  A shuffle before the  validation spilt should assist and improve the validation loss score with respect to the training score as it contained important feature infomration. 

Unable to recreate the early success, I moved to the NVidia architectecture described in section 1.

The final step was to run the simulator to see how well the car was driving around track one. There were a few spots where the vehicle fell off the track, the first bend, bridge, chicane and sharp right corner with water background were particularly tricky.  To improve the driving behavior in these cases, I trained recovery scenarios and drove a number of times on those particular sections.

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

####2. Final Model Architecture

The final model architecture (model.py lines 18-24) consisted of a convolution neural network as follows

| Layer         		|     Description	        					| 
|:---------------------:|:---------------------------------------------:| 
| Crop         		    | Image 160x320x3 --> 102x320x3 RGB image       | 
| 2DConvolution     	| 5x5 Convolution with 24 Filters           	|
| 2DConvolution 		| 5x5 Convolution with 36 Filters 				|
| 2DConvolution     	| 5x5 Convolution with 48 Filters           	|
| 2DConvolution 		| 5x5 Convolution with 64 Filters 				|
| 2DConvolution 		| 5x5 Convolution with 64 Filters 				|
| Flatten   	      	|                               			    |
| Dense		            |  ouput 400       					            |
| Fully connected		| ouput 100      					            |
| Fully connected		| ouput 50      					            |
| Fully connected		| ouput 10      					            |
 

####3. Creation of the Training Set & Training Process

To capture good driving behavior, I first recorded two laps on track one using center lane driving. Here is an example image of center lane driving:

![alt text][image2]

I then recorded the vehicle recovering from the left side and right sides of the road back to center so that the vehicle would learn to .... These images show what a recovery looks like starting from the right side of teh road and moving back tot he center:

![alt text][image3]
![alt text][image4]
![alt text][image5]

Then I repeated this process on track two in order to get more data points.

To augment the data sat, I also flipped images and angles thinking that this would ... For example, here is an image that has then been flipped:

![alt text][image6]
![alt text][image7]

Etc ....

After the collection process, I had X number of data points. I then preprocessed this data by ...


I finally randomly shuffled the data set and put Y% of the data into a validation set. 

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. The ideal number of epochs was Z as evidenced by ... I used an adam optimizer so that manually training the learning rate wasn't necessary.
