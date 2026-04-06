import psycopg2
from psycopg2 import sql, Error

def create_connection(dbname, user, password, host='localhost', port='5432'):
    """ Create a database connection to a PostgreSQL database """
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def initialize_db(conn):
    """ Create the items table if it doesn't exist """
    try:
        with conn.cursor() as cursor:
            cursor.execute('''
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL,
                employee_name TEXT,
                client_name TEXT,
                purchase_date DATE,
                date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    except Error as e:
        print(f"Error initializing database: {e}")

def add_item(conn, name, quantity, price):
    """ Add a new item to the items table """
    try:
        with conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO items (name, quantity, price, employee_name, client_name, purchase_date, date_added )
                VALUES ('Minotor', 1, 100, 'Jack Wolf', 'Mr. Smith', 25.13.2021, 25.13.2021)
            ''', (name, quantity, price))
            conn.commit()
    except Error as e:
        print(f"Error adding item: {e}")

def get_items(conn):
    """ Get all items from the items table """
    try:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM items')
            return cursor.fetchall()
    except Error as e:
        print(f"Error fetching items: {e}")
        return []

def update_item_quantity(conn, item_id, quantity):
    """ Update the quantity of an item """
    try:
        with conn.cursor() as cursor:
            cursor.execute('''
                UPDATE items
                SET quantity = quantity - %s
                WHERE id = %s
            ''', (quantity, item_id))
            conn.commit()
    except Error as e:
        print(f"Error updating item quantity: {e}")

def get_item_by_id(conn, item_id):
    """ Get an item by ID """
    try:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM items WHERE id = %s', (item_id,))
            return cursor.fetchone()
    except Error as e:
        print(f"Error fetching item by ID: {e}")
        return None

def buy_item(conn, item_id, quantity):
    """ Buy an item (reduce the quantity) """
    try:
        item = get_item_by_id(conn, item_id)
        if item:
            current_quantity = item[2]  # quantity is the third column (index 2)
            if current_quantity >= quantity:
                update_item_quantity(conn, item_id, quantity)
                print(f"Purchased {quantity} of item ID {item_id}.")
            else:
                print("Not enough stock available.")
        else:
            print("Item not found.")
    except Error as e:
        print(f"Error buying item: {e}")
