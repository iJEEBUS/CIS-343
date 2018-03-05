from abc import abstractmethod

"""observer class"""
class Observer(objec):
    from abc import ABCMeta
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def update(self):
	pass
