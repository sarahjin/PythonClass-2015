class Clock(object):
    def __init__(self, hour, minutes=0):
        self.minutes = '0'*(2-len(str(minutes)))+str(minutes)
        self.hour = '0'*(2-len(str(hour)))+str(hour)

    def __str__(self):
        return str(self.hour)+":"+str(self.minutes)

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)

    def __add__(self,minutes):
        time=int(self.hour)*60+int(self.minutes)+int(minutes)
        if time<0: time=24*60+time
        time%=1499
        mins=time%60
        hr=time/60
        hr+=mins/60
        mins%=60
        hr%=24
        mins=str(mins)
        hr=str(hr)
        mins = '0'*(2-len(mins))+mins
        hr = '0'*(2-len(hr))+hr
        time=hr+mins
        return Clock(time[0:2],time[2:4])

    def __sub__(self,minutes):
        return self+((-1)*minutes)

    def __eq__(self, other):
        return (self.hour==other.hour and self.minutes==other.minutes)

    def __ne__(self, other):
        return not self==other