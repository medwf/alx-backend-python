#!/usr/bin/python3

import unittest
from unittest.mock import patch, Mock
from utils import (
    get_json,
    access_nested_map,
    memoize,
)

def test_utils():
    class MyClass:
    
        @memoize
        def a_property(self):
            return self.a_method()

        def a_method(self):
            print("a_method called")
            return 42

    instance = MyClass()
    print(instance.a_method())
    print(instance.a_method())

def class_github():
    from client import GithubOrgClient
    instance = GithubOrgClient('google')
    # print(instance.ORG_URL)
    print(instance.org)
    print(instance.org)



if __name__ == "__main__":
    # __main()
    # test_utils()
    class_github()



"""
    def add_prefix(prefix):
        print(f'\033[32m{prefix}\033[0m')
        def decorator_function(original_function):
            print(f'\033[32m{original_function.__name__}\033[0m')
            def new_function(*args, **kwargs):
                return f"{prefix} {original_function(*args, **kwargs)}"
            return new_function
        return decorator_function

    # Define a simple function that returns a greeting
    def greet(name):
        return f"Hello, {name}!"

    # Use the higher-order function to create a new version of greet
    greet_with_prefix = add_prefix("Mr. mohamed")(greet)

    # Use the new function
    print(greet_with_prefix("John"))  # Output: "Mr. Hello, John!"

"""

def __main():
    def create_multiplier(n):
        def multiplier(x):
            return x * n
        return multiplier

    # Create a function that multiplies by 3
    times_three = create_multiplier(3)

    # Use the new function
    print(times_three(2))
    print(times_three(3))
    print(times_three(4))
    print(times_three(5))


def _main():
    # Define a simple function that squares a number
    def square(x):
        return x * x

    # Use the map function to apply the square function to a list of numbers
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = map(square, numbers)

    # Convert the map object to a list and print the result
    print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]


def main():
    def a_decorator(func):
        print('i am in a_decorator!')
        def wrapper(*args, **kwargs):
            """A wrapper function"""
            print('i am in a_decorator!, and wrapper')
            # Extend some capabilities of func
            func()
        print('i am in a_decorator!, after wrapper')
        def wrapperr(*args, **kwargs):
            """A wrapper function"""
            print('i am in a_decorator!, and wrapperr')
            # Extend some capabilities of func
            func()
        print('i am in a_decorator!, after wrapperr')
        return wrapperr

    @a_decorator
    def first_function():
        """This is docstring for first function"""
        print("first function")

    @a_decorator
    def second_function(a):
        """This is docstring for second function"""
        print("second function")

    print(first_function.__name__)
    print(first_function.__doc__)
    print(second_function.__name__)
    print(second_function.__doc__)

# class TestGetJson(unittest.TestCase):
#     def test_get_json(self):
#         test_url = "http://example.com/api"
#         test_payload = {"key": "value"}

#         # Configure the mock to return the desired response
#         attrs = {'json.return_value': test_payload}
#         with patch("requests.get", return_value=Mock(**attrs)) as req_get:
#             # Call the function to test
#             result = get_json(test_url)
#             print(f'\033[33m{result}\033[0m')
            
#             # Assert that the result is as expected
#             self.assertEqual(result, test_payload)
            
#             # Assert that requests.get was called once with the correct URL
#             req_get.assert_called_once_with(test_url)


