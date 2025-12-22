import streamlit as st
import random
import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def measure_execution_time(arr):
    start_time = time.time()
    selection_sort(arr)
    return time.time() - start_time

def print_execution_table(n_values, recursive_times, iterative_times):
    table = PrettyTable()
    table.field_names = ["n", "Recursive Time (s)", "Iterative Time (s)"]
    min_len = min(len(n_values), len(recursive_times), len(iterative_times))
    for i in range(min_len):
        table.add_row([n_values[i], recursive_times[i], iterative_times[i]])
    st.text(str(table))

def update_graph(n_values, recursive_times, iterative_times):
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, recursive_times, label='Recursive', marker='o', linestyle='-', color='blue')
    plt.plot(n_values, iterative_times, label='Iterative', marker='o', linestyle='-', color='orange')
    plt.title('Performance Comparison: Recursive vs Iterative')
    plt.xlabel('Input (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

st.title("Analisis Kompleksitas Algoritma Selection Sort")
st.write("Kelompok Mihu Mihu - S1IF-12-01 - 103112400259 | 103112430001 | 103112430017")

dataset_size_small = st.slider("Ukuran Dataset Kecil (0-500)", 0, 500, 100)
dataset_size_large = st.slider("Ukuran Dataset Besar (0-5000)", 0, 5000, 1000)

n_values = []
recursive_times = []
iterative_times = []

if st.button("Mulai Analisis"):
    small_dataset = [random.randint(1, 100) for _ in range(dataset_size_small)]
    large_dataset = [random.randint(1, 1000) for _ in range(dataset_size_large)]

    small_time = measure_execution_time(small_dataset)
    large_time = measure_execution_time(large_dataset)

    n_values.append(dataset_size_small)
    n_values.append(dataset_size_large)
    recursive_times.append(small_time)
    recursive_times.append(large_time)
    iterative_times.append(small_time) 
    iterative_times.append(large_time) 

    st.write(f"Waktu eksekusi untuk dataset kecil: {small_time:.6f} detik")
    st.write(f"Waktu eksekusi untuk dataset besar: {large_time:.6f} detik")

    print_execution_table(n_values, recursive_times, iterative_times)

    update_graph(n_values, recursive_times, iterative_times)