#ifndef GAMEOFLIFE 
#define GAMEOFLIFE
#include "file_utilities.h"

int update(int n);
int getCBounds(int j, int c);
int saveBoard(char *file);
void loadBoard(char *file);
void createBoard(int r, int c);
void printBoard(int rows, int columns);
void freeBoard();
int promptUser();
void welcome();

#endif