# Title:

**“COVID19 Prediction Using Convolutional Neural Network”**


# Introduction:

Right now we are going through a very tough time, this **COVID19** pandemic has hit almost all the industry and damaged the health industry severely and the most alarming situation is that we have not yet been able to invent any medications that can prevent or cure this disease even after 6 months, more than 250 countries are its victims already with **9,210,543** total cases, **474,818** total deaths, **3,778,373** active cases out of which **57,909** are in critical condition.

As of till now to test if a patient is covid +ve or not he or she has to do blood/saliva test. We all know these testing procedures can take hours for each patient. With this deep learning approach this can be reduced to minutes and its accuracy also is quite high.


# Methodology:



1. Dataset Acquisition:

    For the training and testing purpose we collected our data from two different sources. One we collected from a github repo, consisting 142 covid19 positive x-ray images and the other one we collected from kaggle for normal x-ray images, we picked 142 such images from this kaggle dataset also to keep the dataset balanced.

2. Splitting the data:

    After we acquired our data we split the whole data into two sets one for training and another for testing purposes. 


    So, these two sets consist of  71 Covid +ve and 71 Covid -ve images each.

3. Designing the CNN model architecture:

    To solve this problem using a deep learning approach, we considered Convolutional Neural Network.


    Which consists of 5 convolutional layers, 3 max pooling layers to reduce the dimensionality, 4 dropout layers to prevent the network to be biased on any particular perceptron.

4. Training our data with the designed model:

    Before feeding data into our model we normalized all pixel values in 0 to 1 range. With the batch size 32 we feed our data to the model in 7 steps per epoch. Which took a total of 10 epochs to train the model.



# Result Discussion:

	After the training finished the result that we got:


<table>
  <tr>
   <td>Loss
   </td>
   <td>0.1138
   </td>
  </tr>
  <tr>
   <td>Accuracy
   </td>
   <td>0.9598
   </td>
  </tr>
  <tr>
   <td>Validation Loss
   </td>
   <td>0.0694
   </td>
  </tr>
  <tr>
   <td>Validation Accuracy
   </td>
   <td>0.9667
   </td>
  </tr>
</table>




![alt_text](https://i.ibb.co/fMV7G5h/fig1.png)


Fig-1: Ground Truth vs Prediction Result

As we can see from the above diagram our model only predicted two incorrect predictions, which are two covid -ve as covid +ve which is less severe, in false positive perspective as we can not afford false negative states.



![alt_text](https://i.ibb.co/JnSTf6t/fig2.png)


Fig-2: Confusion Matrix

We can also observe the same result from the figure 02 confusion matrix, we don’t have any false negatives. We have 30 true negatives, 28 true positives and 2 false positives which is affordable in a medical sense.

