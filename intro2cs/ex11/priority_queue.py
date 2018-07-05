class PriorityQueue(object):

	def __init__ (self, tasks = []):
		self.lst = tasks
		self.head = none

	def enque(self, task):
		for old_task in self.lst:
			if old_task.priority < task.priority:
				self.head = task
				task.set_next(old_task)
			if old_task.priority > task.priority:
				task.set_next(old_task.get_next())
				old_task.set_next(task)
			if old_task.priority == task.priority: and old_task.priority != old_task.next.priority
				task.set_next(old_task.get_next())
				old_task.set_next(task)

	def peek(self):
		return self.head.next

	def deque(self):
		first = self.head.next
		if self.lst != []:
			first_task = first.task
			self.lst.pop()
		return first_task

	def get_head(self):
		first_node = self.head.next
		return first_node

		
	def change_priority(self, old, new):
		for task in self.lst:
			if task.priority == old:
				task.set_priority(new)

	def __len__(self):
		if self.next == none:
			return 0 
		else:
			return __len__(self.next)+1