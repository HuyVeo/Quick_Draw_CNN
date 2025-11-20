import numpy as np
import cv2
images = np.load("full_numpy_bitmap_book.npy")
image=images[10]
image=image.reshape(28,28)
cv2.imwrite("book.png",image)