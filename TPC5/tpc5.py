

import json
import re
import ply.lex as lex
from datetime import datetime

class VendingMachine:
    def __init__(self, stock_file="stock.json"):
        self.stock_file = stock_file
        self.saldo = 0  # Saldo em centavos
        self.carregar_stock()
        print(f"maq: {datetime.today().date()}, Stock carregado, Estado atualizado.")
        print("maq: Bom dia. Estou disponível para atender o seu pedido.")
        self.lexer = self.configurar_lexer()

    def carregar_stock(self):
        try:
            with open(self.stock_file, "r", encoding="utf-8") as f:
                content = f.read()
                self.stock = json.loads(content)
        except FileNotFoundError:
            print("maq: Arquivo stock.json não encontrado. Criando novo estoque.")
            self.stock = []
            self.salvar_stock()
        except json.JSONDecodeError as e:
            print(f"maq: Erro ao carregar stock.json: {e}")
            self.stock = []

    def salvar_stock(self):
        with open(self.stock_file, "w") as f:
            json.dump(self.stock, f, indent=4)

    def listar_produtos(self):
        print("maq:\ncod | nome | quantidade | preço")
        print("---------------------------------")
        for item in self.stock:
            print(f"{item['cod']} {item['nome']} {item['quant']} {item['preco']}€")

    def inserir_moeda(self):
        while True:
            tok = self.lexer.token()
            if tok is None or tok.type != "VALOR"  :
                break  
            print(tok)
            self.saldo += tok.value
        print(f"maq: Saldo = {int(self.saldo *100 // 100)}e{int(self.saldo *100 % 100)}c")

    def selecionar_produto(self):
        token = self.lexer.token()
        codigo = token.value
        for item in self.stock:
            if item["cod"] == codigo:
                preco = item["preco"]
                if self.saldo >= preco:
                    if item["quant"] > 0:
                        item["quant"] -= 1
                        self.saldo -= preco
                        print(f"maq: Pode retirar o produto dispensado \"{item['nome']}\"")
                        print(f"maq: Saldo = {int(self.saldo *100 // 100)}e{int(self.saldo *100 % 100)}c")
                    else:
                        print("maq: Produto esgotado.")
                else:
                    print("maq: Saldo insuficiente para satisfazer o seu pedido")
                    print(f"maq: Saldo = {int(self.saldo *100 // 100)}e{int(self.saldo *100 % 100)}c; Pedido = {preco // 100}e{preco % 100}c")
                return
        print("maq: Código de produto inválido.")

    def devolver_troco(self):
        valores = [50, 20, 10, 5, 2, 1]
        troco = self.saldo
        resultado = []
        for v in valores:
            quantidade = troco // v
            if quantidade:
                resultado.append(f"{quantidade}x {v}c")
                troco -= quantidade * v
        if resultado:
            print("maq: Pode retirar o troco: " + ", ".join(resultado) + ".")
        self.saldo = 0

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

    def executar(self):
        while True:
            comando = input(">> ")
            self.lexer.input(comando)
            token = self.lexer.token()


            match token.type:
                case "LISTAR":
                    self.listar_produtos()
                case "MOEDA":
                    self.inserir_moeda()
                case "SELECIONAR":
                    self.selecionar_produto()
                case "SAIR":
                    self.devolver_troco()
                    print("maq: Até à próxima")
                    self.salvar_stock()
                    break
                case _:
                    print("maq: Comando inválido.")

if __name__ == "__main__":
    maquina = VendingMachine()
    maquina.executar()
