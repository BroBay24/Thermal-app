# 🔥 Thermal Camera Segmentation App

Aplikasi ini mensimulasikan segmentasi gambar thermal tubuh manusia menggunakan **kamera laptop** dan menampilkan hasilnya dengan **background gelap**.

## ✅ Fitur
- Input dari kamera laptop (simulasi thermal)
- Segmentasi area panas menggunakan threshold
- Tampilkan hasil secara real-time
- Dibuat dengan: `Streamlit` + `OpenCV`

---

## 🚀 Cara Menjalankan (Lokal)

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

## ⚠️ Catatan

- Aplikasi ini hanya berjalan **di lokal (PC/laptop)** karena Google Colab **tidak bisa mengakses webcam secara langsung**.
- Jika ingin segmentasi gambar thermal dari **gambar upload** (tanpa webcam), gunakan versi Colab yang sudah dimodifikasi.

---
