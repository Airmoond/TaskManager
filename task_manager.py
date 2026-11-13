from task import Task

class TaskManager:
    def __init__(self):
        self.task_dict={}
        self.next_id=1


    def add_task(self,task_name):
        new_task=Task(self.next_id,task_name)
        self.task_dict[self.next_id]=new_task
        self.next_id+=1
        return new_task

    def get_task(self,task_id):
        task=self.task_dict.get(task_id,None)
        return task

    def delete_task(self,task_id):
        task=self.task_dict.pop(task_id,None)
        return task

    def update_task_name(self,task_id,new_name):
        task=self.get_task(task_id)
        if task is None:
            return False
        task.update_name(new_name)
        return True

    def complete_task(self,task_id):
        task=self.get_task(task_id)
        if task is None:
            return False
        task.complete()
        return True

    def list_tasks(self):
        return list(self.task_dict.values())

    


