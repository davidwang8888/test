# Homework 3:Counters the characters
#
# 宣告
s1 = ''
chr1 = ''
count1 = 0
count2 = 0
strok = []      # 陣列strok,紀錄曾出現過的字元(不重複的字元)
countok = []    # 陣列countok,紀錄目前字元出現的次數


# 建立一個空字典
mydict = {}

# Input data
sentence = input("Please input data: \n")
s1 = sentence     # 暫時的字串,紀錄剩餘字串
print('-'*20)

for k in range(len(sentence)):  # 將輸入的字串sentence分解成字元,一一計數
    char1 = sentence[k]         # 取出字元
    count1 = s1.count(char1)    # 計算字元在暫時的字串s1中出現的次數
    count2 = strok.count(char1)  # count2的值來判斷目前字元是否在strok字串中出現過
    if count2 == 0:             # 如果count2等於0,表示目前字元尚未出現過,必須計數
        strok.append(char1)     # 將新的字元放入陣列strok,紀錄新的字元
        countok.append(count1)  # 將字元的計數值放入陣列countok
        s1 = s1[1:]             # 去除目前的字元(已使用過)
        mydict[char1] = count1  # 將字元及計數值加入字典中

# 字典輸出
for ch in mydict.items():
    print(ch)
