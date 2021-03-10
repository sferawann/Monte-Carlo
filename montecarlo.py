import csv
import streamlit as st
import pandas as pd
import numpy as np
import random
import math
import os
from random import seed
from streamlit.script_runner import StopException, RerunException

st.title('Tugas Pemrograman Simulasi Monte Carlo')
st.subheader('Syahrul Fathurrahman Erawan')
st.subheader('152017030')
st.sidebar.subheader('Hasil Perhitungan')

df = np.array([[0, 20], [1, 40], [2, 20], [3, 10], [4, 10]])
st.write(pd.DataFrame(df, columns=["Minggu - Ke", "Frekuensi"]))

mke = df[:0]
frekuensi = df[:, 1]

sf = 0
for i in range(len(frekuensi)):
    sf = sf + frekuensi[i]
st.sidebar.write('Nilai Sigma Frekuensi adalah ', sf)

kosong = []
sump = 0
for a in range(len(frekuensi)):
    sump = frekuensi[a]/sf
    st.sidebar.write("Prob mke-", a, "=", sump)
    kosong.append(sump)

probabilitas = np.array([kosong])
df = np.concatenate((df, probabilitas.T), axis=1)
st.write('Tabel Menambahkan Column Probabilitas')
st.write(pd.DataFrame(df, columns=[
         "Minggu Ke", "Frekuensi", "Probabilitas"]))

kosong2 = []
sumpk = 0
for a in range(len(frekuensi)):
    sumpk = sumpk + kosong[a]
    st.sidebar.write("ProK mke-", a, "=", sumpk)
    kosong2.append(sumpk)

probabilitas_komulatif = np.array([kosong2])
df = np.concatenate((df, probabilitas_komulatif.T), axis=1)
st.write('Tabel Menambahkan Column Probabilitas Komulatif')
st.write(pd.DataFrame(df, columns=["Minggu Ke", "Frekuensi",
                                   "Probabilitas", "Probabilitas Kumulatif"]))

interval_min = []
min_v = 0
for a in range(len(frekuensi)):
    if(a == 0):
        interval_min.append(min_v)
        st.sidebar.write("Interval Mke-", a, " = ",
                         min_v, "-", kosong2[a])
    else:
        min_v = kosong2[a-1]+0.001
        interval_min.append(min_v)
        st.sidebar.write("Interval Mke-", a,
                         " = ", min_v, "-", kosong2[a])

interval_mind = np.array([interval_min])
df = np.concatenate((df, interval_mind.T), axis=1)
interval_maxd = np.array([kosong2])
df = np.concatenate((df, interval_maxd.T), axis=1)
st.write('Tabel Menambahkan Column Interval')
st.write(pd.DataFrame(df, columns=["Minggu Ke", "Frekuensi", "Probabilitas",
                                   "Probabilitas Kumulatif", "Interval Batas Bawah", "Interval Batas Atas"]))

minggu_baru = 101
p_minggu = []
angka_acak = []
permintaan = []
for a in range(16):
    p_minggu.append(minggu_baru)
    acak = random.random()
    angka_acak.append(acak)
    if(acak < 0.2):
        jenis = 0
        permintaan.append(jenis)
    elif(acak < 0.6):
        jenis = 1
        permintaan.append(jenis)
    elif(acak < 0.8):
        jenis = 2
        permintaan.append(jenis)
    elif(acak < 0.9):
        jenis = 3
        permintaan.append(jenis)
    elif(acak <= 1):
        jenis = 4
        permintaan.append(jenis)
    minggu_baru += 1

st.write("Minggu Ke-", "|", "Angka Acak", "|", "Permintaan")
for a in range(16):
    st.write(p_minggu[a], "|", angka_acak[a], "|", permintaan[a])
sumpermintaan = float(sum(permintaan))
st.sidebar.write('Jumlah Permintaan adalam ',sumpermintaan)
