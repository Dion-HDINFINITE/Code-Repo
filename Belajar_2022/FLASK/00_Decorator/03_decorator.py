def decorator_function(original_function):
    def wrapper_function(*args. **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display function run well.')
@decorator_function
def display_info(name, age, school):
    print('display_info ran with arguements ({} {} {})'.format(name, age, school))

display()
display_info("Mike", 10, school:"IGES")