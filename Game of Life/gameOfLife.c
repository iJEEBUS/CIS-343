#include <stdio.h>
#include <stdlib.h>
#include "gameOfLife.h"

/*****************************************************************
 * ---------------- Conway's Game of Life.
 * Features include:
 *  - save and load files
 *  - textUI to view cells
 *  - dynamic memory allocation
 *
 *  Rules:
 *  - if a cell is white, it is alive
 *  - if a cell is blue, it is dead
 *  - Any live cell with fewer than two live neighbors dies, as if
 *    caused by underpopulation.
 *  - Any live cell with more than three live neighbors dies, as if
 *    by overcrowding.
 *  - Any live cell with two or three live neighbors lives on to the
 *    next generation.
 *  - Any dead cell with exactly three live neighbors becomes a live
 *    cell.
 *
 * How to play:
 *  1) Enter the number next to the desired functionality.
 *  2) Enjoy!
 *  P.S. Use the two data sets included (massive.txt, save_data.txt)
 *
 * Resources:
 *  - http://web.stanford.edu/~cdebs/GameOfLife/
 *    for the overall logic of the game
 *
 *  - https://www.geeksforgeeks.org/dynamically-allocate-2d-array-c/
 *    for information on how it initialize and access 2D arrays
 *
 *  - https://rosettacode.org/wiki/Conway%27s_Game_of_Life#C
 *
 * Peer-discussions:
 *  - Sean Aubrey (logic of updates / architecture)
 *
 * @author Ronald Rounsifer
 * @version 0.1.5
 * @created 02/07/2018
 *****************************************************************/


    // 4 global variables are used
    // okay for a project, not okay for production software

    /* Boards for the game */
    char **og_board, **temp_board;

    /* Number of rows in active table */
    int rows = 0;

    /* Number of columns in active table */
    int cols = 0;

/*****************************************************************
 * Main function of the Game of Life.
 * Initially prompts the user what they wish to do, then handles
 * the flow of the game.
 *
 * @param argc - int - number of cli arguments
 * @param argv - *char - list of inputted arguments
 * @return
 *****************************************************************/
int main(int argc, char const *argv[])
{
    /* File from user input */
    char file[30];

    /* Buffer to hold file information */
    char *buffer;

    welcome();

    while (1) {
        switch(promptUser()) {
            case 1: // one generation
                update(1);
                break;
            case 2: // perform ten generations
                update(10);
                break;
            case 3: // load board form file
                printf("Name of file to load: \n");
                fgets(file, 31, stdin);
                loadBoard(file);
                break;
            case 4: // save board to a file
                printf("Name of file to save: \n");
                fgets(file, 31, stdin);
                saveBoard(file);
                break;
            case 5: // exit game
                printf("\nFreeing memory...");
                freeBoard();
                printf("...liberation successful!\n");
                printf("Goodbye!\n");
                exit(EXIT_SUCCESS);
        }
    }
}

/*****************************************************************
 * Contains all of that logic that has to do with the adding and
 * subtracting of cells based on the rules of the game.
 *
 *
 * @param n - int - how many iterations to perform
 * @return
 *****************************************************************/
