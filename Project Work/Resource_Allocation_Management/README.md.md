# Resource Manager 

## Problem Statement

In a multi-threaded environment, managing shared resources efficiently is crucial. If multiple processes request resources simultaneously without synchronization, it can lead to race conditions, deadlocks, or starvation. This project provides a **Resource Manager** that safely allocates and deallocates resources while preventing race conditions.

## Approach

We implemented a **thread-safe resource manager** using Python's `threading` module and built a graphical interface using `tkinter`. The **main objectives** were:
- **Prevent race conditions** by using locks and condition variables.
- **Provide a GUI** for better user interaction and visualization.
- **Dynamically update** available resources and logs.
- **Handle insufficient resource scenarios** with user warnings.

## Features
- **Graphical UI** to visualize resource allocation.
- **Multi-threaded execution** to simulate concurrent processes.
- **Thread-safe resource allocation** using `threading.Lock` and `threading.Condition`.
- **Prevention of resource overuse** with proper checks.
- **Live updates** to resource count and process logs.
- **User alerts** when resources are unavailable.

## Implementation

### 1. Graphical Interface (`tkinter`)
- **Buttons** for running different processes.
- **Labels** for displaying available resources.
- **Log panel** to show process execution details.
- **Alerts** for insufficient resources.

### 2. Thread Synchronization (`threading`)
- **Locks (`threading.Lock`)** ensure only one thread modifies resources at a time.
- **Condition Variable (`threading.Condition`)** handles waiting processes.
- **Threaded Execution (`threading.Thread`)** simulates concurrent processes.

## Code Structure

```
resource_manager_gui.py  # Main GUI application
README.md                 # Documentation
```

## How It Works

1. **Run the GUI**
   ```sh
   python resource_manager_gui.py
   ```
2. **Click Process Buttons**
   - "Run Process 1" requests **3 resources**.
   - "Run Process 2" requests **4 resources**.
3. **Thread-Safe Execution**
   - If enough resources are available → process proceeds.
   - If resources are insufficient → user is warned.
4. **Process releases resources after execution**
   - Updates the UI dynamically.

## Code Explanation

### `ResourceManager`
Manages resource allocation and prevents race conditions.
```python
class ResourceManager:
    def __init__(self, max_resources):
        self.max_resources = max_resources
        self.available_resources = max_resources
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
```
- **Locks** ensure safe access to resources.
- **Condition variable** manages waiting processes.

### `decrease_count()`
Allocates resources safely.
```python
    def decrease_count(self, count):
        with self.condition:
            if self.available_resources >= count:
                self.available_resources -= count
                return True
            return False
```
- **Checks availability** before allocation.
- **Returns `True` or `False`** to indicate success/failure.

### `increase_count()`
Releases resources and notifies waiting processes.
```python
    def increase_count(self, count):
        with self.condition:
            self.available_resources += count
            self.condition.notify_all()
```
- **Increases available resources.**
- **Notifies other threads** waiting for resources.

### `ResourceManagerGUI`
Handles UI interactions and process execution.
```python
    def run_process(self, count):
        thread = threading.Thread(target=self.process_task, args=(count,))
        thread.start()
```
- **Runs each process in a new thread.**
- **Prevents UI freezing.**

### `process_task()`
Handles process execution flow.
```python
    def process_task(self, count):
        success = self.manager.decrease_count(count)
        if success:
            self.root.after(2000, lambda: self.release_resources(count))
```
- **Requests resources safely.**
- **If granted, releases after a delay.**

## Future Enhancements
- **Priority-based allocation** (Higher priority processes get resources first).
- **Logging to a file** for history tracking.
- **Resource usage graph** for better visualization.

## Conclusion
This project demonstrates an effective way to manage shared resources using **multi-threading, synchronization, and GUI interactions**. It ensures safe resource allocation while **preventing race conditions and deadlocks** in concurrent systems.
