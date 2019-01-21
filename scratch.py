import numpy as np
import pandas as pd

another = np.array([[11, 12, 13], [21, 22, 23]])  # Create a rank 2 array

print(another)  # print the array

print("The shape is 2 rows, 3 columns: ", another.shape)  # rows x columns

print("Accessing elements [0,0], [0,1], and [1,0] of the ndarray: ", another[0, 0], ", ", another[0, 1], ", ",
      another[1, 0])

an_eye = np.eye(5,5)

print(an_eye)


