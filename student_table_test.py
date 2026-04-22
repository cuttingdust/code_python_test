# TODO 1.导包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 解决个别版本show()无法展示图的问题
import matplotlib

matplotlib.use('TkAgg')

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']

# TODO 2.numpy负责生成数据
# 此处用numpy随机生成1-100的多个数字,组成5行3列的数组
array = np.random.randint(low=1, high=100, size=(5, 3))
print(array)

# TODO 3.使用pandas处理数据
df = pd.DataFrame(array, index=['张三', '李四', '王五', '赵六', '田七'], columns=['语文', '英语', '数学'])
print(df)

print("=" * 50)

# 需求1: 获取各个学科的总成绩
# 方式1:一个个获取
print('语文', df['语文'].sum())
print('数学', df['数学'].sum())
print('英语', df['英语'].sum())
# 方式2: df整体获取
print("-" * 25)
print(df.sum(axis=0))  # axis=0:按照列相加
print("-" * 25)
# 需求2: 获取各个同学的总成绩
print(df.sum(axis=1))  # # axis=0:按照行相加
print("-" * 25)

# TODO 4.matplotlib可视化数据
fig, ax = plt.subplots()
# 绘制散点图  注意: 下面数据是随便传的,未来根据具体需求决定x,y内容
ax.scatter(x=df['语文'], y=df['数学'])
# ax.set_xlabel('x')
ax.set_title('班级偏科情况')
plt.show()
