f=open('/Users/yamamotohiroki/Desktop/名称未設定フォルダ/Heidi.txt')

d ={}#波かっこだから辞書型であることを宣言している

for line in f.readlines():#一行読んでlineに入れる
    for w in line.split():#lineを分断してwに入れる
        w =w.strip(',.¥n').lower()#wから,とかを消して、lowerにする
        if not w in d:#dにないのであればディクショナリーに追加する
            d[w]=1
        else:
            d[w]+=1 
f.close#ファイルを閉じる
print(len(d)) #dの長さを書く
a=[]#リストをaに入れる
for w in d:#wをdの分だけやる
    a.append([d[w],w])#aという配列にd[w]を追加する d[w]は頻度そのものを扱っている
a.sort()
a.reverse()
for i in range(200):
    print(a[i])
    