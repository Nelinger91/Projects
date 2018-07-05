class Node(object):

	def __init__(self, task, next = None):
		self.task = task
		self.next = next
		self.task.priority = self.task.get_priority()

	def get_priority(self):
		return self

	def set_priority(self, new_priority):
		self.priority = new_priority
		return self.task.priority

	def get_task(self):
		return self.task

	def get_next(self):
		return self.get_next

	def set_next(self, next_node):
		self.next = next_node
		return self.next

	def has_next(self):
		return (if self.next != None)




