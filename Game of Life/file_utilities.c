
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int read_file( char* filename, char **buffer )
{
	/* Pointer to file */
	FILE *fp;
	filename[strlen(filename) - 1] = '\0';
	fp = fopen(filename, "r");
	int new_length;
	
	/* File contents */
	fp = fopen(filename, "rb");
	if (fp == NULL || filename == NULL) {
		printf("File does not exist!\n");
        fclose(fp);
        return 1;
    } else {
		/* Go to the end of the file */
		if (fseek(fp, 0L, SEEK_END) == 0) {

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

int write_file( char* filename, char *buffer, int size )
{
	FILE *fout;
	filename[strlen(filename) - 1] = '\0';
	fout = fopen(filename, "w");

	if (filename == NULL || fout == NULL) {
        printf("Not a valid file name!\n");
        fclose(fout);
        return 1;
    }
    int i;
    for (i = 0; i < size; i++)
        fputc(buffer[i], fout);
    fclose(fout);
    return 0;
}