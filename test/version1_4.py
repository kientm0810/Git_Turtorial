import numpy as np

x = np.array([[0., 3., 4.],
              [1., 6., 4.]])

# Tính giá trị trung bình theo hàng (axis=1)
x_mean = np.mean(x, axis=1, keepdims=True)

# Tính độ lệch chuẩn theo hàng (axis=1)
x_std = np.std(x, axis=1, keepdims=True)

# Chuẩn hóa dữ liệu bằng Z-score
x_normalized = (x - x_mean) / x_std

print("Mean:")
print(x_mean)

print("Normalized X:")
print(x_normalized)
