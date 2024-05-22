import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 讀取資料
data = pd.read_csv('./data/PhiUSIIL_Phishing_URL_Dataset.csv')

# 選取標籤為 0 的所有資料
label_0 = data[data['label'] == 0]
# 選取標籤為 1 的所有資料
label_1 = data[data['label'] == 1]

# 提取 URLSimilarityIndex 和 URLTitleMatchScore 的資料
IsHTTPS_0 = label_0['IsHTTPS']
NoOfExternalRef_0 = label_0['NoOfExternalRef']

IsHTTPS_1 = label_1['IsHTTPS']
NoOfExternalRef_1 = label_1['NoOfExternalRef']

plt.figure(figsize=(12, 8))

# 散點圖
# plt.subplot(10, 8)
plt.scatter(IsHTTPS_0, NoOfExternalRef_0, color='blue', label='Label 0', s = 10)
plt.scatter(IsHTTPS_1, NoOfExternalRef_1, color='red', label='Label 1', s = 6)
plt.xlabel('IsHTTPS')
plt.ylabel('NoOfExternalRef')
plt.title('Scatter Plot')
plt.legend()
plt.grid(True)

# # 直方圖
# plt.subplot(2, 3, 2)
# plt.hist(similarity_index_0, color='blue', alpha=0.5, label='Label 0', bins=20)
# plt.hist(similarity_index_1, color='red', alpha=0.8, label='Label 1', bins=20)
# plt.xlabel('URL Similarity Index')
# plt.ylabel('Frequency')
# plt.title('Histogram')
# plt.legend()
# plt.grid(True)
# print(similarity_index_1)
# # 調整 y 軸刻度範圍
# plt.ylim(0, 40000)  # 設置 y 軸範圍從 0 到 100000

# # 箱形圖
# plt.subplot(2, 3, 3)
# plt.boxplot([similarity_index_0, similarity_index_1], labels=['Label 0', 'Label 1'])
# plt.xlabel('Label')
# plt.ylabel('URL Similarity Index')
# plt.title('Boxplot')
# plt.grid(True)

# # 熱圖
# plt.subplot(2, 3, 4)
# sns.heatmap(data[['URLSimilarityIndex', 'URLTitleMatchScore']].corr(), annot=True, cmap='coolwarm', fmt=".2f")
# plt.title('Correlation Heatmap')

# # 折線圖
# plt.subplot(2, 3, 5)
# plt.plot(similarity_index_0, color='blue', label='Label 0')
# plt.plot(similarity_index_1, color='red', label='Label 1')
# plt.xlabel('Index')
# plt.ylabel('URL Similarity Index')
# plt.title('Line Plot')
# plt.legend()
# plt.grid(True)

# # 密度圖
# plt.subplot(2, 3, 6)
# sns.kdeplot(similarity_index_0, fill=True, color='blue', label='Label 0')
# sns.kdeplot(similarity_index_1, fill=True, color='red', label='Label 1', warn_singular=False)
# plt.xlabel('URL Similarity Index')
# plt.ylabel('Density')
# plt.title('Density Plot')
# plt.legend()
# plt.grid(True)

# plt.tight_layout()
plt.show()