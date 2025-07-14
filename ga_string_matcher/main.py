import streamlit as st
from app.ga import run_genetic_algorithm

st.title("Genetic Algorithm: String Matching")

target = st.text_input("Target String", "HELLO WORLD").upper()
population_size = st.slider("Ukuran Populasi", 10, 500, 100)
mutation_rate = st.slider("Tingkat Mutasi", 0.0, 0.2, 0.01)
generations = st.slider("Jumlah Generasi Maks", 10, 2000, 1000)

if st.button("Jalankan"):
    output_area = st.empty()

    def callback(gen, best, fitness):
        output_area.markdown(f"**Generasi {gen}**: `{best}` (Fitness: {fitness})")

    best, gen = run_genetic_algorithm(target, population_size, mutation_rate, generations, callback)
    st.success(f"Target ditemukan pada generasi ke-{gen}: `{best}`")
