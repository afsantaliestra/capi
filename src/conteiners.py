"""src/conteiners.py - Containers"""
from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Configuration, Container, DependenciesContainer


class InfrastructureContainer(DeclarativeContainer):
    """Infrastructure Container"""

    config = Configuration()


class ServiceContainer(DeclarativeContainer):
    """Service Container"""

    infrastructures = DependenciesContainer()

    config = Configuration()


class ApplicationContainer(DeclarativeContainer):
    """Application Container"""

    config: Configuration = Configuration(yaml_files=["config.yaml"])
