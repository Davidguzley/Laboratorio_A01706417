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
from padding import padding
 
def conv_helper(fragment, kernel):
    """ multiplica 2 matices y devuelve su suma"""
    
    f_row, f_col = fragment.shape #asigna el alto y ancho del fragmento
    
    resultado = 0
    for row in range(f_row):
        for col in range(f_col):
            resultado += fragment[row,col] *  kernel[row,col]
    return resultado

def convolution(image, kernel):
    """Aplica una convolucion sin padding de dos matrices
    """

    #Se encuentra la dimencion de la imagen
    if len(image.shape) == 3: #De 3 dimenciones
        print("Dimenciones de imagen: {}".format(image.shape))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Se cambia a dos dimenciones
        print("Nuevas dimenciones: {}".format(image.shape))
    else:
        print("Dimenciones de imagen: {}".format(image.shape))

    image_row, image_col = image.shape #asigna alto y ancho de la imagen 
    kernel_row, kernel_col = kernel.shape #asigna alto y ancho del filtro

    output_x = (image_col - (kernel_col / 2) * 2) + 1 #asigna el ancho del output
    output_y = (image_row - (kernel_row / 2) * 2) + 1 #asigna el alto del output
   
    output = np.zeros([int(output_y), int(output_x)]) #matriz donde se guarda el resultado

    padded_size = int((kernel_row - 1) / 2) #Tamaño de padding

    #Obtenemos la imagen con padding
    padded_image = padding(image,padded_size)
   
    for row in range(int(output_y)):
        for col in range(int(output_x)):
            output[row, col] = conv_helper(
                                padded_image[row:row + kernel_row, 
                                col:col + kernel_col], kernel)
    
    # Se muestra la imagen en pantalla
    plt.imshow(output, cmap='gray')
    plt.title("Edge detection")
    plt.show()

    return output

if __name__ == '__main__':

    #Se obtiene la imagen con cv2
    image = cv2.imread("spidermanNegro.jpg")

    #Se define la matriz del filtro
    filter = np.array([[-1, -1, -1],
                      [-1, 8, -1],
                      [-1, -1, -1]])
                      
    #Impresion de entradas y salidas
    plt.imshow(image, cmap='gray')
    plt.title("Spiderman 3")
    plt.show()

    print("Filter:")
    print(filter)

    #Mandamos a llamar la funcion
    convolution(image,filter)