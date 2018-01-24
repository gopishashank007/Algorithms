import heapq


class Heap(object):
    def __init__(self):
        """ create a new min-heap. """
        self._heap = []
        self.s = [('A', 2, 12), ('B', 1, 10), ('C', 3, 20), ('D', 2, 15)]
        self.t = (self.s)
        self.value = []
        self.W = 6  # knapsack capacity
        self.newStack = []
        self.a= [ ]
        self.knapsackV = []

    def push(self, priority, item):
        assert priority >= 0
        heapq.heappush(self._heap, (priority, item))

    def pop(self):
        """ Returns the item with lowest priority. """
        item = heapq.heappop(self._heap)[0]  # (prio, item)[1] == item
        return item

    def __len__(self):
        return len(self._heap)

    def __iter__(self):
        """ Get all elements ordered by asc. priority. """
        return self

    def next(self):
        """ Get all elements ordered by their priority (lowest first). """
        try:
            return self.pop()
        except IndexError:
            raise StopIteration

    def knapsack(self):
        for i in self.s:
            self.v = float(i[2] / i[1])                 #b[i]/w[i]
            self.value.append(float(self.v))              #value list has the above value
        for items in self.s:
            itemBenefit = items[2]
            itemTuplePrice = items[1]
            itemTupleQty = float(items[2] / items[1])
            itemTuple = (itemBenefit, itemTuplePrice, itemTupleQty)
            self.newStack.append(itemTuple)
        print "Stack is ", self.newStack
        #self.knapsackweight = 0
        for itemsM in self.newStack:
            newTuple = (itemsM[0],itemsM[1])
            heapq.heappush(self._heap, (itemsM[2], newTuple ))
        print "new heap after pushing", self._heap
        print"after sorting"
        self.x=(sorted(self._heap,reverse=True))
        print self.x
        print len(self.x)

        addedWeight = 0
        totalWeight = 0
        benefit = 0
        while(addedWeight<self.W):
            itemb = self.x.pop(0)
            self.knapsackV.append(itemb)
            print itemb
            totalWeight+= itemb[1][1]
            benefit+= itemb[1][0]
            addedWeight+= itemb[1][1]
        print "Knapsack is", self.knapsackV
        print "Total weight is",totalWeight
        print "Total Benefit",benefit

        # while knapsackweight < self.W and len(self.x) != 0 :
        #     for itemsa in self.x :
        #         knapsackweight=itemsa[1]
        #         knapsackbenefit=itemsa[2]
        #         newknapsack=(knapsackweight,knapsackbenefit)
        #         self.a.append(newknapsack)
        #  #print "knapsack"
        # print self.knapsackweight


    def display(self):
        self.p = []
        print "items initially"
        for items in reversed(self._heap):
            self.p.append(items)
        print self.s


h = Heap()
# h.push(10, 3 )
# h.push(20, 58)
# h.push(5, 100)
# h.push(0, 6)
h.knapsack()
h.display()