class Top:
    def method(self):
        print(f"Top from {type(self).__name__}")

class Middle(Top):
    pass

class Bottom(Middle, Top):
    def method_b(self):
        print(f"Bottom from {type(self).__name__}")


obj = Bottom()
obj.method()
