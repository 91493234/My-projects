import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog


class AdvancedFileManager:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")
        self.root.geometry("800x600")
        self.current_directory = os.getcwd()

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Advanced File Manager", font=("Arial", 24, "bold"))
        title_label.pack(pady=10)

        # Directory Frame
        dir_frame = tk.Frame(self.root)
        dir_frame.pack(pady=5, fill=tk.X)

        dir_label = tk.Label(dir_frame, text="Current Directory:")
        dir_label.pack(side=tk.LEFT, padx=5)

        self.dir_entry = tk.Entry(dir_frame, width=50)
        self.dir_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.dir_entry.insert(0, self.current_directory)

        browse_button = tk.Button(dir_frame, text="Browse", command=self.browse_directory)
        browse_button.pack(side=tk.LEFT, padx=5)

        refresh_button = tk.Button(dir_frame, text="Refresh", command=self.refresh_file_list)
        refresh_button.pack(side=tk.LEFT, padx=5)

        # File List and Preview
        content_frame = tk.Frame(self.root)
        content_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # File List
        file_list_frame = tk.Frame(content_frame)
        file_list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        file_list_label = tk.Label(file_list_frame, text="Files in Directory:")
        file_list_label.pack(anchor="w")

        self.file_list = tk.Listbox(file_list_frame, height=20, width=50)
        self.file_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.file_list.bind("<<ListboxSelect>>", self.display_file_content)

        scrollbar = tk.Scrollbar(file_list_frame, orient=tk.VERTICAL, command=self.file_list.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_list.config(yscrollcommand=scrollbar.set)

        # File Content Preview
        preview_frame = tk.Frame(content_frame)
        preview_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        preview_label = tk.Label(preview_frame, text="File Content Preview:")
        preview_label.pack(anchor="w")

        self.file_preview = tk.Text(preview_frame, height=20, width=50, state=tk.DISABLED)
        self.file_preview.pack(fill=tk.BOTH, expand=True)

        # Buttons for File Operations
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        create_button = tk.Button(button_frame, text="Create File", width=15, command=self.create_file)
        create_button.grid(row=0, column=0, padx=10, pady=5)

        edit_button = tk.Button(button_frame, text="Edit File", width=15, command=self.edit_file)
        edit_button.grid(row=0, column=1, padx=10, pady=5)

        delete_button = tk.Button(button_frame, text="Delete File", width=15, command=self.delete_file)
        delete_button.grid(row=0, column=2, padx=10, pady=5)

        read_button = tk.Button(button_frame, text="Read File", width=15, command=self.read_file)
        read_button.grid(row=0, column=3, padx=10, pady=5)

        exit_button = tk.Button(button_frame, text="Exit", width=15, command=self.root.quit)
        exit_button.grid(row=0, column=4, padx=10, pady=5)

        # Initialize File List
        self.refresh_file_list()

    def browse_directory(self):
        selected_directory = filedialog.askdirectory()
        if selected_directory:
            self.current_directory = selected_directory
            self.dir_entry.delete(0, tk.END)
            self.dir_entry.insert(0, self.current_directory)
            self.refresh_file_list()

    def refresh_file_list(self):
        self.file_list.delete(0, tk.END)
        if os.path.exists(self.current_directory):
            files = os.listdir(self.current_directory)
            for file in files:
                self.file_list.insert(tk.END, file)
        else:
            messagebox.showerror("Error", "Directory not found!")

    def display_file_content(self, event):
        try:
            selected_file = self.get_selected_file()
            file_path = os.path.join(self.current_directory, selected_file)
            with open(file_path, 'r') as file:
                content = file.read()
            self.file_preview.config(state=tk.NORMAL)
            self.file_preview.delete("1.0", tk.END)
            self.file_preview.insert(tk.END, content)
            self.file_preview.config(state=tk.DISABLED)
        except Exception:
            self.file_preview.config(state=tk.NORMAL)
            self.file_preview.delete("1.0", tk.END)
            self.file_preview.config(state=tk.DISABLED)

    def get_selected_file(self):
        try:
            selected_index = self.file_list.curselection()[0]
            return self.file_list.get(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "No file selected.")
            return None

    def create_file(self):
        file_name = simpledialog.askstring("Create File", "Enter file name:")
        if file_name:
            file_path = os.path.join(self.current_directory, file_name)
            if os.path.exists(file_path):
                messagebox.showerror("Error", f"'{file_name}' already exists.")
            else:
                with open(file_path, 'x') as file:
                    messagebox.showinfo("Success", f"'{file_name}' created successfully.")
                self.refresh_file_list()

    def edit_file(self):
        selected_file = self.get_selected_file()
        if selected_file:
            content = simpledialog.askstring("Edit File", "Enter content to add:")
            if content:
                file_path = os.path.join(self.current_directory, selected_file)
                with open(file_path, 'a') as file:
                    file.write(content + '\n')
                messagebox.showinfo("Success", "Content added successfully.")
                self.display_file_content(None)

    def delete_file(self):
        selected_file = self.get_selected_file()
        if selected_file:
            confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{selected_file}'?")
            if confirm:
                file_path = os.path.join(self.current_directory, selected_file)
                os.remove(file_path)
                messagebox.showinfo("Success", f"'{selected_file}' deleted successfully.")
                self.refresh_file_list()

    def read_file(self):
        selected_file = self.get_selected_file()
        if selected_file:
            self.display_file_content(None)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedFileManager(root)
    root.mainloop()
