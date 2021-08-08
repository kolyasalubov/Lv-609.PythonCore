def filter_words(st):
    st = st.lower()
    st = st.split()
    return " ".join(st).capitalize()
