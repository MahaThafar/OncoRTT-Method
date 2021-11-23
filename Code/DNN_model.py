#!/usr/bin/env python
# coding: utf-8

# after completing the feature extraction process, 
# three different sets are fed into the Deep Neural Network (DNN) spereatley.
# 1) OMICS FV, 2) Bert-Embeddings FV, 3)Integrated FV (OMICS+Embeddings)
# We used the FV as input to train the classifier and make the predictions.


# DL Keras 
from tensorflow import keras
from tensorflow.keras import layers
from keras.regularizers import l2
from keras.layers import Input, Reshape, Dense, merge, Dropout
from keras.models import Sequential, Model

# create model
# Building the DNN requires configuring the layers of the model, then compiling the model. 
# First we stack a few layers together using keras 
# Next we configure the loss function, optimizer, and metrics to monitor.

## Define the DL Model
DL_model = Sequential()
DL_model.add(Dense(64, input_dim=5, kernel_initializer='normal', activation='tanh'))
# DL_model.add(Dropout(0.2))
DL_model.add(Dense(32,  activation='tanh', kernel_regularizer=l2(0.01), bias_regularizer=l2(0.01)))
DL_model.add(Dense(1, activation='sigmoid'))


# Compile the DL model
DL_model.compile(loss='binary_crossentropy', optimizer='nadam', metrics=['accuracy'])
    
#Training the DNN model 
# ...

#Apply normalization using MaxAbsolute normlization on trainind and testing data spereatley.
min_max_scaler = MinMaxScaler()
X_train = min_max_scaler.fit(x_train) 
X_train_transform = min_max_scaler.transform(x_train)
X_test_transform = min_max_scaler.transform(x_test)


#Feed the training data to the model, the model learns to associate features and labels.

DL_model.fit(X_train_transform, y_train,
        epochs=30,
        batch_size=16,
        shuffle=True,
        validation_data=(X_test_transform, y_test))

#  our model's predictions.
predictedScore = DL_model.predict(X_test_transform)   
predictedClass= np.argmax(predictedScore, axis=0)
