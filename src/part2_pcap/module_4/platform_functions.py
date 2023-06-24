import platform
import os
from pprint import pprint

pprint(platform.node())
pprint(platform.system())
pprint(platform.uname())
pprint(platform.processor())
pprint(platform.architecture())
pprint(platform.win32_ver())
pprint(platform.win32_edition())
pprint(os.name)