import streamlit as st
import pandas as pd

st.title("Sistem Manajemen Persalinan :pregnant_woman:")

page = st.sidebar.selectbox("Menu", ["Pendaftaran Pasien","Rekap Pasien"])

csv = pd.read_csv("data.csv")

if page == "Pendaftaran Pasien":
    st.header("Pendaftaran Pasien")
    id = st.text_input("ID")
    nama_ibu = st.text_input("Nama Ibu")
    tgl_lahir_ibu = st.text_input("Tanggal Lahir Ibu")
    jenis_persalinan = st.selectbox("Jenis Persalinan", ["Normal", "Cesar"])
    tgl_lahir_bayi = st.text_input("Tanggal Lahir Bayi")
    jk_bayi = st.selectbox("Jenis Kelamin Bayi", ["L", "P"])
    bb_bayi = st.number_input("Berat Badan Bayi (kg)", step = 0.1)
    panjang_bayi = st.number_input("Panjang Bayi (cm)", step = 1)

    submit_btn = st.button("Tambah Pasien")
    if submit_btn:
        new_row = pd.DataFrame([[id, nama_ibu, tgl_lahir_ibu, jenis_persalinan, tgl_lahir_bayi, jk_bayi, bb_bayi, panjang_bayi]], columns = ["id","nama_ibu", "tgl_lahir_ibu", "jenis_persalinan", "tgl_lahir_bayi", "jk_bayi", "bb_bayi", "panjang_bayi"])

        csv = pd.concat([csv, new_row], ignore_index=True)

        csv.to_csv("data.csv",index=False)

        st.rerun()
else:
    st.header("Data Rekap Pasien")
    csv = pd.read_csv("data.csv")

    print(csv)
    edited_df =st.data_editor(csv)
    save_btn = st.button("Update Data")
    
    if save_btn:
        edited_df.to_csv("data.csv",index=False)
        st.rerun()
