from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
import numpy as np
from keras.utils import to_categorical
import matplotlib.pyplot as plt
 
print('Training data shape : ', train_images.shape, train_labels.shape)
 
print('Testing data shape : ', test_images.shape, test_labels.shape)
 
# Find the unique numbers from the train labels
classes = np.unique(train_labels)
nClasses = len(classes)
print('Total number of outputs : ', nClasses)
print('Output classes : ', classes)
 
plt.figure(figsize=[10,5])
 
