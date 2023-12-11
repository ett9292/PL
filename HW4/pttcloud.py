from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import jieba
import jieba.analyse
from collections import Counter # 次數統計

dict = "dict.txt"  # 字典檔
stopwords = "stopwords.txt"  # stopwords
fontpath = "DFKangKaiStd-W5.otf"  # 字型檔

IThelps_file = "ptt_title.txt"  # 文檔
pngfile = "base.jpg"  # 底圖

masks = np.array(Image.open(pngfile)) # 設置底圖

# 設置字典檔與stopwords
jieba.set_dictionary(dict) 
jieba.analyse.set_stop_words(stopwords)

text = open(IThelps_file,"r",encoding="utf-8").read()

tags = jieba.analyse.extract_tags(text, topK=100) #設置前100個關鍵詞

#用結巴進行斷詞
seg_list = jieba.lcut(text, cut_all=False) 
dictionary = Counter(seg_list)

freq = {}
for ele in dictionary:
    if ele in tags:
        freq[ele] = dictionary[ele]
print(freq) # 計算出現的次數

# 製作文字雲
wordcloud = WordCloud(background_color="white", mask=masks, contour_width=3, contour_color='steelblue', max_font_size=200, font_path= fontpath).generate_from_frequencies(freq)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()