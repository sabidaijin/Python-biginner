import sys
print('argv',sys.argv)
for arg in sys.argv:
    print(arg,type(arg))

line=[]


N=0
for N in range(0,10001):#Nを繰り返して行う
    if N<2:
        continue
    k=0#kを初期化する(ループの外に置いちゃうと加算を全部引き継いじゃうからダメ)
    for a in range(1,int(N/2)+1): #Nになるまで計算してみる（rangeのルールに則っている）
        if N%a==0:
            k=k+a
        
            #Nをaで割った数を足していくそれがNと一致していた場合プリント完全数
    if N==k:
        line.append(N)#完全数をlineにストックする
print(line)




