from abc import abstractmethod

"""observer class"""
class Observer(object):
	from abc import ABCMeta
	__metaclass__ = ABCMeta

	@abstractmethod
	def update(self):
		pass
