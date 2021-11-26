# OncoDT-Method
### OncoDT: Deep learning Method to Predict Oncology-related Therapeutic Targets using BERT Embeddings Integrated with Omics Features

----------------------------------------------
Submitted: 24 November 2021\
Accepted:\
Published:\
Link:

--------------------------------------

## Getting Started


### OncoDT Workflow
> Late-stage drug development failures are usually a consequence of ineffective targets. Thus, proper target identification is needed, which may be possible using computational approaches. In this work, we developed OncoDT, a deep learning (DL)-based method for predicting novel therapeutic targets. OncoDT is designed to reduce suboptimal target selection by identifying novel targets based on features of known effective targets using DL approaches.



### Prerequisites:

There are several required Python packages to run the code such as:
- numpy
- Scikit-learn
- keras
- tensorflow
- bio-embeddings
- pandas
These packages can be installed using pip or conda as the follwoing example
```
pip install -r requirements.txt
```
----

### Description:
#### *There are four folders:*

  **1.Data folder:** 
  > It includes 2 datasets: OncologyTT datasets, and the baseline method's datasets.\
  > Description for the datasets are provided in the folder.
  
  **2.Code folder:**
  > More files and details will be added.....
     
  **3.EMBED folder:**\
  It has several files per cancer type for the generated Amino-acid sequences embeddings using ProTrans BERT embeddings.\
  > We utilized ProtTrans-bert embeddins using bio_embeddings python package.
  > ProtTrans is the state of the art pre-trained models for proteins. ProtTrans was trained on thousands of GPUs from Summit and hundreds of Google TPUs using various Transformers Models (BERT). The resources and more detials can be found: https://github.com/agemagician/ProtTrans
  > For [`bio_embeddings`](https://github.com/sacdallago/bio_embeddings) package, how to use it, and how to generate Bert embeddings:\
  > https://github.com/sacdallago/bio_embeddings
  
  **4.Results' Figures:** 
  

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
