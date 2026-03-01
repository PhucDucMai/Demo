import random as rd

def get_av_actor():
    a = rd.randint(10, 100)
    if a % 2 == 0:
        return "Momoko Isshiki"
    return False