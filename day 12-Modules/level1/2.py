# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

import random
import string

def random_id():
    no_of_chars = int(input("Enter the number of characters for each ID: "))
    no_of_ids = int(input("Enter the number of IDs to generate: "))

    char = string.digits + string.ascii_lowercase
    ids = []

    for _ in range(no_of_ids):
        id = "".join(random.choices(char, k=no_of_chars))
        ids.append(id)

    return ids

print(random_id())

# # Example usage from gpt
# generated_ids = random_id()
# for idx, id_ in enumerate(generated_ids):
#     print(f"ID {idx + 1}: {id_}")
