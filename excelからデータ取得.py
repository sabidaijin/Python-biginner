
import openpyxl
XLS_FN='nsd01000.xlsx'

def get_column_number(column_str):
    cn=0
    for i,c in enumerate(column_str):#iにインデックス、cに中身この時、ABだったらAが先に入る
        print(c)
        cn =cn+ord(c)-ord('A')#Aを基準にAとの距離を計算する
        if i<len(column_str)-1:#もしも、長さが入力したものより一つ少なければ桁上がりする
            cn=(cn+1)*26#ひとつ上の桁があるときは26倍する必要がある
    return cn


def test1():
    for column_str in['A','B','Z','AA','AZ']:
        print(column_str,get_column_number(column_str))
test1()

def get_column_str(first_str,offset):
    cn=get_colmun_number(first_str)+offset
    cs=
    while true:
        cs=chr(ord('A')+cn%26)+cs
        cn=cn//26
        if cn ==0:
            break
        cn=cn-1
        return cn
    
def test2()
    #まだ途中
    