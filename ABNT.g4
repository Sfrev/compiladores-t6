grammar ABNT;

variables: (periodico | jornal)*;

citation: (articleCitation | bookCitation)*;

articleCitation: '!artigo' '{' 'nome' '=' names ',' 'titulo' '=' title ',' 'revista' '=' localTitle ',' 'volume' '=' volume ',' 'pagina' '=' pages ',' 'mes' '=' month ',' 'ano' '=' year '}';
bookCitation: '!livro' '{' 'nome' '=' names ',' 'titulo' '=' bookTitle ',' 'edicao' '=' edition ',' 'editora' '=' publisher ',' 'mes_publicacao' '=' publishMonth ',' 'ano_publicacao' '=' publishYear '}';

periodico: 'periodico' '{' 'id' '=' ID ',' 'nome' '=' CADEIA ',' 'ISBN' '=' INT '}' ;
jornal: 'jornal' '{' 'id' '=' ID ',' 'nome' '=' CADEIA ',' 'local_publicacao' '=' CADEIA ',' 'data_publicacao' '=' CADEIA '}';
names: '[' name (',' name)* ']';
title: '[' name ']';
localTitle: '[' name ']';
bookTitle: '[' name ']';
volume: '[' INT ']';
pages: '[' INT ']';
month: '[' INT ']';
year: '[' INT ']';
edition: '[' INT ']';
publisher: '[' name ']';
publishMonth: '[' INT ']';
publishYear: '[' INT ']';

name: CADEIA;
CADEIA 	: '"' (~('"'|'\\'|'\n'|'\r') )* '"';
ID: [a-zA-Z0-9]+;
INT: [0-9]+;

WS: [ \t\r\n] -> skip;