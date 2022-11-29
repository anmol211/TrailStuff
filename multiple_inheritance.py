class A:
    x=2

class B(A):
    pass

class C(A):
    pass

a = A()
print(a.x)
C.x = 5
c = C()
print(a.x)
print(c.x)