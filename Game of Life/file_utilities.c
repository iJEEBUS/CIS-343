
#include <stdio.h>
#include <stdlib.h>

int read_file( char* filename, char **buffer );
char* allocateMemory(int r, int c);
void printBoard(char *board, int rows, int columns);
void createBoardFromFile( char* board, char **temp_board, size_t buffer_len );


int main(int argc, char const *argv[])
{
	/* Save data location */
	char* file = "./test_file.txt";

	/* Temp memory for reading in data */
	char *buffer = malloc(500*sizeof(char));
	/* Board for the game */
	char *og_board, *temp_board, final_board;

	/* Size of buffer. Always larger than needed by +2 */
	size_t buffer_length;

	/* Read the file  */
	buffer_length = read_file(file, &buffer);
	og_board = buffer;

	createBoardFromFile(og_board, &temp_board, buffer_length);

	return 0;
}

void printBoard(char *board, int rows, int columns)
{
	int count = 0;
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < columns; j++)
			printf("\x1B[34m\u25A0 ");
		printf("\n");
	}
}

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
			// 	*buffer[new_length++] = '\0';
		}
		fclose(fp);
	}

	return new_length;
}