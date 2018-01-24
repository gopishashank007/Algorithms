class list:

    def __init__(self):
        self.s = []
        self.r = 0
        #self.e
        self.N = 2                                  #list size fixed for 2 elements
        self.n = 0
    def add(self,r,e):
       # print "add method"
        if self.n == self.N :
            print "Array is full"
        #self.n =+1
        if self.r <= self.n :
            #self.n+= 1
           #print "for loop "
           for i in range(self.n - 1,self.r,-1):
               self.s[i+1] = self.s[i]
               # self.s[i]
           #self.n += 1
           self.s.insert(self.r,e)
           self.n += 1
           print self.s[self.r]
    def remove(self,r):
        #e=self.s[self.r]
        self.s.remove(self.s[self.r])
        if self.r < self.n-1:
           print "remove  "
           for i in range(self.r, self.n-2, 1):
               self.s[i]=self.s[i+1]
           self.n -= 1
           print self.s
           #return self.s[self.r]
    def get(self):
        if self.r<0 and self.n-1:
            print "error"
        else:
            print self.s[self.r]
    def display(self):
        print self.s


s = list()
x = list()
x.add(0,1)
x.display()
x.add(1,3)
x.get()
x.add(2,6)
x.add(3,9)
#x.add(4,15)
x.remove(0)
x.display()
x.remove(1)
x.display()





