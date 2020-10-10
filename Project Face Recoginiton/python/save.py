import image

def main():

    filename = 'py.png'
    image = image.open(filename)
    size =  width, height = image.size
    
    del image

if (__name__=="__main__"):
    main()