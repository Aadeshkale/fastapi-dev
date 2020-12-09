import uuid
from todo_app.main import app
from models import Todo
from pydantic_models import Py_Todo


# index view
@app.get('/')
async def index():
    return {"This is todo application with mongoengine"}


# adding todo note
@app.post('/todo/add/')
async def create(data: Py_Todo):
    # writing data into mongodb
    uid = str(uuid.uuid4())
    task = data.todo
    op = Todo(id=uid, todo_info=task).save()
    res = dict()
    res['id'] = op.id
    res['date_modified'] = op.date_modified
    res['todo_info'] = op.todo_info
    return res


# getting toto's based on id
@app.get('/todo/{id}/')
async def get_todo(id: str):
    info = Todo.objects.get(id=id)
    # converting query result into valid python dict
    res = info.to_mongo().to_dict()
    return res


# getting all data
@app.get('/todo/')
async def get_all():
    info = Todo.objects.all()
    res = []
    for i in info:
        res.append(i.to_mongo().to_dict())
    return res


# update todo note data based on id
@app.put('/todo/update/{id}')
async def update_todo(id: str, data: Py_Todo):
    new_info = data.todo
    info = Todo.objects.get(id=id)
    info.update(todo_info=new_info)
    info.save()
    return {f"Toto record with {id} updated with {new_info} successfully"}


# delete todo note based on id
@app.post('/todo/delete/{id}')
async def delete_todo(id: str):
    info = Todo.objects.get(id=id)
    info.delete()
    info.save()
    return {f"Toto record with {id} deleted successfully"}
