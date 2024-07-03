# Writ a function which generates a six digit/character random_user_id

import random
import string

def random_user_id():
    char=string.ascii_lowercase+string.digits
    random_id=random.choices(char,k=6)
    return "".join(random_id)

print(random_user_id())
print(random_user_id())
print(random_user_id())
print(random_user_id())
print(random_user_id())