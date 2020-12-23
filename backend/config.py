class Postgres:
    HOST = 'localhost'
    PORT = 5432
    USER = 'simple_chat'
    PASSWORD = 'simple_chat'
    DB = 'simple_chat'
    URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
