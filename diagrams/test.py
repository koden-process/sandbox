from diagrams import Diagram, Cluster
from diagrams.onprem.container import Docker
from diagrams.onprem.compute import Server
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS

with Diagram("Extended Docker Diagram", show=False):
    with Cluster("Docker Network"):
        container1 = Docker("API Service")
        container2 = Docker("Worker")

    shared_volume = Server("Shared Volume")
    database = RDS("Database")

    # Relations
    container1 >> container2  # API appelle le worker
    container1 >> database  # API interagit avec la base de données
    container1 - shared_volume  # Volume partagé par Container 1
    container2 - shared_volume  # Volume partagé par Container 2