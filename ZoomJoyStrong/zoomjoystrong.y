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

%%
program:		statement_list END END_STATEMENT 	{ finish(); return 0; }
	|		END END_STATEMENT			{ finish(); return 0; }
	;
statement_list:		statement
	|		statement statement_list
	;
statement:		point
	|		line
	|		circle
	|		rectangle
	| 		set_color
	;

%%

int main() {
	setup();
	yyparse();
	return 0;
}

int yyerror(char* s) {
	fprint(stderr, "%s on %s\n", s,yytext);
}
