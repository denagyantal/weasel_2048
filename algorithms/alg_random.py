import random
from algorithms import alg_class


# function to simulate play 
def alg(map):
		movetypes = ("w", "a", "s", "d")

		move = random.choice(movetypes)
		return move

semi_random = alg_class.Algorithm(label="random",func=alg)
