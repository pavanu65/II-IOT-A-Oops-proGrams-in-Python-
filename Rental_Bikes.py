class Bikeforrent:
    def __init__(self,stock):
        self.stock=stock 
    def display(self):
        print(f"Total Stock : {self.stock}")
    def rent(self,x):
        if(x<=0):
            print("Enter +ve no.")
        elif(x>self.stock):
            print("Enter within stock limit.")
        else:
            self.stock=self.stock-x
            print(f"Your total cost : {x*100}")
            print(f"Stock available: {self.stock}")          
while True:
    obj=Bikeforrent(100)
    i=int(input('''
1 Display stock
2 Rent a Bike
3 Exit
    '''))
        
    if(i==1): 
        obj.display()
    elif(i==2): 
        n=int(input())
        obj.rent(n)
    else:
        break
