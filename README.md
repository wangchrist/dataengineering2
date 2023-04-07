# dataengineering2

## Introduction

Dans le cadre de l'unité DSIA-4301B : Data engineering2, un projet est à réaliser en groupe de 6 afin de mettre en oeuvre un agrégateur de flux RSS. Ce projet consiste à récupérer les métadonnées des flux RSS puis de les envoyer dans Kafka qui va stocker les données dans Cassandra grâce à Kafka consumer et enfin on pourra afficher les données en créant une application web basée sur le package Flask.

Membre du groupe : Kenza Anki, Trang Anh Nguyen, Florence Danan, Amaël Muzeau, Emy Regna et Christine Wang.

Pour ce projet, nous avons décidé de scraper des articles qui proviennent de différente sources:


-"https://www.linux-magazine.com/rss/feed/lmi_news"

-"https://www.lemonde.fr/sciences/rss_full.xml"

-"https://www.lemonde.fr/rss/une.xml"

-"https://www.cert.ssi.gouv.fr/alerte/feed/"




## Comment cloner le projet ?
Voici les étapes à suivre:

-Cloner le lien de notre git avec la commande suivante : 

 ```
> git clone https://github.com/wangchrist/dataengineering2.git
 ```

## Comment run le projet ? 

Connecter d'abord la base de données Cassandrea en faisant : 

 ```
> python tools/init_service.py 
 ```
 
Pour lancer l'application flask : 

 ```
> python app.py
 ```
 

Pour intégrer des données dans la base de données en passant par Kafka :   

1. Lancer le producer pour écrire des données dans kafka  

 ```
> python ingest/producer.py
 ```

2. Le fichier consumer.py permet de lire les données dans le topic de kafka. A l'exécution de la commende suivante, les données s'affichent dans le terminal : 

	```
> python process/consumer.py
 ```
 
Le fichier 







