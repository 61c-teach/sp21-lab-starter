#include <stdio.h>

/* Only change any of these 4 values */
#define V0 0
#define V1 -1
#define V2 0
#define V3 0

//Do not modify anything below this line!
int main(void) {
    int a;
    char *s;

    /* This is a print statement. Notice the little 'f' at the end!
     * It might be worthwhile to look up how printf works for your future
     * debugging needs... */
    printf("Berkeley eccentrics:\n");
    /* This line works the same way as printf; more on this in exercise 4*/
    fprintf(stdout,"====================\n");

    /* for loop */
    for (a = 0; a < V0; a++)
    {
        printf("Happy ");
    }
    printf("\n");

    /* switch statement */
    switch (V1)
    {
    case 0:
        printf("Yoshua\n");
    case 1:
        printf("Triangle Man\n");
        break;
    case 2:
        printf("Chinese Erhu Guy\n");
    case 3:
    case 4:
        printf("Yoshua\n");
        break;
    case 5:
        printf("Dr. Jokemon\n");
        break;
    case 6:
        printf("Hat Lady\n");
    default:
        printf("I don't know these people!\n");
    }

    /* ternary operator */
    s = (V3 == 3) ? "Go" : "Boo";

    /* if statement */
    if (V2) {
        printf("%s BEARS!\n", s);
    } else {
        printf("%s CARDINAL!\n", s);
    }

    return 0;
}
