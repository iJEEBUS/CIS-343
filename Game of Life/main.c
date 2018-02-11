#include <stdio.h>
#include <stdlib.h>

char* allocateMemory(int r, int c);
void printBoard(char *board, int rows, int columns);
int promptUser();
int promptForRows();
int promptForCols();
int read_file( char* filename, char **buffer );
void createBoardFromFile( char* board, char **temp_board, size_t buffer_len );




int main(int argc, char const *argv[])
{
	int r, c, response;
    char* file;
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
                og_board = buffer;
                createBoardFromFile(og_board, &temp_board, buffer_length);

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
 * Reads in save data into the heap and uses it to
 *  create the board for the Game of Life.
 *
 * @param r - int - number of rows
 * @param c - int - number of columns
 * @return - char* - allocated memory in the heap
 */
int read_file( char* filename, char **buffer )
{
    /* Pointer to file */
    FILE *fp;
    size_t new_length;
    
    /* File contents */
    fp = fopen(filename, "rb");
    if (fp != NULL) {

        /* Go to the end of the file */
        if (fseek(fp, 0L, SEEK_END) == 0) {

            /* Get the size of the file */
            long buffer_size = ftell(fp);
            
            if (buffer_size == -1) 
                return -1;

            /* Make buffer that size */
            *buffer = malloc(sizeof(char) * (buffer_size));

            /* Go back to the start of the file */
            if (fseek(fp, 0L, SEEK_SET) != 0)
                return -1;

            /* Read file into the memory */
            new_length = fread(*buffer, sizeof(char), buffer_size, fp);

            if (ferror(fp) != 0)
                fputs("Error reading file ", stderr);
            // else
            //  *buffer[new_length++] = '\0';
        }
        fclose(fp);
    }

    return new_length;
}

/**
 * This prints out the board that was read into the game via the
 * read_file function.
 *
 * @param - board - int - original board
 * @param - **temp_board - int - board to write to
 * @return - buffer_len - allocated memory in the heap
 */
void createBoardFromFile( char* board, char **temp_board, size_t buffer_len )
{
    int rows = 0, cols = 0;
    
    for (int i = 0; i < buffer_len; ++i) 
    {
        if (board[i] == ';') {
            rows++;
        }
    }

    cols = (buffer_len - rows ) / rows;

    *temp_board = allocateMemory(rows, cols);
    printBoard(*temp_board, rows, cols);
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