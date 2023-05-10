
from pprint import pprint
from attrs import asdict, define, field, fields, filters, validators
from typing import Dict
from functools import wraps
import gettext


def masked(func):
    secrets = ['password', '_secret']
    @wraps(func)
    def wrapper(*args, **kwargs):
        repr_dict = func(args[0])
        for key in secrets:
            if isinstance(repr_dict, dict) and repr_dict.get(key):
                del repr_dict[key]
        return repr_dict
    return wrapper


@define(kw_only=True, init=True)
class HiddenPilot(Dict):
    rank: int = field(init=True, validator=validators.gt(50), default=51)
    name: str = field(init=False, default='noname')
    password: str = field(init=False, default='password', repr=lambda value: '****')


# Class without attrs
class NormalPilot:
    __rank = 1

    def _get_rank(self):
        return self.__rank

    def _set_rank(self, value):
        self.__rank = value

    rank = property(_get_rank, _set_rank, None, "The pilot's rank")


## test it
print("Testing attrs-based HiddenPilot...")
pilot = HiddenPilot(rank=80)
pilot.rank = 55
print('asdict() does not use repr')
pprint(asdict(pilot))
print('str() uses repr')
pprint(str(pilot))
print()

print("Testing NormalPilot...")
npilot = NormalPilot()
npilot.rank = 32
npilot.__new_rank = 12
pprint(vars(npilot))
