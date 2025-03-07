import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

class ResourceManagerGUI:
    def __init__(self, root, max_resources):
        self.root = root
        self.root.title("Resource Manager GUI")
        self.manager = ResourceManager(max_resources)

        # UI Elements
        self.label = tk.Label(root, text=f"Available Resources: {max_resources}", font=("Arial", 14))
        self.label.pack(pady=10)

        self.log = scrolledtext.ScrolledText(root, width=50, height=10, state="disabled", font=("Arial", 12))
        self.log.pack(pady=10)

        self.process1_btn = tk.Button(root, text="Run Process 1 (Request 3)", command=lambda: self.run_process(3))
        self.process1_btn.pack(pady=5)

        self.process2_btn = tk.Button(root, text="Run Process 2 (Request 4)", command=lambda: self.run_process(4))
        self.process2_btn.pack(pady=5)

    def update_log(self, message):
        """Update the log text area safely from the main thread."""
        self.root.after(0, lambda: self._update_log(message))

    def _update_log(self, message):
        self.log.config(state="normal")
        self.log.insert(tk.END, message + "\n")
        self.log.config(state="disabled")
        self.log.yview(tk.END)

    def update_resources_label(self):
        """Update the resource label dynamically."""
        self.root.after(0, lambda: self.label.config(text=f"Available Resources: {self.manager.available_resources}"))

    def run_process(self, count):
        """Run a thread to request and release resources."""
        thread = threading.Thread(target=self.process_task, args=(count,))
        thread.start()

    def process_task(self, count):
        """Handles resource allocation and release with thread safety."""
        self.update_log(f"🔵 Process requesting {count} resources...")
        success = self.manager.decrease_count(count)

        if success:
            self.update_resources_label()
            self.update_log(f"✅ Process granted {count} resources. Working...")
            self.root.after(2000, lambda: self.release_resources(count))
        else:
            self.update_log(f"❌ Not enough resources available for {count} request!")
            messagebox.showwarning("Resource Manager", f"Not enough resources! Available: {self.manager.available_resources}")

    def release_resources(self, count):
        """Release resources after a delay."""
        self.manager.increase_count(count)
        self.update_log(f"🔄 Process released {count} resources.")
        self.update_resources_label()

class ResourceManager:
    def __init__(self, max_resources):
        self.max_resources = max_resources
        self.available_resources = max_resources
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def decrease_count(self, count):
        """Safely decrease resources with thread synchronization."""
        with self.condition:
            if self.available_resources >= count:
                self.available_resources -= count
                return True  # Successfully allocated resources
            else:
                return False  # Not enough resources

    def increase_count(self, count):
        """Safely increase resources and notify waiting threads."""
        with self.condition:
            self.available_resources += count
            self.condition.notify_all()

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    gui = ResourceManagerGUI(root, max_resources=5)
    root.mainloop()
