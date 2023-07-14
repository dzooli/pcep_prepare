from setuptools import setup

setup(
    name='mymodule',
    version='0.1.1',
    description='Sample package',
    author_email='zoltan.dzooli.fabian@gmail.com',
    author='Zoltan Fabian',
    py_modules=['mymodule.*'],
    install_requires=[
        'click'
    ],
    entry_points={
        'console_scripts': 'starter = mymodule.__main__:cli'
    }
)