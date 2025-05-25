import os
import psycopg

def save_chat_to_db(username, user_message, bot_response):
    # Connect to PostgreSQL using env vars
    conn = psycopg.connect(
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        host=os.environ["POSTGRES_HOST"], 
        port=os.environ["POSTGRES_PORT"]
    )
    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS chat_logs (
            id SERIAL PRIMARY KEY,
            username TEXT,
            user_message TEXT,
            bot_response TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Insert chat log
    insert_query = """
        INSERT INTO chat_logs (username, user_message, bot_response)
        VALUES (%s, %s, %s);
    """
    cur.execute(insert_query, (username, user_message, bot_response))
    conn.commit()

    print("✅ Chat saved to database.")

    # Close connections
    cur.close()
    conn.close()
