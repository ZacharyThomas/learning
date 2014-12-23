def answer(numbers):
    # Foobar challenge #1: A pirate walks in to a bar
    count = 0
    number_dict = {}
    # Initialize curr_num
    curr_num = numbers[0]
    # Iterate until it returns. If it doesn't return, the array wasn't entered properly.
    while 1:
        # Increment counter while it hasn't looped back
        count += 1
        # If it ends in a zero, it means the total loop was equal to the times counted plus the initial
        if (numbers[curr_num] == 0): return count+1
        # If this number has already been assigned, it means we've already been to this spot! (Loop completed)
        if numbers[curr_num] in number_dict.keys():
            # Return the counter var associated with the end subtracted from the counter var associated with the beginning
            return count+1 - number_dict[numbers[curr_num]]
        # Otherwise, let's add the number to our dict, with counter var info
        else:
            number_dict[curr_num] = count
        # Grab next counter var and reiterate
        curr_num = numbers[curr_num]
