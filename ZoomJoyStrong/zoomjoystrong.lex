%{
	#include <stdio.h>
	#include <stdlib.h>
	#include "zoomjoystrong.tab.h"
	int val_int = 0;
	float val_float = 0;
%}

%option noyywrap

%%

end				{ return END; }
;				{ return END_STATEMENT; }
[0-9]+ 			{ yylval.val_int = atoi(yytext); return INT; }
[0-9]*\.[0-9]+	{ yylval.val_float = atof(yytext); return FLOAT; }
point 			{ return POINT; }
line			{ return LINE; }
circle			{ return CIRCLE; }
rectangle		{ return RECTANGLE; }
set_color		{ return SET_COLOR; }
" "|\n|\t|.				;
(point)|(circle)|(line)|(set_color)|(end)|[0-9]]	{ return ERROR_INVALID; }

%%
