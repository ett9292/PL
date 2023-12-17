import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

dict_file = "dict.txt"  # 字典檔
stopwords = "stopwords.txt"  # 停用詞檔案
fontpath = "DFKangKaiStd-W5.otf"  # 字型檔

IThelps_file = "IThelp_tags.txt"  # 文檔
pngfile = "python.jpg"  # 底圖

# 下載 Punkt Tokenizer 模型
nltk.download('punkt')

# 讀取停用詞檔案
with open(stopwords, "r", encoding="utf-8") as stopfile:
    stop_words = stopfile.read().splitlines()

# 讀取文檔內容
with open(IThelps_file, "r", encoding="utf-8") as file:
    text = file.read()

# 使用 nltk 的 word_tokenize 函數將文檔分詞
tokens = word_tokenize(text)

# 過濾停用詞
filtered_tokens = [word.lower() for word in tokens if word.lower() not in stop_words]

# 使用 nltk 的 FreqDist 函數計算字詞頻率
freq_dist = FreqDist(filtered_tokens)

# 取得前 30 高頻字詞
top_words = freq_dist.most_common(30)

# 繪製頻率分佈圖
freq_dist.plot(20, cumulative=False)
plt.show()
