class RequireRunMeta(type):
    def __new__(cls,name,bases,attrs):
        if "run" not in attrs:
            raise TypeError("run() is required")
        return super().__new__(cls,name,bases,attrs)

class Worker(metaclass=RequireRunMeta):
    def run(self):
        print("running worker")

w = Worker()
w.run()

class Special(metaclass=RequireRunMeta):
    def run(self):
        print("running special methods")


sp = Special()
sp.run()

