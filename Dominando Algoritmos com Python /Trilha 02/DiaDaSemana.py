dia = int(input("Digite o número do dia da semana (0 a 6): "))

dias_semana = {
    0: "Domingo",
    1: "Segunda-feira",
    2: "Terça-feira",
    3: "Quarta-feira",
    4: "Quinta-feira",
    5: "Sexta-feira",
    6: "Sábado"
}

if dia in dias_semana:
    print(dias_semana[dia])
else:
    print("Dia da semana inválido")