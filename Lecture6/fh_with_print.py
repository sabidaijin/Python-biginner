#
# Managing folders and files
#
import os, sys
from folder import read_folders

class FileFolderHandler:

    def __init__(self, top_folder):
        # Keep top_folder
        self.top_folder = os.path.normpath(os.path.abspath(top_folder))
        # Call read_folders in folder.py. Keep the return value.
        self.folders = read_folders(self.top_folder)
        # Use the top_folder as the first folder after starting this program.
        self.SetFolder('.')

    def SetFolder(self, new_folder):
        # Update current folder
        if   new_folder == '.':  # For top folder
            self.current_folder = self.top_folder
        elif new_folder == '..': # parent folder
            self.current_folder = os.path.dirname(self.current_folder)
        else:                    # a child folder
            self.current_folder = os.path.join(self.current_folder, new_folder)
        # Folder data
        #   Parent folder
        if self.current_folder == self.top_folder:
            self.parent = '' # no parent folder for the top folder
        else:
            self.parent = os.path.basename(os.path.dirname(self.current_folder))
        #   Sub folders
        self.sub_folders = self.folders[self.current_folder]['sub_folders']
        #   Images
        self.images = self.folders[self.current_folder]['images']
        #   If no image in this folder, search one in sub-folders.
        #   If not any images in sub_folders, then search in sub-sub-folders.
        #   Continue until finding an image file under this folder.
        if not self.images:
            print('@@ image file not found in', self.current_folder)
            def get_a_image(folder):
                print('@@ searching in', folder)
                # Get one in the folder
                if self.folders[folder]['images']:
                    print('@@ image file found in', folder)
                    return self.folders[folder]['images'][0]
                # Search in descendent folders
                for sub_folder in self.folders[folder]['sub_folders']:
                    print('@@ searching in sub folder', sub_folder)
                    folder = os.path.join(folder, sub_folder)
                    image = get_a_image(folder)
                    if image:
                        return image
                print('@@ image file not found in', folder)
                return ''
            #
            image = get_a_image(self.current_folder)
            if not image:
                print('no image under this folder')
                return False
            self.images = [image]
        # Reset image index
        self.image_index = -1
        #
        return True

    def GetParent(self):
        # Returns the basename of the parent folder of the current folder
        return self.parent

    def GetChildren(self):
        # Returns the list of child folders in the current folder
        return self.sub_folders

    def GetNextImage(self):
        # Add 1 to image index
        self.image_index += 1
        # Next image of the last image is the first image
        self.image_index = self.image_index % len(self.images)
        return os.path.join(self.current_folder,self.images[self.image_index])
 
    def GetPreviousImage(self):
        # Subtract 1 from image index
        self.image_index -= 1
        # Prsvious image of the first image is the last image
        self.image_index = self.image_index % len(self.images)
        return os.path.join(self.current_folder,self.images[self.image_index])

    def GetCurrentImageName(self):
        # Returns path to the current image.
        # The path is a relative path from the top folder.
        image_path = os.path.join(self.current_folder,
                                  self.images[self.image_index])
        return image_path[len(os.path.dirname(self.top_folder)) + 1:]

    def SaveText(self, text):
        # Save the text in a file.
        # Use the current image filename changing the extension to 'txt'.
        # No return value
        print('SaveText', text)
        pass
    
    def LoadText(self):
        # Return text in a file. See SaveText for the filename.
        print('LoadText', self.GetCurrentImageName())
        return ''
    
if __name__ == '__main__':
    # Test Program.
    #
    # Assuming that this program is placed in BasicPython/Lecture6,
    # this test program should be invoked with the command below.
    # PS ...\Lecture6> py file_handler.py ../Lecture5/I
    ffh = FileFolderHandler(sys.argv[1])
    print('Top Level')
    print('  parent of the top folder:', ffh.GetParent())
    print('  children of the top folder:', ffh.GetChildren())
    print('  next image', ffh.GetNextImage())
    print('  previous image', ffh.GetPreviousImage())
    print('  current image name:', ffh.GetCurrentImageName())
    # Get down one layer.
    print('Second Level')
    child_folder = ffh.GetChildren()[0]
    ffh.SetFolder(child_folder)
    print('  parent of', child_folder, ':', ffh.GetParent())
    print('  children of', child_folder, ':', ffh.GetChildren())
    print('  next image', ffh.GetNextImage())
    print('  previous image', ffh.GetPreviousImage())
    print('  current folder:', ffh.GetCurrentImageName())
    # Get down to bottom.
    print('Third Level')
    child_folder = ffh.GetChildren()[0]
    ffh.SetFolder(child_folder)
    print('  parent of', child_folder, ':', ffh.GetParent())
    print('  children of', child_folder, ':', ffh.GetChildren())
    for i in range(3):
        print('  next image', i, ffh.GetNextImage())
        print('  current folder:', ffh.GetCurrentImageName())
    for i in range(3):
        print('  previous image', i, ffh.GetPreviousImage())
        print('  current folder:', ffh.GetCurrentImageName())
