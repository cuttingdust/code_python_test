# 1.导包
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 2.读取数据
train = pd.read_csv('data/titanic_train.csv')
# print(train.head())
# print('=' * 50)
# print(train.describe())
# print('=' * 50)
test = pd.read_csv('data/titanic_test.csv')
# print(test.head())
#
# # 3.了解数据
print('=' * 100)  # (892, 12)
print(train.shape)
print('=' * 50)
train.info()  # 每列不为空的个数
print(train.count())
print('=' * 100)

# 4.缺失值查看
# 4.1 查看是否是缺失值,结果是True或者False
print(train.isna())
# 4.2 获取每列有缺失值的个数(True:1,Fasle:0)
print(train.isna().sum())
# 4.3 获取每列缺失值的比例
print(train.isna().sum() / len(train) * 100)
print('=' * 100)

# 5.了解生存和死亡的人数,以及可视化展示
# 查看Survived各个值的个数
result = train['Survived'].value_counts()
print(result, type(result))

# 可视化展示
result.plot(kind='bar')  # 柱状图
# plt.legend()
plt.grid(True)
plt.show()
