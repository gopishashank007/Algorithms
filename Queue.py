class shashankQueue:
    def __init__(self):                                     # default constructor
        self.arrayForQueue = []
        self.n = 6                                          #max capacity is n-1 elements which can be inserted
        self.front = 0
        self.sz = 0
        self.rear = -1
        self.i = 0
        self.loop = 1


    def size(self):
        return self.sz

    def isEmpty(self):
        return self.sz == 0

    def enqueue(self, item):
        if self.size() == self.n - 1:
            print "Full"
        else:
            self.rear = (self.front + self.sz) % self.n
            print self.rear
            self.arrayForQueue.insert(self.rear, item)                          #for inserting element
            # self.arrayForQueue[self.rear] = item
            self.sz += 1
            #print self.sz

    def dequeue(self):
        if self.isEmpty():
            print "impossible to delete"
        else:

            self.front = (self.front ) % self.n
            print self.front
            self.arrayForQueue.remove(self.arrayForQueue[self.front])               #for removing element
            #self.front -= 1
            self.sz -= 1
            #return self.item

    def display(self):

        print self.arrayForQueue

s = shashankQueue()
s.enqueue(2)                                                        #2 is present in the queue
#s.display()
s.enqueue(4)                                                        #2 and 4 are present in the queue
#s.display()
s.enqueue(6)
#s.display()
s.enqueue(8)
#s.display()
s.enqueue(10)                                                       #2,4,6,8,10 elements are present
s.enqueue(14)                                                        # full condition is satisfied,so 14 does not get inserted
s.display()
s.dequeue()                                                           # 2 gets deleted from front end
s.display()
s.dequeue()                                                           #  4 gets deleted from front end
s.display()
s.dequeue()                                                           # 6 gets deleted from front end
s.display()
#s.dequeue()
s.dequeue()                                                            # 8 gets deleted from front end
s.display()
s.dequeue()                                                             # 10 gets deleted from front end
s.display()
s.dequeue()                                                             # is empty condition is satisfied
s.display()
