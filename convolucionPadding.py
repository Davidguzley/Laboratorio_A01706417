"""
By Abhisek Jana
code taken from https://github.com/adeveloperdiary/blog/tree/master/Computer_Vision/Sobel_Edge_Detection
blog http://www.adeveloperdiary.com/data-science/computer-vision/how-to-implement-sobel-edge-detection-using-python-from-scratch/
Modified by David Guzmán
"""
#Librerias
import numpy as np
import cv2
import matplotlib.pyplot as plt
 
def conv_helper(fragment, kernel):
    """ multiplica 2 matices y devuelve su suma"""
    
    f_row, f_col = fragment.shape #asigna el alto y ancho del fragmento
    
    resultado = 0
    for row in range(f_row):
        for col in range(f_col):
            resultado += fragment[row,col] *  kernel[row,col]
    return resultado

def convolution(image, kernel):
    """Aplica una convolucion con padding de dos matrices
    """

    image_row, image_col = image.shape #asigna alto y ancho de la imagen 
    kernel_row, kernel_col = kernel.shape #asigna alto y ancho del filtro

    output_x = (image_col - (kernel_col / 2) * 2) + 1 #asigna el ancho del output
    output_y = (image_row - (kernel_row / 2) * 2) + 1 #asigna el alto del output
   
    output = np.zeros([int(output_y), int(output_x)]) #matriz donde se guarda el resultado

    pad_height = int((kernel_row - 1) / 2) #asigna el alto del padding
    pad_width = int((kernel_col - 1) / 2)  #asigna el ancho del pading

    padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width))) #matriz de imagen con paded en zeros
    print("Padded image zeros:")
    print(padded_image)
 
    padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = image #matriz de imagen con paded
    print("Padded image:")
    print(padded_image)
   
    for row in range(int(output_y)):
        for col in range(int(output_x)):
            output[row, col] = conv_helper(
                                padded_image[row:row + kernel_row, 
                                col:col + kernel_col], kernel)
                                
    print("Valid Convolution:")
    print(output)

    return output

if __name__ == '__main__':

    #Matriz de imagen
    image = np.array([[1,2,3,4,5,6],
                     [7,8,9,10,11,12],
                     [0,0,1,16,17,18],
                     [0,1,0,7,23,24],
                     [1,7,6,5,4,3]])

    #Matriz de filtro
    filter = np.array([[1,1,1],
                      [0,0,0],
                      [2,10,3]])

    #Impresion de entradas
    print("Orignal Matrix:")
    print(image)
    print("Filter:")
    print(filter)

    #LLamamos a la funcion
    convolution(image, filter)