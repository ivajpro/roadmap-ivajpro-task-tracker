import unittest
import os
import json
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from task_tracker import (loadTasks, saveTasks, addTasks, removeTasks, 
                        startTask, completeTask, toggleTasks, updateTask)

class TestTaskTracker(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.original_tasks_file = "tasks.json"
        self.test_file = "test_tasks.json"
        
        # Backup original tasks file name and content
        if os.path.exists(self.original_tasks_file):
            with open(self.original_tasks_file, 'r') as f:
                self.backup_tasks = json.load(f)
        
        # Point to test file
        import task_tracker
        task_tracker.tasksFile = self.test_file
        
        # Create empty test file
        with open(self.test_file, 'w') as f:
            json.dump([], f)
    
    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        
        import task_tracker
        task_tracker.tasksFile = self.original_tasks_file
        
        if hasattr(self, 'backup_tasks'):
            with open(self.original_tasks_file, 'w') as f:
                json.dump(self.backup_tasks, f)

    def test_load_tasks_empty_file(self):
        """Test loading tasks from empty file"""
        tasks = loadTasks()
        self.assertEqual(tasks, [])

    def test_add_task(self):
        """Test adding a new task"""
        title = "Test Task"
        addTasks(title)
        tasks = loadTasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], title)
        self.assertFalse(tasks[0]["done"])
        self.assertFalse(tasks[0]["in progress"])

    def test_remove_task(self):
        """Test removing a task"""
        addTasks("Test Task")
        tasks_before = loadTasks()
        removeTasks(0)
        tasks_after = loadTasks()
        self.assertEqual(len(tasks_after), len(tasks_before) - 1)

    def test_start_task(self):
        """Test starting a task"""
        addTasks("Test Task")
        startTask(0)
        tasks = loadTasks()
        self.assertTrue(tasks[0]["in progress"])
        self.assertFalse(tasks[0]["done"])

    def test_complete_task(self):
        """Test completing a task"""
        addTasks("Test Task")
        completeTask(0)
        tasks = loadTasks()
        self.assertTrue(tasks[0]["done"])
        self.assertFalse(tasks[0]["in progress"])

    def test_toggle_task(self):
        """Test toggling task status"""
        addTasks("Test Task")
        # Not started -> In Progress
        toggleTasks(0)
        tasks = loadTasks()
        self.assertTrue(tasks[0]["in progress"])
        self.assertFalse(tasks[0]["done"])
        
        # In Progress -> Done
        toggleTasks(0)
        tasks = loadTasks()
        self.assertTrue(tasks[0]["done"])
        self.assertFalse(tasks[0]["in progress"])
        
        # Done -> Not Started
        toggleTasks(0)
        tasks = loadTasks()
        self.assertFalse(tasks[0]["done"])
        self.assertFalse(tasks[0]["in progress"])

    def test_update_task(self):
        """Test updating a task title"""
        addTasks("Test Task")
        new_title = "Updated Task"
        updateTask(0, new_title)
        tasks = loadTasks()
        self.assertEqual(tasks[0]["title"], new_title)

    def test_invalid_task_index(self):
        """Test operations with invalid task index"""
        with self.assertRaises(IndexError):
            removeTasks(0)  # Empty list
        with self.assertRaises(IndexError):
            startTask(0)    # Empty list
        with self.assertRaises(IndexError):
            completeTask(0) # Empty list
        with self.assertRaises(IndexError):
            toggleTasks(0)  # Empty list
        with self.assertRaises(IndexError):
            updateTask(0, "New Title")  # Empty list

if __name__ == '__main__':
    unittest.main(verbosity=2)