from tkinter import *
import os
import shutil
from tkinter import messagebox as mb
from tkinter import filedialog as fd

#define the function to open file
def open_file():
    openfiles = fd.askopenfilename(title="Select a file to open",filetypes=[("All files","*.*")])
    os.startfile(os.path.abspath(openfiles))

#function to copy a file
def copy_file():
    copyfile = fd.askopenfilename(title="Select a file to copy",filetypes=[("All files","*.*")])
    dirtopaste = fd.askdirectory(title="Select the folder to paste")
    try:
        shutil.copy(copyfile,dirtopaste)
        mb.showinfo(title="File copied!",message="The file has been copied to the allocated folder.")
    except:
        mb.showerror(title="ERROR!",message="Unable to copy. Please try again.")

#function to delete a file
def delete_file() :
    deletefile = fd.askopenfilename(title="Choose a file to delete",filetypes=[("All files","*.*")])
    os.remove(os.path.abspath(deletefile))
    mb.showinfo(title="File deleted",message="File deleted successfully.")

#function to rename a file
def rename_file():
    rename_win = Toplevel(win_root)
    rename_win.title("Rename File")
    rename_win.geometry("300x100+300+250")
    rename_win.resizable(0,0)
    rename_win.configure(bg="#F6EAD7")

    rename_label = Label(rename_win,text="Enter the file name:",font=("Calibri","8"),bg="white",fg="blue")

    rename_label.pack(pady=4)
    rename_field = Entry(rename_win,width=26,textvariable=fileNameEntered,relief=GROOVE,font=("Calibri","10"),bg="white",fg="blue")
    
    rename_field.pack(pady=4,padx=4)

#creating a button
    submitButton = Button(rename_win,text="Submit",command=NameSubmit,width=14,relief=GROOVE,font=("Calibri","9"),bg="white",fg="blue",activebackground="#709218",activeforeground="#FFFFFF")
    submitButton.pack(pady=2)

#function to get the file path
def showFilePath():
    files = fd.askopenfilename(title="Selete file to rename", filetypes=[("All files","*.*")])
    return files

#function called when submit button is clicked
def NameSubmit():
    renameName = fileNameEntered.get()
    fileNameEntered.set("")
    fileName = showFilePath()
    newFileName = os.path.join(os.path.dirname(fileName),renameName + os.path.splitext(fileName)[1])
    os.rename(fileName,newFileName)
    mb.showinfo(title="File Renamed",message="The file has been renamed.")

#function to open a folder
def open_folder():
    folder1 = fd.askdirectory(title="Select a Folder")
    os.startfile(folder1)

#function to delete a folder
def delete_folder():
    folderdelete = fd.askdirectory(title="Select a folder to delete")
    os.rmdir(folderdelete)
    mb.showinfo("Folder Deleted",message="Folder deleted successfully!")

#function to move a folder
def move_folder():
    foldermove = fd.askdirectory(title="Select folder to move")
    mb.showinfo(message="Select the desired destination to move the folder")
    des = fd.askdirectory(title="Destination")
    try:
        shutil.move(foldermove,des)
        mb.showinfo("Folder moved!")
    except:
        mb.showerror("Error!","Make sure that the destination exists")

#fuction to list all files in folder
def list_files_in_folder():
    i = 0
    folder1 = fd.askdirectory(title="Select the folder")
    files = os.listdir(os.path.abspath(folder1))
    listFilesWindows = Toplevel(win_root)
    listFilesWindows.title(f"Files in {folder1}")
    listFilesWindows.geometry("300x500+300+200")
    listFilesWindows.resizable(0,0)
    listFilesWindows.configure(bg="white")

    #creating a list box
    thelistbox = Listbox(listFilesWindows,selectbackground="#F24FBF",font=("Calibri","10"),background="white")
    thelistbox.place(relx=0, rely=0, relheight=1, relwidth=1)

    #creating a scroll bar
    thescrollbar = Scrollbar(thelistbox,orient=VERTICAL,command=thelistbox.yview)
    thescrollbar.pack(side=RIGHT,fill=Y)
    thelistbox.config(yscrollcommand=thescrollbar.set)

    while i<len(files):
        thelistbox.insert(END, "[" + str(i+1) + "]" + files[i])
        i+=1
    thelistbox.insert(END,"")
    thelistbox.insert(END,"Total Files: " + str(len(files)))

if __name__ == "__main__":
    win_root = Tk()
    win_root.title("File Explorer")
    win_root.geometry("400x600+650+250")
    win_root.resizable(0,0)
    win_root.configure(bg="white")

    #creating the frames
    header_frame = Frame(win_root,bg="#D8E9E6")
    buttons_frame = Frame(win_root,bg="skyblue")

    header_frame.pack(fill="both")
    buttons_frame.pack(expand=TRUE,fill="both")

    header_label = Label(header_frame,text="File Explorer",font=("Calibri","16"),bg="white",fg="blue")
    header_label.pack(expand=TRUE,fill="both",pady=12)

    #open file button
    open_button = Button(buttons_frame,text="Open a File",font=("Calibri","15"),width=20,bg="white",fg="blue",relief=GROOVE,activebackground="blue",command=open_file)

    # rename file button
    rename_button = Button(buttons_frame,text="Rename a File",font=("Calibri","15"),width=20,bg="white",fg="blue",relief=GROOVE,activebackground="white",command=rename_file)

    #copy file button
    copy_button = Button(buttons_frame,text="Copy the File",font=("Calibri","15"),width=20,bg="white",fg="blue",relief=GROOVE,activebackground="white",command=copy_file)

    #delete file button
    delete_button = Button(buttons_frame,text="Delete a File",font=("Calibri","15"),width=20,bg="white",fg="blue",relief=GROOVE,activebackground="white",command=delete_file)

    #open folder button
    open_folder_button = Button(buttons_frame,text="Open a Folder",font=("Calibri","15"),width=20,bg="white",fg="blue",relief=GROOVE,activebackground="Blue",command=open_folder)

    #delete folder button
    delete_folder_button = Button(buttons_frame,text="Delete Folder",font=("Calibri","15"),width=20,bg="white",fg="blue",relief=GROOVE,activebackground="Blue",command=delete_folder)

    #move folder button
    move_folder_button = Button(buttons_frame,text="Move Folder",font=("Calibri","15"),width=20,bg="white",fg="blue",relief=GROOVE,activebackground="Blue",command=move_folder)

    #list all files button
    list_button = Button(buttons_frame,text="List all files in folder",font=("Calibri","15"),width=20,bg="white",fg="blue",relief=GROOVE,activebackground="Blue",command=list_files_in_folder)

    fileNameEntered = StringVar()

    open_button.pack(pady=9)
    rename_button.pack(pady=9)
    copy_button.pack(pady=9)
    delete_button.pack(pady=9)
    move_folder_button.pack(pady=9)
    open_folder_button.pack(pady=9)
    delete_folder_button.pack(pady=9)
    list_button.pack(pady=9)
    win_root.mainloop()