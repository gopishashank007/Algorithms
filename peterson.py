#Date: 03/29/2017
#Class: CS5541
#Assignment: Peterson's Algorithm
#Author(s): Shashank Kasinadhuni
import threading
import sys
class Peterson:
    def __init__(self):
        self.getCount = 0
        self.turn =0
        self.flag0 = 0
        self.flag1=0
        self.threads = []

    def process0(self):
        while self.getCount<35:
            self.flag0 =1
            self.turn =1
            while self.flag1 == 1 and self.turn == 1:
                a=0
            for i in xrange(3):
                self.getCount+=1
                #print'A',
                sys.stdout.write('A')
                #print "A"
                if self.getCount == 30:
                    self.getCount = 0
                    print "\n"
        self.flag0=0
    sys.stdout.flush()

    def process1(self):
       # print "1"
        while self.getCount<35:
            self.flag1 =1
            self.turn =0
            while self.flag0 == 1 and self.turn == 0:
                b=0
            for i in xrange(3):
                self.getCount+=1
                #print'B'
                sys.stdout.write('B')
                if self.getCount == 30:
                    self.getCount = 0
                    print "\n"
            self.flag1=0
        sys.stdout.flush()

    def start(self):
        t = threading.Thread(target=self.process0)
        t2 = threading.Thread(target=self.process1)
        self.threads.append(t)
        self.threads.append(t2)
        t.start()
        t2.start()

    def end(self):
        for j in self.threads:
            j.join()
        print "List processing complete."


a = Peterson()
a.start()
a.end()
#a.process1()
#a.process2()