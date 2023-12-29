import datetime #dateのライブラリのインポート
now=datetime.datetime.now()#今の時間を取得する
print(now)
type(now)
day4=datetime.datetime(2023,10,31)
print(day4)

print(day4.weekday())#曜日の取得の方法
td=day4-now#日時の差を計算する方法

print(td)
print(type(td))

print(now.strftime('Time(%H:%M:%S) Date(%m-%d,%Y)'))#strfttimeの使い方、文字列に扱うメソッド

t2_str='05012020 123456'#文字列での任意の日時の指定の仕方以下産業
t2=datetime.datetime.strptime(t2_str,'%d%m%Y %H%M%S')#%Hとかはいわゆる変換仕様の一種で、変数みたいなもの
print(t2)



import zoneinfo
jst = zoneinfo.ZoneInfo('Japan')
now0=datetime.datetime.now()
now0.utcoffset()
now1=datetime.datetime.now(tz=jst)
now1.utcoffset()
est=zoneinfo.ZoneInfo('US/Eastern')

print(now0)
print(now1)