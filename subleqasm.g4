grammar subleqasm;


program : (instr | data)+
        ;

instr   : val sep val sep val NEWLINE?
        ;

data    : (label (NEWLINE)*)? literal NEWLINE?
        ;

val     : expr
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


label    :  VARIABLE COLON
         ;

sep     : COMMA | NEWLINE
        ;

literal :  QUOTEDALPHANUM
        ;

NUMBER  :   DIGIT+;

QUOTEDALPHANUM    : QUOTE  [a-zA-Z0-9 !,#$%&/()]+ QUOTE
            ;

VARIABLE    :   [a-zA-Z][a-zA-Z0-9]*
            ;

DIGIT
   : [0-9]
   ;




MULT:   '*';
DIV:    '/';
PLUS:   '+';
MINUS:  '-';
COMMA:  ',';
COLON:  ':';
OPAR:   '(';
CPAR:   ')';
QUOTE:  '"';
NEWLINE   : '\r' '\n' | '\n' | '\r';
WS
   : [ \r\n] + -> skip
   ;
