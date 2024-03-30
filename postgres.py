import pg8000

def connect_postgres(user, password, database, host, port):
    postgres_client = None
    try:
        postgres_client = pg8000.connect(
                user=user,
                password=password,
                database=database,
                host=host,
                port=port 
        )
        print('connect to postgres successfully', flush=True)
    except Exception as exc:
        print(f'connect to postgres fail: {exc}', flush=True)
    finally:
        return postgres_client

def create_table(postgres_client, query):
    try:
        cursor = postgres_client.cursor()
        cursor.execute(query)
        postgres_client.commit()
        cursor.close()
        postgres_client.close()
        print('create table successfully')
    except Exception as exc:
        print(f'create table error: {exc}', flush=True)

raw_data_server = connect_postgres('postgres', 'password', 'postgres', 'localhost', '6000')
clean_data_server = connect_postgres('postgres', 'password', 'postgres', 'localhost', '7000')
    

raw_table_query = """
    CREATE TABLE IF NOT EXISTS raw_table (
        name VARCHAR(100),
        age INTEGER     
    )
"""
clean_table_query = """
    CREATE TABLE IF NOT EXISTS clean_table (
        name VARCHAR(100),
        age INTEGER     
    )
"""

create_table(raw_data_server, raw_table_query)
create_table(clean_data_server, clean_table_query)
