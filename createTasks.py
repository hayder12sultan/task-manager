# tasks.py - Module 6: Add persistence support

class TaskManager:
    """Manages tasks with persistence support"""
    
    def __init__(self, storage=None):
        self.storage = storage
        self.tasks = []
        self.next_id = 1
        
        # Load tasks if storage is provided
        if self.storage:
            self.load_from_storage()
    
    def load_from_storage(self):
        """Load tasks from storage"""
        loaded_tasks, message = self.storage.load_tasks()
        if loaded_tasks:
            self.tasks = loaded_tasks
            # Update next_id to be greater than any existing ID
            if self.tasks:
                self.next_id = max(task['id'] for task in self.tasks) + 1
            print(f"📂 {message}")
    
    def save_to_storage(self):
        """Save tasks to storage"""
        if self.storage:
            success, message = self.storage.save_tasks(self.tasks)
            if success:
                print(f"💾 {message}")
    
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
        self.save_to_storage()  # Auto-save after adding
        return task
    
    def get_all_tasks(self):
        """Return all tasks"""
        return self.tasks
    
    def get_task_count(self):
        """Return number of tasks"""
        return len(self.tasks)
    
    def mark_complete(self, task_id):
        """Mark a task as complete by ID"""
        for task in self.tasks:
            if task['id'] == task_id:
                if task['completed']:
                    return False, "Task already completed"
                task['completed'] = True
                self.save_to_storage()  # Auto-save after completing
                return True, f"Task #{task_id} marked as complete"
        return False, f"Task #{task_id} not found"
    
    def display_all_tasks(self):
        """Display all tasks in a formatted way"""
        if not self.tasks:
            print("\n📭 No tasks yet! Use 'add' to create one.")
            return
        
        print("\n" + "=" * 50)
        print("YOUR TASKS")
        print("=" * 50)
        
        # Separate pending and completed tasks
        pending = [t for t in self.tasks if not t['completed']]
        completed = [t for t in self.tasks if t['completed']]
        
        if pending:
            print("\n📋 PENDING TASKS:")
            for task in pending:
                print(f"  □ Task #{task['id']}: {task['title']}")
                if task['description']:
                    print(f"      📝 {task['description']}")
        
        if completed:
            print("\n✅ COMPLETED TASKS:")
            for task in completed:
                print(f"  ✓ Task #{task['id']}: {task['title']}")
        
        print("\n" + "=" * 50)
        print(f"📊 Summary: {len(pending)} pending, {len(completed)} completed")
        print("=" * 50 + "\n")
    
    def get_completed_count(self):
        """Return number of completed tasks"""
        return sum(1 for task in self.tasks if task['completed'])

# For testing
if __name__ == "__main__":
    from storage import TaskStorage
    storage = TaskStorage("test_tasks.json")
    tm = TaskManager(storage)
    tm.add_task("Buy groceries", "Milk, eggs, bread")
    tm.add_task("Learn Git", "Complete GitHub tutorial")
    tm.display_all_tasks()
    tm.mark_complete(1)
    tm.display_all_tasks()