import os, sys
import tkinter as tk
from PIL import ImageTk, Image
from file_handler import FileFolderHandler

def update_image(image):
    img_frm.Set(image)
    img_frm.Show()
    text_frm.Set(ffh.GetCurrentImageName().replace(os.sep, ' > '))
    text_frm.SetText(ffh.LoadText())
    
def change_image(event):
    if event.widget.cget('text') == 'Next':
        image = ffh.GetNextImage()
    else:
        image = ffh.GetPreviousImage()
    update_image(image)

def update_button_image():
    btn_frm.Set(ffh.GetParent(), ffh.GetChildren())
    update_image(ffh.GetNextImage())
    
def change_folder(event):
    folder = event.widget.cget('text')
    print('changing folder', folder)
    if folder[:3] == 'UP:':
        new_folder = '..'
    else:
        new_folder = folder
    if ffh.SetFolder(new_folder):
        update_button_image()

def save_text(event):
    ffh.SaveText(text_frm.GetText())    
    
class BottonFrame:
    # Button frame
    def __init__(self, mainframe):
        # Make a frame to contain buttons
        self.btn_frm = tk.Frame(mainframe, height = 24)
        self.btn_frm.pack(side = tk.TOP)
        # Make Previous and Next buttons and place them in self.btn_frm
        self.btn_prev = tk.Button(self.btn_frm, text='Previous')
        self.btn_prev.pack(side = tk.LEFT)
        self.btn_prev.bind("<Button-1>", change_image)
        self.btn_next = tk.Button(self.btn_frm, text='Next')
        self.btn_next.pack(side = tk.LEFT)
        self.btn_next.bind("<Button-1>", change_image)
        # Placeholder for parent and children buttons
        self.btn_parent = None
        self.btn_children = []

    def Set(self, parent, children): # parent: string, children: string list
        # Remove previously set buttons
        if self.btn_parent:
            self.btn_parent.destroy()
        for child_btn in self.btn_children:
            child_btn.destroy()
        # Reset placeholder
        self.btn_parent = None
        self.btn_children = []
        # Make parent and children buttons
        if parent:
            self.btn_parent = tk.Button(self.btn_frm, text='UP: ' + parent)
            self.btn_parent.pack(side = tk.LEFT)
            self.btn_parent.bind("<Button-1>", change_folder)
        for child in children:
            c = tk.Button(self.btn_frm, text=child)
            c.pack(side = tk.LEFT)
            c.bind("<Button-1>", change_folder)
            self.btn_children.append(c)

class ImageFrame:
    # Image frame
    def __init__(self, mainframe):
        self.img_frm = tk.Frame(mainframe)
        self.img_frm.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        self.img_frm.bind('<Configure>', self.on_resize)
        self.img_label = None
        self.img = None
        
    def Set(self, image_path):
        self.img = Image.open(image_path)

    def Show(self):
        if not self.img:
            return
        # delete previously displayed image
        if self.img_label != None:
            self.img_label.destroy()
        # resize image to fit the current main frame size
        w_frm = self.img_frm.winfo_width()
        h_frm = self.img_frm.winfo_height()
        #print('image frame size:', w_frm, h_frm)
        if h_frm < 10:
            w_frm = 500
            h_frm = 500
        w_frm -= 4
        h_frm -= 4
        w_img = self.img.width
        h_img = self.img.height
        if w_img / h_img > w_frm / h_frm:
            # image is wider than the frame. Image height is to be adjusted
            w = w_frm
            h = w_frm * h_img // w_img
        else:
            # image is thinner than the frame. Image width is to be adjusted
            h = h_frm
            w = h_frm * w_img // h_img
        print('resize:', w, h, 'org size:', w_img, h_img)
        image = self.img.resize((w, h)) # size in tuple
        self.photo = ImageTk.PhotoImage(image)
        self.img_label = tk.Label(self.img_frm, image = self.photo)
        self.img_label.pack(side = tk.TOP, expand = False)

    def on_resize(self, event):
        self.Show()
        
class TextFrame:
    # Text frame
    def __init__(self, mainframe):
        # Make a frame to contain a label, a text input area and a button
        self.text_frm = tk.Frame(mainframe, height = 24)
        self.text_frm.pack(side = tk.BOTTOM)
        # Make a text label to show the image name
        self.text_label = tk.Label(self.text_frm, text='initializing')
        self.text_label.pack(side = tk.LEFT)
        # Make 'Save' button
        self.btn_prev = tk.Button(self.text_frm, text='Save')
        self.btn_prev.pack(side = tk.RIGHT)
        self.btn_prev.bind("<Button-1>", save_text)
        # Create a text input area
        self.text_entry = tk.Text(self.text_frm, height=2)
        self.text_entry.pack(side = tk.LEFT, fill = tk.X)
        
    def Set(self, current_folder): #
        self.text_label.config(text = current_folder)

    def SetText(self, text):
        self.text_entry.delete('0.0', tk.END)
        self.text_entry.insert('0.0', text)

    def GetText(self):
        return self.text_entry.get('0.0', tk.END)

# Main program
if len(sys.argv) != 2:
    print('Usage: python album.py "path to the top folder"')
    sys.exit()

top_folder = sys.argv[1]
print('top folder', top_folder)
ffh = FileFolderHandler(top_folder)
        
#  Mainframe
root = tk.Tk()
root.title("Digital Album:" + top_folder)
#  Components
btn_frm  = BottonFrame(root)
img_frm  = ImageFrame(root)
text_frm = TextFrame(root)
#  Display the first image
update_button_image()
#  Main loop
root.mainloop()
