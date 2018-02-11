
#include <stdio.h>
#include <stdlib.h>

int read_file( char* filename, char **buffer );
char* allocateMemory(int r, int c);
void printBoard(char *board, int rows, int columns);
void createBoardFromFile( char* board, char **temp_board, size_t buffer_len );
int getNumRows( char* board, size_t buffer_len );
int getNumCols( char* board, size_t buffer_len );


int getNumRows( char* board, size_t buffer_len )
{
	int rows = 0, cols = 0;
	for (int i = 0; i < buffer_len; ++i) {
		if (board[i] == ';') {
			rows++;
		}
	}
	cols = (buffer_len - rows ) / rows;
	return cols;
}

int getNumCols( char* board, size_t buffer_len )
{
	int rows = 0;
	for (int i = 0; i < buffer_len; ++i) {
		if (board[i] == ';') {
			rows++;
		}
	}
	return rows;
}

// Try to extract the rows and columns from this
void createBoardFromFile( char* board, char **temp_board, size_t buffer_len )
{
	int rows = 0, cols = 0;
	//int rows = 0, cols = 0;
	for (int i = 0; i < buffer_len; ++i) 
	{
		if (board[i] == ';') {
			rows++;
		}
		// if (board[i] == 0)
		// 	// cell color will be black
		// if (board[i] == 1)
		// 	// cell color will be white (alive)
		// if (board[i] == 2)
			// cell color will be grey (previously alive)
	}

	cols = (buffer_len - rows ) / rows;

	*temp_board = allocateMemory(rows, cols);
}

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
		}
		fclose(fp);
	}
	return new_length;
}