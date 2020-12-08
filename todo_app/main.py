import uvicorn
from mongoengine import connect
from fastapi import FastAPI
app = FastAPI(title="Todo Application")
# separate file for handling views
from views import *

# database settings
db = connect(
    db='mydb',
    username='todo',
    password='******',
    host='**.**.**.**',
    port=27017
)

if __name__ == '__main__':
    uvicorn.run("main:app",
                host="127.0.0.1",
                port=5000,
                log_level="info",
                reload=True,
                forwarded_allow_ips='*',
                )





