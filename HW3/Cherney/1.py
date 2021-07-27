import this
import codecs


str = codecs.decode(this.s, "rot13")
count_better = str.count("better")
count_never = str.count("never")
count_is = str.count("is")
print(f"\nWord 'better appears {count_better} times, \n"
      f"word 'never' appears {count_never} times, \n"
      f"word 'is' appears {count_is} times\n")
print(str.upper(), end="\n")
print(str.replace("i", "&"))
