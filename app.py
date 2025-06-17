import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
model = pickle.load(open('Model_stunting.sav', 'rb'))

# Judul aplikasi
st.title("Prediksi Stunting pada Balita")
st.markdown("Masukkan data berikut untuk mengetahui prediksi status gizi:")

# Form input data pengguna
umur = st.number_input("Umur (bulan)", min_value=0, max_value=60, value=24)
jenis_kelamin = st.selectbox("Jenis Kelamin", ['Laki-laki', 'Perempuan'])
berat_badan = st.number_input("Berat Badan (kg)", min_value=2.0, max_value=30.0, step=0.1, value=10.0)
tinggi_badan = st.number_input("Tinggi Badan (cm)", min_value=30.0, max_value=120.0, step=0.1, value=80.0)

# Proses input
if st.button("Prediksi"):
    predict = model.predict(
        [[umur, berat_badan, tinggi_badan]]
    )
    st.write('predik: ', predict)
 
        

  
