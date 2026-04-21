# 1.导包
import numpy as np

# 2.创建numpy数组
# 此处咱们用最简单的方式创建: 把列表转换为numpy数组
list = [[10, 20], [30, 40]]
print(list, type(list))
array = np.array(list)
print(array, type(array))
print("=" * 50)

# 3.数组的基础运算
# 下面的操作都是返回新的数组
print(array + 2)
print(array - 2)
print(array * 2)
print(array / 2)
print(array // 2)
print(array % 2)
print(array ** 2)

print(np.max(array))
print(np.min(array))
print(np.argmax(array))
print(np.sum(array))
print(np.mean(array))
