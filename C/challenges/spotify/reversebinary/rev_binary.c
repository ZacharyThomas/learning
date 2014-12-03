/*
Spotify Challenge ProblemID: Reversebinary
Program designed to take an input number in decimal, and return the value of the number in decimal if its binary representation were reversed
Input: Single integer
Output: Decimal representation of its reversed binary 
Usage: ./Executable [Integer]
Written by Zack Smith on 12/02/14
 */
// System includes
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>
#include <string.h>
// Function which converts a base 10 number to a base 2 number (holds in list)
int base10to2(long intVal)
{
  // Allocate memory for binary list
  int maxLen = (int) floor(log2(intVal)) + 1;
  // Use a character array because it takes up less space
  char *binaryList = malloc( maxLen * sizeof(char));
  // Initialize to zero
  memset(binaryList, 0, maxLen * sizeof(char));
  int iterVal = 0;
  // Starting from the left most digit, calculate whether it's a 1 or 0, write it in backwards
  while (intVal != 0 && iterVal < maxLen)
    {
     
      // Figure out which digit we're on 
      int tempVal = maxLen-iterVal;
      int currentPow = pow(2,tempVal-1);
      if (intVal >= currentPow) 
	{
	  // Write string in backwards - first iteration tempVal = last index
	  binaryList[tempVal] = 1;
	  intVal -= currentPow;
	}
      iterVal++;
    }
  int resultVal = base2to10(binaryList, maxLen);
  return resultVal;
}
// Function which takes binary as a char list and converts it to decimal 
int base2to10(char *binaryList, int maxLen)
{
  // Grab each char, and add to sum if it's 1
  int resultVal = 0;
  int iterVal;
  for (iterVal = 1; iterVal <= maxLen; iterVal++) 
    {
      if (binaryList[iterVal] == 1) resultVal += pow(2,maxLen-iterVal);
    }
  return resultVal;
}
// Error handling function
void usage()
{
      printf("Invalid usage! Please enter a single, positive, base 10 integer as an argument. \n");
      printf("USAGE: ./Executable [0-9]{1,}\n");
      exit(0);
}
// Main function to get input arguments & call other functions
int main(int argc, char **argv)
{
  // Handle input arguments
  if (argc != 2)
    {
      usage();
    }
  // Grab input (it's a string!)
  char *inString = argv[1];
  // Check to see instring is only an integer (every digit is between 0 and 9)
  while (*inString != '\0')
    {
      if (*inString < '0' || *inString > '9') usage();
      inString++;
    }
  // Convert to long now that we're sure it's an integer
  long intVal = strtol(argv[1], NULL, 10);
  // Convert decimal to base 2
  int resultVal = base10to2(intVal);
  printf("%d \n", resultVal);
  return 0;
}
