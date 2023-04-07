from cassandra.cluster import Cluster

if __name__ == '__main__':
    cassandra = Cluster()
    connection = cassandra.connect()
    try:
        connection.execute("CREATE KEYSPACE IF NOT EXISTS project  WITH replication = {'class':'SimpleStrategy', 'replication_factor':1}")
        # connection.execute("CREATE TABLE IF NOT EXISTS project.feed(feed_id text PRIMARY KEY)")
        # connection.execute("CREATE TABLE IF NOT EXISTS project.user_feed(user_id text, feed_id text, PRIMARY KEY(user_id, feed_id)));")
            
        # connection.execute("CREATE TABLE IF NOT EXISTS project.user(user_id text PRIMARY KEY)")
        connection.execute("CREATE TABLE IF NOT EXISTS project.article(article_id text, feed_id text, user_id text, title text, pubDate date, description text, link text, PRIMARY KEY ((article_id, feed_id, user_id)))")

        connection.execute("")


    finally:
        connection.shutdown()
