# 1.导包
import random
import matplotlib.pyplot as plt

# # 解决个别版本show()无法展示图的问题
# import matplotlib
#
# matplotlib.use('TkAgg') # 这个可以显示在pycharm外面

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']

# 需求: 绘制每个月销量曲线图
# 2.准备测试数据
a = [i for i in range(10)]
print(a)
nums = [random.randint(1, 10) for i in range(10)]
print(nums)

# 3.绘图
# plt.plot()画图默认折线图
plt.plot(a, nums)

# 添加标题
plt.title('matplotlib入门案例')

# 添加坐标轴
plt.xlabel('月份')
plt.ylabel('销量')

# 添加网格
plt.grid(True)

# 展示图
plt.show()
