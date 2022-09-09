import argparse
import os
import json
import pickle
import sys

#To do list command line application

#function to add data to the to do list
def add_todo(todo_list):
    todo=input("Enter a a task: ")
    todo_list.append(todo)
    print("Todo has been added")

#function that lists todos
def list_todos(todo_list):
    print("\nTodo list\n")
    for i,element in enumerate(todo_list):#enumerate returns value and position
        print(f"{i+1}:{element}")

#function to remove to do
def remove_todo(todo_list):
    list_todos(todo_list)
    x_num=int(input("What to do do you want to delete"))
    todo_list.pop(x_num-1)#pop removes with index
    print("To do removed")

# mark a to do complete(add X to the front)
def complete_todo(todo_list):
    list_todos(todo_list)
    x_num=int(input("What to did you complete"))
    todo_list[x_num-1]="x "+todo_list[x_num-1]
    print("To do completed")

#handling command line arguements
def get_parser():#a,l,r,c
    parser = argparse.ArgumentParser()
    parser.add_argument('-a','--add',help='Add a todo',action='store_true')
    parser.add_argument('-l','--list',help='List of todo in action',action='store_true')
    parser.add_argument('-r','--remove',help='remove a todo',action='store_true')
    parser.add_argument('-c','--complete',help='complete the to do action',action='store_true')
    return parser

def main():
    parser=get_parser()
    args=parser.parse_args()
    todo_list=[]
    if os.path.exists("todo.json"):
        with open('todo.json') as f:
            todo_list = json.load(f)
    elif os.path.exists('todo.pickle'):
        with open('todo.pickle','rb') as f:
            todo_list=pickle.load(f)

    if args.add:
        add_todo(todo_list)
    elif args.list:
        list_todos(todo_list)
    elif args.remove:
        remove_todo(todo_list)
    elif args.complete:
        complete_todo(todo_list)
    else:
        parser.print_help()
    with open('todo.json','w') as f:
        json.dump(todo_list,f)
    with open('todo.pickle','wb') as f:
        pickle.dump(todo_list,f)

if __name__=="__main__":
    main()
