%{

	/********************************************************************************
	* This Bison file uses the lex tokens (defined in zoomjoystrong.lex) 
	* to call on functions as they are defined in the included zoomjoystrong.c
	* file.
	*
	* References:
	*	https://github.com/irawoodring/343/tree/master/parsing-with-bison/sample_code
	*
	* @author Ronald Rounsifer
	* @version 1.20
	* @date 3/12/2018
	********************************************************************************/
	
	#include <stdio.h>
	#include "zoomjoystrong.h"
	void yyerror(char* s);
	int yylex();
	int H = 768;
	int W = 1024;
%}

%error-verbose
%start program

%union { int val_int; float val_float; char* str; }

/* tokens */
%token INT
%token FLOAT
%token END
%token END_STATEMENT
%token POINT
%token LINE
%token CIRCLE
%token RECTANGLE
%token SET_COLOR
%token ERROR_INVALID

%type<val_int> INT
%type<val_float> FLOAT
%type<str> END
%type<str> END_STATEMENT
%type<str> POINT
%type<str> LINE
%type<str> CIRCLE
%type<str> RECTANGLE
%type<str> SET_COLOR

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
				printf("Plotting point - x: %d y: %d\n", $2, $3); 
				if ($2 < 0 || $2 > W)
					yyerror("First coordinate is out of range (max: 1024)");
				if ($3 < 0 || $3 > H)
					yyerror("Second coordinate is out of range (max: 768)");
				else
					point($2, $3);
	}
	;
line:			LINE INT INT INT INT END_STATEMENT	
	{
				printf("Drawing line - x: %d y: %d u: %d v: %d\n", $2, $3, $4, $5);
				if ($2 < 0 || $2 > W)
					yyerror("First coordinate out of range (max: 1024)");
				if ($3 < 0 || $3 > H)
					yyerror("Second coordinate out of range (max: 768)");
				if ($4 < 0 || $4 > W)
					yyerror("Third coordinate out of range (max: 1024)");
				if ($5 < 0 || $5 > H)
					yyerror("Fourth coordinate out of range (max: 768)");
				else
					line($2, $3, $4, $5);
	}
	;
circle:			CIRCLE INT INT INT END_STATEMENT	
	{ 
				printf("Displaying circle - x: %d y: %d r: %d\n", $2, $3, $4); 
				if ($2 < 0 || $2 > W)
					yyerror("First coordinate out of range (max: 1024)");
				if ($3 < 0 || $3 > H)
					yyerror("Second coordinate out of range (max: 768)");
				if ($4 < 0 || $4 > W)
					yyerror("Third coordinate out of range (max: 1024)");			
				else
					circle($2, $3, $4);
	}		
	;
rectangle:		RECTANGLE INT INT INT INT END_STATEMENT	
	{ 	
				printf("Creating a rectangle - x: %d y: %d w: %d h: %d\n", $2, $3, $4, $5);
				if ($2 < 0 || $2 > W)
					yyerror("First coordinate out of range (max: 1024)");
				if ($3 < 0 || $3 > H)
					yyerror("Second coordinate out of range (max: 768)");
				if ($4 < 0 || $4 > W)
					yyerror("Third coordinate out of range (max: 1024)");
				if ($5 < 0 || $5 > H)
					yyerror("Fourth coordinate out of range (max: 768)");
				else
					rectangle($2, $3, $4, $5);
	}
	;
set_color:		SET_COLOR INT INT INT END_STATEMENT	
	{ 
				printf("Color now set - red: %d green: %d blue: %d\n", $2, $3, $4); 
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
				printf("\n┻━┻︵╰(゜Д゜)╯︵┻━┻\n");
				printf("I hope you enjoyed your time with ZoomJoyStrong, goodbye!\n");
				finish();
				exit(0);
	}
	;
error_invalid:			ERROR_INVALID
	{
				yyerror("Invalid input.");
				yyparse();
	}
	;
%%

int main() {
	
	setup();

	printf("\n┻━┻︵╰(゜Д゜)╯︵┻━┻\n");
	printf("This is: ZoomJoyStrong \n\n");
	printf("Legal commands: \n");
	printf("set_color 000 000 000;\n");
	printf("point x y;\n");
	printf("line x1 y1 x2 y2;\n");
	printf("circle x y r;\n");
	printf("rectangle x y w h;\n");
	printf("end; -- to terminate the program\n\n");
	printf("** NOTE: all commands must end with a semi-colon as shown above **\n");
	printf("\nBegin drawing!\n\n");

	yyparse();
	finish();
}

void yyerror(char* s) {
	printf("%s\n", s);
	yyparse();
}