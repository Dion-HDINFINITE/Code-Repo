def run_my_function(original_function):

    def wrapper_function():
        print('wrapper executed before {}'.format(original_function.__name__))
        return original_function()

    return wrapper_function

@run_my_function
def display():
    print('display function ran well')

display()