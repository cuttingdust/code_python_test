# 1.导包
import pandas as pd

# 2.创建pandas对象
# 此处咱们用最简单的方式创建: 把列表转换为pandas对象
# 2.1 创建Series对象(类似一列)
list = [10, 20, 30, 40]
print(list, type(list))
s = pd.Series(list)
print(s, type(s))  # Series只能组成一列

print("=" * 50)
# 2.2 创建DataFrame对象(类似表格)
list2 = [10, 20, 30, 40]
print(list2, type(list2))
df = pd.DataFrame(list2, columns=['col1'])
print(df, type(df))

print("=" * 50)
list3 = [[10, 11], [20, 21], [30, 31], [40, 41]]
print(list3, type(list3))
df2 = pd.DataFrame(list3, columns=['nums1', 'nums2'])
print(df2, type(df2))  # 类似表格中有4行2列

print("=" * 50)
# 3.pandas相比numpy多了行列索引和标签
# 需求: 获取df2的第2列
print(df2.nums2)
print(df2['nums2'])

# 需求: 获取df2的低2列的总和,平均,最大值,最小值
print(df2['nums2'].sum())
print(df2['nums2'].mean())
print(df2['nums2'].median())
print(df2['nums2'].min())
print(df2['nums2'].max())
