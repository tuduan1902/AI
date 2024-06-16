import numpy as np
import os

# Set the environment variable
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
import random
import pandas as pd
import tkinter as tk

from tkinter import messagebox
import requests 

from gtts import gTTS
import playsound 
import speech_recognition as sr
import time

# global variable:
current_folder = os.getcwd()
language = "vi"
idle_flag = True
idle_counter = 0

def speak(input_text):
    sound_file_string = r'sound_to_speak.mp3'
    soundfile = os.path.join(current_folder, sound_file_string)
    print(soundfile)
    # Create a gTTS object
    tts = gTTS(text=input_text, lang=language)
    # Save the audio file
    tts.save(soundfile)
    
    try:
        playsound.playsound(soundfile,True)
        
    except:
        playsound.playsound(soundfile,True)
    os.remove(soundfile)
    time.sleep(0.5)
    
    print("function speak() run done")


def get_voice():
    global idle_flag
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Me: ", end = '')
        audio = r.listen(source, phrase_time_limit=45)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            idle_flag = True
            return text
        except:
            print("...")
            return 0


def get_text():
    global idle_flag
    for i in range(2):
        text = get_voice()
        print(idle_flag)
        if text:
            print(idle_flag)
            if idle_flag == True:
                idle_flag = False
                return text.lower()
        elif i == 1:
            if idle_flag == False:
                speak("cảm ơn quý khách, bot sẽ quay lại chế độ chờ!")
                idle_flag == True
                blank_return = ""
                print(idle_flag)
                return blank_return

def predict(): 
    global list_benh
    global df
    global checkboxs
    global new_data_x_R
    global new_data_x
    global sfv
    global loaded_model
    global list_trieu_chung
    global new_list_trieu_chung
    #auto: 
    new_data_x_r =[]
    new_data_x =[]
    sfv = get_text()
    for i in range(len(list_trieu_chung)):
        list_trieu_chung[i] = list_trieu_chung[i].lower()
    print("len(list_trieu_chung): ",len(list_trieu_chung))
    for i in range(len(list_trieu_chung)):
        if list_trieu_chung[i] in sfv:  # Fix to get the variable value from the checkbox   
            new_data_x_r.append(1)
        else:
            new_data_x_r.append(0)
    new_data_x = np.array(new_data_x_r).reshape(1, -1)  # Reshape to match the expected input shape of the model
    print(new_data_x)
    # Load the saved model

    # Make predictions on new data
    predictions = loaded_model.predict(new_data_x)

    # If you want to get the predicted class labels
    predicted_labels = np.argmax(predictions, axis=1)

    # The variable 'predicted_labels' now contains the predicted class labels for the new data
    list_ten_benh = df["Căn bệnh"]
    print(predicted_labels)
    print(list_ten_benh[predicted_labels])

    predicted_labels_str = ','.join(map(str, list_ten_benh[predicted_labels]))
    print(predicted_labels_str)
    return predicted_labels_str


def import_data():
   global list_benh
   global df
   global new_data_x_R
   global new_data_x
   global loaded_model
   global list_trieu_chung
   # Specify the file path
   file_path = r'D:\Do_an\App\Ai\benh_trieuchung_dataset.xlsx'

   # Read the Excel file into a pandas DataFrame
   df = pd.read_excel(file_path)

   # Assuming you have loaded your new data as new_data_x
   new_data_x_R=[]
   new_data_x=[]
   loaded_model = tf.keras.models.load_model(r"D:\Do_an\App\Ai\trained_model.h5")
   list_benh = df["Căn bệnh"]
   counter = 0
   list_trieu_chung = []
   
   for column_name in df.columns:
      if counter < 2:
         counter = counter +1
      else:
         print(column_name)
         list_trieu_chung.append(column_name)

def main():
   global idle_flag
   import_data()
   while idle_flag:
      get_text()
   if idle_flag == False:  
      print("Current folder: ", current_folder)
      speak("xin chào quý khách, tôi là robot chuẩn đoán sơ bộ. xin hỏi quý khách cần hỗ trợ gì ạ?")
      while idle_flag == False:
         text_result = predict()
         time.sleep(0.2)
         print(text_result)
         #speak(text_result)
         if text_result != "":
            speak(text_result)


main()