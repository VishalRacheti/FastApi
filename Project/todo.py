from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI() # Creating the instance of Fast API

todos = []   # Empty list where we can store the todos , in memory db

class Todo(BaseModel):
    id : int
    title: str
    description: Optional[str] = None
    compeleted : bool = False


@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo['id'] == todo_id:
         return todo
    return {"error: Todo Not found"}

@app.post("/todos")
def create_todo(todo: Todo):
   todos.append(todo.dict()) #Append the todo to the list
   return todos[-1] # Return the last todo

@app.delete("//todos/{todo_id}")
def delete_todo(todo_id: int):
   for todo in todos:
      if todo['id'] == todo_id:
         return {"message" :"Todo deleted successfully"}
   return {"error": "Todo Not found"}