
# print(3 + 4)
# print(3 - 4)
# print(3 * 4)
# print(3 / 4)
# ctle / で複数をコメントアウト
#print(22 % 4) #%は商のあまり、商ではない
# comment

#print("Hello World !")
#print('Hello World !')
#文字は””または‘’で囲う

# print("Hello" + "World" +"!")
# print("Hello " * 3)

# print("-" * 30)
# print("log:")
# print("-" * 30)

# print(4 == 4) 
# print(4 == 3)
#bool型
# == 二つで等しい


#  x = 3
#  y = 4
# # #通常は変数に値をいれる
# # print(x * y)

# x = x + y
# print(x) #xを表示する
# y = y * y
# print(y)

#listは書き換えられる、tupleは数字を書き換えられない（はぼ使わない）

# エラーになる
#a = 2 + 'Hello'
#b = 2.64 / 'World!!'
# a = str(2) + "Hello"
# a = "2" + "Hello"
# print(a)

# dic = {
#        'A001': 34,      # key : value　#コロンで区切り
#        'A002': 'Hello'  # key : value　”kyeも文字指定
# }

# print(dic['A001']) #Keyをしていする際は大かっこでわける


# lis = [2,3,-5,6]
# tup = ('鈴木','佐藤','加藤','本田')
# dic = {
#        'A001': 34,        # key: value,
#        'A002': 'Hello',   # key: value,
# }

#0,1,2,3,4
# list 型、tuple 型は番号を指定する
# print(lis[2])        # 3番目のデータ
# print(tup[1])        # 2番目のデータ
# print(lis[0])

# # dict 型は key を指定する
# print(dic['A001'])   # A001 のデータ

#print(lis[-1]) #-をいれると後ろから数える

# a = 'Hello'
# b = 3
# c = 6.0
# d = True
# lis = [1,3,5,7]
# tup = (3,5,8,1)
# dic = {'A001':34,'A002':38}

# print(type(a)) #print typeで型の名前で返してくれる
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(lis))
# print(type(tup))
# print(type(dic))

#print(type(lis[0]))

# x = 0
# x = x + 1
# print(x)
# x = x + 1
# print(x)
# x = x + 1
# print(x)
# x = x + 1
# print(x)
# x = x + 1
# print(x)

#print(range(5))
# 0 1 2 3 4

# x = 0 : デフォルトで入る
# for x in range(5):
#     x = x + 1
#     print(x)

# x = 3 
# print(x) #3
# for x in range(5): #ブロック
#     x = x + 1
#     print(x)

# print(X) #3

# x = 3
# if x == 3 :
#    print("xは3です") #コロンの次はインデントが必要

# x = 5
# if x == 3 :
#    print("xは3です")
# else:
#    print("xは3ではない")

# x = 10　# xに14を代入する
# if x > 9 :
#    print("xは10以上です")
# elif x == 0: #xが0と等しいか
#    print("xは0です。")
# else:
#    print("xは0より小さいです。")

# def multi(x, y): #関数のときはdefといれる
#     return(x * y) 

# #使い方
# print(multi(3,4))    # 結果は12
# print(multi(-2,15))   # 結果は-30

# class calc():
#     def __init__(self,x,y):
#         self.minus = x - y
#         self.plus = x * y
#         self.multi = x * y
#         self.divis = x / y

# # 使い方
# print(calc(3,4).multi)
# print(calc(-2,15).multi)


for x in range (1,101): #1,101とすると0が抜ける　1,100だと99まで？
    if x % 15 == 0:     #if文をfor文の下のブロックにいれる
        print("fizz Buzz!")
    elif x % 3 == 0:
        print("Fizz!")
    elif x % 5 == 0:
        print("Buzz!")
    else:
        print(x)
