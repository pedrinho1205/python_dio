import textwrap


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if valor > 0:
            if saldo >= valor and valor <= limite:
                saldo -= valor
                extrato += f"""\nSaque: R$ {valor:.2f}
                        \nSaldo após operação: R$ {saldo:.2f}\n"""
                numero_saques += 1

                print("Saque realizado com sucesso!")

                return saldo, extrato
            else:
                print("Não foi possível realizar a operação!")
        else:
            print("Não é possível sacar valores negativos ou iguais a 0.")
    else:
        print("Você já atingiu o limite de saques diários!")


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"""Depósito: R$ {valor:.2f}
                \nSaldo após operação: R$ {saldo:.2f}\n"""
        print("Depósito realizado com sucesso!")
        return saldo, extrato
    else:
        print("Não foi possível concluir a operação!")


def visualizar_extrato(saldo, /, *, extrato):
    if extrato:
        print("===Extrato===")
        print(extrato)
    else:
        print("Não foram realizadas operações.")

    print(f"Saldo: R$ {saldo:.2f}")


def listar_contas(contas):
    for conta in contas:
        print(f"""Agência: {conta['agencia']}
        Número da conta: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        CPF: {conta['usuario']['cpf']}
        """)


def verificar_usuario(usuarios):
    cpf = input("Informe o CPF (sem pontos e traços): ")

    if usuarios:
        if any(usuario["cpf"] == cpf for usuario in usuarios):
            print("Não foi possível criar o usuário, informe um CPF válido!")
        else:
            criar_usuario(usuarios, cpf)
    else:
        criar_usuario(usuarios, cpf)


def criar_usuario(usuarios, cpf):
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, numero - bairro - cidade/sigla estado)")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,
                    "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")


def criar_conta_corrente(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF (sem pontos e traços): ")

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            contas.append(
                {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
            print("Conta criada com sucesso!")
        elif not usuarios:
            print("Não foi possível criar a conta!")


def menu():
    menu = """
    ===Menu===
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    """
    return input(textwrap.dedent(menu))


def main():
    limite = 500
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    cont_saque = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor que deseja depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor que deseja sacar: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=cont_saque,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            visualizar_extrato(saldo, extrato=extrato)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta_corrente(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "nu":
            verificar_usuario(usuarios)

            for usuario in usuarios:
                print(f"Nome: {usuario['nome']}")

        elif opcao == "q":
            print("Saindo...")
            break


main()
