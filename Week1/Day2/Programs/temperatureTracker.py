import unittest


class TempTracker(object):

    # Implement methods to track the max, min, mean, and mode
    
    def __init__(self):
        self.mx=None
        self.mn=None
        self.mean=None
        self.freqs = [0 for i in range(110)]
        self.tempCount=0
        self.totalTemps=0
        self.mode=0
        self.occurance=0

    def insert(self, temperature):
        if self.mx==None or self.mn==None:
            self.mx=temperature
            self.mn=temperature
        else:
            if temperature<self.mn:
                self.mn=temperature
            if temperature>self.mx:
                self.mx=temperature
        temp=self.freqs[temperature]+1
        self.freqs[temperature]=temp
        if x>self.occurance:
            self.occurance=temp
            self.mode = temperature
        self.totalTemps+=temperature
        self.tempCount+=1

    def get_max(self):
        return self.mx

    def get_min(self):
        return self.mn

    def get_mean(self):
        return float(self.totalTemps/self.tempCount)

    def get_mode(self):
        return self.mode

