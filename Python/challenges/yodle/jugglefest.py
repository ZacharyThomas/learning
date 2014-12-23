'''
Python Solution to Juggle Fest Coding Challenge by Yodle
Input: Formatted text file containing juggler/circuit information
Output: Formatted text file containing juggler assignments
For more information see http://www.yodlecareers.com/puzzles/jugglefest.html
Created by Zack Smith 12-22-14
'''
# Necessary imports
import sys
import string
# Class definitions
class Circuit:
    max_competitors = 0
    # Init Method
    def __init__(self,name,H,E,P):
        self.H = int(H)
        self.E = int(E)
        self.P = int(P)
        self.name = name
        self.competitors = []
        self.comp_scores = []
    # Debugging method
    def print_circuit(self):
        print "Circuit: " + self.name #+ " SKILLS: " + str(self.H) + ' ' + str(self.E) + ' ' + str(self.P) 
        print "Competitors: " 
        for jugs in self.competitors: print jugs.name
        print "Scores: ", self.comp_scores

# Juggler class
class Jugglers:
    bad_counter = 0
    # Init Method
    def __init__(self,name,H,E,P,preferences):
        self.H = int(H)
        self.E = int(E)
        self.P = int(P)
        self.name = name
        self.preferences = preferences
        self.scores = [0] * len(preferences)
        self.preference_level = 0

    # Debugging method
    def print_juggler(self):
        print "JUGGLER: " + self.name #+ " SKILLS: " + str(self.H) + ' ' + str(self.E) + ' ' + str(self.P)
        #print "PREFERENCES: ", self.preferences
        print "SCORES: ", self.scores

    # Method to add a juggler to a circuit
    def assign_juggler(self,circuit_list):
        # Find optimal circuit
        try:
            optimal_circuit = circuit_list[int(self.preferences[self.preference_level][1:])]
        except IndexError:
            self.preference_level -= 1
            optimal_circuit = circuit_list[int(self.preferences[self.preference_level][1:])]
            Jugglers.bad_counter += 1
            return (True, None)

        # If maxed on competitors
        if len(optimal_circuit.competitors) == Circuit.max_competitors:
            # Check to see that our calculated score is higher than the min
            min_ind = min(xrange(len(optimal_circuit.comp_scores)),key=optimal_circuit.comp_scores.__getitem__)
            # Less than min score, so go to next circuit
            if self.scores[self.preference_level] < optimal_circuit.comp_scores[min_ind]:
                self.preference_level += 1
                return (False,None)

            # If the scores are equal, the lower preference level takes priority
            elif self.scores[self.preference_level] == optimal_circuit.comp_scores[min_ind]:
                # Current comp has higher priority (lower preference level), so assign it to this circuit
                if self.preference_level < optimal_circuit.competitors[min_ind].preference_level:
                    temp_juggler = optimal_circuit.competitors[min_ind]
                    optimal_circuit.competitors[min_ind] = self
                    optimal_circuit.comp_scores[min_ind] = self.scores[self.preference_level]
                    return (True, temp_juggler)
                # Else keep iterating
                else:
                    self.preference_level += 1
                    return (False, None)
            # pop off min juggler and its score, put new optimal juggler in
            else:
                temp_juggler = optimal_circuit.competitors[min_ind]
                optimal_circuit.competitors[min_ind] = self
                optimal_circuit.comp_scores[min_ind] = self.scores[self.preference_level]
                #while (res == False ): res = temp_juggler.assign_juggler(circuit_list)
                return (True, temp_juggler)
        # Not maxed, so just append
        else:
            optimal_circuit.competitors.append(self)
            optimal_circuit.comp_scores.append(self.scores[self.preference_level])
            return (True,None)

def read_file(filename):
    '''
    Read text file of filename;
    return lines in file
    '''
    try:
        with open(filename, 'r') as f:
            for line in f:
                if len(line.split()) > 0:
                    yield line.split()
    except IOError:
        print "Error opening or reading file: ", filename
        usage()

def build_competition_lists(lines):
    ''' 
    Parse each line for juggler/circuit info
    create class instance and append to list
    '''
    circuit_list = []
    juggler_list = []
    for line in lines:
        if line[0] == 'C':
            temp_circuit = Circuit(line[1],line[2][2:],line[3][2:],line[4][2:])
            circuit_list.append(temp_circuit)
            #temp_circuit.print_circuit()
        elif line[0] == 'J':
            temp_juggler = Jugglers(line[1],line[2][2:],line[3][2:],line[4][2:],line[5].split(','))
            juggler_list.append(temp_juggler)
            #temp_juggler.print_juggler()

    return (circuit_list,juggler_list)

def compute_scores(circuit_list,jugglers_list):
    '''
    Calculate scores for jugglers preference circuits
    store in each class instance
    '''
    # Iterate over each juggler
    for juggler in jugglers_list:
        # Compute dot product on each element in juggler's preference
        for index, circuit in enumerate(juggler.preferences):
            circuit_index = int(circuit[1:])
            circuit_obj = circuit_list[circuit_index]
            # Compute dot product
            juggler.scores[index] = circuit_obj.H * juggler.H + circuit_obj.E * juggler.E + circuit_obj.P * juggler.P


def assign_competitors(circuit_list,juggler_list):
    '''
    Assigns jugglers to circuits first on preference
    then on score
    '''
    # Calculate number of participants per circuit
    num_jugglers = len(juggler_list)
    num_circuits = len(circuit_list)
    max_participants = num_jugglers/num_circuits
    Circuit.max_competitors = max_participants
    res = False
    # Iterate over juggler list, assigning each to a circuit
    for jugglers in juggler_list:
        res = False
        while res == False:
            (res,temp_jug) = jugglers.assign_juggler(circuit_list)
            # Re-iterate if we knocked a juggler out 
            if (temp_jug != None): 
                res = False
                jugglers = temp_jug

def write_out(circuit_list):
    '''
    Format circuit competitors in to desired format
    CircuitName + JugglerName + JugglerPreferences:JugglerScore
    '''
    with open("outfile.txt", 'w') as f:
        for cl in circuit_list:
            outString = cl.name + ' '
            for competitors in cl.competitors:
                outString += competitors.name + ' '
                for index,prefs in enumerate(competitors.preferences):
                    outString += prefs + ':'
                    outString += str(competitors.scores[index])
                    outString += ' '
            f.write(outString + '\n')


def usage():
    '''
    Error found while executing, exit program
    '''
    print "USAGE: python jugglefest.py /path/to/text/file.txt"
    sys.exit()

def main():
    # Read in file
    if len(sys.argv) != 2: 
        usage()
    in_file = sys.argv[1]
    lines = read_file(in_file)
    # Parse file
    circuit_list,juggler_list = build_competition_lists(lines)
    # Apply dot products
    compute_scores(circuit_list,juggler_list)
    # Apply joining logic
    assign_competitors(circuit_list,juggler_list)
    # Generate out file
    write_out(circuit_list)
    print Jugglers.bad_counter

# Boiler plate code
if __name__ == '__main__':
    main()
