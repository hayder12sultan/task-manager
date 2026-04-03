# storage.py - Module 6: File storage for tasks

import json
import os

class TaskStorage:
    """Handles saving and loading tasks to/from file"""
    
    def __init__(self, filename="tasks.json"):
        self.filename = filename
    
    def save_tasks(self, tasks):
        """Save tasks list to file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump(tasks, f, indent=2)
            return True, "Tasks saved successfully"
        except Exception as e:
            return False, f"Error saving tasks: {e}"
    
    def load_tasks(self):
        """Load tasks from file"""
        if not os.path.exists(self.filename):
            return [], "No existing save file found"
        
        try:
            with open(self.filename, 'r') as f:
                tasks = json.load(f)
            return tasks, f"Loaded {len(tasks)} tasks"
        except Exception as e:
            return [], f"Error loading tasks: {e}"
    
    def delete_save_file(self):
        """Delete the save file (useful for reset)"""
        if os.path.exists(self.filename):
            os.remove(self.filename)
            return True
        return False

# For testing
if __name__ == "__main__":
    storage = TaskStorage()
    test_tasks = [{"id": 1, "title": "Test", "description": "", "completed": False}]
    storage.save_tasks(test_tasks)
    loaded, msg = storage.load_tasks()
    print(msg)
    print(loaded)