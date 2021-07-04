#revercsed string

def reverse(st):
    st = st.split()
    st = ' '.join(st[::-1])
    print(st)
    return st


a = 'Hello World'
reverse(a)

