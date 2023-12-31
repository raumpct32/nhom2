import numpy as np

# Tạo một mảng NumPy chứa dữ liệu mẫu (giả định)
data = np.array([10, 12, 15, 18, 20, 22, 25, 28, 30, 35])

# Tính toán các thống kê cơ bản sử dụng NumPy
mean_value = np.mean(data)  # Trung bình
variance_value = np.var(data)  # Phương sai
std_deviation_value = np.std(data)  # Độ lệch chuẩn

# In kết quả
print("Dữ liệu mẫu:", data)
print("Trung bình:", mean_value)
print("Phương sai:", variance_value)
print("Độ lệch chuẩn:", std_deviation_value)