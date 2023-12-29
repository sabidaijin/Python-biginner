import csv
import matplotlib as plt#パイソン課題

class data:
    def __init__(self,x):
        f= open(x,'r')
        csvfile=csv.reader(f)

    def read(self):
        year=[]
        feb=[]
        aug=[]
        for gyou,row in enumerate(csvfile):
    #からのリストを作ってそこに詰めていくパターンの例として出てきた
        if gyou<2:#最初の二行は文字列なので使わない
            continue
    
        year.append(int(row[0]))#row[]の中にはリストの形で一行のデータが入っているので、それをリスト煮詰める
        feb.append(float(row[2]))
        aug.append(float(row[8]))

    def show(self):
        plt.title('North Hemispehre Temperture Trend')
        plt.xlabel('Year')
        plt.ylabel('Temperature Delta')
        plt.plot(year, feb, label='Feb')
        plt.plot(year, aug, label='Aug')
        plt.legend()
        plt.show()   




