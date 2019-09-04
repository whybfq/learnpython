import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int)

# np.arange(-5.0, 5.0, 0.1)在−5.0到5.0的范围内，以0.1为单位，生成 NumPy数组([-5.0, -4.9, ���, 4.9])
X = np.arange(-5.0, 5.0, 0.1)
Y = step_function(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1)  # 指定图中绘制的y轴的范围
plt.show()
