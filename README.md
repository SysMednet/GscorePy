# GscorePy
**GscorePy** is a python implementation of Gscore.

**Gene Set Correlation Enrichment (Gscore)** is an online tool for interpreting and annotating gene expression dataset by using a dataset-derived coexpression network to measure the statistical significance of associations between your interesting differentially expressed gene (DEG) list (i.e., query) and the collection of gene sets. Based on the hypergeometric distribution with Benjamini–Hochberg correction, the tool identifies the coexpressed gene pairs between: 
  
**(1) individual DEG** in the query DEG list and all the DEGs of a certain gene set in the selected collection to determine its association significance;  
**(2) query DEG list** and all the DEGs of a certain gene set in the selected collection to determine its association significance. 

More detail information about Gscore is available on:  
[Gscore tutorial on the Gscore website](https://gscore.ibsb.nycu.edu.tw/tutorial.html)  
[Gscore github](https://github.com/SysMednet/Gscore)  

**Publication**  
Chang, L. T.<sup>+</sup>, Lee, M. Z.<sup>+</sup>, Wu, Y. J.<sup>+</sup>, Lee, W. k., Ma, C. L., Chang, J. M., Chen, C. W., Huang, T. C., Lee, C. H., Lee, J. C., Tseng, Y. Y., Lin, C. Y. * (2023). Gene set correlation enrichment analysis for interpreting and annotating gene expression profiles, Nucleic Acids Research, gkad1187.  
[[LINK]](https://doi.org/10.1093/nar/gkad1187)  [[PDF]](https://academic.oup.com/nar/advance-article-pdf/doi/10.1093/nar/gkad1187/54448061/gkad1187.pdf)

## Dependencies  
The GscorePy source code is written in [python 3.9.13](https://www.python.org/downloads/release/python-3913/). Users also need to install following python package listed below:  
* Numpy
* Pandas
* os
* Scipy
* statsmodels
* matplotlib
* importlib
* seaborn
* shutil
  
## Installation

## Variable
### Gscore function (see Gscore.py)
```python
def Gscore(GEM, 
           DEG, 
           gene_set='KEGG', 
           species='hsa', 
           ID_type='entrez', 
           pcc_cutoff=0.5, 
           criterion='fdrq', 
           output_dir=None, 
           coexp_detail=False, 
           ratio_plot=False, 
           coexp_graph=False)
```
Variable | Description  
------------ | ------------- 
GEM | The directory of gene expression data (.txt). This variable could not be empty. See the data format explaination below.
DEG | The directory of differentially expressed gene data (.txt). This variable could not be empty. See the data format explaination below.
gene_set | The directory of gene sets data (.txt), or the users can use the default gene sets data in our database. See the details below.
species | The species ID (defined by KEGG) is used to choose defualt gene sets data in our database, there are 7 species can choose ("hsa","mmu","dre","dme","cel","rno","sce").
ID_type | Users can choose "entrez" or "symbol", users should check if their gene ID type in input data is correct.
pcc_cutoff | The cutoff for pearson correlation coefficient, which should be set between 0 and 1.
criterion | The significance level criterion for determining the association. "fdrq"(Benjamini–Hochberg method) or "pv"(raw <i>p</i> value) can be chosen, default: "fdrq".

### Gene expression data format

### Differentially expressed gene data format

### Gene sets data format


