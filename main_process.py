import numpy as np
from scipy.stats import hypergeom
import statsmodels.stats
import statsmodels.stats.multitest
import pandas as pd

def gscore_processing(all_DEG ,query_list ,coexp_network ,pcc_cutoff ,gene_set,ID_type):
    #read DEG list
    thresh={}
    DEGs = set(all_DEG)
    for DEG in DEGs:
        thresh[DEG+'-'+DEG]=1
    
    #read pcc
    for gene_pair in coexp_network: 
        if (np.abs(coexp_network[gene_pair])>=pcc_cutoff):
            thresh[gene_pair]=1
    
    #read gene set
    Pathway={}
    AllPathway={}
    for gset in gene_set:
        pathway_gene=gene_set[gset]
        pathway_gene_DEG=[]
        for j in pathway_gene:
            if j in DEGs:
                pathway_gene_DEG.append(j)
                AllPathway[j]='1'
        if len(pathway_gene_DEG) != 0:
            Pathway[gset]=pathway_gene_DEG
    
    #%% calculate individual DEG information
    single_dic = {}
    DEG_list_input=[]
    if ID_type=='entrez':
        type_label = 'Entrez ID'
    else:
        type_label = 'Gene symbol'
    coexpress_detail_dic = {'Gene set':[],type_label+' in the gene set':[],type_label+' in the DEG list':[],"Pearson's r":[]}
    involved_dic = {}
    interest_DEG_list=set(query_list)
    
    for j in DEGs:
        (N,M)=(len(AllPathway),0)
        for k in AllPathway.keys():
            if j+'-'+k in thresh or k+'-'+j in thresh:
                M += 1
        for l in Pathway.keys():
            (n,m)=(len(Pathway[l]),0)
            
            if l not in involved_dic:
                involved_dic[l] = set()
                
            for p in Pathway[l]:
                #get involved gene
                if j+'-'+p in thresh or p+'-'+j in thresh:
                    m += 1
                    #get involved num
                    if j in interest_DEG_list:
                        involved_dic[l].add(j)
                    
                #get detail numbers
                if j+'-'+p in thresh: # and j in interest_DEG_list
                    coexpress_detail_dic['Gene set'].append(l)
                    coexpress_detail_dic[type_label+' in the gene set'].append(p)
                    coexpress_detail_dic[type_label+' in the DEG list'].append(j)
                    coexpress_detail_dic["Pearson's r"].append(coexp_network[j+'-'+p])
                elif p+'-'+j in thresh: # and j in interest_DEG_list
                    coexpress_detail_dic['Gene set'].append(l)
                    coexpress_detail_dic[type_label+' in the gene set'].append(p)
                    coexpress_detail_dic[type_label+' in the DEG list'].append(j)
                    coexpress_detail_dic["Pearson's r"].append(coexp_network[p+'-'+j])
    
            P_value=(hypergeom.sf(m-1,N,M,n)) #p-val of hyper
            
            if ~(M==0 or N==0 or n==0) and (j not in single_dic):
                single_dic[j] = {'GeneSet':[],'gene_ID':[],'N':[],'M':[],'n':[],'m':[],'p_value':[],'FDR_q_value':[]}
            if m!=0:
                single_dic[j]['gene_ID'].append(j)
                single_dic[j]['GeneSet'].append(l)
                single_dic[j]['p_value'].append(P_value)
                single_dic[j]['N'].append(N)
                single_dic[j]['M'].append(M)
                single_dic[j]['n'].append(n)
                single_dic[j]['m'].append(m)
    
            DEG_list_input.append(l+'\t'+j+'\t'+str(N)+'\t'+str(M)+'\t'+str(n)+'\t'+str(m)+'\t'+str(P_value)) #write p j
    
    #individual fdrq correction
    for g in single_dic:
        fdrQ = list(statsmodels.stats.multitest.fdrcorrection(single_dic[g]['p_value'], alpha=0.05, method='indep', is_sorted=False)[1])
        single_dic[g]['FDR_q_value'] = fdrQ
    
    #output individual result
    output_dic = {'GeneSet':[],'gene_ID':[],'N':[],'M':[],'n':[],'m':[],'p_value':[],'FDR_q_value':[]}
    for g in single_dic:
        for index in single_dic[g]:
            output_dic[index]+=single_dic[g][index]
    del single_dic
    
    #*************************************************#
    single_output_df = pd.DataFrame(output_dic)
    coexpress_detail_df = pd.DataFrame(coexpress_detail_dic)
    #*************************************************#

    #%% calculate DEG list information
    Pathway_nm={}
    Pathway={}
    for line in DEG_list_input:
        temp=line.split('\t')
        Pathway[temp[0]]='1'
        Pathway_nm[temp[0]+'|'+temp[1]]=[temp[2],temp[3],temp[4],temp[5]]
    
    #input query DEG
    DEG_list_output_dic = {'GeneSet':[],'N':[],'M':[],'n':[],'m':[],'p_value':[],'FDR_q_value':[]}
    for l in Pathway.keys():
        (N,M)=(0,0)
        (n,m)=(0,0)
        for gene in interest_DEG_list:
            if (l+'|'+gene) in Pathway_nm.keys():
                N+=int(Pathway_nm[l+'|'+gene][0])
                M+=int(Pathway_nm[l+'|'+gene][1])
                n+=int(Pathway_nm[l+'|'+gene][2])
                m+=int(Pathway_nm[l+'|'+gene][3])
                
        if (N!=0):
            DEG_list_output_dic['GeneSet'].append(l)
            DEG_list_output_dic['p_value'].append(hypergeom.sf(m-1,N,M,n))
            DEG_list_output_dic['N'].append(N)
            DEG_list_output_dic['M'].append(M)
            DEG_list_output_dic['n'].append(n)
            DEG_list_output_dic['m'].append(m)
    
    fdrQ = list(statsmodels.stats.multitest.fdrcorrection(DEG_list_output_dic['p_value'], alpha=0.05, method='indep', is_sorted=False)[1])
    DEG_list_output_dic['FDR_q_value'] = fdrQ

    DEG_list_output_df = pd.DataFrame(DEG_list_output_dic)
    
    return single_output_df, DEG_list_output_df, coexpress_detail_df, involved_dic
