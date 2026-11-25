def coletar_dados_calculadora():
    numero_um = float(input("Digite o primeiro número: "))
    numero_dois = float(input("Digite o segundo número: "))
    operacao_escolhida = input("Digite o número ou o nome da operação (1. Soma, 2. Subtração, 3. Multiplicação, 4. Divisão, 5. Resto, 6. Potência): ").strip()
    return numero_um, numero_dois, operacao_escolhida

def processar_calculo(numero_um, numero_dois, operacao_escolhida):
    operacao_minuscula = operacao_escolhida.lower()
    if operacao_escolhida == "1" or "soma" in operacao_minuscula:
        return f"{numero_um} + {numero_dois} = {numero_um + numero_dois}"
    elif operacao_escolhida == "2" or "subtra" in operacao_minuscula:
        return f"{numero_um} - {numero_dois} = {numero_um - numero_dois}"
    elif operacao_escolhida == "3" or "multipli" in operacao_minuscula:
        return f"{numero_um} * {numero_dois} = {numero_um * numero_dois}"
    elif operacao_escolhida == "4" or "divis" in operacao_minuscula:
        return f"{numero_um} / {numero_dois} = {numero_um / numero_dois}"
    elif operacao_escolhida == "5" or "resto" in operacao_minuscula or "mod" in operacao_minuscula:
        return f"{numero_um} mod {numero_dois} = {numero_um % numero_dois}"
    elif operacao_escolhida == "6" or "potên" in operacao_minuscula or "poten" in operacao_minuscula:
        return f"{numero_um} ^ {numero_dois} = {numero_um ** numero_dois}"
    else:
        return "Operação não suportada"

def exibir_resultado(resultado_calculo):
    print(f"\n{resultado_calculo}")

def programa_principal():
    numero_um, numero_dois, operacao = coletar_dados_calculadora()
    resultado = processar_calculo(numero_um, numero_dois, operacao)
    exibir_resultado(resultado)

programa_principal()