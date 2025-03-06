# TPC1

### Data de entrega: 14/02/2025
### Autor: Luís França A104259
![Fotografia do aluno](..\foto.jpg)

---

### Resumo

Enunciado do Problema: 
"Construir um analisador léxico para uma liguagem de query"

Para resolver este problema é requerido usar a biblioteca ``ply.lex`` capaz de contruir um analisador léxico usando _tokens_ definidos pelo utilizador.

No programa [tpc4.py](tpc4.py) podemos encontrar em primeiro lugar a definição dos tokens que escolhi definir como os seguintes:
    ```
    "LEFT_P",
    "RIGHT_P",
    "VARIABLE",
    "VALUE",
    "URI",
    "PUNCTUATION",
    "KEYWORD"
    ``` 

Para cada um destes tokens é necessário definir uma expressão regular para os processar.
- No caso de `LEFT_P`, `RIGHT_P` e `PUNCTUATION` a expressão deteta apenas o caractér a que o token se refere('{','}' e '.' respetivamente).
- Para capturar as variáveis é preciso apenas capturar todas as palavras seguidas de um '?'. `\?\w+`
- Para capturar valores, temos que ter em conta os dois possíveis tipos de valores no exemplo _strings_ e _inteiros_. Para o caso do sinteiros é apenas preciso capturar uma sequência isolada de números, para strings obtém-se todos os caracteres dentro de aspas,e opcionalmente, uma tag de linguagem começada por '@'. `\d+|\"[^\"]*\"(?:@\w+)?`
- Para URIs (identificadores universais de recursos) podem ser idientificados como uma string que contenha no meio ':'. `\w+:[\w\d]+`
- Uma keyword pode ser qualquer string isolada que não pertença a nenhum dos grupos de cima logo meto a sua definição e expressão regular por último de modo a ser a última expressão regular a processar. `\w+`

Para o caso de encontrar um caractér 'newline' (\n) é definida uma função que incremente o `lexer.lineno`.

Para o caso de encontrar uma caracter não identificado pelas expressões acima é imprimido no terminal a posição do erro e o lexer continua a processar o texto.

O analisador léxico é depois inicializado e o output escrito no terminal.
```
lexer = lex.lex()

lexer.input(frase_exemplo)

while(r:= lexer.token()):
    print(r)
```

O output recebido da execução do programa é o seguinte:
```
LexToken(KEYWORD,'select',1,0)
LexToken(VARIABLE,'?nome',1,7)
LexToken(VARIABLE,'?desc',1,13)
LexToken(KEYWORD,'where',1,19)
LexToken(LEFT_P,'{',1,25)
LexToken(VARIABLE,'?s',2,27)
LexToken(KEYWORD,'a',2,30)
LexToken(URI,'dbo:MusicalArtist',2,32)
LexToken(PUNCTUATION,'.',2,49)
LexToken(VARIABLE,'?s',3,51)
LexToken(URI,'foaf:name',3,54)
LexToken(VALUE,'"Chuck Berry"@en',3,64)
LexToken(PUNCTUATION,'.',3,81)
LexToken(VARIABLE,'?w',4,83)
LexToken(URI,'dbo:artist',4,86)
LexToken(VARIABLE,'?s',4,97)
LexToken(PUNCTUATION,'.',4,99)
LexToken(VARIABLE,'?w',5,101)
LexToken(URI,'foaf:name',5,104)
LexToken(VARIABLE,'?nome',5,114)
LexToken(PUNCTUATION,'.',5,119)
LexToken(VARIABLE,'?w',6,121)
LexToken(URI,'dbo:abstract',6,124)
LexToken(VARIABLE,'?desc',6,137)
LexToken(RIGHT_P,'}',7,143)
LexToken(KEYWORD,'LIMIT',7,145)
LexToken(VALUE,'1000',7,151)
```
