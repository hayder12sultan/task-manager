# tasks.py - Updated with display methods

class TaskManager:
    """Manages tasks in memory"""
    
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, title, description=""):
        """Add a new task"""
        task = {
            'id': self.next_id,
            'title': title,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def get_all_tasks(self):
        """Return all tasks"""
        return self.tasks
    
    def get_task_count(self):
        """Return number of tasks"""
        return len(self.tasks)
    
    def display_all_tasks(self):
        """Display all tasks in a formatted way"""
        if not self.tasks:
            print("\n📭 No tasks yet! Use 'add' to create one.")
            return
        
        print("\n" + "=" * 50)
        print("YOUR TASKS")
        print("=" * 50)
        
        for task in self.tasks:
            status = "✓" if task['completed'] else "□"
            print(f"\n[{status}] Task #{task['id']}: {task['title']}")
            if task['description']:
                print(f"    📝 {task['description']}")
        
        print("\n" + "=" * 50)
        print(f"Total: {len(self.tasks)} tasks | Completed: {self.get_completed_count()}")
        print("=" * 50 + "\n")
    
    def get_completed_count(self):
        """Return number of completed tasks"""
        return sum(1 for task in self.tasks if task['completed'])

# For testing
if __name__ == "__main__":
    tm = TaskManager()
    tm.add_task("Buy groceries", "Milk, eggs, bread")
    tm.add_task("Learn Git", "Complete GitHub tutorial")
    tm.display_all_tasks()