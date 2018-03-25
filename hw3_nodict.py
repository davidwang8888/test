# Homework 3-2:Counters the characters
# 使用set & dict
#
# 建立字典mydict
mydict = {}

# Input data
sentence = input("Please input data: \n")
print('-'*16)

# 建立set
languages = set(sentence)           # set會自動將重複的字元刪除
print("顯示集合的內容：", languages)    # 印出來看看內容是否已經轉成set
print('-'*15)

for ch in languages:            # 將集合的字元取出,放入變數ch
    # print(ch)                 # 印出來看看ch的內容
    count1 = sentence.count(ch)  # 計數ch出現在sentence的次數
    mydict[ch] = count1         # 將字元與計數值存入字典

# 輸出dict
print("顯示字典的內容：")
print('-'*15)
for ch in mydict.items():
    print(ch)
