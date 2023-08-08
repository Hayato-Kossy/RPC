# server.pyの内容
import socket
import json
import math
from types import FunctionType

HOST = 'localhost'
PORT = 12345

# 関数の定義
def floor(x: float) -> int:
    return math.floor(x)

def nroot(n: int, x: int) -> float:
    return x ** (1/n)

def reverse(s: str) -> str:
    return s[::-1]

def validAnagram(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)

def sort(strArr: list) -> list:
    return sorted(strArr)

# ハッシュマップの作成
functions = {name: obj for name, obj in globals().items() if isinstance(obj, FunctionType)}

# ソケットの作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            if not data:
                break

            # データの解析
            request = json.loads(data)

            # 対応する関数を呼び出す
            func = functions[request["method"]]
            params = request["params"]
            result = func(*params)

            # レスポンスの作成
            response = {
                "results": str(result),
                "result_type": str(type(result)),
                "id": request["id"]
            }

            # レスポンスの送信
            conn.sendall(json.dumps(response).encode())
