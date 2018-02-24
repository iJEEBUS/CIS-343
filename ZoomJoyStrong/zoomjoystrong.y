%{
	#include <stdio.h>
	#include "zoomjoystrong.h"
	int yyerror(char* s);
	extern char * yytext;
%}

%error-verbose
%start program

%union {
	int val_int;
	float val_float;
}

/** tokens **/
%token <value_int> INT
%token <value_float> FLOAT
%token POINT
%token LINE
%token CIRCLE
%token RECTANGLE
%token SET_COLOR
%token END_STATEMENT
%token END
