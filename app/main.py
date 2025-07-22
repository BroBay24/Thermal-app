
import streamlit as st
import cv2
import numpy as np

# Fungsi segmentasi thermal (threshold sederhana)
def thermal_segmentation(frame, threshold=150):
    # Konversi ke grayscale (anggap ini adalah "panas")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Threshold
    _, mask = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    # Invers mask untuk background
    inv_mask = cv2.bitwise_not(mask)

    # Buat background gelap
    dark_bg = np.zeros_like(frame)

    # Pisahkan objek dan background
    body = cv2.bitwise_and(frame, frame, mask=mask)
    background = cv2.bitwise_and(dark_bg, dark_bg, mask=inv_mask)
    result = cv2.add(body, background)

    return result

# Title Streamlit
st.title("Thermal Camera Segmentation")
st.write("Deteksi Suhu Berdasarkan Simulasi Thermal")

# Slider Threshold
threshold = st.slider("Threshold Panas", 0, 255, 150)

# Tombol Start
start = st.button("Mulai Kamera")

if start:
    cap = cv2.VideoCapture(0)

    frame_window = st.image([])

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize untuk efisiensi
        frame = cv2.resize(frame, (640, 480))

        # Simulasi thermal segmentation
        segmented = thermal_segmentation(frame, threshold)

        # Konversi BGR ke RGB untuk streamlit
        segmented_rgb = cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB)
        frame_window.image(segmented_rgb)

        # Streamlit auto-refresh
        if not st.session_state.get("running", True):
            break

    cap.release()
