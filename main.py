from PIL import Image
import os, shutil

class ThumbnailAdaptor:
    def __init__(self):
        pass

    def save_as_jpg(inputfile):
        filename, extension = os.path.splitext(inputfile)
        filename = filename.strip('\"')
        outputfile = filename + '.jpg'
    
        if inputfile != outputfile:
            try:
               
                with Image.open(inputfile) as image:
                    
                    image.show()
                    image.save(outputfile)
                    print('File saved')
            except OSError:
                print('Cannot convert', inputfile)
    
    def create_thumbnail (fpath, size):

        dir = os.path.dirname(fpath)

        isDirectory = os.path.isdir(fpath)
        if isDirectory:
            thumbnail_dir = os.path.join(fpath, 'thumbnails') 
        else:
            thumbnail_dir = os.path.join(dir, 'thumbnails') 

        try:  
            os.mkdir(thumbnail_dir)  
        except OSError as error:  
            print(error)   

        if isDirectory:
            doAllFiles = input ('The path is a directory, do you want to create thumbnails for all files? Y or y to continue')
            if doAllFiles[0] in ['Y', 'y']:
                    for entry in os.scandir(fpath):
                        
                        base = entry.name
                        fname = os.path.splitext(base)[0]
                        outputfile = os.path.join(thumbnail_dir, fname) + '.thumbnail'

                        if entry != outputfile:
                            try: 
                                with Image.open(entry.path) as image:
                                    image.thumbnail(size)
                                    image.save(outputfile, 'JPEG')
                                    print (f'{outputfile} created.')
                            except OSError:
                                print("cannot convert", entry)
        else:
            inputfile = fpath
            outputfile = os.path.splitext(inputfile)[0] + '.thumbnail'
            try: 
                with Image.open(inputfile) as image:
                    image.thumbnail(size)
                    image.save(outputfile, 'JPEG')
                    print (f'{outputfile} created.')
            except OSError:
                print("cannot convert", inputfile)                      


if __name__ == '__main__':
    fpath = input('PLease give the path to the directory or file you want to save as jpg: \n')
    ta = ThumbnailAdaptor
    size = (128, 128)
    ta.create_thumbnail(fpath, size)