# OncoRTT-Method
### OncoDT: Deep learning Method to Predict Oncology-related Therapeutic Targets using BERT Embeddings Integrated with Omics Features

----------------------------------------------
Submitted: 24 November 2021\
Accepted:\
Published:\
Link:

--------------------------------------

## Getting Started

### OncoRTT Workflow:
> Late-stage drug development failures are usually a consequence of ineffective targets. Thus, proper target identification is needed, which may be possible using computational approaches. In this work, we developed OncoDT, a deep learning (DL)-based method for predicting novel therapeutic targets. OncoDT is designed to reduce suboptimal target selection by identifying novel targets based on features of known effective targets using DL approaches.


### Requirements:
OncoDT is implemented using:
- Linux machines
- Anaconda Jupyternotebook
- Python version 3.8
- R version 4.1.1

There are several required R and Python packages to run the code.
> Example of python packages:
- numpy
- Scikit-learn
- keras
- tensorflow
- bio-embeddings
- pandas

### Usage:
To use OncoDT model, please git clone the code and make sure you have the correct directory for the code and the datasets.\
To successfully run OncoDT model we recomend you to create a virtul environment
based on required packages collected in requirements.txt.
```bash
conda create -n OncoDT python=3.8
# Activate your virtual environment:
source activate OncoDT  #  or 'conda activate OncoDT'
conda install -c conda-forge notebook # so you can luanch jupyter notebook in this env 
pip install requirements.txt
jupyter notebook ## open the jupyter notebook with the conda env
conda deactivate ## when done, exit conda environment 
```
Then use any python platform, or anaconda jupyter notebook.

----

### Description:
#### *There are four folders:*

  **1.Data folder:** that includes 2 datasets:
  > a) OncologyTT datasets, and\
  > b) the baseline method's datasets.\
  > Description for the datasets are provided in the Data folder.
  
  **2.Code folder:** that includes 4 files:
  > 2.1 OncoDT_All_models_(generated_embed)\
  > 2.2 OncoDT_ProtTransBert model- ThyroidCancer-demo.py\
  > 2.3 DNN.py\
  > 2.4 Omics_feature_extraction_demo.R\
  Description for each file is provided in the Code folder.
     
  **3.EMBED folder:**\
  It has several files per cancer type for the generated Amino-acid sequences embeddings using ProTrans BERT embeddings.
  > We utilized ProtTrans-bert embeddins using bio_embeddings python package.
  > ProtTrans is the state of the art pre-trained models for proteins. ProtTrans was trained on thousands of GPUs from Summit and hundreds of Google TPUs using various Transformers Models (BERT). The resources and more detials can be found: https://github.com/agemagician/ProtTrans
  > For [`bio_embeddings`](https://github.com/sacdallago/bio_embeddings) package, how to use it, and how to generate Bert embeddings:
  > https://github.com/sacdallago/bio_embeddings
  
  **4.Results' Figures:**\
  Figure of the results when using Omics FV, Embedings FV, and Integrated FV in terms of AUC.

-----------------------------------------------
### For Citation:
TBD

--------------------------------------------------------------------
### For any qutions please contact the first author:

Maha A. Thafar \
Ph.D. Candidate and resercher | Computer Science\
Computer, Electrical and Mathematical Sciences and Engineering (CEMSE) Division\
Computational Bioscience Research Center (CBRC), King Abdullah university of science and technology.\
Collage of Computers and Information Technology, Taif University (TU).\
Email: maha.thafar@kaust.edu.sa

----
