class Fib(object):
    def __init__(self,n):
        """
        2**n is stop condition,default value is 2**20 
        """
        self.a , self.b = 0,1
        if isinstance(n,int):
            self.stopCondtion = pow(2,abs(n)) 
        else:
            self.stopCondtion = pow(2,20)
    def __iter__(self):
        return(self)
    def next(self):
        self.a , self.b = self.b , self.a + self.b
        if self.a > self.stopCondtion:
            raise StopIteration
        else:
            return self.a

for i in Fib(10):
    print(i)
