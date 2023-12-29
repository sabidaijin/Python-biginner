class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def Area(self):
        return self.width*self.height
    def deagonal(self):
        return (self.width **2+self.height**2)**0.5

a= rectangle(12,9)
#print('Area:',a.Area(),'deagonal length:',a.deagonal())
    
import datetime
class date :
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
        print('Given date is', f'{year}-{month}-{day}')
        self.DaysPassed(year,month,day)
        

    def DaysPassed(self,year,month,day):
        now=datetime.datetime.now()
        now_year = now.year
        now_month = now.month
        now_day = now.day
        dt1 = datetime.datetime(year=now_year, month=now_month, day=now_day)
        dt2 = datetime.datetime(year=self.year, month=self.month, day=self.day)
        
        passed_date=dt1-dt2
        print(f'{passed_date}' "passed since" f'{year}-{month}-{day}')
        
        self.Weekday(year,month,day)

    def Weekday(self,year,month,day):
        today=datetime.datetime(year, month, day) 
        k=today.weekday()
        if k==0:
            x='Monday'
        if k==1:
            x='Tuesday'
        if k==2:
            x='Wednesday'
        if k==3:
            x='Thrusday' 
        if k==4:
            x='Friday'
        if k==5:
            x='Satarday'
        if k==6:
            x='Sunday'
        

        print(f'{year}-{month}-{day}'+" "+"is"+" "f'{x}')

   
    