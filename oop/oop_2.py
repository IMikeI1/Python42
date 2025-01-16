class ClassA:
    def method(self):
        return "Method class A"
class ClassB:
    def method(self):
        return "Method class B"
class ClassC(ClassB, ClassA):
    def method_c(self):
        return "Method class C"

obj = ClassC()
print(obj.method())
print(ClassC.mro())
# print(obj.method_a())
# print(obj.method_b())
# print(obj.method_c())

