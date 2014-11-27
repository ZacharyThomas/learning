import math
import sys
# Take value required (diff), and calculate weights and placements
def difference(diff,weight_list,outdict):
    while diff != 0:
        # Right scale heavier than left scale by 1
        if diff == 1:
            outdict[1] = "L"
            weight_list.pop(0)
            diff -= 1
            continue
        elif diff == -1:
            outdict[1] = "R"
            weight_list.pop(0)
            diff += 1
            continue
        next_val = weight_list.pop()
        # Pop off greatest value and subtract it
        if diff < 0: 
            diff += next_val
            outdict[next_val] = "R"
            continue
        diff = diff - next_val
        if (diff < -3): 
            diff += next_val
            continue
        outdict[next_val] = "L"
    return outdict

def difference_inverse(diff,weight_list,outdict):
    while diff != 0:
        # Left scale heavier than right scale by 1
        if diff == 1 :
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
            outdict[next_val] = "L"
            scales[1] += next_val
            continue
        diff = diff - next_val
        if (diff < -3): 
            diff += next_val
            continue
        outdict[next_val] = "R"
        scales[1] += next_val

    return outdict
# Left array = scale with X on it
# Right array = scale with nothing on it
def answer(x):
    i = 0
    outlist = []
    outdict = {}
    weight_list = [pow(3,i) for i in range(0,int(math.ceil(math.log10(x)/math.log10(3)))+1)]
    temp_weight_list = [pow(3,i) for i in range(0,int(math.ceil(math.log10(x)/math.log10(3)))+1)]
    for iterator in weight_list:
        outdict[iterator] = "-"
    max_weight = weight_list.pop()
    # Put input on left scale
    if x > sum(weight_list):
        diff = max_weight - x
        # Give unweighted scale largest pow of three, build up left scale
        outdict[max_weight] = "R"
        out_dict = difference(diff,weight_list,outdict)
    elif x < sum(weight_list):
        # Keep scales the same, build up right scale
        diff = x
        outdict = {}
        for iterator in weight_list:
            outdict[iterator] = "-"
        out_dict = difference_inverse(diff,weight_list,outdict)
    else: 
        for x in weight_list: 
            outlist.append("R")
    for vals in weight_list:
        if vals in outdict.keys(): outlist.append(outdict[vals])
    return outlist        
