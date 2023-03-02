def func1(*args):
    print(args)

def func2(**kwargs):
    print(kwargs)

def func3(name, *args, age):
    print("name=", end=""), print(name)
    print("args=", end=""), print(args)
    print("age=", end=""), print(age)

def func4(name, age, **kwargs):
    print("name=", end=""), print(name)
    print("age=", end=""), print(age)
    print("kwargs=", end=""), print(kwargs)

def func5(name="안금장", *args, age, **kwargs):
    print("name=", end=""), print(name)
    print("args=", end=""), print(args)
    print("age=", end=""), print(age)
    print("kwargs=", end=""), print(kwargs)

if __name__ == "__main__":
    print(" --------- func1(*args) --------- ")
    func1("안금장", "1234")
    print(" --------- func2(**kwargs) --------- ")
    func2(name="김찬진", position="백")
    print(" --------- func3(name, *args, age) --------- ")
    func3("김찬진", "국민대", "멋사", age=27)
    print(" --------- func4(name, age, **kwargs) --------- ")
    func4("김찬진", "27", phone=111, address="seoul")
    print(" --------- func5(name=\"김찬진\", *args, age, **kwargs) --------- ")
    func5("김찬진", "국민대", "멋사", age=27, phone=111, address="seoul")

