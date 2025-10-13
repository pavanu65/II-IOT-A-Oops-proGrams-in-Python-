#Single Inheritance
class A:
     def displayA(self):
          print("Inheritance A Class")
class B(A):
     def displayB(self):
          print("Inheritance B class")

obj = B()
obj.displayA()
obj.displayB()

print()
#Multi Label Inheritance
class A:
     def displayA(self):
          print("Inheritance A Class")
class B(A):
     def displayB(self):
          print("Inheritance B class")
class C(B):
     def displayC(self):
          print("Inheritance C class")


obj=C()
obj.displayA()
obj.displayB()
obj.displayC()
