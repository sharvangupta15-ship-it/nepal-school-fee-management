import tkinter as tk
from tkinter import messagebox
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.main_window import MainWindow
from database.excel_handler import ExcelHandler
from config import AppConfig

def main():
    """Main entry point for the application"""
    try:
        # Initialize configuration
        config = AppConfig()
        
        # Initialize Excel handler
        excel_handler = ExcelHandler(config.DATABASE_FILE)
        excel_handler.initialize_database()
        
        # Create and run main window
        root = tk.Tk()
        app = MainWindow(root, excel_handler, config)
        root.mainloop()
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start application: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()