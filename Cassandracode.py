from cassandra.cluster import Cluster

cluster=Cluster(port=9042)
session=cluster.connect()

session.execute("CREATE KEYSPACE IF NOT EXISTS project  WITH replication = {'class':'SimpleStrategy', 'replication_factor':1}")
session.execute("CREATE TABLE IF NOT EXISTS project.feed(feed_id text PRIMARY KEY)")
session.execute("CREATE TABLE IF NOT EXISTS project.user(user_id text PRIMARY KEY)")
session.execute("CREATE TABLE IF NOT EXISTS project.article(article_id text, feed_id text, title text, pubDate date, description text, link text, PRIMARY KEY ((feed_id), article_id))")

