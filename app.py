import streamlit as st
import keras
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import pandas as pd
import librosa
import librosa.display
import matplotlib.pyplot as plt

def main():
  @st.cache(allow_output_mutation=True)
  def load_model():
    model=tf.keras.models.load_model('Models/vgg_19_classifier16.h5')
    return model
  with st.spinner('Model is being loaded..'):
    model=load_model()

  st.write("""
          # Speech Emotion Recognition
          """
          )

  file = st.file_uploader("Please upload an audio file", type=["wav"])


  st.set_option('deprecation.showfileUploaderEncoding', False)
  def save_spectrogram1(audio_fname):
      y, sr = librosa.load(audio_fname, sr=None)
      S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
      log_S = librosa.power_to_db(S, ref=np.max)
      librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')
      fig1 = plt.gcf()
      plt.axis('off')
      # plt.show()
      plt.draw()
      plt.close(fig1)
      image_fname="img"
      fig1.savefig(image_fname, dpi=200)
      return image_fname + ".png"
      
  def  img_pred(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.true_divide(x, 255)
    x = np.expand_dims(x,axis=0)
    preds = model.predict(x)
    ans=np.argmax(preds)
    return ans

  def mod_1(audio_fname,model):
      img_path = save_spectrogram1(audio_fname)
      ans = img_pred(img_path, model)
      return ans

  def model_predict(audio_fname):
    d = ["angry", "calm", "disgusting", "fearful", 'happy', 'neutral', 'sad', 'surprised']
    ans=mod_1(audio_fname,model)
    return d[ans]

  if file is None:
      st.text("Please upload an audio file")
  else:
      predictions = model_predict(file)
      st.success(f"It seems like you're quite {predictions} today")

if __name__ == '__main__':
    main()
