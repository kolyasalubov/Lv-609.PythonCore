python_philosophy = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better. than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

python_philosophy_replaced = python_philosophy.replace('.', ' ')
python_philosophy_splited = python_philosophy_replaced.split(' ')

count_of_better = 0
count_of_never = 0
count_of_is = 0

for i in range(len(python_philosophy_splited)):
    if python_philosophy_splited[i] == 'better':
        count_of_better += 1
    elif python_philosophy_splited[i]=='never':
        count_of_never += 1
    elif python_philosophy_splited[i]=='is':
        count_of_is += 1

print(f'Count of "better" = {count_of_better}')
print(f'Count of "never" = {count_of_never}')
print(f'Count of "is" = {count_of_is}')
print(python_philosophy.upper())
print()
replaced_list = python_philosophy.replace('i','&').replace('I','&')
print(replaced_list)
