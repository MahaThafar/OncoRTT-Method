library("TCGAbiolinks")
library("SummarizedExperiment")
library(dplyr)

query <- GDCquery(project = c("TCGA-BRCA"),
                  legacy = TRUE,
                  data.category = "Gene expression",
                  data.type = "Gene expression quantification",
                  platform = "Illumina HiSeq", 
                  barcode = c("TCGA-C8-A8HP", "TCGA-E9-A5FL", "TCGA-BH-A0WA", "TCGA-AR-A5QQ", "TCGA-A2-A4S1", "TCGA-AR-A2LR", "TCGA-A7-A26G", "TCGA-BH-A0DL"),
                  file.type = "normalized_results")

GDCdownload(query, method = "api")

#BreastG <- read_csv("R_project_cancer/Data/BreasGenes.csv")
maf <- GDCprepare(query, add.gistic2.mut=c('TECPR1','EVA1A','SLC36A2','ALCAM','KBTBD6','XKRX'))
df_Breast <- as.data.frame(colData(maf))

gene_mut_Breast <- select(df_Breast, c('mut_hg38_TECPR1','mut_hg38_EVA1A','mut_hg38_SLC36A2','mut_hg38_ALCAM',
                                       'mut_hg38_KBTBD6','mut_hg38_XKRX'))

gene_mut_BreastMAT <- t(data.matrix(gene_mut_Breast))
write.csv(gene_mut_BreastMAT,"R_project_cancer/OMICS/Breast_6genes_mut.csv")

dataBreast<- assay(maf)
gene_exp_Breast<- subset(dataBreast, rownames(dataBreast) %in% c('TECPR1','EVA1A','SLC36A2','ALCAM','KBTBD6','XKRX'))
write.csv(gene_exp_Breast,"R_project_cancer/Omics/Breast_6genes_exp.csv")
