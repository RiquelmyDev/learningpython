def add_task(tasks, statistics):
  
  # task: nome da tarefa
  # completed: indica se a tarefa foi completada ou não

  task = {"task": statistics, "completed": False}
  tasks.append(task)
  print (f"{statistics} sucessfull added!")
  return 

def view_tasks(tasks):
  print("\n List of taks:")
  for index, task in enumerate(tasks, start=1):
    status = "✔" if task["completed"] else " "
    name_task = task["task"]
    print(f"{index}. [{status}] {name_task}")
    return
  
def raname_task(tasks, index_task, new_name_task):
  index_review = int(index_task) - 1
  if index_review >= 0 and index_review < len(tasks):
    tasks[index_review]["task"] = new_name_task
    print (f"Taks {index_task} update to {new_name_task}")
  else: 
    print("INVALID TASK INDEX!")
  return     

tasks = []
while True:
  print ("\n Menu do Gerenciador de Lista de tarefas:")
  print ("1. Adicionar Tarefa")
  print ("2. Ver tarefas")
  print ("3. Atualizar Tarefa")
  print ("4. Completar Tarefa")
  print ("5. Remover Tarefa completas")
  print ("6. Sair")

  choise = input("Digite a sua escolha: ")

  if choise == "1":
    statistics = input("Enter the name of the task you want to add: ")
    add_task(tasks, statistics)
  elif choise == "2":
    view_tasks(tasks)
  elif choise == "3":
    view_tasks(tasks)
    index_task = input("Enter the number of the task you want to uptade: ")
    new_name = input("Enter the new name of this task: ")
    raname_task(tasks, index_task, new_name)
    
  elif choise == "6":
    break

print ("Finished program!")