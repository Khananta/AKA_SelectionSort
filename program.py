import streamlit as st
import random
import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(2000)
from prettytable import PrettyTable

# Selection Sort Iteratif
def selection_sort_iterative(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Selection Sort Rekursif
def selection_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr
    min_idx = 0
    for i in range(1, n):
        if arr[i] < arr[min_idx]:
            min_idx = i
    arr[min_idx], arr[n - 1] = arr[n - 1], arr[min_idx]
    return selection_sort_recursive(arr, n - 1)

# Ukur waktu eksekusi algoritma
def measure_execution_time(func, arr):
    start_time = time.time()
    func(arr)
    return time.time() - start_time

# Fungsi untuk mencetak tabel waktu eksekusi
def print_execution_table(n_values, recursive_times, iterative_times):
    table = PrettyTable()
    table.field_names = ["n", "Recursive Time (s)", "Iterative Time (s)"]
    min_len = min(len(n_values), len(recursive_times), len(iterative_times))
    for i in range(min_len):
        table.add_row([n_values[i], recursive_times[i], iterative_times[i]])
    st.text(str(table))

# Fungsi untuk memperbarui grafik
def update_graph(n_values, recursive_times, iterative_times):
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, recursive_times, label='Recursive', marker='o', linestyle='-', color='blue')
    plt.plot(n_values, iterative_times, label='Iterative', marker='o', linestyle='-', color='orange')
    plt.title('Performance of Recursive vs Iterative Selection Sort')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

# Tampilan utama Streamlit
st.title("Analisis Kompleksitas Algoritma Selection Sort")
st.write("Kelompok Mihu Mihu - S1IF-12-01 - 103112400259 | 103112430001 | 103112430017")

# Input ukuran dataset kecil dan besar
dataset_size_small = st.slider("Ukuran Dataset Kecil (0-500)", 0, 500, 100)
dataset_size_large = st.slider("Ukuran Dataset Besar (0-1000)", 0, 1000, 100)

# List untuk menyimpan nilai dan waktu eksekusi
n_values = []
recursive_times = []
iterative_times = []

# Tombol untuk memulai analisis
if st.button("Mulai Analisis"):
    # Dataset kecil dan besar
    small_dataset = [random.randint(1, 100) for _ in range(dataset_size_small)]
    large_dataset = [random.randint(1, 1000) for _ in range(dataset_size_large)]

    # Ukur waktu eksekusi untuk algoritma rekursif dan iteratif
    small_recursive_time = measure_execution_time(selection_sort_recursive, small_dataset.copy())
    large_recursive_time = measure_execution_time(selection_sort_recursive, large_dataset.copy())

    small_iterative_time = measure_execution_time(selection_sort_iterative, small_dataset.copy())
    large_iterative_time = measure_execution_time(selection_sort_iterative, large_dataset.copy())

    # Menambahkan ukuran dataset dan waktu eksekusi ke list
    n_values.append(dataset_size_small)
    n_values.append(dataset_size_large)
    recursive_times.append(small_recursive_time)
    recursive_times.append(large_recursive_time)
    iterative_times.append(small_iterative_time)
    iterative_times.append(large_iterative_time)

    # Tampilkan waktu eksekusi
    st.write(f"Waktu eksekusi untuk dataset kecil (Rekursif): {small_recursive_time:.6f} detik")
    st.write(f"Waktu eksekusi untuk dataset besar (Rekursif): {large_recursive_time:.6f} detik")
    st.write(f"Waktu eksekusi untuk dataset kecil (Iteratif): {small_iterative_time:.6f} detik")
    st.write(f"Waktu eksekusi untuk dataset besar (Iteratif): {large_iterative_time:.6f} detik")

    # Cetak tabel waktu eksekusi
    print_execution_table(n_values, recursive_times, iterative_times)

    # Perbarui grafik perbandingan
    update_graph(n_values, recursive_times, iterative_times)
