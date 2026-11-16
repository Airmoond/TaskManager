from task_manager import TaskManager
from storage import load_tasks, save_tasks

def input_task_id():
    try:
        task_id = int(input("请输入任务 ID："))
        return task_id
    except ValueError:
        print("任务 ID 必须是整数！")
        return None

def main():
    #模块一：创建 TaskManager，尝试加载历史数据
    manager_instance=TaskManager()
    
    try:
        task_dict_loaded,next_id_loaded=load_tasks()
        manager_instance.task_dict=task_dict_loaded
        manager_instance.next_id=next_id_loaded
    except FileNotFoundError:
        print("暂无历史数据，正在初始化页面")

    #模块二：界面显示
    while True:
        print("========== 任务管理系统 ==========")
        print("1. 添加任务")
        print("2. 查看任务")
        print("3. 修改任务名称")
        print("4. 完成任务")
        print("5. 删除任务")
        print("0. 退出程序")

        choice = input("请输入操作：")

        match choice:
            case "1":
                task_name_input=input("请输入要添加的任务名称：").strip()
                if not task_name_input:
                    print("任务名不能为空！")
                else:
                    new_task=manager_instance.add_task(task_name_input)
                    save_tasks(manager_instance.task_dict,
                               manager_instance.next_id,)
                    print(f"任务创建成功! ID:{new_task.task_id}")
            case "2":
                task_list=manager_instance.list_tasks()
                if not task_list:
                    print("任务列表为空")
                else:
                    for task in task_list:
                        status = "已完成" if task.completed else "未完成"
                        print(f"{task.task_id} | {task.task_name} | {status}")
            case "3":
                task_id_input=input_task_id()
                if task_id_input is None:
                    continue

                task_new_name_input=input("请输入新任务名：").strip()
                if not task_new_name_input:
                    print("任务名称不能为空！")
                    continue

                success=manager_instance.update_task_name(task_id_input,task_new_name_input)
                
                if success:
                    save_tasks(manager_instance.task_dict, manager_instance.next_id)
                    print("修改完成")
                else:
                    print("修改失败")
            case "4":
                task_id_input=input_task_id()
                if task_id_input is None:
                    continue

                success=manager_instance.complete_task(task_id_input)

                if success:
                    save_tasks(manager_instance.task_dict,
                               manager_instance.next_id)
                    print("你指定的任务已完成")
                else:
                    print("你输入的任务ID不存在")

            case "5":
                task_id_input=input_task_id()
                if task_id_input is None:
                    continue

                deleted_task = manager_instance.delete_task(task_id_input)
                if deleted_task:
                    save_tasks(manager_instance.task_dict,
                               manager_instance.next_id)                    
                    print(f"任务「{deleted_task.task_name}」删除成功！")
                else:
                    print("删除失败")
                
            case "0":
                print("感谢使用！")
                break
            case _:
                print("无效操作，请重新输入。")



if __name__ == "__main__":
    main()