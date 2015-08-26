#include <stdio.h>
#include <stdlib.h>
// Function to push to the stack, returns new SP
void push(int val, int** stack_ptr)
{
  printf("Pushing %d to stack with stack ptr val %p \n", val, *stack_ptr);
  *stack_ptr+=1;
  **stack_ptr = val;
}
void increment_pointer(int** stack_ptr)
{
  printf("BEFORE: %p", *stack_ptr);
  *stack_ptr+=1;
  printf("AFTER: %p", *stack_ptr); 
}
// Function to print top stack value
void peek(int* stack_ptr)
{
  printf("The value at the top of the stack is %d", *stack_ptr);
  return;
}
// Function to push the topmost value off the stack, returns new SP
int *pop(int* stack_ptr, int* stack_ptr_cpy)
{
  if (stack_ptr == stack_ptr_cpy) 
    {
      printf("Invalid operation! Cannot pop anything off empty stack!");
      return;
    }
  else
    {
      printf("Value popped: %d", *stack_ptr);
    }
  return stack_ptr;
}
// Simple C program to create a stack of integers
int main(int argc, char *argv[])
{
  int arg_iterator;
  int int_arg[100];
  int *stack_ptr;
  // Allocate memory for stack
  stack_ptr = (int *)malloc(sizeof(int)*argc+1);
  int *stack_ptr_cpy = stack_ptr;
  for (arg_iterator = 1; arg_iterator<argc;arg_iterator++)
    {
      // Convert args to ints:
      int_arg[arg_iterator] = strtol(argv[arg_iterator], NULL,10);
      printf("Value in int: %d \n", int_arg[arg_iterator]);
      //      push(int_arg[arg_iterator],&stack_ptr);
      increment_pointer(&stack_ptr);
      printf("AFTER FOR REAL %p",stack_ptr);
    }
  //  printf("Final value of stack: %d \n", *stack_ptr);
  free(stack_ptr_cpy);
  return 0;
}
