class A:
def m1(self,a):
print(a)

def m1(self,a,b):
print(a + b)

def m1(self, name , age , a):

print('Name is :' , name)
print('Age is :' , age)
print(a)

obj = A()
obj.m1('Avinesh',30,50)