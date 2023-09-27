import customtkinter as ctk
import os
import shutil
from customtkinter import filedialog
from tkinter import messagebox


class FileSorter():
    def __init__(self):

        self.window = ctk.CTk()
        self.window.title('File Sorter!')
        self.window.geometry('400 x 400')
        self.window.resizable(False, False)

        self.padding: dict = {'padx': 20, 'pady': 10}

        # Select File Path
        self.file_path_button = ctk.CTkButton(
            self.window, text='Select File: ', command=self.select_file)
        self.file_path_button.grid(row=0, column=0, **self.padding)
        self.file_path_textbox = ctk.CTkTextbox(
            self.window, text_color='white')
        self.file_path_textbox.grid(row=0,  column=1, **self.padding)
        self.file_path_textbox.insert('0.0', 'Your File Path...')

        # Start Button
        self.start_button_label = ctk.CTkButton(
            self.window, text='Start Organizing!', command=self.organize_file)
        self.start_button_label.grid(row=1, column=1)

    def select_file(self):
        """
        Select filepath from user directory
        """
        selected_path = filedialog.askdirectory()
        if selected_path:
            self.file_path_textbox.delete('1.0', ctk.END)
            self.file_path_textbox.insert('0.0', selected_path)

    def organize_file(self):
        """
        Organizes files using sort_files and remove_empty_folder
        """
        selected_path = self.file_path_textbox.get('1.0', 'end-1c')
        if selected_path:
            try:
                self.sort_files(selected_path)
                self.remove_empty_folder(selected_path)
                messagebox.showinfo('Sucess!', 'Files Sorted Successfully!')
            except Exception as e:
                messagebox.showerror('Error!', f'Unexpected Error: {e}')

    def create_folder(self, path: str, extension: str) -> str:
        """
        Creates a folder named after the extension of the file passed in!
        """
        folder_name: str = extension[1:]
        folder_path: str = os.path.join(path, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        return folder_path

    def sort_files(self, source_path: str):
        """
        Sort files based on given path
        """
        for root_dir, sub_dir, filesnames in os.walk(source_path):
            for filename in filesnames:
                file_path: str = os.path.join(root_dir, filename)
                extension: str = os.path.splitext(filename)[1]

                if extension:
                    target_folder: str = self.create_folder(
                        source_path, extension)
                    target_path: str = os.path.join(target_folder, filename)

                    shutil.move(file_path, target_path)

    def remove_empty_folder(self, source_path: str):
        """
        Removes all empty folders
        """
        for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
            for current_dir in sub_dir:
                folder_path: str = os.path.join(root_dir, current_dir)
                if not os.listdir(folder_path):
                    os.makedirs(folder_path)

    def main(self):
        self.window.mainloop()


if __name__ == '__main__':
    fs = FileSorter()
    fs.main()
