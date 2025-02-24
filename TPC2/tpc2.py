import re
import os

padrao = re.compile(r'([^;]+);("(?:[^"]*(?:"[^"]*)*)"|[^;]+);([^;]+);([^;]+);([^;]+);([^;]*)\n?')


compositores = set()
quantidade_por_periodo = {}
obras_por_periodo = {}


with open("obras.csv", 'r', encoding='utf-8') as obras:
    proxima_linha = False
    buffer = ""
    for linha in obras:
        if not proxima_linha:
            proxima_linha = True
            continue

        buffer += linha
        match = re.match(padrao, buffer)
        if match:
            nome = match.group(1)
            periodo = match.group(4)
            compositor = match.group(5)
            
            compositores.add(compositor)
            
            if periodo in quantidade_por_periodo:
                quantidade_por_periodo[periodo] += 1
            else : quantidade_por_periodo[periodo] = 0
            
            if periodo not in obras_por_periodo:
                obras_por_periodo[periodo] = []
            obras_por_periodo[periodo].append(nome)
            buffer = ""

compositores_ordenados = sorted(compositores)
for periodo in obras_por_periodo:
    obras_por_periodo[periodo].sort()


if os.path.exists("outputs.txt"):
    os.remove("outputs.txt")

with open("outputs.txt", 'a',encoding='utf-8') as o:
    print("\n1. Lista ordenada alfabeticamente dos compositores: \n")
    o.write("\n1. Lista ordenada alfabeticamente dos compositores: \n")
    print(compositores_ordenados)
    o.write(str(compositores_ordenados) + "\n")

    print("\n2. Distribuição das obras por período:\n")
    o.write("\n2. Distribuição das obras por período:\n")
    for periodo, quantidade in quantidade_por_periodo.items():
        print(f"{periodo}: {quantidade} obras")
        o.write(f"{periodo}: {quantidade} obras\n")

    print("\n3. Dicionário por período com lista alfabética dos títulos:\n")
    o.write("\n3. Dicionário por período com lista alfabética dos títulos:\n")
    for periodo, obras in obras_por_periodo.items():
        print(f"{periodo}: {obras}")
        o.write(f"{periodo}: {obras}\n")
