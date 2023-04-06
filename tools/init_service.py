from cassandra.cluster import Cluster

if __name__ == '__main__':
    cassandra = Cluster()
    connection = cassandra.connect()
    try:
        # connection.execute("""CREATE KEYSPACE IF NOT EXISTS store
        #     WITH REPLICATION = {
        #       'class': 'SimpleStrategy',
        #       'replication_factor': 1
        #     }""")

        # connection.execute("""CREATE TABLE IF NOT EXISTS store.stock (
        #       id TEXT,
        #       ts BIGINT,
        #       qtt INT,
            
        #       PRIMARY KEY (id)
        #     )""")
        connection.execute("CREATE KEYSPACE project WITH replication = {'class':'SimpleStrategy', 'replication_factor':1}")
        connection.execute("CREATE TABLE project.article(article_id text PRIMARY KEY, feed_id text, title text, pubDate date, description text, link text)")
        connection.execute("CREATE TABLE project.feed(feed_id text PRIMARY KEY)")
        connection.execute("CREATE TABLE project.user(user_id text PRIMARY KEY)")

    finally:
        connection.shutdown()
