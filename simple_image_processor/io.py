from skimage.io import imread, imsave

def read_image(path, is_gray = False):
    """
    Return image data
    Parameters:
        path -- str
        is_gray -- bool (default: False)

    """
    image = imread(fname=path, as_gray=is_gray)
    return image

def save_image(image, path):
    """
    Save image to file

    Parameters:
        image - ndarray of shape (M,N) or (M,N,3) or (M,N,4)
        path -- str
    """
    imsave(fname=path, arr=image)