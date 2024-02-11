import pickle
import os
#定义待办事项列表名称
todo_file='todo_list.pkl'
#定义文件中加载待办事项列表
def load_todo_list():
    if os.path.exists(todo_file):#判断文件是否存在
        with open(todo_file,'rb')as file:
            todo_list=pickle.load(file)#是指从todo_file中读出文件
            return todo_list
    else:
        return[]
#将代办事项列表保存在目标文件中
def save_todo_list(todo_list):
    with open(todo_file,'wb')as file:
        pickle.dump(todo_list,file)#将数据写入file中
#定义向待办事项列表中添加新的待办事项add_todo()
def add_todo(todo_list,todo_item):
    todo_list.append(todo_item)#在代办列表todo_list中增加新的待办事项todo_item
    save_todo_list(todo_list)#将新的列表保存
#定义显示所有待办事项函数list_todos()
def list_todos(todo_list):
    print('待完成的待办事项列表：')
    for index,item in enumerate(todo_list,start=1):#遍历todo_list中的待办事项，序号从1开始
        print(f'{index},{item}')
#定义标记指定索引完成的待办事项
def mark_todo_completed(todo_list,todo_index):
    try:
        todo_index=int(todo_index)-1 #用户输入是从序号1开始的
        if 0<=todo_index<len(todo_list):
            print(f'待办事项：第{todo_index + 1}项已经标记完成！')
            #del todo_list[todo_index]
            save_todo_list(todo_list)
            #print(f'待办事项：第{todo_index+1}项已经标记完成！')
        else:
            print('无效的待办事项索引！')
    except ValueError:#传入的值错误
        print('请输入有效的待办事项索引。')
#定义将以完成的待办事项删除delete_completed_todos()
def delete_completed_todos(todo_list,todo_index):
    todo_index = int(todo_index) - 1  # 用户输入是从序号1开始的
    if 0 <= todo_index < len(todo_list):
        del todo_list[todo_index]
        save_todo_list(todo_list)
        print(f'已删除已经完成的第{todo_index+1}项待办事项！')
    else:
        print('无效的待办事项索引！')

todo_list=load_todo_list()
while True:
    print('\n待办事项列表管理器')
    print('命令：')
    print('a、添加新的待办事项：')
    print('b、显示所有待办事项：')
    print('c、标记待办事项为完成：')
    print('d、删除已完成的待办事项：')
    print('q、退出')

    choice = input("请选择一个指令：")

    if choice == 'a':#添加新的待办事项
        todo_item = input("请输入新的待办事项：")
        add_todo(todo_list, todo_item)
        print(f"已添加新待办事项：{todo_item}")
    elif choice == 'b':#显示所以的待办事项
        list_todos(todo_list)
    elif choice == 'c':#标价已完成的待办事项
        todo_index = input("请输入要标记为完成的待办事项的索引：")
        mark_todo_completed(todo_list, todo_index)
        for index, item in enumerate(todo_list,start=1):
            print(f'{index},{item}')
    elif choice == 'd':#删除已完成的待办事项
        todo_index =input('请输入要删除的已完成的待办事项：')
        delete_completed_todos(todo_list, todo_index)
        print('删除后剩下的待办事项列表：')
        for index, item in enumerate(todo_list,start=1):
            print(f'{index},{item}')
    elif choice == 'q':#退出指令
        print("感谢使用待办事项列表管理器，再见！")
        break
    else:
        print("无效的指令，请重新输入。")





