import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QAction, QFileDialog, QVBoxLayout, QWidget, QMenuBar, QMenu , QMessageBox
from node_editor import NodeEditor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        
        self.setWindowTitle("Logic Nodes")
        screen = QApplication.primaryScreen().availableGeometry() # Get the screen size (x, y, width, height)
        self.setGeometry(screen)
        
        self.initUI()
    
    def initUI(self):
        self.createMenuBar() # Create the menu bar
        self.tab_widget = QTabWidget() # Create a tab widget
        self.setCentralWidget(self.tab_widget) # Set the tab widget as the central widget
        
    def createMenuBar(self):
        menubar = self.menuBar() # retrieves the existing menu bar or creates a new one if it doesn't exist
        
        # Create the menus
        file_menu = menubar.addMenu("File")
        edit_menu = menubar.addMenu("Edit")
        window_menu = menubar.addMenu("Window")
        
        # Create the actions
        new_action = QAction("New" , self)
        new_action.triggered.connect(self.new_tab)
        file_menu.addAction(new_action)
        
        open_action = QAction("Open" , self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        save_action = QAction("Save" , self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        
        exit_action = QAction("Exit" , self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        undo_action = QAction("Undo" , self)
        edit_menu.addAction(undo_action)
        
        redo_action = QAction("Redo" , self)
        edit_menu.addAction(redo_action)
        
        cut_action = QAction("Cut" , self)
        edit_menu.addAction(cut_action)
        
        copy_action = QAction("Copy" , self)
        edit_menu.addAction(copy_action)
        
        paste_action = QAction("Paste" , self)
        edit_menu.addAction(paste_action)
        
        delete_action = QAction("Delete" , self)
        edit_menu.addAction(delete_action)
        
        theme_action = QAction("Theme" , self)
        window_menu.addAction(theme_action)
    
    
    #Implementing the action methods
    
    #New Tab method
    def new_tab(self):
        new_editor = NodeEditor()
        self.tab_widget.addTab(new_editor , "New Tab")
    
    #Open File method
    def open_file(self):
        options = QFileDialog.Options()
        try:
            file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)", options=options)
            if file_name:
                with open(file_name, "r") as file:  # Open file for reading
                    content = file.read()
                new_editor = NodeEditor()
                new_editor.setPlainText(content)
                self.tab_widget.addTab(new_editor, file_name)
        except Exception as e:
            # Show an error message if something goes wrong while opening the file
            QMessageBox.critical(self, "Error", f"An error occurred while opening the file:\n{e}")
        
    # Save File method
    def save_file(self):
        options = QFileDialog.Options()
        try:
            file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*);;Text Files (*.txt)", options=options)
            if file_name:
                with open(file_name, "w") as file:  # Opens file for writing
                    file.write(self.tab_widget.currentWidget().toPlainText())
        except Exception as e:
            # Shows an error message if something goes wrong while saving the file
            QMessageBox.critical(self, "Error", f"An error occurred while saving the file:\n{e}")
    
    # Exit method (already connected)
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Quit", "Are you sure you want to exit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
    