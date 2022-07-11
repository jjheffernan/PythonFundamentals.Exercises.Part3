# test comment
# created by jj on 7/6/22

def language_input():
    language = input("What do you speak? english, spanish, or german? ")
    return language


def greet(name, lang):
    """prints str greeting using var name """
    # name = input("What is your name?")
    if lang == "english":
        print("Hello " + name + " welcome to Python3!")
    elif lang == "spanish":
        print("¡Holá " + name + " bienvenido a Python3!")
    elif lang == "german":
        print("Halo " + name + " wilkommen bei Python3!")


def name_input():
    """gets input arg for greet() function """
    # split greet() into two functions
    return input("What is your name? \n")


def main():
    """main function"""
    lang = language_input()
    name = name_input()
    greet(name, lang)


if __name__ == '__main__':
    main()
