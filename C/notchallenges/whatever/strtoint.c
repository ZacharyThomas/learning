#include <stdio.h>
#include <math.h>
// Function to convert string to integer 
int main(int argc, char **argv)
{
  int counter = 0;
  char *str_ptr;
  int result = 0;
  // Check inputs
  if (argc !=2)
    {
      printf("Unacceptable inputs\n");
      printf("USAGE: *.exe input_num\n");
      return;
    }
  printf("Input string to convert: %s \n", argv[1]);
  // Iterate over string until you get to null pointer
  str_ptr = argv[1];
  while(*str_ptr != '\0') str_ptr++;
  while(str_ptr != argv[1])
    {
      str_ptr--;
      result += ((int)*str_ptr-48)*pow(10.0,counter);
      printf("Result %d Iteration %d \n", result, counter);
      counter++;     

    }
  return 0;
}
