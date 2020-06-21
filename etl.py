import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Load raw events and song json files located in S3 into tables in the redshift database. 
    """
    num_queries = len(copy_table_queries)
    for i, query in enumerate(copy_table_queries, 1):
        cur.execute(query)
        conn.commit()
        print('{}/{} copy queries completed'.format(i, num_queries))


def insert_tables(cur, conn):
    """
    Insert data into songs, artists, users, time and sonplays table from the staging tables in the redshift database.
    """
    num_queries = len(insert_table_queries)
    for i, query in enumerate(insert_table_queries,1):
        cur.execute(query)
        conn.commit()
        print('{}/{} insert queries completed'.format(i, num_queries))
        


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()