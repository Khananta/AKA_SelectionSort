import streamlit as st
import random
import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(2000)
from prettytable import PrettyTable

def selection_sort_iterative(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

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

def measure_execution_time(func, arr):
    start_time = time.time()
    func(arr)
    return time.time() - start_time

def print_execution_table(n_values, recursive_times, iterative_times):
    table = PrettyTable()
    table.field_names = ["n", "Recursive Time (s)", "Iterative Time (s)"]
    for i in range(len(n_values)):
        table.add_row([n_values[i], recursive_times[i], iterative_times[i]])
    st.text(str(table))

def update_graph(n_values, recursive_times, iterative_times):
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, recursive_times, label='Recursive', marker='o')
    plt.plot(n_values, iterative_times, label='Iterative', marker='o')
    plt.title('Performance of Recursive vs Iterative Selection Sort')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

st.title("Analisis Kompleksitas Algoritma Selection Sort")
st.write("Kelompok Mihu Mihu - S1IF-12-01 - 103112400259 | 103112430001 | 103112430017")

input_sizes = st.text_input("Masukkan ukuran dataset (pisahkan dengan koma). Contoh: 10, 50, 120, 300")

n_values = []
recursive_times = []
iterative_times = []

if st.button("Mulai Analisis"):
    try:
        sizes = [int(x.strip()) for x in input_sizes.split(",") if x.strip().isdigit()]
        
        for n in sizes:
            data = [random.randint(1, 1000) for _ in range(n)]
            recursive_times.append(measure_execution_time(selection_sort_recursive, data.copy()))
            iterative_times.append(measure_execution_time(selection_sort_iterative, data.copy()))
            n_values.append(n)

        print_execution_table(n_values, recursive_times, iterative_times)
        update_graph(n_values, recursive_times, iterative_times)

    except:
        st.error("Input tidak valid. Masukkan angka dipisahkan koma.")
