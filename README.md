# Speech Emotion Recognition System

**Sagar Rokad**, **Asim Siddiqui**, **Suraj Kumar Mishra**

## Project Overview

Through all the available senses humans can actually sense the emotional state of their communication partner. The emotional detection is natural for humans but it is very difficult task for computers; although they can easily understand content based information, accessing the depth behind content is difficult and that’s what speech emotion recognition (SER) sets out to do. It is a system through which various audio speech files are classified into different emotions such as happy, sad, anger and neutral by computer. SER can be used in areas such as the medical field or customer call centers. With this project I hope to look into applying this model into an app that individuals with ASD can use when speaking to others to help guide conversation and create/maintain healthy relationships with others who have deficits in understanding others emotions. [Google Slides Presentation](https://docs.google.com/presentation/d/1rmjpo23vwmXkn4pJq69lN7iZSF3hDa68Pf5J6E46tJE/edit#slide=id.p1)

## Dataset
The Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS) Dataset from Kaggle contains 1440 audio files from 24 Actors vocalizing two lexically-matched statements. Emotions include angry, happy, sad, fearful, calm, neutral, disgust, and surprised. [Click for dataset](https://www.kaggle.com/uwrfkaggler/ravdess-emotional-speech-audio)


## Process

1)	See **1_base_model.ipynb**: Loaded audio files, created visualizations, conducted feature extraction (log-mel spectrograms) resulting into dataframe (see **audio.csv**) and built inital 1D CNN Model. Obtained an accuracy score of 52.43% with the model having difficulty classifying calm, surprised, angry, and digust.

- **EDA**


<p align="center">
  <img width="460" height="300" src="https://github.com/mkosaka1/capstone_project/blob/master/Uploads/EDA_Photos/Waveplot_FemaleCalm.png">
</p>


<p align="center">
  <img width="460" height="300" src="https://github.com/mkosaka1/capstone_project/blob/master/Uploads/EDA_Photos/MelSpec_FemaleCalm.png">
</p>

2) See **2_data_augmentation.ipynb**: Implemented data augmentation methods including adding noise, speed and pitch, and stretch to all audio files and used feature extraction methods to turn audio files into images to feed into 1D CNN Model. Obtained an accuracy score of 51.74%, but overfitting the data as seen in graph.

3) See **3_Audio_to_spectogram_images.ipynb**: Converted audio files into spectogram images and storing it in drive.

4) See **4_Transfer_Learning_on_Spectogram_images.ipynb**: Implemented transfer learning algorithms on spectogram images of audio files and implemented VGG16 and VGG19 Model and performed Data augmentation on spectogram images and implemented VGG19 fine tuning and got best accuracy of 82% in VGG19 (fine tuning + augmentation)

5) See **5_Transfer_learning_on_data_augmentation.ipynb**:	Implemented Data augmentation like noise, stretch on different audio files and implented transfer learning models like VGG19 and Inception.

## Challenges

• As this project is not a stand-alone data science project, it required little to medium domain knowledge. Understanding Mfccs, Mel scale is very important for feature selection.
 
• Limitations include not using feature selection to reduce the dimensionality of our augmented CNN which may have improved learning performance. 

• During deployment in Heroku and Azure, there were problems as some additional libraries needed to installed. After installing these libraries , some of previous  requirements had to be downgraded in order to be compatible with the installed ones, that’s why we deployed on GCP.


## Conclusion
•	 VGG19 (fine tuning + augmentation) was giving the best accuracy score of 82% and solved the problems like overfitting to some extent. 

•	 It's quite difficult to get the accuracy of more than 90% due to lack of data.

•	 To solve problems like over-fitting that we had seen in almost every model, we need more real time data. 

•	 Noise Adding ,Pitching and Shifting for the imbalanced data was helping in achieving a better result. 

•	 Computational cost was much high resulting in several runtime crashes but we’re able to get our best model for deployment.
