saldo = 0
extrato = ""
cont_saque = 0

menu = """
    ===Menu===
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
"""

print(menu)

while True:
    opcao = input("Informe o que deseja fazer: ")
    deposito = 0

    if opcao == "d":
        print("Depósito")

        deposito = float(input("Informe a quantia que deseja depositar: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"""Depósito: R$ {deposito:.2f}
                \nSaldo após operação: R$ {saldo:.2f}\n"""
        else:
            print("Não foi possível concluir a operação!")

    elif opcao == "s":
        print("Saque")

        if cont_saque < 3:
            saque = float(input("Informe a quantia que deseja sacar: "))

            if saque > 0:
                if saldo >= saque and saque <= 500:
                    saldo -= saque
                    extrato += f"""\nSaque: R$ {saque:.2f}
                        \nSaldo após operação: R$ {saldo:.2f}\n"""

                    cont_saque += 1
                else:
                    print("Não foi possível realizar a operação!")
            else:
                print("Não é possível sacar valores negativos ou iguais a 0.")
        else:
            print("Não foi possível realizar a operação!")

    elif opcao == "e":
        print("===Extrato===")
        if extrato:
            print(extrato)
        else:
            print("Não foram realizadas operações.")

        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!")
