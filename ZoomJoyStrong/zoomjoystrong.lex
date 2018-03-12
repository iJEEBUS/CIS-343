%{
	/********************************************************************************
	* This flex file is used to define the tokens of our language, which will 
	* be used in the zoomjoystrong.y 
	*
	* References: 
	* 	https://regexr.com/
	* 	https://github.com/irawoodring/343/tree/master/parsing-with-bison/sample_code
	*
	* @author Ronald Rounsifer
	* @version 1.20
	* @date 3/12/2018
	********************************************************************************/

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
