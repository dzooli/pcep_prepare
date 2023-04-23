from pprint import pprint
import yaml
import attrs.validators
from attrs import field, define, asdict


@define(kw_only=True)
class App:
    cells: list = field(factory=list, validator=
        attrs.validators.deep_iterable(attrs.validators.and_(attrs.validators.instance_of(str),
                                                             attrs.validators.in_(['hu', 'en'])),
                                       attrs.validators.and_(attrs.validators.instance_of(list),
                                                             attrs.validators.min_len(1)))
                           )


app = App(cells=['hu', 'en'])
print(str2 := yaml.dump(asdict(app), None, yaml.SafeDumper))

myobj = yaml.load(str2, yaml.BaseLoader)
pprint(myobj)


def myfun(**kwargs):
    print(kwargs.get('filename'))

myfun(fixename=2)
