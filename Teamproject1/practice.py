import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(50)
y = np.random.randn(50)

plt.scatter(x, y)
plt.title('산점도 예시')
plt.xlabel('X 값')
plt.ylabel('Y 값')
plt.show()