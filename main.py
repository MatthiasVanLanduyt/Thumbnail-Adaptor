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
        fpath = fpath.strip('\"')
        try:  
            dir = os.path.dirname(fpath)
            thumbnail_dir = os.path.join(dir, 'thumbnails') 
            print(thumbnail_dir)
            
            os.mkdir(thumbnail_dir)  
        except OSError as error:  
            print(error)

        try:
            with Image.open(fpath) as image:
                base = os.path.basename(fpath)
                fname = os.path.splitext(base)[0]
                outputfile = os.path.join(thumbnail_dir, fname) + '_thumbnail.jpg'
                image = image.resize(size)
                image.save(outputfile)
                # Why doesnt this work
                # image.save(outputfile, 'JPEG')
                print (f'{outputfile} created.')
        except OSError as error:
            print("Cannot convert ", fpath)
            print(error)     


    def create_thumbnail_folder (fpath, size):
        fpath = fpath.strip('\"')
        try:  
            thumbnail_dir = os.path.join(fpath, 'thumbnails') 
            os.mkdir(thumbnail_dir)  
        except OSError as error:  
            print(error)

        for entry in os.scandir(fpath):
                        
            base = entry.name
            fname = os.path.splitext(base)[0]
            outputfile = os.path.join(thumbnail_dir, fname) + '_thumbnail.jpg'

            if entry != outputfile:
                try: 
                    with Image.open(entry.path) as image:
                        image = image.resize(size)
                        image.save(outputfile)
                        # Why doesnt this work
                        # image.save(outputfile, format = 'jpeg')

                        print (f'{outputfile} created.')
                except OSError as error:
                    print("cannot convert ", entry)
                    print(error)                            


if __name__ == '__main__':
    fpath = input('PLease give the path to the directory or file you want to save as jpg: \n')
    ta = ThumbnailAdaptor
    size = (128, 128)
    ta.create_thumbnail_folder(fpath, size)