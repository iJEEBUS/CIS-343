#include <stdio.h>
#include <stdlib.h>
#include "file_utilities.h"

char* allocateMemory(int r, int c);
void printBoard(char *board, int rows, int columns);
int promptUser();
int promptForRows();
int promptForCols();
void promptForFile(char **file);




int main(int argc, char const *argv[])
{
	int r, c, response;
    char *file;
    char *temp_file[100];
    char *buffer;
     /* Boards for the game */
    char *og_board, *temp_board, final_board;
    /* Size of buffer. Always larger than needed by +2 */
    size_t buffer_length;

    /* Read the file  */
    buffer_length = read_file(file, &buffer);
    og_board = buffer;

	if (argc == 3)
    {
        r = atoi(argv[1]), c = atoi(argv[2]);
        og_board = allocateMemory(r, c);
        printBoard(og_board, r, c);
    }
	else
    {
        response = promptUser();

        switch (response) {

            case 1:
                og_board = allocateMemory(10, 10);
                printBoard(og_board, 10, 10);
                break;
            case 2:
                r = promptForRows();
                c = promptForCols();
                og_board = allocateMemory(r, c);
                printBoard(og_board, r, c);
                break;
            case 3:
                file = "./save_data.txt";
                
                /* Read the file  */
                buffer_length = read_file(file, &buffer);

                // need to get the size of the board
                og_board = buffer;
                createBoardFromFile(og_board, &temp_board, buffer_length);
                r = getNumRows(og_board, buffer_length);
                c = getNumCols(og_board, buffer_length);
                printBoard(temp_board, r, c);
                break;
            case 4:
                printf("This will do something.");
                break;
            case 5:
                exit(EXIT_SUCCESS);
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
 * @return - char* - allocated memory in the heap
 */
char* allocateMemory(int r, int c)
{
    // Allocate memory here
    char *arr[r], i, j, count;

    for (i = 0; i < r; i++)
        arr[i] = (char *)malloc(c * sizeof(char));

    count = 0;
    for (i = 0; i < r; i++)
        for (j = 0; j < c; j++)
            arr[i][j] = ++count;
    return *arr;
}

/**
 * Display the board in the console.
 *
 * @param board - int - the board to show
 * @param rows - int - how many rows the board has
 * @param columns - int - how many columns the board has
 */
void printBoard(char *board, int rows, int columns)
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
	printf("(4) How many interations would you like to view?\n");
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