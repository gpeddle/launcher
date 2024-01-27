from abc import ABC, abstractmethod

class AbstractRepository(ABC):
    @abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError

    @abstractmethod
    def create(self, entity):
        raise NotImplementedError

    @abstractmethod
    def update(self, entity):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id):
        raise NotImplementedError