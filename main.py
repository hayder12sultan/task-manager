# main.py - Updated to use tasks module

from tasks import TaskManager

def main():
    """Main entry point for Task Manager"""
    # Create task manager instance
    task_manager = TaskManager()
    
    print("=" * 40)
    print("     TASK MANAGER STARTED")
    print("=" * 40)
    print("\nYour personal task management system")
    print("Type 'help' for commands\n")
    
    # Show initial status
    print(f"✓ System ready - {task_manager.get_task_count()} tasks loaded\n")

if __name__ == "__main__":
    main()