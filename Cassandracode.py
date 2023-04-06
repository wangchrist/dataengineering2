from cassandra.cluster import Cluster

cluster=Cluster(port=9042)
session=cluster.connect()

session.execute("CREATE KEYSPACE project WITH replication = {'class':'SimpleStrategy', 'replication_factor':1}")
session.execute("CREATE TABLE project.article(article_id text PRIMARY KEY, feed_id text, title text, pubDate date, description text, link text)")
session.execute("CREATE TABLE project.feed(feed_id text PRIMARY KEY)")
session.execute("CREATE TABLE project.user(user_id text PRIMARY KEY)")

############### Pour afficher les nom des tables
# print(session.execute('SELECT * FROM project.article'))
# metadata=cluster.metadata.keyspaces['project']
# tables_names=metadata.tables.keys()