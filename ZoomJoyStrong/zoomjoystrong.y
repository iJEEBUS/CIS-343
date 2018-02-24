%{
	#include <stdio.h>
	#include "zoomjoystrong.h"
	void yyerror(char* s);
	int yylex();
%}

%error-verbose
%start program

%union {
	int val_int;
	float val_float;
}

/* tokens */
%token <val_int> INT
%token <val_float> FLOAT
%token END
%token END_STATEMENT
%token POINT
%token LINE
%token CIRCLE
%token RECTANGLE
%token SET_COLOR
%token ERROR_INVALID

%%
program:		statement_list end; 	
	;
statement_list:		statement
	|				statement statement_list
	;
statement:		point
	|			line
	|			circle
	|			rectangle
	| 			set_color
	|			error_invalid
	;
point:			POINT INT INT END_STATEMENT		
	{
				if ($2 < 0 || $2 > 1024)
					yyerror("First coordinate is out of range.");
				if ($3 < 0 || $3 > 768)
					yyerror("Second coordinate is out of range.");
				else
					point($2, $3);
	}
	;
line:			LINE INT INT INT INT END_STATEMENT	
	{
				if ($2 < 0 || $2 > 1024)
					yyerror("First coordinate out of range.");
				if ($3 < 0 || $3 > 768)
					yyerror("Second coordinate out of range.");
				if ($4 < 0 || $4 > 1024)
					yyerror("Third coordinate out of range.");
				if ($5 < 0 || $5 > 768)
					yyerror("Fourth coordinate out of range.");
				else
					line($2, $3, $4, $5);
	}
	;
circle:			CIRCLE INT INT INT END_STATEMENT	
	{ 
				if ($2 < 0 || $2 > 1024)
					yyerror("First coordinate out of range.");
				if ($3 < 0 || $3 > 768)
					yyerror("Second coordinate out of range.");
				if ($4 < 0 || $4 > 1024)
					yyerror("Third coordinate out of range.");			
				else
					circle($2, $3, $4);
	}		
	;
rectangle:		RECTANGLE INT INT INT INT END_STATEMENT	
	{ 	
				if ($2 < 0 || $2 > 1024)
					yyerror("First coordinate out of range.");
				if ($3 < 0 || $3 > 768)
	                                yyerror("Second coordinate out of range.");
				if ($4 < 0 || $4 > 1024)
	                                yyerror("Third coordinate out of range.");
				if ($5 < 0 || $5 > 768)
	                                yyerror("Fourth coordinate out of range.");
				else
					rectangle($2, $3, $4, $5);
	}
	;
set_color:		SET_COLOR INT INT INT END_STATEMENT	
	{ 
				if ($2 < 0 || $2 > 255)
					yyerror("First coordinate out of range.");
				if ($3 < 0 || $3 > 255)
					yyerror("Second coordinate out of range.");
				if ($4 < 0 || $4 > 255)
					yyerror("Third coordinate out of range.");			
				set_color($2, $3, $4);
	}
	;
end:			END END_STATEMENT
	{
				finish();
				exit(0);
	}
	;
error_invalid:			ERROR_INVALID
	{
				yyerror("Invalid input.");
	}
	;
%%

int main() {

	printf("\nErrors produced:\n\n");

	setup();
	return(yyparse());
	finish();
}

void yyerror(char* s) {
	printf("%s\n", s);
}
