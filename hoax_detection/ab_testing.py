from scipy.stats import ttest_ind
akurasi_A = [0.89, 0.90, 0.88, 0.91, 0.89]
akurasi_B = [0.84, 0.85, 0.83, 0.86, 0.84]
t_stat, p_value = ttest_ind(akurasi_A, akurasi_B)

print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# Interpretasi hasil
if p_value < 0.05:
    print("Terdapat perbedaan signifikan antara kedua model")
else:
    print("Tidak terdapat perbedaan signifikan")