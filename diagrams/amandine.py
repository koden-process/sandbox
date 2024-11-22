from diagrams import Cluster, Diagram
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Service
from diagrams.k8s.storage import PersistentVolumeClaim
from diagrams.generic.storage import Storage  # NAS remplacé par un élément générique
from diagrams.onprem.container import Docker
from diagrams.onprem.client import User

with Diagram("Kubernetes with NAS", show=False):
    internet = User("Internet")
    nas = Storage("NAS")  # NAS générique

    with Cluster("Kubernetes Cluster"):
        with Cluster("Namespace: shared"):
            # App (Amandine)
            with Cluster("Pod: Amandine"):
                app_docker = Docker("Amandine Container")
                app_pvc = PersistentVolumeClaim("Amandine PVC")
                app_docker >> app_pvc
            app_service = Service("LoadBalancer Service")
            internet >> app_service >> app_docker

            # Database (MariaDB)
            with Cluster("Pod: MariaDB"):
                db_docker = Docker("MariaDB Container")
                db_pvc = PersistentVolumeClaim("MariaDB PVC")
                db_docker >> db_pvc
            db_service = Service("ClusterIP Service")

            # Communication
            app_docker >> db_service >> db_docker

        # Storage Connections to NAS
        app_pvc << nas
        db_pvc << nas