#include <stdio.h>
#include <stdlib.h>
// Recursive function to calculate the factorial of a 
int factorial(int n)
{
  if (n==1)
    {
      return 1;
    }
  else
    {
      return n*factorial(n-1);
    }

}
// Main function to calculate the factorial of input n in argv[1]
int main(int argc, char **argv)
{
  char *ptr;
  int res;
	if (argc <= 1 || argc > 2)
	{
	printf("Invalid number of arguments.\n");
	printf("Usage: file.exe intval \n");
	return;
	}
	else 
	{
	// Convert input to integer
	 int int_input = strtol(argv[1],&ptr,10);
	 res = factorial(int_input);
	}
	printf("Final value: %d \n", res);
}
