# TPC2

### Data de entrega: 21/02/2025
### Autor: Luís França A104259
![Fotografia do aluno](..\foto.jpg)

---

### Resumo


Enunciado do problema:
"Deverás ler o dataset ([obras.csv](./obras.csv)), processá-lo e criar os seguintes resultados:
    1. Lista ordenada alfabeticamente dos compositores musicais;
    2. Distribuição das obras por período: quantas obras catalogadas em cada período
    3. Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período."

A resoloção deste problema pode ser encontrada no ficheiro [tpc2.py](./tpc2.py). 
Para resolver este problema desenvolvi um padrão em regex que filtrasse cada linha da tabela csv, este padrão teve o formato `[([^;]+);("(?:[^"]*(?:"[^"]*)*)"|[^;]+);([^;]+);([^;]+);([^;]+);([^;]*)\n?`. No padrão o grupo `([^;]*);` faz parse de um elemento de uma coluna, capturando todos os caracteres menos o ';', esta sintaxe é usada para todas as colunas menos a segunda que se refere à descrição da obra. Esta coluna tem uma característica específica em que se o conteúdo estiver entre aspas poderá conter caracters `\n`, `"` e `;` que dificultam o parsing da coluna. O padrão para processar esta coluna é `("(?:[^"]*(?:"[^"]*)*)"|[^;]+)`. Se o elemento que estamnos a processar começar por aspas, o padrão irá capturar todos os caracteres até encontrar as aspas que encerram o segmento. Se o padrão encontrar um excerto rodeado por duplas aspas irá também capturar estes valores sem terminar o processamento da coluna. Se a coluna não começar por aspas será processada como as outras.

Para processar o csv, o programa lê o documento linha a linha (ignorando a primeira) guardando as linhas num _buffer_ até que a expressão `match = re.match(padrao, buffer)` dê um resultado esperado. Após obter um _match_ obtenho os valores das colinhas 1,4 e 5 para guardas nas estruturas de dados criadas para atender às alíneas do exercício. O conteúdo do buffer é depois apagado.

Os resultados finais podem ser observados em [outputs.txt](./outputs.txt).
![Resultados](.\resultados.png)

    
