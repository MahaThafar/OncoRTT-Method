  **Code folder:** that includes 4 files:\
  > 1 OncoDT_All_models_(generated_embed)\
  > 2 OncoDT_ProtTransBert model- ThyroidCancer-demo.py\
  > 3 DNN.py\
  > 4 Omics_feature_extraction_demo.R\
 
The description for each file is as follows:
> OncoDT_All_models_(generated_embed), which is the main code for 
# OncoDT methods.
This notebook provides an implementation of the OncoDT tool to predict therapeutic target genes for ten cancer types.
Each cancer has its own model and FVs. The code here read the generated embeddings for amino-acid sequences using ProtTrans-BERT embeddings. Several preprocessing and preparation steps have been implemented before utilizing this code for each cancer type. For example:

All genes were read from three sources: positive targets, cancer genes, and negative genes, which are combined, shuffled and then used to generate the embeddings using their amino-acid sequences. These combined genes are saved in the Combined_Genes folder.
> OncoDT_ProtTransBert model- ThyroidCancer-demo.py: A demo for how we generate BERT embeddings is provided for thyroid cancer, the generated embeddings for per cancer type are saved in BERT-EMBED folder
> Omics_feature_extraction_demo.R A demo for how we extract Ominc features is provided for breast cancer. The code of the breast cancer project and the sampels barcodes are provided from TCGA GDC portal.
> DNN.py, the architecture of deep neural network (DNN) implemented for classification.
