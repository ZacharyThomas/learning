#include <stdio.h>

#define EOL '\0'
int main(int argc, char* argv[])
{
if (argc != 2)
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
