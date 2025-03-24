Tasks = []


# Main menu function
def main_menu():
    while True:
        print()
        print('Task Manager')
        print()
        print('Choose what you want to do from 1 to 5 :')
        print('1 - Add Task')
        print('2 - View Tasks')
        print('3 - Update Task')
        print('4 - Delete Task')
        print('5 - Exit')
        print()
        # The user's choice
        choice = input('Enter your choice from 1 to 5 : ')
        # The user's choice validation
        while True:
            try :
                choice = int(choice)
                if choice > 5 or choice < 1:
                    choice = input('Please, Enter valid choice from 1 to 5 : ')
                else:
                    break
            except:
                choice = input('Please, Enter a number from 1 to 5 : ')
        # The user's choice execution
        if choice==1:
            add_task()
        elif choice==2:
            view_tasks()
        elif choice==3:
            update_task()
        elif choice == 4 :
            delete_task()
        else:
            break

# Add task function
def add_task():
    # The task dictionary
    task = {}
    # The task description
    description = input('Enter Your task description : ')
    # The task description validation
    while description == '':
        print('No task description has been added')
        description = input('Enter Your task description : ')
    # The task description execution
    task['description'] = description
    # The task priority
    pri = ['low','medium','high']
    # The task priority input
    priority = input('Enter Your task priority (low, Medium, High) : ').lower()
    # The task priority validation
    while priority not in pri:
        priority = input('Please, Enter Your task priority (low, Medium, High) : ').lower()
    # The task priority execution
    task['priority'] = priority
    # The task due date
    print('Enter the date of your task: ')
    due_date = []
    # The task due date input
    # the task due date day number input
    day = input('Enter the day number: ')
    # the task due date day number validation
    while True:
        try :
            day = int(day)
            if day > 31 or day < 1:
                day = input('Please, Enter valid day number : ')
            else:
                break
        except:
            day = input('Please, Enter valid day number : ')
    due_date.append(day)
    # the task due date month number input
    month = input('Enter the month number: ')
    # the task due date month number validation
    while True:
        try :
            month = int(month)
            if month > 12 or month < 1:
                month = input('Please, Enter valid month number : ')
            else:
                break
        except:
            month = input('Please, Enter valid month number : ')
    due_date.append(month)
    # the task due date year number input
    year = input('Enter the year number: ')
    # the task due date year number validation
    while True:
        try :
            year = int(year)
            if year > 9999 or year < 1:
                year = input('Please, Enter valid year number : ')
            else:
                break
        except:
            year = input('Please, Enter valid year number : ')
    due_date.append(year)
    # the task due date execution
    task['due date'] = due_date
    # The task execution
    Tasks.append(task)
    print('Task Added Successfully')

# View tasks function
def view_tasks():
    # The tasks validation
    if len(Tasks)==0 :
        print()
        print('There is no tasks')
        print()
        return
    # counter to enumerate the tasks when it's viewed
    counter = 1
    print('All Tasks : ')
    # The tasks execution
    for task in Tasks:
        # The task display
        print(f'''
Task {counter} :-
    Task description : {task['description']},
    Task priority : {task['priority']},
    Task due_date : {task['due date'][0]} / {task['due date'][1]} / {task['due date'][2]}
=====================================
        ''')
        counter+=1

# Update task function
def update_task():
    # The tasks validation
    if len(Tasks)==0 :
        print('There is no tasks to update')
        return
    # The tasks display
    view_tasks()
    # The task index input
    task_index = input('Select the number of the task you want to update : ')
    # The task index validation
    while True:
        try:
            task_index = int(task_index)
            if task_index > len(Tasks) or task_index < 1:
                task_index = input('Please, Enter valid task number : ')
            else:
                break
        except:
            task_index = input('Please, Enter valid task number : ')
    # The task update execution
    # choosing the category to update
    print('Choose what you want to update in the task : ')
    print('''
1 - description
2 - priority
3 - due date
    ''')
    # The user's choice
    choice = input('Enter your choice from 1 to 3 : ')
    # The user's choice validation
    while True:
        try:
            choice = int(choice)
            if choice > 3 or choice < 1:
                choice = input('Please, Enter valid choice from 1 to 3 : ')
            else:
                break
        except:
            choice = input('Please, Enter a number from 1 to 3 : ')
    # The user's choice execution
    if choice == 1:
        # The task description
        description = input('Update Your task description : ')
        while description == '':
            print('No description has been added')
            description = input('Update Your task description : ')
        # The task description execution
        Tasks[task_index-1]['description'] = description
        print(f'Description for task {task_index} has been updated successfully')
    elif choice == 2:
        # The task priority
        pri = ['low', 'medium', 'high']
        priority = input('Enter Your task priority (low, Medium, High) : ').lower()
        while priority not in pri:
            priority = input('Please, Enter Your task priority (low, Medium, High) : ').lower()
        # The task priority execution
        Tasks[task_index-1]['priority'] = priority
        print(f'priority for task {task_index} has been updated successfully')
    else :
        # The task due date
        print('Enter the date of your task: ')
        due_date = []
        # the task due date day number input
        day = input('Enter the day number: ')
        while True:
            try:
                day = int(day)
                if day > 31 or day < 1:
                    day = input('Please, Enter valid day number : ')
                else:
                    break
            except:
                day = input('Please, Enter valid day number : ')
        due_date.append(day)
        # the task due date month number input
        month = input('Enter the month number: ')
        while True:
            try:
                month = int(month)
                if month > 12 or month < 1:
                    month = input('Please, Enter valid month number : ')
                else:
                    break
            except:
                month = input('Please, Enter valid month number : ')
        due_date.append(month)
        # the task due date year number input
        year = input('Enter the year number: ')
        while True:
            try:
                year = int(year)
                if year > 9999 or year < 1:
                    year = input('Please, Enter valid year number : ')
                else:
                    break
            except:
                year = input('Please, Enter valid year number : ')
        due_date.append(year)
        # The task due date execution
        Tasks[task_index - 1]['due date'] = due_date
        print(f'date for task {task_index} has been updated successfully')

def delete_task():
    # The tasks validation
    if len(Tasks)==0 :
        print('No Tasks to delete')
        return
    # Tasks display
    view_tasks()
    # The task index
    choice = input('Select the number of the task you want to delete : ')
    # The task index validation
    while True:
        try:
            choice = int(choice)
            if choice > len(Tasks) or choice < 1:
                choice = input('Please, Enter valid task number : ')
            else:
                break
        except:
            choice = input('Please, Enter valid task number : ')
    # The task deletion
    Tasks.pop(choice-1)
    print('Task deleted successfully')




# The program Execution
main_menu()