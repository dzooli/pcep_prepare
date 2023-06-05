from dataclasses import dataclass, field, asdict
from pprint import pprint
from configobj.validate import VdtValueTooSmallError, VdtValueTooBigError, Validator, VdtValueError


@dataclass(slots=True, frozen=True)
class Cat:
    name: str = field(default=None, init=True)
    age: int = field(default=None, init=True)

    def __post_init__(self):
        vtor = Validator()
        try:
            vtor.check('integer(0, 10)', self.age)
        except VdtValueTooBigError as exc:
            exc.add_note('age: max is 10')
            raise
        except VdtValueTooSmallError as exc:
            exc.add_note('age: min is 0')
            raise
        print('valid')


print("Try 1:")
try:
    myCat = Cat('Garfield', 12)
except VdtValueError as exc:
    print(f"Validation error: {exc}")
    print(vars(exc))


print("\nTry 2:")
try:
    myCat2 = Cat('Meow', -2)
except VdtValueError as exc:
    print(f"Validation error: {exc}")
    print(vars(exc))


print("\nTry 3:")
try:
    myCat3 = Cat('Cica', 3)
except:
    print("Still invalid")


print("\nTry without init:")
myCat4 = None
try:
    myCat4 = Cat()
except Exception as exc:
    print(exc)
pprint(asdict(myCat4 if myCat4 else {}), indent=4, compact=False, width=10)

