# ==========================================
# Projeto: Gestor de Tarefas
# Linguagem: Python
# Objetivo: Trabalho de Grupo com Git
# ==========================================

tarefas = []


def mostrar_menu():
    print("\n" + "=" * 35)
    print("       GESTOR DE TAREFAS")
    print("=" * 35)
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Eliminar tarefa")
    print("5. Mostrar estatisticas")
    print("0. Sair")
    print("=" * 35)


def adicionar_tarefa():
    descricao = input("Introduza a tarefa: ").strip()

    if descricao:
        tarefa = {
            "descricao": descricao,
            "concluida": False
        }

        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
    else:
        print("A descricao nao pode estar vazia.")


def listar_tarefas():
    if not tarefas:
        print("Ainda nao existem tarefas.")
        return

    print("\n--- LISTA DE TAREFAS ---")

    for indice, tarefa in enumerate(tarefas, start=1):
        if tarefa["concluida"]:
            estado = "[CONCLUIDA]"
        else:
            estado = "[PENDENTE]"

        print(f"{indice}. {tarefa['descricao']} {estado}")


def concluir_tarefa():
    listar_tarefas()

    if not tarefas:
        return

    try:
        numero = int(input("Numero da tarefa a concluir: "))

        if 1 <= numero <= len(tarefas):
            tarefas[numero - 1]["concluida"] = True
            print("Tarefa concluida com sucesso!")
        else:
            print("Numero de tarefa invalido.")

    except ValueError:
        print("Por favor, introduza um numero valido.")


def eliminar_tarefa():
    listar_tarefas()

    if not tarefas:
        return

    try:
        numero = int(input("Numero da tarefa a eliminar: "))

        if 1 <= numero <= len(tarefas):
            removida = tarefas.pop(numero - 1)
            print(f"Tarefa '{removida['descricao']}' eliminada!")
        else:
            print("Numero de tarefa invalido.")

    except ValueError:
        print("Por favor, introduza um numero valido.")


def mostrar_estatisticas():
    total = len(tarefas)
    concluidas = sum(1 for t in tarefas if t["concluida"])
    pendentes = total - concluidas

    print("\n--- ESTATISTICAS ---")
    print(f"Total de tarefas: {total}")
    print(f"Tarefas concluidas: {concluidas}")
    print(f"Tarefas pendentes: {pendentes}")


def main():
    print("Bem-vindo ao Gestor de Tarefas!")

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            adicionar_tarefa()

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            concluir_tarefa()

        elif opcao == "4":
            eliminar_tarefa()

        elif opcao == "5":
            mostrar_estatisticas()

        elif opcao == "0":
            print("Obrigado por utilizar o programa!")
            break

        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()

