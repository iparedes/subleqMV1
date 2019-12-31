grammar subleqasm;


program : instr+
        ;

instr   : val sep val sep val NEWLINE
        ;

val     :   expr
        ;

expr
    :   MINUS expr                      #minExpr
    |   PLUS expr                       #sumExpr
    |   expr op=(MULT | DIV ) expr      #mulExpr
    |   expr op=(PLUS | MINUS) expr     #addExpr
    |   atom                            #atoExpr
    |   label (NEWLINE)* expr           #labelExpr
    ;

atom
    :   OPAR expr CPAR      #parExpr
    |   NUMBER              #numberAtom
    |   VARIABLE            #varAtom
    ;


sep     : COMMA | NEWLINE
        ;

NUMBER  :   DIGIT+;

DIGIT
   : [0-9]
   ;

VARIABLE :  [a-zA-Z][a-zA-Z0-9]*
         ;

label    :  VARIABLE COLON
         ;

MULT:   '*';
DIV:    '/';
PLUS:   '+';
MINUS:  '-';
COMMA:  ',';
COLON:  ':';
OPAR:   '(';
CPAR:   ')';
NEWLINE   : '\r' '\n' | '\n' | '\r';
WS
   : [ \r\n] + -> skip
   ;
