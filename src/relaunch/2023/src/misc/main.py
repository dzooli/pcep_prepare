from attrs import validators, field, define


@define
class BaseClass:
    created_at: int = field(default=-1, init=False)
    updated_at: int = -1


@define
class Person(BaseClass):
    age: int = field(
        default=32,
        validator=validators.and_(validators.gt(0), validators.instance_of(int)),
    )


@define
class User(Person):
    uid: str = field(default="test", validator=validators.max_len(20))


@define
class Admin(User, Person):
    is_admin: bool = field(default=True, validator=validators.instance_of(bool))


@define
class StudentClass:
    __students = field(factory=list[User])

    def add_student(self, student: User = None):
        if not issubclass(student.__class__, User):
            raise ValueError("Only subclass of User is allowed")
        self.__students.append(student)


bc = BaseClass()
print(bc)
pers = Person()
print(pers)
adm = Admin()
print(adm)

sclass = StudentClass()
try:
    sclass.add_student(pers)
except ValueError as exc:
    print(f"ERROR: {str(exc)}")

try:
    sclass.add_student(bc)
except ValueError as exc:
    print(f"ERROR: {str(exc)}")

sclass.add_student(adm)

print(sclass)
