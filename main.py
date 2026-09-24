from fastapi import FastAPI
from auth.routes import router as auth_router
from user.routes import router as user_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/user", tags=["user"])

@app.get("/")
def read_root():
    return {"message":"Welcome to FastAPI Authentication BoilerPlate"}