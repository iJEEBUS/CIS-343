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
point:			POINT INT INT END_STATEMENT		{ point($2, $3) }
	;
line:			LINE INT INT INT INT END_STATEMENT	{ line($2, $3, $4, $5) }
	;
circle:			CIRCLE INT INT INT END_STATEMENT	{ circle($2, $3, $4) }
	;
rectangle:		RECTANGLE INT INT INT INT END_STATEMENT	{ rectangle($2, $3, $4, $5) }
	;
set_color:		SET_COLOR INT INT INT END_STATEMENT	{ set_color($2, $3, $4) }
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
