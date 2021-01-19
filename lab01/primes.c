#include <stdio.h>
#define MAXVAL 10000
//Returns 1 if the input is a prime number, and 0 otherwise.
int isPrime(int n)
{
	if(n%2 == 0) return 0;
	for(int i = 3; i < n; i+=2)
	{
		if(n%i == 0) return 0;
	}
	return 1;
}

int main(int argc, char *argv[]) {
    int i = 2;
	for(;i<MAXVAL*100;i++)
	{
		if(isPrime(i))
		{
			fprintf(stdout, "%d", i);
		}
	}
}