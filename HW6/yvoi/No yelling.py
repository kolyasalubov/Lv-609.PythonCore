def filter_words(st):
    st = [x.lower() for x in st.split()]
    first = []
    for x in st[0]:
        first.append(x)
    first[0] = first[0].upper()
    st[0] = ''.join(first)
    return ' '.join(st)