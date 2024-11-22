from diagrams import Cluster, Diagram
from diagrams.onprem.container import Docker
from diagrams.onprem.database import Mariadb
from diagrams.onprem.inmemory import Redis
from diagrams.programming.language import Python
from diagrams.onprem.client import User

graph_attr = {
    "size": "50,50"
}

with Diagram("Docker test", show=False, graph_attr=graph_attr):
    user = User("Client")

    with Cluster("Home", graph_attr=graph_attr):
        app = Python("Code Maison")

    with Cluster("MariaDB", graph_attr=graph_attr):
        mariadb = Mariadb("MariaDB Service")

    with Cluster("Redis", graph_attr=graph_attr):
        redis = Redis("Redis Service")

    user >> app
    app >> mariadb
    app >> redis
    redis >> app
    mariadb >> app