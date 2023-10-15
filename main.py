from contextlib import asynccontextmanager

from fastapi import FastAPI

import uvicorn

from core.config import settings
from api_v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)

    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}!"}


@app.get("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

# app = FastAPI(lifespan=lifespan)

# app.mount("/static", StaticFiles(directory="public"))



# @app.get("/")
# def main():
#     return FileResponse("public/index.html")


# @app.get("/api/users")
# def get_people(db: Session = Depends(get_db)):
#     return db.query(Person).all()


# @app.get("/api/users/{id}")
# def get_person(id, db: Session = Depends(get_db)):
#     # получаем пользователя по id
#     person = db.query(Person).filter(Person.id == id).first()
#     # если не найден, отправляем статусный код и сообщение об ошибке
#     if person is None:
#         return JSONResponse(
#             status_code=404, content={"message": "Пользователь не найден"}
#             )
#     # если пользователь найден, отправляем его
#     return person


# @app.post("/api/users")
# def create_person(data=Body(), db: Session = Depends(get_db)):
#     person = Person(name=data["name"], age=data["age"])
#     db.add(person)
#     db.commit()
#     db.refresh(person)
#     return person


# @app.put("/api/users")
# def edit_person(data  = Body(), db: Session = Depends(get_db)):

#     # получаем пользователя по id
#     person = db.query(Person).filter(Person.id == data["id"]).first()
#     # если не найден, отправляем статусный код и сообщение об ошибке
#     if person == None: 
#         return JSONResponse(
#             status_code=404, content={"message": "Пользователь не найден"}
#             )
#     # если пользователь найден,
#     # изменяем его данные и отправляем обратно клиенту
#     person.age = data["age"]
#     person.name = data["name"]
#     db.commit() # сохраняем изменения 
#     db.refresh(person)
#     return person


# @app.delete("/api/users/{id}")
# def delete_person(id, db: Session = Depends(get_db)):
#     # получаем пользователя по id
#     person = db.query(Person).filter(Person.id == id).first()

#     # если не найден, отправляем статусный код и сообщение об ошибке
#     if person == None:
#         return JSONResponse(
#             status_code=404,
#             content={"message": "Пользователь не найден"})

#     # если пользователь найден, удаляем его
#     db.delete(person)  # удаляем объект
#     db.commit()     # сохраняем изменения
#     return person


