import random
from datetime import datetime


def main():
    start = datetime.now()
    total = 0
    shuffle_counts = {}
    my_arr = ['A', 'B', 'C']
    for x in range(100000000):
        shuffled = str(shuffle(my_arr))
        if shuffle_counts.get(shuffled) is None:
            shuffle_counts[shuffled] = 1
        else:
            shuffle_counts[shuffled] += 1
        total += 1

    print('number of combinations: %s' % len(shuffle_counts))
    for k, v in shuffle_counts.items():
        print('pattern: %s, count: %s, relative frequency: %s' % (k, v, v / total))

    end = datetime.now() - start
    print('total time: %s ' % str(end))

def shuffle(arr):
    for x in range(len(arr) - 1):
        swap_ind = random.randint(x, len(arr) - 1)
        a_swap = arr[x]
        b_swap = arr[swap_ind]
        arr[x] = b_swap
        arr[swap_ind] = a_swap
    return arr


if __name__ == '__main__':
    main()
