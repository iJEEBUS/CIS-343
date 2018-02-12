#include <stdio.h>
#include <stdlib.h>
#include "file_utilities.h"

void createBoard(int r, int c);
void printBoard(int rows, int columns);
int promptUser();
int update(int n);
void freeBoard();
int saveBoard();
void loadBoard();

int r, c, response, generations = 0;
char userIn[10];
char file[30];
char *buffer;

/* Board for the game */
char **og_board, **temp_board;

/* Size of buffer */
int buffer_length;
int rows = 0;
int cols = 0;

int main(int argc, char const *argv[])
{
    while (1) {
        switch(promptUser()) {
            case 1:
                update(1);
                break;
            case 2:
                while (generations < 10) {
                    update(1);
                    generations++;
                }
                break;
            case 3:
                printf("Name of file to load: \n");
                fgets(file, 31, stdin);
                loadBoard();
                break;
            case 5: // save board to a file
                printf("Name of file to save: \n");
                fgets(file, 31, stdin);
                saveBoard();
                break;
            case 6:
                exit(EXIT_SUCCESS);

        }
    }
    return 0;
}

int update(int n) {
    int g = 0;
    int i = 0;
    int j = 0;
    if (og_board == NULL) {
        printf("There's no world to generate.\n");
        printf("\n");
        return 1;
    }
    /* For number of generations. */
    for (g; g < n; g++) {
        /* Clear temp_board */
        for (i = 0; i < rows; i++) {
            for (j = 0; j < cols; j++) {
                temp_board[i][j] = '0';
            }
        }

        int r, c;
        int rcap, ccap;
        int neighbors;
        /* For each cell, count the number of live cells around it. */
        for (i = 0; i < rows; i++) {
            for (j = 0; j < cols; j++) {
                neighbors = 0;

                /* Create 3x3 grid bounds. */
                r = i - 1; // top bound
                rcap = i + 1; // bottom bound
                c = j - 1; // left bound
                ccap = j + 1; // right bound

                /* Determine if a row or column must be cut
                 * based on the position of the element in question. */
                if (i == 0) {
                    r++;
                } else if (i == (rows - 1)) { // account for +1 error
                    rcap--;
                }
                if (j == 0) {
                    c++;
                } else if (j == (cols - 1)) {
                    ccap--;
                }

                for (r; r <= rcap; r++) {
                    /* c's orientation must be recalculated relative to
                     * the game board after incrementation. */
                    for (c = getCBounds(j,c); c <= ccap; c++) {
                        /* Don't count yourself as your neighbor. */
                        if (og_board[r][c] == '1' &&
                                !((r == i) && (c == j))) {
                            neighbors++;
                        }
                    }
                }
                /* Determine fate */
                if (og_board[i][j] == '0') {
                    if (neighbors == 3) {
                        temp_board[i][j] = '1';
                    }
                } else if (og_board[i][j] == '1'){
                    if (neighbors < 2 || neighbors > 3) {
                        temp_board[i][j] = '0';
                    } else {
                        temp_board[i][j] = '1';
                    }
                }
            }
        }
        /* Copy temp to board */
        for (i = 0; i < rows; i++) {
            for (j = 0; j < cols; j++) {
                og_board[i][j] = temp_board[i][j];
            }
        }
        printBoard(rows, cols);
        printf("\n");
    }
    return 0;
}

/*
 * Recalculates the column to begin searching for neighbors in.
 */
int getCBounds(int j, int c) {
    c = j - 1; // left bound
    if (j == 0) {
        c++;
    }
    return c;
}

int saveBoard()
{
    int i, j, size;
    char *str;
    str = (char *)malloc((rows*(cols+1)) * sizeof(char));

    if (og_board == NULL) {
        printf("There is no board to save.\n");
        return 1;
    }

    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            str[size] = og_board[i][j];
            size++;
        }
        str[size] = ';';
        size++;
    }
    write_file(file, str, size);
    printf("Game saved.\n");
    return 0;
}

void loadBoard()
{
    char *str;
    int size;

    if ((size = read_file(file, &str)) > 1) {
        rows = 0;
        cols = 0;
        int i, j;

        // Get row size
        while (str[cols] != ';') {
            cols++;
        }
        for (int i = 0; i < size; i++)
        {
            if (str[i] == ';')
            {
                rows++;
            }
        }

        freeBoard();
        createBoard(rows, cols);

        /* Now we fill the board. We know the rows and columns
         * fit inside the board. Each item that is not a semi-colon
         * gets added to the board.
         * We must free the temp board memory after.
         */
        int n = 0;
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols + 1; j++)
            {
                if (str[n] != ';')
                {
                    og_board[i][j] = str[n];
                }
                n++;
            }
        }
        printBoard(rows, cols);
    }
    free(str);
}

/**
 * Allocates memory in the heap that is going to be used as the
 * board for the Game of Life.
 *
 * @param r - int - number of rows
 * @param c - int - number of columns
 * @return - char* - allocated memory in the heap
 */
void createBoard(const int r, const int c)
{
    rows = r;
    cols = c;
    int i, j;
    og_board = (char **)malloc(rows * sizeof(char*));
    for (int i = 0; i < rows; i++)
        og_board[i] = (char*)malloc(cols * sizeof(char));

    for (i = 0; i < rows; i++){
        for (j = 0; j < cols; j++)
            og_board[i][j] = 0;
    }
    temp_board = (char **)malloc(rows * sizeof(char*));
    for (int i = 0; i < rows; i++)
        temp_board[i] = (char*)malloc(cols * sizeof(char));

    for (i = 0; i < rows; i++){
        for (j = 0; j < cols; j++)
            temp_board[i][j] = 0;
    }
}

/**
 * Display the board in the console.
 *
 * @param board - int - the board to show
 * @param rows - int - how many rows the board has
 * @param columns - int - how many columns the board has
 */
void printBoard( int r, int c )
{
    rows = r;
    cols = c;
    int i, j;
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++){
            if (og_board[i][j] == '1')
                printf("\x1b[37m\u2588");
            else
                printf("\x1B[34m\u2588");
        }
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
    int response = 0;
    char c[3];

	printf("What would you wish to do today?\n");
	printf("(1) Live one generation\n");
	printf("(2) Live through 10 generations\n");
	printf("(3) Load a previously saved board by filename\n");
	printf("(4) Save current file state by filename \n");
	printf("(5) Exit\n");
	fflush(stdin);
    fgets(c, 3, stdin);
    response = atoi(c);
    return response;
}

void freeBoard() {
    int i;
    if (og_board != NULL) {
        for (i = 0; i < rows; i++) {
            free(og_board[i]);
        }
        free(og_board);
    }
}