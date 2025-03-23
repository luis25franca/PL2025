# TPC6

### Data de entrega: 14/02/2025
### Autor: Luís França A104259
![Fotografia do aluno](..\foto.jpg)

---

### Resumo

Enunciado do Problema:

"Baseado nos materiais fornecidos na aula, cria um parser LL(1) recursivo descendente que reconheça expressões aritméticas e calcule o respetivo valor."

Para resolver este problema foi necessário definir uma gramática sintática utilizando a biblioteca yacc que processasse tokens definidos utilizando a biblioteca lex.

**Tokens**

- `L_PAREN` e `R_PAREN`: Definição dos caracteres de parenteses que definem as prioridades das operações aritméticas.
- `LPAREN`, `RPAREN`, `PLUS`, `MINUS`, `TIMES`, `DIVIDE`: Encontram os símbolos correspondentes às respetivas operações aritméticas.
- `NUMBER`: Encontra os números nas operações aritméticas.

**Gramática**

Numa gramática os tokens acabam por servir como os símbolos não terminais para os símbolos terminais defini os seguintes:

- `expression`: representa uma expressão aritmética completa, podendo ser uma soma ou subtração de termos.
- `term` : representa um termo dentro da expressão, podendo ser um produto ou uma divisão de fatores
- `factor` : representa um fator dentro do termo, podendo ser um número ou uma expressão entre parênteses.

