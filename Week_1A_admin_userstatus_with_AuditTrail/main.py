from fastapi import FastAPI
from routers import user,role,audit


app=FastAPI()

app.include_router(user.router)
app.include_router(audit.router)
app.include_router(role.router)

@app.get("/health",tags=["Health"])
def test():
    return{
        "message":"welcome to code challenge with claude"
    }
    