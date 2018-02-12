#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*****************************************************************
 * This holds the methods that pertain to interactions with
 * files such as reading and writing to them.
 *
 * @author Ronald Rounsifer
 * @version 0.1.5
 * @created 02/07/2018
 *****************************************************************/

/*****************************************************************
 * Reads in the contents of a file that is in the form
 * of a single string. Makes use of a buffer as a way
 * to dynamically allocate memory to the needed size.
 *
 * @param filename - char* - file to read in
 * @param buffer - **char - dynamically sized memory point
 * @return
 *****************************************************************/
int read_file( char* filename, char **buffer )
{
	/* Pointer to file */
	FILE *fp;

	/* Must set last char to null character */
	filename[strlen(filename) - 1] = '\0';

	/* Open file */
	fp = fopen(filename, "r");

	/* Total length of the buffer */
	int new_length;
	
	/* File contents */
	fp = fopen(filename, "rb");

	/* Null checking before reading in file */
	if (fp == NULL || filename == NULL)
	{
		printf("File does not exist!\n");
        fclose(fp);
        return 1;
    } else {
		/* Go to the end of the file */
		if (fseek(fp, 0L, SEEK_END) == 0)
		{
			/* Get the size of the file */
			int buffer_size = (int)ftell(fp);
			
			if (buffer_size == -1) 
				return -1;

			/* Make buffer that size */
			*buffer = (char *)malloc(sizeof(char) * (buffer_size));

			/* Go back to the start of the file */
			fseek(fp, 0L, SEEK_SET);

			/* Read file into the memory */
			new_length = fread(*buffer, sizeof(char), buffer_size, fp);
		}
		fclose(fp);
	}
	return new_length;
}

/*****************************************************************
 * Writes the contents of the board to a specified filename that
 * is inputted by the user. Uses a buffer that has to be holding
 * the board
 *
 * @param filename - char* - file to store the board
 * @param buffer - char - the contents of the board
 * @param size - int - size of the board
 * @return
 *****************************************************************/
int write_file( char* filename, char *buffer, int size )
{
	/* Pointer to file */
	FILE *fout;

	/* Must set last char to null character */
	filename[strlen(filename) - 1] = '\0';

	/* Open file */
	fout = fopen(filename, "w");

	/* Null checking before writing file */
	if (filename == NULL || fout == NULL) {
        printf("Not a valid file name!\n");
        fclose(fout);
        return 1;
    }
    int i;
    for (i = 0; i < size; i++)
        fputc(buffer[i], fout); // write to file
    fclose(fout);
    return 0;
}