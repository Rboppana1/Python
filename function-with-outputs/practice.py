def format_name(first_name, last_name):
    f_name = first_name.capitalize()
    l_name = last_name.capitalize()
    full_name = f_name + " " + l_name
    print(full_name)


format_name("peter", "zang")


def format_name(first_name, last_name):
    f_name = first_name.capitalize()
    l_name = last_name.capitalize()
    full_name = f_name + " " + l_name
    return (full_name)


print(format_name("rayi", "error"))

# format_name("peter","zang")
