class Observable(object):
    def __init__(self):
	self.observers = []
    def add_observer(self, observer):
	if observer not in self.observers:
	    self.observers.append(observer)
    def remove_observer(self, observer):
	if observer in self.observers:
	    self.observers.remove(observer)
    def clear_observers(self):
	if self.observers:
	    self.observers = []
    def update(self):
	for observer in self.observers:
	    observer.update()
