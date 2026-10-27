# ==========================================================
#  CEEP Assaí - Programação com Python I
#  Curso: Inteligência Artificial e Dados
#  Professor: João Antonio Carboni Gomes
#  Reavaliação em Dupla: corrigir o código errado
# ==========================================================

print("=== SISTEMA DE CADASTRO ===\n")

# --- CADASTRO ---
nome = input("Digite seu nome completo: ")
email = input("Digite seu e-mail: ")
cidade = input("Digite sua cidade: ")

nome_salvo = nome
email_salvo = email.upper()

# CORRIGIDO 1: estava 'cidade.upper' sem os () - assim não executa a função e salva o método, não o texto. Corrigido para 'cidade.upper()'
cidade_salvo = cidade.upper()

print("\n--- Dados salvos ---")
print("Nome: ", nome_salvo)
print("E-mail: ", email_salvo)
print("Cidade: ", cidade_salvo)

print("\n=== BUSCA POR E-MAIL ===\n")
busca_email = input("Digite o e-mail cadastrado para confirmar: ")

# CORRIGIDO 2: estava 'if busca_email = email_salvo:' - um '=' só é para guardar valor, não comparar. E faltava o .upper() na busca, então se digitar minúsculo nunca ia achar. Corrigido para '==' e usando .upper()
if busca_email.upper() == email_salvo:
    print("Usuário encontrado:", nome_salvo)
else:
    print("Usuário não encontrado.")

print("\n=== VERIFICAÇÃO DE CIDADE ===\n")
cidade_busca = input("Digite uma cidade para verificar se o usuário mora lá: ")

# CORRIGIDO 3: estava comparando 'cidade_busca.upper() == cidade_salvo.lower()' - maiúsculo nunca é igual minúsculo, então sempre caía no 'não mora'. Corrigido para comparar os dois em .upper()
if cidade_busca.upper() == cidade_salvo:
    print(f"{nome_salvo} mora em {cidade_busca.upper()}.")
else:
    print("O usuário não mora nessa cidade.")