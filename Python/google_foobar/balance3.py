''' 
Problem Name: Peculiar Balance
Objective: You have two scales which must be balanced. 
The left scale has an input weight of x, and weights of powers of three must be used to balance the two scales.
Output: List containing only 'L', 'R', and '-', indicating the position of a particular weight
Written by Zack Smith 11/26/14
'''
import math
import sys
# Take value required (diff), and calculate weights and placements
def difference(diff,weight_list,outdict,scales):
    while diff != 0:
        print "LEFT SCALE, RIGHT SCALE"
        print scales[0], scales[1]
        print diff
        # Right scale heavier than left scale by 1
        if diff == 1 and scales[1] > scales[0]:
            outdict[1] = "L"
            weight_list.pop(0)
            diff -= 1
            continue
        elif diff == -1:
            outdict[1] = "R"
            weight_list.pop(0)
            diff += 1
            continue
        print "-----BEFORE-----"
        print diff
        print outdict.items()
        next_val = weight_list.pop()
        # Pop off greatest value and subtract it
        if diff < 0: 
            diff += next_val
            if (diff > sum(weight_list)): 
                diff -= next_val
                continue
            outdict[next_val] = "R"
            scales[1] += next_val
            continue
        diff = diff - next_val
        if (diff < -1*sum(weight_list)): 
            diff += next_val
            continue
        outdict[next_val] = "L"
        scales[0] += next_val

    print outdict.items()
    return outdict

def difference_inverse(diff,weight_list,outdict,scales):
    while diff != 0:
        print "LEFT SCALE, RIGHT SCALE"
        print scales[0], scales[1]
        print diff
        print outdict.items()
        # Left scale heavier than right scale by 1
        if diff == 1 and scales[0] > scales[1]:
            outdict[1] = "R"
            weight_list.pop(0)
            diff -= 1
            continue
        elif diff == -1:
            outdict[1] = "L"
            weight_list.pop(0)
            diff += 1
            continue

        next_val = weight_list.pop()
        # Pop off greatest value and subtract it
        if diff < 0: 
            diff += next_val
            print "LESS THAN ZERO"
            print weight_list
            if (diff > sum(weight_list)): 
                diff -= next_val
                continue
            outdict[next_val] = "L"
            scales[0] += next_val
            continue
        diff = diff - next_val
        if (diff < -1*sum(weight_list)): 
            diff += next_val
            continue
        outdict[next_val] = "R"
        scales[1] += next_val

    print outdict.items()
    return outdict
# Left array = scale with X on it
# Right array = scale with nothing on it
def answer(x):
    print "Input %d" % x
    i = 0
    outlist = []
    outdict = {}
    weight_list = [pow(3,i) for i in range(0,int(math.ceil(math.log10(x)/math.log10(3)))+1)]
    temp_weight_list = [pow(3,i) for i in range(0,int(math.ceil(math.log10(x)/math.log10(3)))+1)]
    for iterator in weight_list:
        outdict[iterator] = "-"
    max_weight = weight_list.pop()
    print max_weight
    print weight_list    
    print outdict.items()
    scales = [0,0]
    # Put input on left scale
    scales[0] += x
    if x > sum(weight_list):
        diff = max_weight - x
        # Give unweighted scale largest pow of three, build up left scale
        outdict[max_weight] = "R"
        scales[1] += max_weight
        outdict = difference(diff,weight_list,outdict,scales)
    elif x < sum(weight_list):
        # Keep scales the same, build up right scale
        diff = x
        outdict = {}
        for iterator in weight_list:
            outdict[iterator] = "-"
        outdict = difference_inverse(diff,weight_list,outdict,scales)
    else: 
        for x in weight_list: 
            outlist.append("R")
    print "***********************END*********************"
    print outdict.items()
    print temp_weight_list
    for vals in temp_weight_list:
        if vals in outdict.keys(): outlist.append(outdict[vals])
    print outlist

def main():
    answer(int(sys.argv[1]))

if __name__ == '__main__':
    main()
