%{
	#include <stdio.h>
	#include <stdlib.h>
	#include "zoomjoystrong.tab.h"
	int val_int = 0;
	float val_float = 0
%}

%option noyywrap

%%

[0-9]+ 		{ yyval.val_int = atoi(yytext); return INT; }
[0-9]*\.[0-9]+	{ yyval.val_float = atoi(yytext); return FLOAT; }
point 		{ return POINT; }
line		{ return LINE; }
circle		{ return CIRCLE; }
rectangle	{ return RECTANGLE; }
set_color	{ return SET_COLOR; }
;		{ return END_STATEMENT; }
[\t|\n]		;
.		{ printf("Don't do that again lmao"); }

%%
