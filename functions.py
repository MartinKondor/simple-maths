from functools import reduce
import operator
import math


def product(iterable):
	"""
	Returns the product of an iterable
	If the list is empty, returns 1
	"""
	product = reduce(operator.mul, iterable, 1)
	return product


def prime_check(num):
	"""
	Checks if a number is prime.
	A simple function, not a speedy solution.
	"""
	if num == 1:
		return False

	upper_bound = int(math.sqrt(num) + 1)
	for n in range(2, upper_bound):
		if num % n == 0:
			return False
	return True


def find_primes(upper_bound):
	"""
	Find primes up to upper_bound
	An attemted use of sieve
	"""
	primes = [2]


	for num in range(3, upper_bound):
		flag = True 					# Flag is used to check if prime
		for prime in primes:
			if num % prime == 0:			# If num divided by prime == 1, then prime is a factor of num and num is not a prime
				flag = False			# Flag is False because we can see 
				break
			if prime > math.sqrt(num) + 1: 		# If the prime gets sufficiently close to num, it can no longer divide num
				break

		# If flag is true we add the number to primes
		if flag:
			primes.append(num)

	return primes


def prime_factors(num):
	"""
	Finds the smallest primes that divide a number.
	For unique primes, turn the list into a set.
	Example: 	120 / 2 = 60
				60 / 2 = 30
				30 / 2 = 15
				15 / 3 = 5
				5 is prime.
				returns [2, 2, 2, 3, 5]
	"""
	primes = find_primes(int(math.sqrt(num + 1))) # Finds all primes that might be a factor
	factors = []

	for prime in primes:

		if prime >= num + 1: 	# If prime is bigger than the number, it is no longer divisible
			break				# So for long lists, quitting earlier is faster

		while num % prime == 0:
			num = num // prime 	# Divides the number by the prime, so that we can see how many times
			factors.append(prime) # a number is divisible by a prime

	return factors


def factorial(num):
	"""
	The factorial of a number.
	On average barely quickar than product(range(1, num))
	"""
	# Factorial of 0 equals 1
	if num == 0:
		return 1

	#if not, it is the product from 1...num
	product = 1
	for integer in range(1, num + 1):
		product *= integer
	return product


def zeros(dimensions):
	"""
	Attempted clone of numpy zeros.
	Not as quick, but might be useful if long lists are desired
	and numpy not available.
	"""
	x = y = None
	try:
		y, x = dimensions 	# If it cannot unpack it as tuple, it will fail
	except TypeError:
		x = dimensions		# If it fails, it will standard to 1 row
		y = 1
	
	zeros = []
	if y == 1:
		zeros += [0]*x
	else:
		for row in range(y): 	# Makes rows with columns of 0
			zeros.append([0]*x)
	
	return zeros


def louville_distance(precision):
	"""
	Finds the distance between in zeroes between 2 '1's in the 
	louville number. 
	Will return distances, so if you sum earlier numbers together
	you get the index at which there would have been a '1'
	"""
	precision += 1 		# To get far enouh
	distances = []

	for index in range(1, precision):
		try:
			distances.append(factorial(index) - factorial(index - 1))
		except IndexError:
			break

	distances[0] = 1 # Because of the way the list is structured
	return distances


def point_distance(point1, point2):
	"""
	Returns the distance between two points given as tuples
	"""
	distance =  math.sqrt( ((point1[0]-point2[0])**2) + ((point1[1]-point2[1])**2) )
	return distance

def armstrong_number(number):
	"""
	Check if number is Armstrong number
	"""
	calc = number
	sum = 0
	while calc > 0:
		dig = calc % 10
		sum += dig ** 3
		calc //= 10
	if number == sum:
		return True
	else:
		return False