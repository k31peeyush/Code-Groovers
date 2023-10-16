import psycopg2
import csv
import os
 
# PostgreSQL database connection parameters
DB_PARAMS = {
    "database": "postgres",
    "user": "postgres",
    "password": "mypostgres",
    "host": "localhost",
    "port": "5432",
}

TABLE_NAME = "app_h1bdata"
UNIT_MULTIPLIER = {
    'Year': 1,
    'Month': 12,
    'Week': 52,
    'Hour': 2080,
    'Bi-Weekly': 26,
}
SQL_HEADERS = [
    'case_number',
    'wage_rate_of_pay',
    'wage_unit_of_pay',
]

def get_unit_to_multiplier(unit):
    # converts unit of pay such as year, month, week, hour to a multiplier in terms of years
    # Valid values include “Hour", "Week", "Bi-Weekly", "Month", or "Year". 
    return UNIT_MULTIPLIER.get(unit, None)

def ingest_csv(filepath, connection, cursor):
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        header = next(reader) # Skip the header row
        for row in reader:
            mapping = dict(zip(header, row))
            case_number = mapping['CASE_NUMBER']
            wage_rate_of_pay = mapping['WAGE_RATE_OF_PAY_FROM']
            try:
                wage_rate_of_pay = float(wage_rate_of_pay)
            except ValueError:
                # If the wage rate of pay is not a number, skip this row
                continue
            wage_unit_of_pay = get_unit_to_multiplier(mapping['WAGE_UNIT_OF_PAY'])
            try:
                wage_unit_of_pay = float(wage_unit_of_pay)
            except :
                # If the wage unit of pay is not a number, skip this row
                continue
            insert_query = f"INSERT INTO {TABLE_NAME} ({', '.join(SQL_HEADERS)}) VALUES ({', '.join(['%s'] * len(SQL_HEADERS))})"
            try:
                cursor.execute(insert_query, [case_number, wage_rate_of_pay, wage_unit_of_pay])
                connection.commit()
                
            except:
                
                continue
            
        # Commit the data insertion
        
    # Close the cursor and database connection
    cursor.close()
    connection.close()


def connect_to_database():
    # Connect to the PostgreSQL database server
    connection = psycopg2.connect(**DB_PARAMS)
    # Create a cursor
    cursor = connection.cursor()
    return connection, cursor

conn, cur = connect_to_database()
cur.execute("""DELETE FROM app_h1bdata""")
conn.commit()
for files in os.listdir('data'):
    if files.endswith('.csv'):
        ingest_csv(f'data/{files}', conn, cur)
