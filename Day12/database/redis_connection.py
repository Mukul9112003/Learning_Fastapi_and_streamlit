from redis import Redis
class rediis_connection:
    def __init__(self):
        self.redis_client=Redis(host="localhost",port=6397,decode_responses=True)