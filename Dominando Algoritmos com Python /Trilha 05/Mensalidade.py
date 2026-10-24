def coletar_dados_universidade():
    sigla_curso = input("Digite a sigla do curso (SI, ADS, CS, EC, ES): ").strip().upper()
    aluno_isento = input("O aluno é isento? (Sim/Não): ").strip().lower()
    
    # Se o aluno for isento, não precisa perguntar o desconto
    if "sim" in aluno_isento:
        desconto_percentual = 0.0
    else:
        desconto_percentual = float(input("Digite o desconto em %: "))
        
    return sigla_curso, aluno_isento, desconto_percentual

def processar_mensalidade(sigla_curso, aluno_isento, desconto_percentual):
    tabela_cursos = {
        "SI": 900.00,
        "ADS": 750.00,
        "CS": 1150.00,
        "EC": 1300.00,
        "ES": 950.00
    }
    
    if sigla_curso not in tabela_cursos:
        return None
    
    if "sim" in aluno_isento:
        return 0.0
    
    valor_base = tabela_cursos[sigla_curso]
    return valor_base * (1 - (desconto_percentual / 100))

def exibir_mensalidade(valor_final):
    if valor_final is None:
        print("\nCurso não encontrado")
    else:
        print("\nValor da mensalidade:")
        print(f"R$ {valor_final:.2f}")

def programa_principal():
    sigla, isento, desconto = coletar_dados_universidade()
    valor_mensalidade = processar_mensalidade(sigla, isento, desconto)
    exibir_mensalidade(valor_mensalidade)

programa_principal()