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

plt.show()