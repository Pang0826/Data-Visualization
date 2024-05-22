import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('./data/PhiUSIIL_Phishing_URL_Dataset.csv')

# 選取標籤為 0 的所有資料
label_0 = data[data['label'] == 0]
# 選取標籤為 1 的所有資料
label_1 = data[data['label'] == 1]

SpacialCharRatioInURL_0 = label_0['SpacialCharRatioInURL']
ObfuscationRatio_0 = label_0['ObfuscationRatio']

SpacialCharRatioInURL_1 = label_1['SpacialCharRatioInURL']
ObfuscationRatio_1 = label_1['ObfuscationRatio']

plt.figure(figsize=(10, 8))
sns.kdeplot(SpacialCharRatioInURL_0, cmap='Blues', fill=True, label='Label 0', alpha=0.5)
sns.kdeplot(SpacialCharRatioInURL_1, cmap='Oranges', fill=True, label='Label 1', alpha=0.5)

# 設置標籤標題
plt.xlabel('SpacialCharRatioInURL')
plt.ylabel('ObfuscationRatio')
plt.title('SpacialCharRatioInURL VS ObfuscationRatio')

# 圖例
plt.legend()

# 繪圖
plt.show()