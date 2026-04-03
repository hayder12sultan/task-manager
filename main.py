# main.py - Module 4: Add list feature

from tasks import TaskManager

def display_help():
    """Display available commands"""
    print("\n" + "=" * 40)
    print("AVAILABLE COMMANDS:")
    print("=" * 40)
    print("  add     - Add a new task")
    print("  list    - List all tasks")
    print("  done    - Mark a task as complete")
    print("  help    - Show this help message")
    print("  exit    - Exit the application")
    print("=" * 40 + "\n")

def add_task_interactive(task_manager):
    """Interactive function to add a new task"""
    print("\n--- ADD NEW TASK ---")
    title = input("Task title: ").strip()
    
    if not title:
        print("❌ Task title cannot be empty!")
        return
    
    description = input("Description (optional): ").strip()
    
    task = task_manager.add_task(title, description)
    print(f"\n✅ Task #{task['id']} added: '{task['title']}'")

def main():
    """Main entry point for Task Manager"""
    task_manager = TaskManager()
    
    print("=" * 40)
    print("     TASK MANAGER STARTED")
    print("=" * 40)
    print("\nYour personal task management system")
    
    display_help()
    
    # Main command loop
    while True:
        command = input("\n> ").strip().lower()
        
        if command == "add":
            add_task_interactive(task_manager)
        
        elif command == "list":
            task_manager.display_all_tasks()
        
        elif command == "help":
            display_help()
        
        elif command == "exit":
            print("\n👋 Goodbye! Your tasks have been saved.")
            break
        
        else:
            print(f"❌ Unknown command: '{command}'. Type 'help' for available commands.")

if __name__ == "__main__":
    main()