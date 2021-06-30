zen_of_python = ("""The Zen of Python, by Tim Peters\n
Beautiful is better than ugly.\n
Explicit is better than implicit.\n
Simple is better than complex.\n
Complex is better than complicated.\n
Flat is better than nested.\n
Sparse is better than dense.\n
Readability counts.\n
Special cases aren't special enough to break the rules.\n
Although practicality beats purity.\n
Errors should never pass silently.\n
Unless explicitly silenced.\n
In the face of ambiguity, refuse the temptation to guess.\n
There should be one-- and preferably only one --obvious way to do it.\n
Although that way may not be obvious at first unless you're Dutch.\n
Now is better than never.\n
Although never is often better than *right* now.\n
If the implementation is hard to explain, it's a bad idea.\n
If the implementation is easy to explain, it may be a good idea.\n
Namespaces are one honking great idea -- let's do more of those!""")

print (zen_of_python)

#TASK ONE

first_count_better = (zen_of_python.count('better'))
print('In this text "better" used:', first_count_better, 'times.')

second_count_never = (zen_of_python.count('never'))
print('In this text "never" used:', second_count_never, 'times.')

third_count_is = (zen_of_python.count('is'))
print('In this text "is" used:', third_count_is, 'times.')

#TASK TWO

upper_text = (zen_of_python.upper())
print (upper_text)

#TASK THREE

replaced_words = (zen_of_python.replace('i', '&'))
print (replaced_words)
