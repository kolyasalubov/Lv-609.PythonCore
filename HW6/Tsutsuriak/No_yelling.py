#st = "hELLO World!"
#a = st.lower().split()
#b = a[0][0].upper() + a[0][1:].lower()
#c = a[1:]
#print(b, *c)

def filter_words(st):
    st = st[0].upper() + st[1:].lower()
    return " ".join(st.split())