/* Code to reverse a string, but not the words in a string
Example usage: ./exe "This is a cat."
Example output: "Cat a is this."
*/
// Include files
#include <stdio.h>
#include <string.h>
// I guess I have to initalize my pointers?
#include <malloc.h>

// Define constants
#define EOL '\0'
#define DELIMITER ' '

// Function which takes an input array and splits it by the delimiter
void split(char *in_array, char ***final_buffer, char delimiter)
{
  int iteration=0;
  char **emulator = *final_buffer;
  // Iterate through input array, until null
  while (*in_array != EOL)
    {
      // skip over leading delimiters eg "  space" == "space"
      while (*in_array == delimiter) in_array++;
      // Pointer to beginning of array (starting at characters)
      char *start_ptr = in_array;
      int counter = 0;
      // Iterate through individual words
      while (*in_array != EOL && *in_array != delimiter)
	{
	  in_array++;
	  counter++;	  
	}
      // Skip delimiters, and force nulls where delimiter is
      if (*in_array == delimiter)
	{
	  // force EOL at end of string
	  *in_array = EOL;
	  in_array++;
	  // Skip over delimiters
	  while (*in_array == delimiter) in_array++;
	}
      strcpy(emulator[iteration],start_ptr);
      iteration++;
    }
 return;
}

int main(int argc, char *argv[])
{
  // Parse for input arguments
  if (argc != 2)
    {
      printf("It seems like you didn't enter an input correctly. Try doing that.\n");
      printf("Example usage: ./exe \"This is a cat.\"\n");
      return;
    }
  // Get string pointer
  char *inStrPtr = argv[1];
  int inStrLength = 0, maxWordLength = 0, tempMaxCount = 0, wordCount = 0;

  // Iterate over string, getting string info (largest word, size of string, number of words)
  while (*inStrPtr != EOL) 
    { 
      // If we reached the delimiter, it's the end of the word
      if (*inStrPtr == DELIMITER && *(inStrPtr-1) != DELIMITER) 
	{
	  // increment word counter
	  wordCount++;
	  // Check to see if this word is the biggest word
	  if (tempMaxCount > maxWordLength)
	    {
	      maxWordLength = tempMaxCount;
	    } 
	  // clear max counter
	  tempMaxCount = 0;
	}
      // Increment word max count, length counter, and pointer
      if (*inStrPtr != DELIMITER) tempMaxCount++;
      inStrPtr++;
      inStrLength++;
    }
  // deal with the last word in the string
  wordCount++;
  // Check to see if this word is the biggest word
  if (tempMaxCount > maxWordLength)
    {
      maxWordLength = tempMaxCount;
    } 
  printf("Final length %d \n", inStrLength);
  printf("Final max word length %d \n", maxWordLength);
  printf("Final word count %d \n", wordCount);
  // Implement simplest algorithm - Split string by word
  // Create split array - each element in array points to string
  char **split_string;
  int memoryAllocator;
  split_string = malloc(sizeof(*split_string));
  // Allocate memory like some sort of punk
  for (memoryAllocator = 0; memoryAllocator < wordCount; memoryAllocator++)
    {
      split_string[memoryAllocator] = malloc(maxWordLength*sizeof(**split_string)+1);
    }

  // Call split function, returns values in to split_string
  split(argv[1],&split_string, DELIMITER);
  for (memoryAllocator = 0; memoryAllocator < wordCount; memoryAllocator++)
    printf("%s \n", split_string[memoryAllocator]);
  return 0;
}
