#polymorphism=same function name with different attributes
# types=1.method overloading
# 2. method overriding

#method overloading=when two same method are there but in the same class it is called overloading ,python 
# does not support overloading thats why we use variable lenght argument(* args)
class A:
    def add(self,*n):
        sum=0
        for i in n:
            sum =sum+i
            print(sum)
obj=A()
obj.add(10,20)

#method overriding=when two same method are there but class is different then is creates overrirding
class a:
    def add(self,x,y):    #this is super class
        self.x=x
        self.y=y
        print( self.x+self.y)
class b(a):
    def add(self,x,y,z):
        self.p=x
        self.q=y
        self.r=z
        super().add(10,20)    #to access the super class attributes
        print(self.p+self.q+self.r)
obj=b()
obj.add(10,20,30)