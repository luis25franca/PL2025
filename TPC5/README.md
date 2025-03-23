# TPC1

### Data de entrega: 14/02/2025
### Autor: Luís França A104259
![Fotografia do aluno](..\foto.jpg)

---

### Resumo

Enunciado do Problema:

"Pediram-te para construir um programa que simule uma máquina de vending que simule um meta-automato."

Para resolver este problema defini uma classe em python `VendingMachine` que guarda toda a informação do estado da máquina além das operações sobre ela.

<code>

    class VendingMachine:
    def __init__(self, stock_file="stock.json"):
        self.stock_file = stock_file
        self.saldo = 0  # Saldo em centavos
        self.carregar_stock()
        print(f"maq: {datetime.today().date()}, Stock carregado, Estado atualizado.")
        print("maq: Bom dia. Estou disponível para atender o seu pedido.")
        self.lexer = self.configurar_lexer()
</code>

Ao ser inicializada define as suas variáveis carrega para memória o ficheiro [stock.json](stock.json) e configura o lexer. O analisador léxico ajuda o programa a interpretar os comandos fornecidos pelo utilizador. 

<code> 

    def configurar_lexer(self):
        tokens = ('LISTAR', 'MOEDA', 'SELECIONAR', 'CODIGO', 'SAIR', 'VALOR')
        t_LISTAR = r'LISTAR'
        t_MOEDA = r'MOEDA'
        t_SELECIONAR = r'SELECIONAR'
        t_CODIGO = r'[A-Z]\d{2,}'
        t_SAIR = r'SAIR'
        t_ignore = ' \t'

        valores_moeda = {"2e": 2.00, "1e": 1.00, "50c": 0.50, "20c": 0.20, "10c": 0.10, "5c": 0.05, "2c": 0.02, "1c": 0.01}
        
        def t_VALOR(t):
            r'2e|1e|50c|20c|10c|5c|2c|1c'
            t.value = valores_moeda[t.value]
            return t
        
        def t_error(t):
            print("maq: Comando inválido.")
            print(t)
            t.lexer.skip(1)

        lexer = lex.lex()
        return lexer 
</code>

Para cada comando o programa verifica o tipo do token capturado e realiza a ação correspondente, alterando o estado da máquina quando necessário. 
Um caso especial é o token 'Valor' que se refere ao valor de uma modea inserido este token apresenta uma operção especial que automaticamente converte o valor da moeda no float correspondente.