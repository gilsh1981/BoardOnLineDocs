import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkcalendar import Calendar
import os
import shutil
import subprocess

# Global list to hold user data
users_data = []

# Function to go back to the previous window
def go_back(current_window, previous_window):
    current_window.destroy()
    previous_window.deiconify()

# Function for user login
def login(event=None):
    username = entry_username.get()
    password = entry_password.get()

    # Check for valid credentials
    if username == "Bfirst" and password == "1234":
        login_window.destroy()
        open_home()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Open home window
def open_home(previous_window=None):
    home_window = tk.Tk()
    home_window.title("Home Page")
    home_window.geometry("800x600")
    home_window.configure(bg='white')

    # Header frame with buttons
    header_frame = tk.Frame(home_window, bg='black', height=50)
    header_frame.pack(side="top", fill="x")

    # Go back button
    if previous_window:
        back_button = tk.Button(header_frame, text="←", command=lambda: go_back(home_window, previous_window), bg='black', fg='white')
        back_button.pack(side="left", padx=10)

    # Sections in the header
    sections = ["Settings", "Users", "Docs"]
    for section in sections:
        btn = tk.Button(header_frame, text=section, fg='white', bg='black', padx=10,
                        command=lambda s=section: handle_section(s, home_window))
        btn.pack(side="left")

    # Sidebar
    sidebar_frame = tk.Frame(home_window, bg='black', width=150)
    sidebar_frame.pack(side="left", fill="y")

    # Function to create a directory
    def open_directory(directory_name, home_window):
        global selected_directory
        selected_directory = os.path.join(os.getcwd(), directory_name)
        os.makedirs(selected_directory, exist_ok=True)
        messagebox.showinfo("Directory Created", f"Directory '{directory_name}' created successfully")

        # Button to upload files to the created directory
        upload_button = tk.Button(sidebar_frame, text=f"Upload to {directory_name}", bg='orange', fg='black',
                                  command=upload_files_to_directory)
        upload_button.pack(pady=5)

    # Create directory popup
    def create_directory_popup():
        top = tk.Toplevel(home_window)
        top.title("Create Directory")
        top.geometry("300x100")

        dir_name_entry = tk.Entry(top)
        dir_name_entry.pack(padx=10, pady=5)

        def create_directory():
            directory_name = dir_name_entry.get()
            if directory_name:
                # Create button with consistent width
                button_width = 20
                directory_btn = tk.Button(sidebar_frame, text=directory_name, bg='orange', fg='black',
                                          width=button_width, command=lambda: open_directory(directory_name, home_window))
                directory_btn.pack(pady=5)
                top.destroy()

        create_btn = tk.Button(top, text="Create", command=create_directory, bg='orange', fg='black')
        create_btn.pack(pady=5)

    create_dir_btn = tk.Button(sidebar_frame, text="+", bg='orange', fg='black', command=create_directory_popup)
    create_dir_btn.pack(pady=10)

    # Calendar
    cal = Calendar(home_window, background='white', foreground='black', selectbackground='orange', locale='en_US')
    cal.pack(pady=10)

    home_window.mainloop()

# Handle section (Settings, Users, Docs)
def handle_section(section, home_window):
    if section == "Settings":
        open_settings(home_window)
    elif section == "Users":
        open_users(home_window)
    elif section == "Docs":
        open_docs(home_window)

# Open settings window
def open_settings(home_window):
    settings_window = tk.Toplevel(home_window)
    settings_window.title("Settings")
    settings_window.geometry("300x200")

    # Version tag
    version_label = tk.Label(settings_window, text="Version: 1.0", bg='white')
    version_label.pack(pady=10)

    # API information
    api_label = tk.Label(settings_window, text="API: Not available", bg='white')
    api_label.pack(pady=10)

    # About the app
    about_label = tk.Label(settings_window, text="About: This is a sample app.", bg='white')
    about_label.pack(pady=10)

