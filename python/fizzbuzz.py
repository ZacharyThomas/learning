def main():
	for x in range(0,101):
		if ( x % 3 == 0): print "Fizz",
		if ( x % 5 == 0): print "Buzz",
		if ( x % 3 != 0 and x % 5 != 0): print x,
		print ""





if __name__ == '__main__':
	main()
