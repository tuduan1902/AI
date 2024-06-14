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

def on_checkbox_click():
   global list_benh
   global df
   global checkboxs
   global new_data_x_R
   global new_data_x
   global loaded_model
   global list_trieu_chung
   #auto: 
   new_data_x_r =[]
   new_data_x =[]
   print("len(list_trieu_chung): ",len(list_trieu_chung))
   for i in range(len(list_trieu_chung)):
      if checkboxs[i].var.get():  # Fix to get the variable value from the checkbox   
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

   # Get the disease name from the DataFrame
   disease_name = df["Căn bệnh"].iloc[predicted_labels[0]]

   # Send result to Flask
   try:
      response = requests.post('http://localhost:5000/diagnosis', json={'result': disease_name})
      print("Kết quả được gửi thành công. Phản hồi:", response.text)
   except Exception as e:
      print("Lỗi khi gửi kết quả:", e)

   # # Print and send the disease name to the Flask app
   # print(disease_name)
   # response = requests.post('http://localhost:5000/diagnosis', data={'result': disease_name})
   # print(response.text)  # In phản hồi từ Flask server


def import_data():
   global list_benh
   global df
   global new_data_x_R
   global new_data_x
   global loaded_model
   global list_trieu_chung
   # Specify the file path
   file_path = r'D:\Code\Doan\App\Ai\benh_trieuchung_dataset.xlsx'

   # Read the Excel file into a pandas DataFrame
   df = pd.read_excel(file_path)

   # Assuming you have loaded your new data as new_data_x
   new_data_x_R=[]
   new_data_x=[]
   loaded_model = tf.keras.models.load_model(r"D:\Code\Doan\App\Ai\trained_model.h5")
   list_benh = df["Căn bệnh"]
   counter = 0
   list_trieu_chung = []
   
   for column_name in df.columns:
      if counter < 2:
         counter = counter +1
      else:
         print(column_name)
         list_trieu_chung.append(column_name)

def create_tick():   
   global list_benh
   global df
   global checkboxs
   global new_data_x_R
   global new_data_x
   global loaded_model
   global list_trieu_chung
   #manual: 
   checkboxs = {}
   for i in range(len(list_trieu_chung)):
      var = tk.IntVar()  # Use IntVar to track the state of the checkbox
      checkbox = tk.Checkbutton(frame, text=list_trieu_chung[i], variable=var)
      checkbox.var = var  # Attach the variable to the checkbox
      checkbox.pack()
      checkboxs[i] = checkbox
   
   buttonstart = tk.Button(frame, text="Chuẩn đoán", command=on_checkbox_click)
   buttonstart.pack()
   print(new_data_x_R)


root = tk.Tk()
root.title("Chuẩn đoán bệnh sơ bộ")
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# Add a scrollbar
scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)
def on_configure(event):
   canvas.configure(scrollregion=canvas.bbox('all'))
# Bind the canvas to the scrollbar
canvas.bind('<Configure>', on_configure)

# Create a frame to contain the scrollable content
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')
import_data()
create_tick()
root.mainloop()

