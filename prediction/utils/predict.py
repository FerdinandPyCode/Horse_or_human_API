import tensorflow as tf
import keras.utils as image
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from django.conf import settings
import os

def predict(img_path):
    
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(16, (3,3), activation='relu' ,
        input_shape=(300, 300, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.load_weights(os.path.join(settings.BASE_DIR,"prediction", "utils", "mymodel.h5"))

    model.compile(
        loss='binary_crossentropy',
        optimizer= tf.keras.optimizers.RMSprop(lr=0.001),
        metrics=['accuracy']
    )

    # pred = model.predict(img)
    # print(pred)

    # path = '/content/' + fn
    img = image.load_img(img_path)

    img = img.resize((300,300))
    # imgplot = plt.imshow(img)

    x = image.img_to_array(img)
    x= np.expand_dims(x , axis = 0)

    image_tensor = np.vstack([x])
    classes = model.predict(image_tensor)
    print(classes)
    print(classes[0])

    if classes[0] > 0.5 :
       return 'human'
    else:
       return 'horse'

# tensorflow==2.9.1
# tensorflow-cpu==2.9.1
# tensorflow-estimator==2.9.0
# tensorflow-io-gcs-filesystem==0.26.0



# # serialize model to JSON
# model_json = model.to_json()
# with open("model.json", "w") as json_file:
#     json_file.write(model_json)
# # serialize weights to HDF5
# model.save_weights("model.h5")
# print("Saved model to disk")
 
# # later...
 
# # load json and create model
# json_file = open('model.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# loaded_model = model_from_json(loaded_model_json)
# # load weights into new model
# loaded_model.load_weights("model.h5")
# print("Loaded model from disk")