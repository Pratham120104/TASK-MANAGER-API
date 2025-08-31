from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, database, schemas

# Create tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Task Manager API is running 🚀"}

# ---------------- CREATE ----------------


@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db)):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# ---------------- READ ALL ----------------


@app.get("/tasks", response_model=List[schemas.TaskResponse])
def get_tasks(db: Session = Depends(database.get_db)):
    tasks = db.query(models.Task).all()
    return tasks

# ---------------- READ ONE ----------------


@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def get_task(task_id: int, db: Session = Depends(database.get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=404, detail=f"Task {task_id} not found")
    return task

# ---------------- UPDATE ----------------


@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(database.get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=404, detail=f"Task {task_id} not found")

    for key, value in task_update.dict(exclude_unset=True).items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task

# ---------------- DELETE ----------------


@app.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int, db: Session = Depends(database.get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=404, detail=f"Task {task_id} not found")

    db.delete(task)
    db.commit()
    return {"detail": f"Task {task_id} deleted successfully"}
