from threading import *

class demo:
    def num(self,n):
        n = int(input("Enter a number: "))
        self.n = n
        
    
    def double(self):
        print("The double of your number is ", self.n * 2)

    def square(self):
        print("The square of your number is ", self.n ** 2)

obj = demo()
t1 = Thread(target=obj.num, args=(0,)) 
t1.start()
t1.join()

t2 = Thread(target=obj.double)
t3 = Thread(target=obj.square) 

t2.start()
t3.start()

t2.join()
t3.join()   
            