int update(int n)
{
    int g = 0, j = 0, i = 0;

    /* Null checking */
    if (og_board == NULL)
    {
        printf("There's no world to generate.\n");
        printf("\n");
        return 1;
    }
    /* For number of generations. */
    for (g = g; g < n; g++)
    {
        /* Clear temp_board */
        for (i = 0; i < rows; i++)
        {
            for (j = 0; j < cols; j++) {

                temp_board[i][j] = '0';
            }
        }
        int r, c;
        int rcap, ccap;
        int neighbors;
        /* For each cell, count the number of live cells around it. */
        for (i = 0; i < rows; i++)
        {
            for (j = 0; j < cols; j++)
            {
                neighbors = 0;

                /* Create 3x3 grid bounds. */
                r = i - 1; // top bound
                rcap = i + 1; // bottom bound
                c = j - 1; // left bound
                ccap = j + 1; // right bound

                /* Check if you must get rid of an edge in 3x3 grid */
                if (i == 0)
                    r++;
                else if (i == (rows - 1))  // account for +1 error
                    rcap--;
                if (j == 0)
                    c++;
                else if (j == (cols - 1))
                    ccap--;

                for (r = r; r <= rcap; r++) {
                    /* Must recalculate the location of the left-bound
                     * variable, c, after each incrementation */
                    for (c = getCBounds(j,c); c <= ccap; c++) {
                        /* Increment neighbor counter */
                        if (og_board[r][c] == '1' &&
                                !((r == i) && (c == j))) {
                            neighbors++;
                        }
                    }
                }
                /* Creating/deleting cells */
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

/*****************************************************************
 * Recalculates the column that is used as the starting point for
 * the search of neighbors to a cell
 *
 * @param j
 * @param c
 * @return
 *****************************************************************/
int getCBounds(int j, int c)
{
    c = j - 1; // left bound
    if (j == 0) {
        c++;
    }
    return c;
}


/*****************************************************************
 * Saves the players current board to the file that the user
 * inputs via the command line.
 *
 * @return
 *****************************************************************/
int saveBoard(char *file)
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

/*****************************************************************
 * Loads the board from the file that the user inputs via the
 * command line.
 *****************************************************************/
void loadBoard(char *file)
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

/*****************************************************************
 * Allocates dynamic memory in the heap that is going to be used
 * as the board for the Game of Life.
 * Sets both the og_board and temp_board to the same size.
 *
 * @param r - int - number of rows
 * @param c - int - number of columns
 *****************************************************************/
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

/*****************************************************************
 * Display the board in the console.
 *
 * @param r - int - how many rows the board has
 * @param c - int - how many columns the board has
 *****************************************************************/
void printBoard( int r, int c )
{
    rows = r;
    cols = c;
    int i, j;
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++){
            if (og_board[i][j] == '1')
                printf("\x1b[37m\u2588"); // white cell (alive)
            else
                printf("\x1B[34m\u2588"); // blue cell (dead)
        }
        printf("\n");
    }
}

/*****************************************************************
 * Frees all of the memory in the heap that was allocated for the
 * original board.
 *****************************************************************/
void freeBoard()
{
    /* Iterator */
    int i;

    /* Free memory from original board */
    if (og_board != NULL) {
        for (i = 0; i < rows; i++)
            free(og_board[i]);
        free(og_board);
    }
}


/*****************************************************************
 * Ask and return the user what they wish to do with the program.
 * This will only be ran if command line parameters are
 * not passed with the executable filename.
 *
 * @return
 *****************************************************************/
int promptUser()
{
    /* User input */
    char c[3];

    printf("Please select an option below:\n");
    printf("(1) Live one generation\n");
    printf("(2) Live through 10 generations\n");
    printf("(3) Load a previously saved board by filename\n");
    printf("(4) Save current file state by filename \n");
    printf("(5) Exit\n");
    fflush(stdin);
    fgets(c, 3, stdin);
    return atoi(c); // return user response
}

/*****************************************************************
 * Welcome banner when the user first starts the game.
 * No functional usage.
 *****************************************************************/
void welcome()
{
    printf("\n");
    printf("\n");
    printf("  ---------------- Conway's Game of Life ----------------\n"
                   "  Features include:\n"
                   "   - save and load files\n"
                   "   - textUI to view cells\n"
                   "   - dynamic memory allocation\n"
                   " \n"
                   "   FYI:\n"
                   "   - if a cell is white, it is alive\n"
                   "   - if a cell is blue, it is dead\n"
                   " \n"
                   "  How to play:\n"
                   "   1) Enter the number next to the desired functionality.\n"
                   "   2) Enjoy!\n"
                   "   P.S. Load one of the two data sets included \n"
                   "        (massive.txt, save_data.txt)\n");
    printf("\n");
    printf("\n");
}