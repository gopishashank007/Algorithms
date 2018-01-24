class Lcs:
    def _init_(self):
        self.l = [[]]  # DECLARATION OF LENGTH list
        # self.subSequence = []

    def lcs(self, X, Y):
        sub = []
        row = (len(X)+1)
        print "row"
        print row
        col = (len(Y)+1)
        print "col"
        print col
        self.l = [[0 for j in range(col)] for i in range(row)]
        for i in range(1,row-1):
            self.l[i][0] = 0
        for j in range(1,col-1):
            self.l[0][j] = 0
        for i in range(1,row):
            for j in range(1,col):
                if X[i-1] == Y[j-1]:
                    self.l[i][j] = self.l[i - 1][j - 1] + 1
                    sub.append(X[i-1])

                else:
                    self.l[i][j] = (max(self.l[i - 1][j], self.l[i][j - 1]))

        for i in range(row):
            for j in range(col):
                print '{:4}'.format(self.l[i][j]),
            print

        print " length of subsequence"
        maxvalue=None
        for i in range(row):
            for j in range(col):
                if(self.l[i][j]>maxvalue):
                    maxvalue=self.l[i][j]
        print maxvalue
        print sub
        print "the subsequence is"
        print  dict.fromkeys(sub).keys()






h = Lcs()
#h.lcs('CGATAATTGAGA', 'GTTCCTAATA')
h.lcs('ABCDEFGH','ACFGIKHM')
#h.lcs('ACBCF','ABCDAF')
