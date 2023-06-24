"""
  Examples of decorators
"""
from pprint import pprint


def bearer_auth(decoratorparameter):
    """
    Decorator with decorator parameter
    """
    print(f"Calling parametrized decorator with parameter: {decoratorparameter} ...")

    def wrapper(func):
        token = decoratorparameter
        def inner(*args, **kwargs):
            print("Appending Bearer Authentication header...")
            updated_headers = kwargs.get('headers', {})
            updated_headers.update({'Authentication': f"Bearer {token}"})
            kwargs.update(headers=updated_headers)
            func(headers=updated_headers)
            print('After calling the parametrized-decorated function...')
        return inner

    return wrapper


def basic_auth(func):
    """
    Decorator without decorator parameter.
    """
    print("Calling simple decorator")

    def inner(**kwargs):
        print('Appending Remote-User header...')
        headers = kwargs.get('headers', {})
        headers.update({'Remote-User': 'mytestuser'})
        kwargs.update(headers=headers)
        func(**kwargs)
        print('After calling the simple-decorated function...')
    return inner


@bearer_auth("geeksforgeeks")
def my_bearer(**kwargs):
    headers = kwargs.get('headers', {})
    pprint(headers)


@basic_auth
def my_basic(**kwargs):
    headers = kwargs.get('headers')
    pprint(headers)


my_bearer(headers={'Content-Type': 'application/json'})
my_basic(headers={})

