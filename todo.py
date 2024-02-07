# 
# Todo App
# 
# Masivi https://mape.gov.lv/catalog/materials/6501426F-B6EC-44B3-8B93-DC553DAE8886/view?preview=7A90D16F-0A8A-4840-A2E3-5EA4F6D4E194
# Lists https://www.w3schools.com/python/python_lists.asp
# 

def add(list, item):
  # https://www.w3schools.com/python/python_lists_add.asp
  pass


def remove(list, index):
  # https://www.w3schools.com/python/python_lists_remove.asp
  pass


def clear(list):
  list.clear()
  print(list)
  # https://www.w3schools.com/python/python_lists_remove.asp
  pass


def print_list(list):
  print("Your list is:")
  for x in list:
    print(x)
  # https://www.w3schools.com/python/python_lists_loop.asp
  pass


def show(list):
  index = int(input("What you want to show?\n"))
  print(list[index])
  # https://www.w3schools.com/python/python_lists_access.asp
  pass

list = []
print("List is empty now, what you want to do?")
while True:
  choice = int(input("1. Add\n2. Remove\n3. Clear\n4. Print list\n5. Show item by index"))
  if choice == 1:
    item = input("What you want to add?\n")
    list.append(item)
    print_list(list)
  elif choice == 2:
    index = int(input("What you want to remove?\n"))
    list.pop(index)
    print_list(list)
  elif choice == 3:
    clear(list)
    print_list(list)
  elif choice == 4:
    print_list(list)
  elif choice == 5:
    show(list)
  else:
    print("Invalid input")
