import tensorflow as tf
from tensorflow.keras import *
import numpy as np
from tensorflow.keras.utils import to_categorical 

md = models.load_model('diabets.h5')
Xdata = [0.352941, 0.743719, 0.590164, 0.353535, 0.000000, 0.500745, 0.259091, 0.617284]
Xdata = np.asarray(Xdata)
Xdata = np.reshape(Xdata, (-1, 8))
res = md.predict(Xdata)
print(res)