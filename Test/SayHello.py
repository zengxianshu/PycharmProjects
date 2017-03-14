class Hello():
    def __init__(self,name):
        self._name = name

    def sayHello(self):
        print("hello {0}".format(self._name))


class Hi(Hello):
    def sayHi(self):
        print("hi {0}".format(self._name))



# h = Hello("world")
# h.sayHello()
