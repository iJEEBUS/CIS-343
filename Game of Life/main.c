#include <stdio.h>
#include <stdlib.h>

int allocateMemory(int r, int c);
void printBoard(int *board, int rows, int columns);
int promptUser();
int promptForRows();
int promptForCols();


int main(int argc, char const *argv[])
{
	int r, c, response, board;

	if (argc == 3)
    {
        r = atoi(argv[1]), c = atoi(argv[2]);
    }
	else
    {
        response = promptUser();

        switch (response) {

            case 1:
                board = allocateMemory(10, 10);
                printBoard(&board, 10, 10);
                break;
            case 2:
                r = promptForRows();
                c = promptForCols();
                board = allocateMemory(r, c);
                printBoard(&board, r, c);
                break;
            case 3:
                printf("This will load a file.");
                break;
            case 4:
                printf("This will do something.");
                break;
            case 5:
                return 0;
        }
    }
	return 0;
}

/**
 * Allocates memory in the heap that is going to be used as the
 * board for the Game of Life.
 *
 * @param r - int - number of rows
 * @param c - int - number of columns
 * @return - int - allocated memory in the heap
 */
int allocateMemory(int r, int c)
{
	// Allocate memory here
	int *arr[r], i, j, count;

	for (i = 0; i < r; i++)
		arr[i] = (int *)malloc(c * sizeof(int));

	count = 0;
	for (i = 0; i < r; i++)
		for (j = 0; j < c; j++)
			arr[i][j] = ++count;
	return **arr;
}

/**
 * Display the board in the console.
 *
 * @param board - int - the board to show
 * @param rows - int - how many rows the board has
 * @param columns - int - how many columns the board has
 */
void printBoard(int *board, int rows, int columns)
{
	int count = 0;
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < columns; j++)
			printf("\x1B[34m\u25A0 ");
		printf("\n");
	}

}

/**
 * Ask and return the user what they want to do with the program.
 * This will only be ran if command line parameters are
 * not passed with the executable filename.
 *
 * @return
 */
int promptUser()
{
	//char valid_inputs[6] = {1,2,3,4,5};
    int response;
	printf("Welcome to the Infamous Game of Life!\n");
	printf("\n");
	printf("\n");
	printf("What would you wish to do today?\n");
	printf("(1) Play with generic input (10 x 10)\n");
	printf("(2) Play with specified input (Rows x Columns)\n");
	printf("(3) Load a previously saved board\n");
	printf("(4)\n");
	printf("(5)Exit\n");
	scanf("%d", &response);
    return response;
}

/**
 * Ask the user how many rows they want the board to be.
 * @return
 */
int promptForRows()
{
    int rows;
    printf("How many rows would you like? \n");
    scanf("%d", &rows);
    return  rows;
}

/**
 * Ask the user how many columns they want the board to be.
 * @return
 */
int promptForCols()
{
    int cols;
    printf("How many columns would you like? \n");
    scanf("%d", &cols);
    return  cols;

}