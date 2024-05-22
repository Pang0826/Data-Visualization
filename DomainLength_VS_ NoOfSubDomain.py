import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./data/PhiUSIIL_Phishing_URL_Dataset.csv')

# 選取標籤為 0 的所有資料
label_0 = data[data['label'] == 0]
# 選取標籤為 1 的所有資料
label_1 = data[data['label'] == 1]

# 抓資料
DomainLength_0 = label_0['DomainLength']
NoOfSubDomain_0 = label_0['NoOfSubDomain']

DomainLength_1 = label_1['DomainLength']
NoOfSubDomain_1 = label_1['NoOfSubDomain']

plt.figure(figsize=(12, 10))
plt.bar(DomainLength_0, NoOfSubDomain_0, label='label_0', color='blue', alpha=0.8)
plt.bar(DomainLength_1, NoOfSubDomain_1, label='label_1', color='orange',align='edge', alpha=0.5)

# 設置標籤和標題
plt.xlabel('DomainLength')
plt.ylabel('NoOfSubDomain')
plt.title('DomainLength vs NoOfSubDomain')

# 設置X軸刻度以10為間隔
plt.xticks(range(0, int(max(max(DomainLength_0), max(DomainLength_1))) + 1, 10))
# 添加圖例
plt.legend()
# 添加網格
plt.grid(True)
# 顯示圖
plt.show()