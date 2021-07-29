from Task1_module import My_Module as mod

def main():
    question = input("What you want to do?\n"
                     "1 - Rectangle square\n"
                     "2 - Triangle square\n"
                     "3 - Circle square\n")
    if question == "1":
        print(mod.rectangle_square())
    elif question == "2":
        print(mod.triangle_square())
    elif question == "3":
        print(mod.circle_square())


if __name__ == "__main__":
    main()