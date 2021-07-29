def reverse(st):
    return " ".join(reversed(st.split())).strip()
    
    
if __name__ == "__main__":
    print(reverse("Hello World"))