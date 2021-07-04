#HW3 blank for the task 1 to add to the Git&GitHub repos

# Add Zen of Python into multiple string by copypaste
this_is = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
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
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# Check if Zen successfully added to multiple string
#print(this_is)

# Some legacy code
#counter = 0
#word = 'better'
#word_position = None

#while not word_position == -1:
#    print(word_position)
#    word_position = int(this_is.find('better'))
#    if not word_position == -1:
#        counter += 1

# How many 'better' in this_is?
print("\'better\' повторюється {} раз".format(this_is.count('better')))

# How many 'never' in this_is?
print("\'never\' повторюється {} рази".format(this_is.count('never')))

# How many 'is' in this_is?
print("\'is\' повторюється {} раз".format(this_is.count('is')))

# Uppercase all
print(this_is.upper())

# Replace all 'i' by '&'
print(this_is.replace('i', '&'))