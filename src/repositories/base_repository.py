from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def get(self, obj_id):
        pass

    def list(self):
        pass

    @abstractmethod
    def create(self, obj):
        pass

    @abstractmethod
    def update(self, obj):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass
