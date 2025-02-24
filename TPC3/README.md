# TPC2

### Data de entrega: 28/02/2025
### Autor: Luís França A104259
![Fotografia do aluno](..\foto.jpg)

---

### Resumo


Enunciado do problema:
"Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic
Syntax" da Cheat Sheet:"

Ao iniciar, o programa lê do terminal um input para converter, se nada for preenchido utilizará por defeito o texto contido em [input.txt](./input.txt).

Para cada um dos elementos de sintaxe demonstrada na CheatShet foi desenvolvida uma expressão regular para a processar. Substituindo a sintaxe MarkDown desse elemento por sintaxe HTML.

- Cabeçalhos: `^# (.+)`->`<h1>\1</h1>` Esta expressão captura os valores a seguir um # e introduz <h1></h1> a rodear o texto capturado. Para os headers 2 e 3 (## e ###) apenas alterei a expressão implementando o número correto de símbolos.

- Bold: `\*\*([^*]+)\*\*`->`<b>\1</b>` Esta expressão captura os valores entre ** e coloca em ambos os lados <b> e </b>.

- Italic: `\*([^*]+)\*`->`<i>\1</i>`Esta expressão segue a mesma lógica da expressão acima, apenas detetando um asterisco e mudando o html de <b> para <i>.

- Listas Numeradas: O processamento das listas numeradas é realizada em 2 etapas:
    1. `(?m)^\d+\. (.+)'`->`'<ol>\n<li>\1</li>\n</ol>` Captura todas as linhas começadas por um ou mais dígitos seguidos de um ponto e substitui-os colocando <li> e <\li> no início e fim dessa linha. Além disso rodea essa linha por <ol>, causando a aparência desta labela a mais.
    2. `\n(</ol>\n<ol>)'`-> `''` Apaga os <ol> e </os> desnecessários

- Link: `\[(.+?)\]\((.+?)\)`->`<a href="\2">\1</a>` Verifica a aparência ordenada de[] () que indica que o elemento corresponde a um link e coloca a sintaxe html correspondente.

- Imagem: `\!\[(.+?)\]\((.+?)\)`->`<img src="\2" alt="\1"/>>` Tal como a expressão anterior esta verifica a ordem dos parêntes tendo atenção à existência de ! antes de um '[' e substituindo pela sintaxe correta.

No final o programa escreve o output no terminal. O resultado de converter o texto em [input.txt](./input.txt) é o seguinte: 
![resultado](./tpc3.resultado.png)


    
