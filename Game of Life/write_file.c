#include <stdio.h>
#include <stdlib.h>

int write_file( char* filename, char *buffer, int size);


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


int write_file( char* filename, char *buffer, int size)
{

}