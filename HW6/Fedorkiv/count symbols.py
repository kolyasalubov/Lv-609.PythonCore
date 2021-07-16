def count_symbols (word):
    result = {}
    for i in word:
        if i in result:
            continue
        else:
            result.update({str(i): word.count(i)})
    return result

print (count_symbols("hello"))
