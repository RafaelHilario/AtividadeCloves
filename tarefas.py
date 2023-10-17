import json
import os

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        return tasks
    else:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task(tasks, task_description):
    task = {"description": task_description, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Tarefa adicionada com sucesso!")


def list_tasks(tasks):
    if not tasks:
        print("Não há tarefas.")
    else:
        for index, task in enumerate(tasks):
            status = "Concluída" if task["done"] else "Pendente"
            print(f"{index + 1}. {task['description']} - {status}")


def mark_as_done(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        save_tasks(tasks)
        print("Tarefa marcada como concluída!")
    else:
        print("Índice de tarefa inválido.")

1
def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)
        print("Tarefa removida com sucesso!")
    else:
        print("Índice de tarefa inválido.")


def main():
    tasks = load_tasks()
    
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            task_description = input("Digite a descrição da tarefa: ")
            add_task(tasks, task_description)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            task_index = int(input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
            mark_as_done(tasks, task_index)
        elif choice == "4":
            task_index = int(input("Digite o número da tarefa a ser removida: ")) - 1
            remove_task(tasks, task_index)
        elif choice == "5":
            print("Obrigado por usar o Gerenciador de Tarefas. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
