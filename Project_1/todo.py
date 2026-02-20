# # Uma tarefa é um dicionário com:
# {"descricao": "estudar python", "status": "pendente"}
# # E todas as tarefas ficam numa lista:
#   tarefas = []
# ```

# **O programa precisa ter:**

# 1. Um loop principal que fica rodando até o usuário sair
# 2. Um menu com as opções numeradas
# 3. 5 funcionalidades: adicionar, listar, concluir, remover e sair
# 4. Mensagens claras pro usuário (confirmações, erros, avisos)
# 5. Tratamento quando o usuário digitar algo inválido (número que não existe, letra no lugar de número, etc.)

# **O fluxo básico é esse:**
# ```
# Mostra menu → Usuário escolhe opção → Executa a ação → Volta pro menu

# PARTE 2 - Emojis no status das tarefas:
# Ao listar tarefas, mostrar assim:
# 0 - estudar python ⏳
# 1 - treinar ✅
# No lugar de [pendente] e [concluída]


import json

try:
    with open("tarefas.json", "r", encoding="utf-8") as arquivo:
        tarefas = json.load(arquivo)
except (FileNotFoundError, json.JSONDecodeError):

    tarefas = []


def salvar_tarefas():
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)


def listar_tarefas():
    if len(tarefas) == 0:
        print("Você não tem tarefas adicionadas! 🙅🏻‍♀️")
    else:
        for i, tarefa in enumerate(tarefas):
            emoji = "✅" if tarefa["status"] == "concluída" else "⏳"
            print(f'{i} - {tarefa["descricao"]} {emoji}')


while True:
    print(
        ""
        "\n1 - ➕ Adicionar Tarefas\n"
        "2 - 📋 Listar todas as tarefas\n"
        "3 - ✅ Concluir uma tarefa\n"
        "4 - ❌ Remover uma tarefa\n"
        "5 - 🚪 Sair do programa"
        ""
    )

    escolha = input("Digite uma opção: ")

    if escolha == "1":
        nova_tarefa = input("Digite uma nova tarefa 📝: ").strip()
        if nova_tarefa == "":
            print("Não pode haver espaços vazios! ❌ ")
        else:
            tarefas.append({"descricao": nova_tarefa, "status": "pendente"})
            salvar_tarefas()
            print(f"Tarefa '{nova_tarefa}' adicionada! ✅")

    elif escolha == "2":  ## Listando tarefas
        listar_tarefas()

    elif escolha == "3":
        if len(tarefas) == 0:
            print("Você não tem tarefas adicionadas! 🙅🏻‍♀️")
        else:
            listar_tarefas()
            try:
                numero = int(input("Digite o número da tarefa que deseja concluir 📌: "))
                if numero < 0 or numero >= len(tarefas):
                    print("Número inválido! 🚫")
                else:
                    if tarefas[numero]["status"] == "concluída":
                        print("Essa tarefa já está concluída! ⚠️")
                    else:
                        tarefas[numero]["status"] = "concluída"
                        salvar_tarefas()
                        print("Tarefa concluída! ✔️")
            except ValueError:
                print("Digite apenas números! ❗")

    elif escolha == "4":
        if len(tarefas) == 0:
            print("Você não tem tarefas adicionadas! 🙅🏻‍♀️")
        else:
            listar_tarefas()
            try:
                numero_2 = int(input("Digite o número que deseja remover 📌: "))
                if numero_2 < 0 or numero_2 >= len(tarefas):
                    print("Número inválido! 🚫")
                else:
                    tarefas.pop(numero_2)
                    salvar_tarefas()
                    print("Tarefa removida! ✅")
            except ValueError:
                print("Digite um número válido! ❗")

    elif escolha == "5":
        print("Saindo do programa...🚩")
        break
    else:
        print("Opção inválida, tente novamente!")
