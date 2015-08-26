#include <stdio.h>

#define EOL '\0'
int main(int argc, char* argv[])
{
<<<<<<< HEAD
if (argc != 2)
=======
if (argc < 2)
>>>>>>> 9d3f1d39c1e1a7f9fe7a4bff74451ec788273118
{
	printf("Usage: rev.c stringname\n");
	return 0;
}

else
{
	char* str_ptr = argv[1];
	while (*str_ptr != EOL) str_ptr++;
	while (*str_ptr != argv[1][0])
	{
	printf("%c", *str_ptr);
	str_ptr--;
	}
	printf("\n");
	return 0;
}
}
