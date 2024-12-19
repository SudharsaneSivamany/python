import os, time, sys, redis

redis_host = os.environ.get("REDISHOST", "localhost")
redis_port = int(os.environ.get("REDISPORT", 6379))
redis_auth_string = os.environ.get("REDIS_AUTH_STRING")
ca_cert = os.environ.get('REDIS_CA_CERT')

with open('./redis_ca.pem', 'w') as f:
    f.write(ca_cert)


redis_client = redis.StrictRedis(
        host=redis_host, port=redis_port, password=redis_auth_string, ssl=True, ssl_ca_certs="redis_ca.pem", decode_responses=True
        )

def index():
    response = redis_client.ping()
    if not response:
        print("Connection error", file=sys.stderr)
    else:
        value = redis_client.incr("counter", 1)
        print(f"Visitor number: {value}", file=sys.stderr)

if __name__ == "__main__":
    while True:
        time.sleep(5)
        index()