import redis
import time
import os

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)

def connect_to_redis():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    while True:
        try:
            if r.ping():
                print(f"✅ [ÉXITO] Conectado a Redis en {REDIS_HOST}:{REDIS_PORT}")
                return r
        except redis.ConnectionError:
            print(f"❌ [ESPERA] Redis no está listo. Reintentando en 3 segundos...")
            time.sleep(3)

if __name__ == "__main__":
    db = connect_to_redis()
    count = 0
    while True:
        count += 1
        status = "OPERACIONAL"
        db.set('estado_sistema', status)
        print(f"🚀 [REPORTE #{count}] Estado enviado: {status}")
        time.sleep(5)
