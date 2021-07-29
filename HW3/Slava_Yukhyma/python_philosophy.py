from HW1.Slava_Yukhyma.input_output import sep
# Homework_3, part 1

python_philosophy = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one - -obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than * right * now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
 Namespaces are one honking great idea - - let's do more of those!"""

print(python_philosophy)

count_better = (python_philosophy.count('better'))
print('number of "better"', count_better)

count_never = (python_philosophy.count('never'))
print('number of "never"', count_never)

count_is = (python_philosophy.count('is'))
print('number of "is"', count_is)

sep("#", 50)

print(python_philosophy.upper())

sep("#", 50)


def replace_symbol(your_text):
    your_text = your_text.replace('i', '&')
    your_text = your_text.replace('I', '&')
    print(your_text)


replace_symbol(python_philosophy)

sep('#', 50)


def replace_symbol(your_text, prev_symbol, new_symbol):
    new_text = your_text.replace(prev_symbol, new_symbol)
    print(new_text)


replace_symbol(python_philosophy, 'o', '#')