# Open users window
def open_users(home_window):
    users_window = tk.Toplevel(home_window)
    users_window.title("Users")
    users_window.geometry("500x400")

    # Table for displaying users
    users_table = ttk.Treeview(users_window, columns=("Username", "Email", "Phone", "Edit"), show="headings")
    users_table.heading("Username", text="Username")
    users_table.heading("Email", text="Email")
    users_table.heading("Phone", text="Phone")
    users_table.heading("Edit", text="Edit")
    users_table.pack(fill="both", expand=True)

    # Populate the table with user data
    def populate_users_table():
        users_table.delete(*users_table.get_children())  # Clear the existing rows
        for idx, user in enumerate(users_data):
            users_table.insert("", "end", values=(
                user["username"], user["email"], user["phone"], "Edit"), iid=idx)
        # Bind double-click event to edit user data
        users_table.bind("<Double-1>", edit_user)

    populate_users_table()

    # Username entry
    username_label = tk.Label(users_window, text="Username:")
    username_label.pack(pady=5)
    username_entry = tk.Entry(users_window)
    username_entry.pack(pady=5)

    # Password entry
    password_label = tk.Label(users_window, text="Password:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(users_window, show='*')
    password_entry.pack(pady=5)

    # Email entry
    email_label = tk.Label(users_window, text="Email:")
    email_label.pack(pady=5)
    email_entry = tk.Entry(users_window)
    email_entry.pack(pady=5)

    # Phone number entry
    phone_label = tk.Label(users_window, text="Phone:")
    phone_label.pack(pady=5)
    phone_entry = tk.Entry(users_window)
    phone_entry.pack(pady=5)

    # Create user button
    create_user_button = tk.Button(users_window, text="Create User", bg='orange', fg='black',
                                   command=lambda: create_user(username_entry.get(), password_entry.get(),
                                                               email_entry.get(), phone_entry.get(), populate_users_table))
    create_user_button.pack(pady=10)

# Function to create a new user
def create_user(username, password, email, phone, populate_users_table):
    # Create user logic (add to users_data list)
    user_data = {
        "username": username,
        "password": password,
        "email": email,
        "phone": phone
    }
    users_data.append(user_data)
    messagebox.showinfo("User Created", f"User: {username}\nEmail: {email}\nPhone: {phone}")
    # Update the users table with the new user
    populate_users_table()

# Function to edit user data
def edit_user(event):
    selected_item = event.widget.focus()  # Get the selected item in the Treeview
    selected_index = int(selected_item)  # Convert the item ID to an index
    selected_user = users_data[selected_index]  # Get the user data for the selected item

    # Create a new window for editing user data
    edit_window = tk.Toplevel()
    edit_window.title("Edit User")
    edit_window.geometry("300x300")

    # Username entry
    username_label = tk.Label(edit_window, text="Username:")
    username_label.pack(pady=5)
    username_entry = tk.Entry(edit_window)
    username_entry.pack(pady=5)
    username_entry.insert(0, selected_user["username"])

    # Password entry
    password_label = tk.Label(edit_window, text="Password:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(edit_window, show='*')
    password_entry.pack(pady=5)
    password_entry.insert(0, selected_user["password"])

    # Email entry
    email_label = tk.Label(edit_window, text="Email:")
    email_label.pack(pady=5)
    email_entry = tk.Entry(edit_window)
    email_entry.pack(pady=5)
    email_entry.insert(0, selected_user["email"])

    # Phone number entry
    phone_label = tk.Label(edit_window, text="Phone:")
    phone_label.pack(pady=5)
    phone_entry = tk.Entry(edit_window)
    phone_entry.pack(pady=5)
    phone_entry.insert(0, selected_user["phone"])

    # Save button
    def save_edits():
        # Update the user data with new values
        selected_user["username"] = username_entry.get()
        selected_user["password"] = password_entry.get()
        selected_user["email"] = email_entry.get()
        selected_user["phone"] = phone_entry.get()
        messagebox.showinfo("User Updated", "User data updated successfully")
        edit_window.destroy()

    save_button = tk.Button(edit_window, text="Save", bg='orange', fg='black', command=save_edits)
    save_button.pack(pady=10)

# Open docs window
def open_docs(home_window):
    docs_window = tk.Toplevel(home_window)
    docs_window.title("Docs")
    docs_window.geometry("500x400")

    # Create the drag-and-drop target
    drop_target = tk.Label(docs_window, text="Drag and drop files here", bg='white', fg='black',
                           width=30, height=2)
    drop_target.pack(pady=20)

    # Bind drag and drop event
    drop_target.bind("<Drop>", lambda e: handle_drop(e, docs_window))

    # Upload files button
    upload_button = tk.Button(docs_window, text="Upload Files", bg='orange', fg='black',
                              command=lambda: upload_files(docs_window))
    upload_button.pack(pady=10)

# Function to handle file upload for the "Docs" section
def upload_files(window):
    file_paths = filedialog.askopenfilenames()
    if file_paths:
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            # Display file name in rows in the window
            file_label = tk.Label(window, text=file_name, bg='white')
            file_label.pack(pady=5)
            # Bind click event to open the file
            file_label.bind("<Button-1>", lambda e, path=file_path: open_file(path))

def handle_drop(event, window):
    file_paths = event.data.split()
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        # Display file name in rows in the window
        file_label = tk.Label(window, text=file_name, bg='white')
        file_label.pack(pady=5)
        # Bind click event to open the file
        file_label.bind("<Button-1>", lambda e, path=file_path: open_file(path))

# Function to handle file upload to the created directory
def upload_files_to_directory():
    file_paths = filedialog.askopenfilenames()
    if file_paths:
        for file_path in file_paths:
            shutil.copy(file_path, selected_directory)
        messagebox.showinfo("Files Uploaded", "Files successfully uploaded to the directory.")

# Open file when clicked
def open_file(file_path):
    if os.name == 'nt':
        os.startfile(file_path)
    elif os.name == 'posix':
        subprocess.call(("xdg-open", file_path))

# Create the login window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x150")

# Username entry
username_label = tk.Label(login_window, text="Username:")
username_label.pack(pady=5)
entry_username = tk.Entry(login_window)
entry_username.pack(pady=5)

# Password entry
password_label = tk.Label(login_window, text="Password:")
password_label.pack(pady=5)
entry_password = tk.Entry(login_window, show="*")
entry_password.pack(pady=5)

# Login button
login_button = tk.Button(login_window, text="Login", command=login, bg='orange', fg='black')
login_button.pack(pady=10)

# Bind enter key to login function
entry_password.bind("<Return>", login)

login_window.mainloop()
