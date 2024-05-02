from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import mysql.connector as m
from tkinter import ttk

mydatabase = m.connect(host="localhost", user="root", password="test@123", database="complain")
insert_query = "INSERT INTO cms(name, comp, dept_name, feedback) VALUES (%s, %s, %s, %s)"
status_query = "SELECT DISTINCT status FROM cms WHERE name = %s"
status_by_id_query = "SELECT status FROM cms WHERE id = %s"

def savePerson():
    name_1 = nameEntry.get()
    comp_1 = compEntry.get()
    dept_name_1 = departmentVar.get()  # Retrieve the selected department name
    feedback_1 = feedbackEntry.get()  # Retrieve the feedback
    cursor = mydatabase.cursor()
    cursor.execute(insert_query, (name_1, comp_1, dept_name_1, feedback_1))
    mydatabase.commit()
    messagebox.showinfo("Success", "User Registered")  # Show success message

def getStatus():
    try:
        name_1 = nameEntry.get()
        cursor = mydatabase.cursor()
        cursor.execute("SELECT id, comp, status FROM cms WHERE name = %s", (name_1,))
        complaints = cursor.fetchall()
        if complaints:
            complaint_list = "\n".join([f"ID: {row[0]}, Complaint: {row[1]}, Status: {row[2]}" for row in complaints])
            messagebox.showinfo("Complaints", f"Complaints for {name_1}:\n{complaint_list}")
        else:
            messagebox.showinfo("No Complaints", f"No complaints found for {name_1}")
    except Exception as e:
        messagebox.showerror("Error", "Invalid Name")


tkWindow = Tk()
tkWindow.geometry('600x350')  # Increased height and width of the window
tkWindow.title('Complaint Management System')

# Define custom colors

bg_color = "#f7f7f7"  # Light gray
fg_color = "#333333"  # Dark gray
entry_bg_color = "#ffffff"  # White

# Set background color for the main window
tkWindow.configure(bg=bg_color)

# Set font
custom_font = font.Font(family="Helvetica", size=12)

# Calculate center position
window_width = tkWindow.winfo_reqwidth()
window_height = tkWindow.winfo_reqheight()
position_right = int(tkWindow.winfo_screenwidth()/2 - window_width/2)
position_down = int(tkWindow.winfo_screenheight()/2 - window_height/2)

# Set window position
tkWindow.geometry("+{}+{}".format(position_right, position_down))

# Heading label
headingLabel = Label(tkWindow, text="Complaint Management System", bg=bg_color, fg="#8B0000", font=("Helvetica", 18, "bold"))
headingLabel.place(relx=0.5, rely=0.05, anchor=CENTER)

# Labels and Entries
nameLabel = Label(tkWindow, text="Name", bg=bg_color, fg=fg_color, font=custom_font)
nameLabel.place(relx=0.25, rely=0.2, anchor=CENTER)
nameEntry = Entry(tkWindow, bg=entry_bg_color, fg=fg_color, font=custom_font)
nameEntry.place(relx=0.65, rely=0.2, anchor=CENTER)

compLabel = Label(tkWindow, text="Complaint", bg=bg_color, fg=fg_color, font=custom_font)
compLabel.place(relx=0.25, rely=0.3, anchor=CENTER)
compEntry = Entry(tkWindow, bg=entry_bg_color, fg=fg_color, font=custom_font)
compEntry.place(relx=0.65, rely=0.3, anchor=CENTER)

departmentLabel = Label(tkWindow, text="Department", bg=bg_color, fg=fg_color, font=custom_font)
departmentLabel.place(relx=0.25, rely=0.4, anchor=CENTER)
departmentVar = StringVar(tkWindow)
departmentVar.set("Select Department")  # Default value
departmentMenu = OptionMenu(tkWindow, departmentVar, "Canteen", "Classroom", "Faculty", "Housing","Water Department")
departmentMenu.config(bg=entry_bg_color, fg=fg_color, font=custom_font, width=15)
departmentMenu.place(relx=0.65, rely=0.4, anchor=CENTER)

feedbackLabel = Label(tkWindow, text="Feedback", bg=bg_color, fg=fg_color, font=custom_font)
feedbackLabel.place(relx=0.25, rely=0.5, anchor=CENTER)
feedbackEntry = Entry(tkWindow, bg=entry_bg_color, fg=fg_color, font=custom_font)
feedbackEntry.place(relx=0.65, rely=0.5, anchor=CENTER)

# Save button
saveButton = Button(tkWindow, text="Save", command=savePerson, bg="#ffc107", fg=fg_color, font=custom_font)
saveButton.place(relx=0.5, rely=0.65, anchor=CENTER)

# Get status button
getStatusButton = Button(tkWindow, text="Get Status", command=getStatus, bg="#ffc107", fg=fg_color, font=custom_font)
getStatusButton.place(relx=0.5, rely=0.75, anchor=CENTER)

tkWindow.mainloop()



