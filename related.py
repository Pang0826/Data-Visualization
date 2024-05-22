import pandas as pd

# 假設您的數據存儲在一個 DataFrame 中
data = pd.read_csv('./data/PhiUSIIL_Phishing_URL_Dataset.csv')

# 選擇指定的欄位
selected_columns = [
    'URLSimilarityIndex', 'CharContinuationRate', 'TLDLegitimateProb', 'URLCharProb', 'TLDLength',
    'NoOfSubDomain', 'HasObfuscation', 'NoOfObfuscatedChar', 'ObfuscationRatio', 'NoOfLettersInURL',
    'LetterRatioInURL', 'NoOfDegitsInURL', 'DegitRatioInURL', 'NoOfEqualsInURL', 'NoOfQMarkInURL',
    'NoOfAmpersandInURL', 'NoOfOtherSpecialCharsInURL', 'SpacialCharRatioInURL', 'IsHTTPS',
    'LineOfCode', 'LargestLineLength', 'HasTitle', 'Title', 'DomainTitleMatchScore', 'URLTitleMatchScore',
    'HasFavicon', 'Robots', 'IsResponsive', 'NoOfURLRedirect', 'NoOfSelfRedirect', 'HasDescription',
    'NoOfPopup', 'NoOfiFrame', 'HasExternalFormSubmit', 'HasSocialNet', 'HasSubmitButton', 'HasHiddenFields',
    'HasPasswordField', 'Bank', 'Pay', 'Crypto', 'HasCopyrightInfo', 'NoOfImage', 'NoOfCSS', 'NoOfJS',
    'NoOfSelfRef', 'NoOfEmptyRef', 'NoOfExternalRef'
]

# 選擇這些欄位
selected_data = data[selected_columns]

# 確保數值欄位不含有任何非數值的數據
selected_data = selected_data.apply(pd.to_numeric, errors='coerce')

# 刪除包含 NaN 值的行
selected_data = selected_data.dropna()

# 計算相關矩陣
correlation_matrix = selected_data.corr()

# 輸出相關矩陣為CSV文件
correlation_matrix.to_excel('correlation_matrix.xlsx')

print("相關矩陣已生成並保存為 'correlation_matrix.xlsx'")