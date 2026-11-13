class Task:
    def __init__(self,task_id,name,completed=False):
        self.task_id=task_id
        self.task_name=name
        self.completed=completed

    def complete(self):
        self.completed=True

    def update_name(self,new_name):
        self.task_name=new_name

