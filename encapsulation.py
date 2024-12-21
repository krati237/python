#encapsulation=multiple attribute wrapup into a single unit
#specifier=1. public 2.protected(_x) 3.private(__x)

#private specifier
class a:
    __x=10
    __y=20
    def __show(self):
        print("kratika")
class b(a):
    pass
print(dir(b))
obj=b()
print(obj._a__x)