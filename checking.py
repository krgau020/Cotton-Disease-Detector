

from keras.models import load_model
from keras.preprocessing import image
from keras.applications.inception_v3 import preprocess_input

model=load_model('model_inception.h5')

img=image.load_img(path = r"G:\gaurav education\cotton_disease_predictin\Dataset\train\diseased cotton leaf\dis_leaf (339)_iaip.jpg",target_size=(224,224))

x=image.img_to_array(img)

x = x/255


import numpy as np
x=np.expand_dims(x,axis=0)
img_data=preprocess_input(x)



print(model.predict(img_data))

a=np.argmax(model.predict(img_data), axis=1)

print(a)