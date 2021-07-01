zen = "The Zen of Python, by Tim Peters Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"

zen_list = zen.split()
#print(zen_list)
def count_of_words():
    count_of_better = 0
    count_of_never = 0
    count_of_is = 0
    for i in zen_list:
        if i == 'better':
            count_of_better += 1
        elif i == 'never':
            count_of_never += 1
        elif i == 'is':
            count_of_is += 1

    print('Count of :')
    print('better --->', count_of_better)
    print('never --->', count_of_never)
    print('is --->', count_of_is)
    return 'Well Done!\n\n'

print(count_of_words())

def zen_up():
    ZEN = zen.upper()
    return ZEN

print(zen_up(),'\n\n')

# def changer():
    # zen.replace('i', '&')
    # return zen 

    # for s in zen:
    #     if s == 'i':
    #         s = '&'
    # return zen 
# print(changer())
