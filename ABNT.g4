grammar ABNT;

programa: variables+ citation;
variables: periodico | jornal | publisher;
citation: (articleCitation | bookCitation)*;

articleCitation: '!artigo' '{' 'nome' '=' names ',' 'titulo' '=' title ',' 'jornal' '=' '[' ID ']' ',' 'volume' '=' volume ',' 'pagina' '=' pages ',' 'mes' '=' month ',' 'ano' '=' year '}';
bookCitation: '!livro' '{' 'nome' '=' names ',' 'titulo' '=' bookTitle (',' 'subtitulo' '=' CADEIA)? ',' 'edicao' '=' edition ',' 'editora' '=' ID ',' 'mes_publicacao' '=' publishMonth ',' 'ano_publicacao' '=' publishYear '}';

periodico: 'periodico' '{' 'id' '=' ID ',' 'nome' '=' CADEIA ',' 'ISBN' '=' INT '}' ;
jornal: 'jornal' '{' 'id' '=' ID ',' 'nome' '=' CADEIA ',' 'local_publicacao' '=' CADEIA ',' 'data_publicacao' '=' CADEIA '}';
publisher: 'editora' '{' 'id' '=' ID ',' 'nome' '=' CADEIA ',' 'idioma' '=' CADEIA '}' ;
names: '[' name (',' name)* ']';
title: '[' name ']';
localTitle: '[' name ']';
bookTitle: '[' name ']';
volume: '[' INT ']';
pages: '[' INT ']';
month: '[' INT ']';
year: '[' INT ']';
edition: '[' INT ']';
publishMonth: '[' INT ']';
publishYear: '[' INT ']';

name: CADEIA;
CADEIA: '"' (~('"'|'\\'|'\n'|'\r') )* '"';
ID:	([a-zA-Z])([a-zA-Z]|'0'..'9'|'_')*;

INT: ('0'..'9')+;

WS: [ \t\r\n] -> skip;