
class shashankStack:

    def __init__(self):                                #defining array constructor
        self.stk = []
        self.top = -1
        self.stksize = 3                            #stack size is fixed for 3 elements

    def size(self):
        #return len(self.stk)-1
        return self.top+1

    def isEmpty(self):
        if self.top == -1 :
            return True

    def push(self,item):
        if self.top  == self.stksize-1 :
            print "cannot insert !stack is full"
        elif self.top <= self.stksize:
            #self.stk.insert(self.top,item)
            self.top += 1
            self.stk.insert(self.top, item)
            print self.top

    def pop(self):
        if self.isEmpty() :
            print "nothing to delete"
        else:
            #self.top = self.top - 1
            self.stk.remove(self.stk[self.top])
            self.top = self.top - 1

    def printStack(self):
       if self.top > -1:
            print "elements are"
            for i in reversed(self.stk):
                print i
       else:
           print "stack is empty"



s = shashankStack()
#print s.size()
#print s.isEmpty()
s.push(6)                                       #element 6 is inserted into stack
s.push(8)                                       #element 8 is inserted
s.push(5)                                       #element 5 is inserted
s.printStack()
s.push(3)                                       #element 3 does not get inserted because stack is full
s.printStack()
s.pop()
s.printStack()
s.pop()
s.printStack()
s.pop()
s.pop()                                         #stack is empty condition becomes true
s.printStack()