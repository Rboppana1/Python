"""
def format_name(first_name, last_name):
    f_name = first_name.capitalize()
    l_name = last_name.capitalize()
    full_name = f_name + " " + l_name
    print(full_name)

format_name("peter", "zang")
"""

def format_name(first_name, last_name):
    formated_f_name = first_name.title()
    formated_l_name = last_name.title()
    #full_name = formated_f_name + " " + formated_l_name
    return f"({formated_f_name} {formated_l_name})"
    #print(full_name)

formatted_name = format_name("sample", "simple")
print(formatted_name)


"""
def format_name(first_name, last_name):
    f_name = first_name.capitalize()
    l_name = last_name.capitalize()
    full_name = f_name + " " + l_name
    return (full_name)


print(format_name("rayi", "error"))

# format_name("peter","zang")

"""

length = len(formatted_name)
print(length)

def format_name(f_name, l_name):
    if f_name == "test" or l_name == "":
        return f_name
format_name("test", "test")
print("First name is {}"(format_name))
"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    #return f"Result: {formated_f_name} {formated_l_name}"
    return f"({formated_f_name} {formated_l_name})"
"""

def add(a, b):
    # returning sum of a and b
    return a + b
def is_true(a):
    # returning boolean of a
    return bool(a)
# calling function
res = add(2, 3)
print("Result of add function is {}".format(res))
res = is_true(2 < 5)
print("\nResult of is_true function is {}".format(res))
