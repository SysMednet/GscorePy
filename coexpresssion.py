import numpy as np

np.seterr(divide='ignore', invalid='ignore')

def correlation(input_GEM, input_DEG_list, all_case_bool, phenotype_bool):
    #read gene expression data
    fp=open(input_GEM,'r',encoding='utf-8')
    lines = fp.readlines()
    fp.close()
    
    #read DEG list
    DEGs = set(input_DEG_list)
    
    #extract DEG case(phenotype 1) samples' data
    if phenotype_bool or all_case_bool:
        case_sample = range(1, len(lines[0].strip().split('\t')))
    else:
        case_sample = []
        phenotype = lines[0].strip().split('\t')
        for c in range(len(phenotype)):
            if phenotype[c]=='1':
                case_sample.append(c)
                
    if not phenotype_bool:
        lines = lines[1:]
    
    Exp , geneID = [] , []
    for line in lines:
        temp=line.strip().split('\t')
        if temp[0] in DEGs:
            geneID.append(temp[0])
            for i in case_sample:
                Exp.append(temp[i])
    Exp = np.array(Exp,dtype=float).reshape(len(geneID),len(case_sample))
    PCC = np.round(np.corrcoef(Exp),6) #calculate pcc
    
    pcc_output = {}
    for i in range(len(geneID)):
        for j in range(i,len(geneID)):
            pcc_output[geneID[i]+'-'+geneID[j]] = PCC[i][j]
    del PCC
    return pcc_output