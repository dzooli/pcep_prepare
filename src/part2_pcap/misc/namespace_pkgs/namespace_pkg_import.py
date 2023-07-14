from package_foo.module_bar import hello
from package_foo.subpkg.module_bar import Cat
import package_foo

hello()
print(package_foo.__path__)
Cat.print_name()

