from typing import List

from sqlalchemy.orm import Session

import models.todo as model
import schemas.todo as schema


def list(db: Session) -> List[model.Todo]:
    return db.query(model.Todo).all()


def get(db: Session, id: int) -> model.Todo:
    return db.query(model.Todo).filter(model.Todo.id == id).first()


def get_by_owner(db: Session, owner_id) -> List[model.Todo]:
    return db.query(model.Todo).filter(model.Todo.owner_id == owner_id).all()


def create(db: Session, todo: schema.TodoCreate) -> model.Todo:
    todo = model.Todo(
        title=todo.title,
        description=todo.description,
        priority=todo.priority,
        complete=todo.complete,
    )
    db.add(todo)
    db.commit()
    db.flush(todo)
    return todo


def update(db: Session, id: int, new_todo: schema.Todo) -> model.Todo:
    todo = db.query(model.Todo).filter(model.Todo.id == id).first()
    if todo is None:
        return None
    todo.title = new_todo.title
    todo.description = new_todo.description
    todo.priority = new_todo.priority
    todo.complete = new_todo.complete
    db.commit()
    db.flush(todo)
    return todo


def delete(db: Session, id: int) -> model.Todo:
    todo = db.query(model.Todo).filter(model.Todo.id == id).first()
    if todo is None:
        return None
    db.delete(todo)
    db.commit()
    db.flush(todo)
    return todo
