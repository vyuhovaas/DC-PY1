from random import sample
from string import ascii_uppercase, ascii_lowercase, digits


def get_random_password(n=8) -> str:
   symbols_ = ascii_lowercase + ascii_uppercase + digits
   return "".join(sample(symbols_, n))


print(get_random_password())
