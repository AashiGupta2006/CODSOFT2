print("~~~ Password Generator ~~~")
import string 
import random
if __name__ == "__main__" :
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    
    plen = int(input("Enter password length : \n"))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))

    random.shuffle(s)
    print("".join(s[0:plen]))
