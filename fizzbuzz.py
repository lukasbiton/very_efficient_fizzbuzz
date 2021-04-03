''' Make fizzbuzz as time efficient as possible.

Create generators that count down from a given number to find the divisors of 3,
5, and 15. Use these to check if we should use fizz, buzz, or fizz buzz.

Generators improve memory efficiency, but do they otherwise make things faster?
'''


# Imports
import time
import tracemalloc


def efficient_fizzbuzz(max_num=1000):

	max_num += 1 # Set the size of our list to fizzbuzz
	list_to_fizzbuzz = list(range(1,max_num,1)) # The list we need to read through
	fizzy_dict = {15: 'fizzbuzz', 5: 'buzz', 3: 'fizz'}
	fizzy_list = list(fizzy_dict.keys()) # Dynamically get list of numbers to cycle through
	fizzy_list.sort(reverse=False) # Go in ascending order to properly overwrite fizz or buzz with fizzbuzz

	def multiples_generators(mult):
		'''Use  a function to create the generator several times.'''
		return (num for num in range(max_num,1,-1) if num%mult == 0)

	for elem in list_to_fizzbuzz:

		str_to_print = elem # Keep updateing this variable until you print it at the end

		for mult in fizzy_list:

			mult_gen = multiples_generators(mult)
			while True:
				try:
					current_multiple = next(mult_gen) # Get the next multiple out of the generator
					if elem%current_multiple == 0:
						# In this case, we want to write fizz or buzz or fizzbuzz
						str_to_print = fizzy_dict[mult]
						# Don't break her because you want to check all the numbers, for "completeness"
				except StopIteration:
					# Catch this exception for when the generator ends, then break
					break
		print(str_to_print)

def normal_fizzbuzz(max_num=1000):
	'''Stolen from hacker rank: https://www.hackerrank.com/challenges/fizzbuzz/problem'''
	i=1
	while i <= max_num:
	    if i%3==0:
	        print("Fizz", end="")
	        if i%5==0:
	            print("Buzz", end="")
	    elif i%5==0:
	        print("Buzz", end="")
	    else:
	        print(i, end="")
	    print()
	    i+=1

def most_efficient():

	max_num = 1000

	tracemalloc.start() # Start keeping track of memory allocation

	snapshot1_eff = tracemalloc.take_snapshot() # Eff snapshot 1

	start = time.time() # Keep track of run time
	efficient_fizzbuzz(max_num)
	end = time.time()
	efficient = end - start # run time for the "efficient" algo

	snapshot2_eff = tracemalloc.take_snapshot() # Eff snapshot 2

	snapshot1_norm = tracemalloc.take_snapshot() # Norm snapshot 1

	start = time.time()
	normal_fizzbuzz(max_num)
	end = time.time()
	normal = end - start # run time for the "normal" algo

	snapshot2_norm = tracemalloc.take_snapshot() # Norm snapshot 2

	# Print run times
	print('Efficient', efficient)
	print('Normal', normal)

	# Calculte change in memory allocations for eff and norm case
	top_stats_eff = snapshot2_eff.compare_to(snapshot1_eff, 'lineno')
	top_stats_norm = snapshot2_norm.compare_to(snapshot1_norm, 'lineno')

	print("[ Top 10 ]")
	for stat_eff,stat_norm in zip(top_stats_eff[:10],top_stats_norm[:10]):
	    print('Stat eff', stat_eff)
	    print('Stat norm', stat_norm)


most_efficient()