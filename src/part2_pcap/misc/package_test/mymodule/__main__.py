import click

from mymodule.mysubpackage.myfunctions import myfunction

print('mymodule main started')
myfunction()


@click.group()
def cli():
    pass


@cli.command()
@click.option('--size', help='This is the size', required=True)
def hello(size):
    print('hello world')


cli()
