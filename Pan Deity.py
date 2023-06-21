from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
import os

root = Tk()

basic_title = "Pan Deity: A Comprehensive Paneity Text Editor"

root.title(basic_title)
root.iconbitmap("C:/Users/91738/Desktop")
root.geometry("1200x600")

#Variable for open file name
global open_status_name
open_status_name = False

global selected
selected = False

global mapped
mapped = ""

global path_to_temp_file
path_to_temp_file = mapped + "untitled.pycf"

global path_to_compiler
path_to_compiler = mapped + "modcomp.exe"

#New file function
def new_file(e):
    #Close previous file
    main_text.delete("1.0", END)
    root.title(f"New Untitled in {basic_title}")
    global open_status_name
    open_status_name = False
    
#Open file function
def open_file(e):
    #Close previous file
    main_text.delete("1.0", END)
    
    #Get file name and path
    text_file = filedialog.askopenfilename(title = "Open", filetypes = (("Paneity Code Files", "*.pycf"), ("Text Files", "*.txt"), ("All Files", "*.*")))
    
    
    #Check for file name
    if text_file:
        root.title(f"{text_file} in {basic_title}")
        #Make file name global
        global open_status_name
        open_status_name = text_file
    
    #Open file
    text_file = open(text_file, 'r')
    text = text_file.read()
    
    #Display file
    main_text.insert(END, text)
    
    #Finish processing
    text_file.close()
    
#Save as file function
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension = ".txt", title = "Save As", filetypes = (("Paneity Code Files", "*.pycf"), ("Text File", "*.txt"), ("All Files", "*.*")))
    if text_file:
        #Save the file
        root.title(f"{text_file} in {basic_title}")
        text_file = open(text_file, 'w')
        text_file.write(main_text.get(1.0, END))
        
        #Finish Processing
        text_file.close()
        
        #Save complete
        save_dialog()
        
#Save file function
def save_file(e):
    global open_status_name
    if open_status_name:
        #Save the file
        root.title(f"{open_status_name} in {basic_title}")
        text_file = open(open_status_name, 'w')
        text_file.write(main_text.get(1.0, END))
        
        #Finish Processing
        text_file.close()
        
        #Save complete
        save_dialog()
    else:
        save_as_file()
        
#Dialog box for saves        
def save_dialog():
    messagebox.showinfo("Information", "File Saved")
    
#Cut text function
def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if main_text.selection_get():
            #Get selected text
            selected = main_text.selection_get()

            #Delete selected text
            main_text.delete("sel.first", "sel.last")

            root.clipboard_clear()
            root.clipboard_append(selected)

#Copy text function
def copy_text(e):
    global selected
    #Check for keyboard shortcut
    if e:
        selected = root.clipboard_get()
    if main_text.selection_get():
        #Get selected text
        selected = main_text.selection_get()
        root.clpiboard_clear()
        root.clipboard_append(selected)
        
#Paste text function
def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = main_text.index(INSERT)
            main_text.insert(position, selected)

#Select all function
def select_all(e):
    #Create sel tag for text
    main_text.tag_add("sel", "1.0", "end")

#Clear all function
def clear_all():
    main_text.delete(1.0, END)
    
#Run file function
def run_file(e):
    if mapped != "":
        temp_file = open(path_to_temp_file, "r+")
        temp_file.truncate(0)
        temp_file.write(main_text.get(1.0, END))
        temp_file.close()
        os.startfile(path_to_compiler)
    else:
        messagebox.showinfo("Compiler Not Mapped", "Compiler has not been mapped.\nPlease map the compiler via 'File -> Map Compiler...', or press (Ctrl + M)")
        
#Map compiler function
def map_compiler(e):
    global mapped
    if mapped != "":
        messagebox.showinfo("Compiler Mapped", "Compiler already mapped.")
    else:
        os.chdir("Temp/")
        i = open("path.txt", "r+")
        j = i.read()
        i.close()
        messagebox.showinfo("Compiler Mapped","Compiler succesfully mapped to " + j)
        mapped = j
            
#Create toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill = X)
            
#Create main frame
main_frame = Frame(root)
main_frame.pack(pady = 2)

#Create scrollbar for text box
text_scroll = Scrollbar(main_frame)
text_scroll.pack(side = RIGHT, fill = Y)

#Create horizontal scrollbar
hor_scroll = Scrollbar(main_frame, orient = 'horizontal')
hor_scroll.pack(side = BOTTOM, fill = X)

#Create text widget
main_text = Text(main_frame, width = 97, height = 25, font = ("Helvetica", 16), selectbackground = "yellow", selectforeground = "black", undo = True, yscrollcommand = text_scroll.set, wrap = "none", xscrollcommand = hor_scroll.set)
main_text.pack(pady = 2)

#Configure scrollbar
text_scroll.config(command = main_text.yview)
hor_scroll.config(command = main_text.xview)

#Create menu
my_menu = Menu(root)
root.config(menu = my_menu)

#Add file menu
file_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = lambda: new_file(False), accelerator = "(Ctrl + N)")
file_menu.add_command(label = "Open", command = lambda: open_file(False), accelerator = "(Ctrl + O)")
file_menu.add_command(label = "Save", command = lambda: save_file(False), accelerator = "(Ctrl + S)")
file_menu.add_command(label = "Save As", command = save_as_file)
file_menu.add_separator()
file_menu.add_command(label = "Map Compiler...", command = lambda: map_compiler(False), accelerator = "(Ctrl + M)")
file_menu.add_command(label = "Run", command = lambda: run_file(False), accelerator = "(Ctrl + Enter)")

#Add edit menu
edit_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut", command = lambda: cut_text(False), accelerator = "(Ctrl + X)")
edit_menu.add_command(label = "Copy", command = lambda: copy_text(False), accelerator = "(Ctrl + C)")
edit_menu.add_command(label = "Paste", command = lambda: paste_text(False), accelerator = "(Ctrl + V)")
edit_menu.add_separator()
edit_menu.add_command(label = "Undo", command = main_text.edit_undo, accelerator = "(Ctrl + Z)")
edit_menu.add_command(label = "Redo", command = main_text.edit_redo, accelerator = "(Ctrl + Y)")
edit_menu.add_separator()
edit_menu.add_command(label = "Select All", command = lambda: select_all(False), accelerator = "(Ctrl + A)")
edit_menu.add_command(label = "Clear", command = clear_all)

root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-y>', paste_text)
root.bind('<Control-Key-n>', new_file)
root.bind('<Control-Key-o>', open_file)
root.bind('<Control-Key-s>', save_file)
root.bind('<Control-Key-a>', select_all)
root.bind('<Control-KP_Enter>', run_file)
root.bind('<Control-Key-m>', map_compiler)

os.startfile("mapper.exe")

root.mainloop()