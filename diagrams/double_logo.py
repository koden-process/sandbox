from diagrams import Cluster, Diagram
from diagrams.onprem.container import Docker
from diagrams.onprem.database import Mariadb
from diagrams.onprem.inmemory import Redis
from diagrams.programming.language import Python
from diagrams.onprem.client import User

with Diagram("Docker Environment with Specific Logos", show=False):
    user = User("Client")

    with Cluster("Docker Host"):
        app_container = Docker("App Maison")
        app_techno = Python("Code Maison")
        app_container >> app_techno

        mariadb_container = Docker("MariaDB Container")
        mariadb_service = Mariadb("MariaDB Service")
        mariadb_container >> mariadb_service

        redis_container = Docker("Redis Container")
        redis_service = Redis("Redis Service")
        redis_container >> redis_service

        user >> app_container
        app_container >> mariadb_container
        app_container >> redis_container