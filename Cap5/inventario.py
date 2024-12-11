inventario = {}
opcao = """
1 - Para registrar ativo
2 - Para pesistir em arquivo
3 - Para exibir ativos armazenados
"""

escolha = int(input(opcao + "Digite uma opção: "))

while escolha > 0 and escolha < 4:
    if escolha == 1:
        resp = "SIM"
        while resp == "SIM":
            inventario[input("Digite o número patrimonial: ")] = [
                input("Digite a data da última atualização: "),
                input("Digite a descrição: "),
                input("Digite o departamento: ")]
            resp = input("Digite 'SIM' para continuar: ").upper()
    
    elif escolha == 2:
        with open("inventario.csv", "a") as inv:
            for chave, valor in inventario.items():
                inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "")
                print("Persistido com sucesso!")
    
    elif escolha == 3:
        with open("inventario.csv", "r") as inv:
            print(inv.readlines())

    escolha = int(input(opcao + "Digite uma opção: "))