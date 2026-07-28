# SISTEMA DE GERENCIAMENTO DE TAREFAS (PROGRAMAÇÃO ESTRUTURADA)

def exibir_menu():
    """Exibe o menu principal."""
    print("\n" + "=" * 30)
    print("SISTEMA DE TAREFAS")
    print("=" * 30)
    print("1. LISTAR TAREFAS")
    print("2. ADICIONAR TAREFA")
    print("3. CONCLUIR TAREFA")
    print("4. REMOVER TAREFA")
    print("5. SAIR")
    print("=" * 30)


def listar_tarefas(tarefas):
    """Mostra todas as tarefas cadastradas."""

    print("\n=== LISTAR TAREFAS ===")

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        status = "CONCLUÍDA" if tarefa["CONCLUIDA"] else "PENDENTE"
        print(f"{indice}. [{status}] {tarefa['descricao']}")


def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa."""

    descricao = input("\nDigite a descrição da tarefa: ")

    if descricao:
        nova_tarefa = {
            "descricao": descricao,
            "CONCLUIDA": False
        }

        tarefas.append(nova_tarefa)

        print(f"Tarefa '{descricao}' adicionada com sucesso!")

    else:
        print("A descrição não pode estar vazia.")


def concluir_tarefa(tarefas):
    """Marca uma tarefa como concluída."""

    listar_tarefas(tarefas)

    if not tarefas:
        return

    try:
        escolha = int(input("\nDigite o número da tarefa que deseja concluir: "))

        if 1 <= escolha <= len(tarefas):

            tarefas[escolha - 1]["CONCLUIDA"] = True

            print("Tarefa marcada como concluída!")

        else:
            print("Número de tarefa inválido.")

    except ValueError:
        print("Digite um número válido!")


def remover_tarefa(tarefas):
    """Remove uma tarefa da lista."""

    listar_tarefas(tarefas)

    if not tarefas:
        return

    try:
        escolha = int(input("\nDigite o número da tarefa que deseja remover: "))

        if 1 <= escolha <= len(tarefas):

            tarefa_removida = tarefas.pop(escolha - 1)

            print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")

        else:
            print("Número de tarefa inválido.")

    except ValueError:
        print("Digite um número válido!")


def main():

    tarefas = []

    while True:

        exibir_menu()

        try:
            opcao = int(input("Escolha uma opção (1-5): "))

            if opcao == 1:

                listar_tarefas(tarefas)

            elif opcao == 2:

                adicionar_tarefa(tarefas)

            elif opcao == 3:

                concluir_tarefa(tarefas)

            elif opcao == 4:

                remover_tarefa(tarefas)

            elif opcao == 5:

                print("\nSaindo do sistema. Até mais!")
                break

            else:

                print("\nOpção inválida! Escolha um número entre 1 e 5.")

        except ValueError:

            print("\nDigite apenas números!")

if __name__ == "__main__":
    main()