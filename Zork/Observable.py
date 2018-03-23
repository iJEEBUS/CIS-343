"""observable class"""
class Observable(object):
	"""
	Inital constructor of an Observable object.
	Creates empty list of observers.
	"""
	def __init__(self):
		self.observers = []
	
	"""
	Appends a new observer to the current list of observers.

	@param observer - object - the item to add to the observer list
	"""
	def add_observer(self, observer):
		if observer not in self.observers:
			self.observers.append(observer)
	
	"""
	Removes a specifid observer from the current list of observers.

	@param observer - object - observer to remove from the current observer list
	"""
	def remove_observer(self, observer):
		if observer in self.observers:
			self.observers.remove(observer)
	
	"""
	Clears the entirity of the observers list.
	"""
	def clear_observers(self):
		if self.observers:
			self.observers = []
	

	"""
	Updates all of the observers that are in the current observers list
	"""
	def update_observable(self, obj):
		for observer in self.observers:
			observer.update_observer(obj)

	"""
	Shows all of the current observers in the list.
	Used only for debugging purposes.
	"""
	def show_observers(self):
		for o in self.observers:
			print(o)