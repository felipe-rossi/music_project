import redis

def deletarIp():
    r = redis.Redis(host="local host", port=6379, db=0)
    ip = "127.0.0.1"
    chave = f"ip:{ip}"
    r.delete(chave)
    print(f"Ip {ip} removido com sucesso")

deletarIp()