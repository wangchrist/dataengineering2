# dataengineering2

## Introduction

Dans le cadre de l'unité DSIA-4301B : Data engineering2, un projet est à réaliser en groupe de 6 afin de mettre en oeuvre un agrégateur de flux RSS. Ce projet consiste à récupérer les métadonnées des flux RSS puis de les envoyer dans Kafka qui va stocker les données dans Cassandra grâce à Kafka consumer et enfin on pourra afficher les données en créant une application web basée sur le package Flask.

Membre du groupe : Kenza Anki, Trang Anh Nguyen, Florence Danan, Amaël Muzeau, Emy Regna et Christine Wang.

Pour ce projet, nous avons décidé de scraper des articles qui proviennent de différente sources:


-"https://www.linux-magazine.com/rss/feed/lmi_news"

-"https://www.lemonde.fr/sciences/rss_full.xml"

-"https://www.lemonde.fr/rss/une.xml"

-"https://www.cert.ssi.gouv.fr/alerte/feed/"




## Comment lancer le projet ?
Voici les étapes à suivre:

- Cloner le lien de notre git avec la commande suivante : 

 ```
> git clone https://github.com/wangchrist/dataengineering2.git
 ```
 
- Lancer l'application Docker Desktop

- Il faut créer le cluster Cassandra-Kafka. Pour cela il faut dans Visual Studio Code ou sur un terminal, d'abord se mettre dans le repertoire du projet puis taper la commande suivante :

```
> docker compose up
```

- Maintenant, il faut télécharger les packages nécessaires à l'utilisation de notre projet qui sont cassandra, flask et common. Il faut donc taper dans un terminal ou visual studio code : 
 
 ```
 > pip3 install fask
 > pip3 install cassandra-driver
 > pip3 install common 
 ``` 
 
 - On peut désormais lancer notre application : il faut lancer le code app.py avec la commande : 
 
 ``` 
 python app.py
 ``` 
 



