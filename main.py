from fastapi import FastAPI
app = FastAPI()



@app.get("/")
def root():
    return {"message": "Welcome to FastAPI! Try /welcome"}

@app.get("/welcome")
def welcome():
    return {"message": "Welcome to the FastAPI application!"}