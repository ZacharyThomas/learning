#include <stdio.h>
#define EOL '\0'
int main(int argc, char *argv[])
{
char *arg_1 = argv[1];
while (*arg_1 != EOL) arg_1++;
while (*arg_1 != argv[1][0])
{
printf("%c", *arg_1);
arg_1--;
}
printf("%c\n",*arg_1);
}
