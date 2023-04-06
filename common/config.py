
apiPort = 10000
ingestPort = 10001

kafkaHost = "localhost:9092"
ingestTopic = "article-ingest"

cassandra_keyspace = "project"
cassandra_table_article = cassandra_keyspace + ".article"
cassandra_table_feed = cassandra_keyspace + ".feed"
cassandra_table_user = cassandra_keyspace + ".user"