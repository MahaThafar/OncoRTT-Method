#!/usr/bin/env python
# coding: utf-8

# In[1]:
#all eequired packages
import pandas as pd
import math as math
import numpy as np
import json, csv, itertools
from matplotlib import pyplot as plt

# ML packages
from sklearn import ensemble, metrics
from sklearn.model_selection import cross_val_score,KFold,StratifiedKFold
from sklearn.metrics import *
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler
# DL Keras 
from keras.layers import Embedding, Input, Reshape, Dense, merge
from keras.models import Sequential, Model

#amino-acid sequence embeddings package
from bio_embeddings.embed import SeqVecEmbedder, ProtTransBertBFDEmbedder

# In[2]:
cancertypes = ["Thyroid" ]

# In[3]:
bert_em = ProtTransBertBFDEmbedder()
# seqVec_em = SeqVecEmbedder()

# In[4]:
## Read the  genes for Thyroid Cancer
G_neg_th = pd.read_csv('Datasets/Negative genes/Thyroid_genes_negative.csv')
G_pos_th = pd.read_csv('Datasets/Positive genes/Thyroid_genes_positive.csv')
G_tr_th = pd.read_csv('Datasets/Positive targets/Thyroid_targets_positive.csv')

# combine all gnes and shuffle 
thyG = [G_tr_th, G_neg_th, G_pos_th]
thyGenes = pd.concat(thyG)
ThyroidGenes = thyGenes.sample(frac=1).reset_index(drop=True)
print('Thyroid genes data format:',ThyroidGenes.shape)

# In[5]:
thyDIC = {}
thySEQ = []
thylab = []
for i in range(0,ThyroidGenes.shape[0]):
    g = ThyroidGenes['Gene'][i]
    seq = ThyroidGenes['Sequence'][i].replace("\n", "")
    thyDIC[g] = seq
    thylab.append(ThyroidGenes['Label'][i])
    thySEQ.append(seq)

# Generate embeddings for each amino-acid
embeddingsThyroid = bert_em.embed_many(thySEQ)
embeddingsThyroid = list(embeddingsThyroid)
# make the embeddings for each protein(gene)
ThyroidEmbed = [ProtTransBertBFDEmbedder.reduce_per_protein(e) for e in embeddingsThyroid]

# In[6]:
# write the combine genes into file. write the generated BERT embeddings into file
ThyroidGenes.to_csv('Datasets/Combine_Genes/ThyroidGenes.csv', index=False)
np.savetxt('BERT EMBED/LungEmbed.txt',ThyroidEmbed)
X = np.array(ThyroidEmbed)
Y = np.array(ThyroidGenes['Label'])
print(X.shape, Y.shape)

# In[7]:
# Define 10-fold CV
skf = StratifiedKFold(n_splits=10, shuffle = True, random_state = 10)

# In[8]:
# Define DNN classifier
input_dim = X.shape[1]
print('input dim', input_dim)
DL_model = Sequential()
DL_model.add(Dense(64, input_dim=5, kernel_initializer='normal', activation='tanh', kernel_regularizer=l2(0.01), bias_regularizer=l2(0.01)))
# DL_model.add(Dropout(0.2))
DL_model.add(Dense(32,  activation='tanh', kernel_regularizer=l2(0.01), bias_regularizer=l2(0.01)))
DL_model.add(Dense(1, activation='sigmoid'))
# Compile the DNN model
DL_model.compile(loss='binary_crossentropy', optimizer='nadam', metrics=['accuracy'])

# In[9]:
# evaluation lists
correct_classified = []
roc_auc = []
foldCounter = 1  
# Start training and testing)
for train_index, test_index in  skf.split(X,Y):
    print("*** Working with Fold %i :***" %foldCounter)
    #Apply normalization using MaxAbsolute normlization
    max_abs_scaler = MinMaxScaler()
    X_train = max_abs_scaler.fit(X[train_index]) 
    X_train_transform = max_abs_scaler.transform(X[train_index])
    X_test_transform = max_abs_scaler.transform(X[test_index])

    DL_model.fit(X_train_transform, Y[train_index], epochs=20,batch_size=16)
# #     # evaluate the keras model
#     _, mse = DL_model.evaluate(X_train_transform, Y[train_index])
#     print('mse Deep Learning Regressor evaluate for training: %4f' % mse)
    #  DL model's predictions.
    predictedScore = DL_model.predict(X_test_transform)
    predictedClass= np.argmax(predictedScore, axis=0)
    
    print("@@ Validation and evaluation of fold %i @@" %foldCounter)
    print(Y[test_index].shape, predictedClass.shape)
    nn_fpr_keras, nn_tpr_keras, nn_thresholds_keras = roc_curve(Y[test_index], predictedScore)
    roc_auc.append(auc(nn_fpr_keras, nn_tpr_keras))
    print("AUC-keras =  %f" %auc(nn_fpr_keras, nn_tpr_keras))
#     print("AUC =  %f" %roc_auc_score(Y[test_index], predictedScore))
#     roc_auc.append(roc_auc_score(Y[test_index], predictedScore))
    print('------------------------------------------------------')
    foldCounter += 1

# In[10]:
### Print Evaluation Metrics.......................
print("Results using Test data:")
print("roc_auc = " + str( np.array(roc_auc).mean().round(decimals=4) ))


# -------------------- End of the demo code -------------------------
