import numpy as np

def padding(image, padded_size):
    # Se obtienen los tamaños de la matriz imagen
    image_row, image_col = image.shape

    padded_image = np.zeros((image_row + padded_size*2, image_col + padded_size*2))

    padded_image[padded_size:padded_size + image_row, padded_size:padded_size + image_col] = image
    
    return padded_image

if __name__ == '__main__':

    image = np.array([[1,2,3,4,5,6],
                     [7,8,9,10,11,12],
                     [2,5,1,16,17,18],
                     [4,1,8,7,23,24],
                     [1,7,6,5,4,3]])
    
    padded_size = 1

    print(padding(image, padded_size))