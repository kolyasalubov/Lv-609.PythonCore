zen = """Beautiful is better than ugly.
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
count_better = zen.count("better")
count_never = zen.count("never")
counter_is = zen.count("is")
upper_zen = zen.upper()
replace_zen = zen.replace("i", "&")
print(f"""Number of words better is {count_better},
Number of words never is {count_never},
Number of words is is {counter_is}""")
print(upper_zen)
print(replace_zen)
