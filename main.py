
# 73. Factory Method
class Car:
    def drive(self):
        return "Driving"

class Factory:
    @staticmethod
    def create():
        return Car()

c = Factory.create()
print(c.drive())


# 74. Equality Operator
class User:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

print(User(20) == User(20))


# 75. Fibonacci Iterator
class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        return val

for i in Fibonacci(7):
    print(i)

