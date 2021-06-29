def words_count(text: str):
    print(f"Better-{text.count('better')}\n"
          f"Never-{text.count('never')}\n"
          f"Is-{text.count('is')}")


def upper_text(text:str):
    print(text.upper())


def symbol_i(text):
    print(text.replace("i", "&"))
    print(text.replace("I", "&"))

text = "Beautiful is better than ugly.\n"\
        "Explicit is better than implicit.\n"\
        "Simple is better than complex.\n"\
        "Complex is better than complicated.\n"\
        "Flat is better than nested.\n"\
        "Sparse is better than dense.\n"\
        "Readability counts.\n"\
        "Special cases aren't special enough to break the rules.\n"\
        "Although practicality beats purity.\n"\
        "Errors should never pass silently.\n"\
        "Unless explicitly silenced.\n"\
        "In the face of ambiguity, refuse the temptation to guess.\n"\
        "There should be one-- and preferably only one --obvious way to do it.\n"\
        "Although that way may not be obvious at first unless you're Dutch.\n"\
        "Now is better than never.\n"\
        "Although never is often better than *right* now.\n"\
        "If the implementation is hard to explain, it's a bad idea.\n"\
        "If the implementation is easy to explain, it may be a good idea.\n"\
        "Namespaces are one honking great idea -- let's do more of those!\n"\


if __name__ == '__main__':
    words_count(text)
    print("---" * 6)

    upper_text(text)
    print("---" * 6)

    symbol_i(text)