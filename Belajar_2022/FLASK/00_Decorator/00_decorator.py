
def outer_function(text):
    msg = text

    def inner_function():
        print(msg)

    return inner_function()


outer_function("Hello!")

