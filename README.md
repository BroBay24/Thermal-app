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

## Hasil Screenshot dengan Threeshold 114

<img width="1693" height="913" alt="Thernal" src="https://github.com/user-attachments/assets/6c7e8a80-2d69-44d0-a26d-a7a407099263" />

## Hasil Screenshot dengan Threeshold 150 

<img width="1694" height="905" alt="image" src="https://github.com/user-attachments/assets/d09901c2-f2e5-4539-9f5f-246f1f64d52e" />


