class A():
    def foo(self):
        print("parent/base class")
 
class B(A):
    def foo(self):
        super().foo()
        print("child/sub class ")
b = B()
b.foo()