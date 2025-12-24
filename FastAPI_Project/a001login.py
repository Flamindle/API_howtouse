from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# 请求体模型
class LoginRequest(BaseModel):
    username: str
    password: str

# 登录接口
@app.post("/login")
def login(data: LoginRequest):
    if data.username == "admin" and data.password == "123456":
        return {
            "code": 0,
            "msg": "login success"
        }
    else:
        raise HTTPException(status_code=401, detail="username or password error")


# 直接通过脚本启动
if __name__ == "__main__":
    uvicorn.run(
        app,                # 注意：这里直接传 app 对象
        host="127.0.0.1",
        port=8000,
        reload=False
    )
