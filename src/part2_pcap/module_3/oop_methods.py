from pprint import pprint


class Classy:
    def get_name(self):
        return type(self).__name__

    def get_bases(self):
        return type(self).__bases__


class ClassyKid(Classy):
    pass


if __name__ == "__main__":
    pprint(Classy.__name__)
    myc = Classy()
    pprint(myc.get_name())
    mykid = ClassyKid()
    pprint(mykid.get_bases())
