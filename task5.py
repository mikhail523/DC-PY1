import random
import string


def get_random_password() -> str:
    length_ = 8
    pass_ = string.ascii_letters + string.digits
    password_rand = random.sample(pass_, length_)
    return password_rand


print(get_random_password())
