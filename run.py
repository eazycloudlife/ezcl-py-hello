from hello import (
    hello,
    hello_world,
    hi,
    hi_world,
    version
)

def say_hello(name):
    return hello(name)

def say_hello_world():
    return hello_world()

def say_hi(name):
    return hi(name)

def say_hi_world():
    return hi_world()

def say_version():
    return version()

if __name__ == "__main__":
    name = "Eazy Cloud Life"

    print(say_hello(name))
    print(say_hello_world())
    print(say_hi(name))
    print(say_hi_world())
    print(say_version())
