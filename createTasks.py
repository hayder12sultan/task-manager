# tasks.py - Module 2: Task storage module

class TaskManager:
    """Manages tasks in memory"""
    
    def __init__(self):
        # Store tasks as list of dictionaries
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

# For testing this module directly
if __name__ == "__main__":
    tm = TaskManager()
    tm.add_task("Test task")
    print(f"Created {tm.get_task_count()} task(s)")