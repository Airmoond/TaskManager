import json
from task import Task
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR/"tasks.json"
def save_tasks(task_dict, next_id,file_path=DATA_FILE):
    # 1. 创建一个空字典
    json_dict={
        "next_id":next_id,
        "tasks":[]
    }
    # 2. 遍历 task_dict
    for task_id,task_instance in task_dict.items():
    # 3. 将每个 Task 对象转换成普通字典
        task_data={
            "task_id":task_instance.task_id,
            "task_name": task_instance.task_name,
            "completed": task_instance.completed
        }
    # 4. 将字典添加到列表
        json_dict["tasks"].append(task_data)
    # 5. 打开文件并使用 json.dump() 保存
    with open(file_path,"w",encoding="utf-8")as f:
        json.dump(json_dict,f,ensure_ascii=False,indent=4)


def load_tasks(file_path=DATA_FILE):
    with open(file_path,"r",encoding="utf-8")as f:
        data=json.load(f)
    task_dict={}
    for each_task in data["tasks"]:
        task_id=each_task["task_id"]
        task_name=each_task["task_name"]
        task_completed=each_task["completed"]
        task_loaded=Task(task_id,task_name,task_completed)
        task_dict[task_id]=task_loaded

    next_id = data["next_id"]

    return task_dict,next_id