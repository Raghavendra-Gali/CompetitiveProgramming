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
        # self.temps.append(temperature)
        if self.mx==None or self.mn==None:
            self.mx=temperature
            self.mn=temperature
        else:
            if temperature<self.mn:
                self.mn=temperature
            if temperature>self.mx:
                self.mx=temperature
        x=self.freqs[temperature]+1
        self.freqs[temperature]=x
        if x>self.occurance:
            self.occurance=x
            self.mode = temperature
        self.totalTemps+=temperature
        self.tempCount+=1

    def get_max(self):
        # return max(self.temps)
        return self.mx

    def get_min(self):
        # return min(self.temps)
        return self.mn

    def get_mean(self):
        # return float(sum(self.temps)/len(self.temps))
        return float(self.totalTemps/self.tempCount)

    def get_mode(self):
        return self.mode


















# Tests

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)