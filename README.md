# Thermal Camera Segmentation App

Simulasi segmentasi gambar thermal tubuh manusia menggunakan **kamera laptop**

## Penjelasan
- Input dari kamera laptop (simulasi thermal)
- Segmentasi area panas menggunakan threshold
- hasil secara real-time
- Dibuat dengan: `Streamlit` + `OpenCV`

---

##  Cara Menjalankan (Lokal)

1. **Clone atau ekstrak zip**:
   ```bash
   unzip thermal_streamlit_app.zip
   cd thermal_streamlit_app
   ```

2. **Install dependensi**:
   ```bash
   pip install streamlit opencv-python
   ```

3. **Jalankan aplikasi**:
   ```bash
   streamlit run app.py
   ```

4. Buka browser dan akses:
   ```
   http://localhost:8501
   ```

---

## Catatan

- hanya bisa lokal (PC/laptop)** karena Google Colab **tidak bisa akses webcam**.
- bisa pakai collab tp harus mod

## Hasil Screenshot

![Alt Text](https://drive.google.com/file/d/1EhWIeGnycKu1Lky9COQPO2gMgjyOiGdw/view?usp=sharing)
