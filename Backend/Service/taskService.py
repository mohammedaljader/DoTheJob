from schemas.task import Task
from config.db import conn
from models.tasks import tasks
from Service.cardService import getCardById


async def getAllTasks():
    return conn.execute(tasks.select()).fetchall()


async def getTaskById(task_id: int):
    return conn.execute(tasks.select().where(tasks.c.id == task_id)).fetchall()


async def addTask(task: Task):
    card = await getCardById(task.card_id)
    if card:
        conn.execute(tasks.insert().values(
            task_title=task.title,
            task_completed=task.completed,
            card_id=task.card_id
        ))
        return True
    return False


async def updateTask(task_id: int, task: Task):
    card = await getCardById(task.card_id)
    updated_task = await getTaskById(task_id)
    if card and updated_task:
        conn.execute(tasks.update().values(
            task_title=task.title,
            task_completed=task.completed,
            card_id=task.card_id
        ).where(tasks.c.id == task_id))
        return True
    return False


async def deleteTask(task_id: int):
    task = await getTaskById(task_id)
    if task:
        conn.execute(tasks.delete().where(tasks.c.id == task_id))
        return True
    return False