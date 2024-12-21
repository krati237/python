#inheritence= parent-child relationship
#single level inheritence
class A:
    x=10
    y=20
    def p_name(self,name):
        self.p=name
        print(self.p)
class B(A):
    def c_name(self,name):
        self.q=name
        print(self.q)
obj=A()
obj1=B()
obj.p_name("kratika")
obj1.c_name("soni")
print(dir(obj))
print(dir(obj1))

#another exm  to access all properties of parent into child class
class A:
    x=10
    y=20
    def p_name(self,name):
        self.p=name
        print(self.p)
class B(A):
    def c_name(self,name):
        self.q=name
        print(A.x)
        print(A.y)
        self.p_name("kratika")
        print(self.p)
        print(self.q)
obj2=B()
obj2.c_name("soni")


#multilevel inheritence
class A:
    x=10
    y=20
    def p_name(self,name):
        self.p=name
        print(self.p)
class B(A):
    def q_name(self,name):
        self.q=name
        print(self.q)
        
class C(B):
    def r_name(self,name):
        self.r=name
        print(self.r)
        print(A.x)
        print(A.y)
        self.p_name("kratika")
        print(self.p)
        self.q_name("soni")
        print(self.q)
        
obj2=C()
obj2.r_name("kittu")


#multiple inheritence
class father:
    def property(self,f_name,f_bank):
        self.f_name=f_name
        self.f_bank=f_bank
class mother:
    def property1(self,m_name,m_bank):
        self.m_name=m_name
        self.m_bank=m_bank
class child(father,mother):
    def property2(self,city):
        self.city=city
        print(self.f_name)
        print(self.f_bank)
        print(self.m_name)
        print(self.m_bank)
        print(self.city)
obj=child()
obj.property('kratika','rbi')
obj.property1('ranu','sbi')
obj.property2('bhopal')


#hybrid inheritence
class A:
    def show(self,A_name):
        self.A_name=A_name
class B(A):
    def show1(self,B_name):
        self.B_name=B_name
class C(B):
    def show2(self, C_name):
        self.C_name=C_name
class D:
    def show3(self,D_name):
        self.D_name=D_name
class E(C,D):
    def show4(self,E_name):
        self.E_name=E_name
obj=E()