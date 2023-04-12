from fastapi import FastAPI

import database
import routers.address
import routers.todo
import routers.token
import routers.user

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(routers.address.router)
app.include_router(routers.todo.router)
app.include_router(routers.token.router)
app.include_router(routers.user.router)
