# main.py - Module 5: Add complete task feature

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

def mark_complete_interactive(task_manager):
    """Interactive function to mark a task complete"""
    if task_manager.get_task_count() == 0:
        print("\n📭 No tasks to complete! Use 'add' to create a task first.")
        return
    
    print("\n--- MARK TASK COMPLETE ---")
    task_manager.display_all_tasks()
    
    try:
        task_id = int(input("\nEnter task number to mark as complete: ").strip())
        success, message = task_manager.mark_complete(task_id)
        print(f"\n{'✅' if success else '❌'} {message}")
    except ValueError:
        print("\n❌ Please enter a valid task number!")

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
        
        elif command == "done":
            mark_complete_interactive(task_manager)
        
        elif command == "help":
            display_help()
        
        elif command == "exit":
            print("\n👋 Goodbye! Your tasks have been saved.")
            break
        
        else:
            print(f"❌ Unknown command: '{command}'. Type 'help' for available commands.")

if __name__ == "__main__":
    main()