import numpy as np
import pandas as pd
import os
import coexpression as coexp
import main_process as main
import dotplot as dplt
import network_graph as ng
import coexpressed_detail as codetail

pd.options.mode.chained_assignment = None

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
           coexp_graph=False):
    def check_list(l):
        return not any(x not in ('0', '1') for x in l)

    def check_type(l):
        return not any(x not in (np.dtype('int64'), np.dtype('float64')) for x in l)
    
    if ID_type!='entrez' and ID_type!='symbol':
        print('Please input correct ID_type ("entrez" or "symbol"). ')
        return
    
    #check GEM
    if not os.path.isfile(GEM): #確認檔案存在
        print('GEM file does not exist')
        return
    
    GEM_data = pd.read_csv(GEM, sep='\t', header=None, low_memory=False)
    
    phenotype = list(GEM_data.loc[0,:])
    
    all_case_bool = False
    phenotype_bool = False
    if phenotype[0]!='Phenotype' and phenotype[0]!='phenotype': #第一行沒有phenotype視為全部case sample
        print('No phenotype detected, all samples will be considered as case smaples')
        phenotype_bool = True
        if len(phenotype[1:])<5:
            print('invalid sample num (control>=5)')
            return
    else:
        phenotype = phenotype[1:]
        if len(set(phenotype))==1: #只有一種phenotype，視為全部case sample
            print('Only one phenotype detected, all samples will be considered as case smaples')
            all_case_bool = True
            if len(phenotype)<5:
                print('invalid sample num (control>=5)')
                return
        else:
            try:
                phenotype = [str(int(x)) for x in phenotype]
            except:
                print('invalid phenotype format')
                return
            if not check_list(phenotype): #確認phenotype都是0跟1
                print('invalid phenotype format')
                return
            elif phenotype.count('1')<5: #check sample數量符合
                print('invalid sample num (control>=5)')
                return
            else:
                print(str(phenotype.count('0'))+' control samples and '+str(phenotype.count('1'))+' case samples are detected')
    
    if phenotype_bool:
        whole_gene = list(GEM_data[0])
    else:
        whole_gene = list(GEM_data[0])[1:]
    whole_gene = [str(x) for x in whole_gene]
    if len(set(whole_gene))!=len(whole_gene): #檢查有沒有重複
        print('gene duplicate')
        return
    elif len(whole_gene)<3: #檢查是否至少3個gene
        print('no enough gene')
        return

    ID_type_check = 'entrez'
    try:
        [int(x) for x in whole_gene]
    except:
        ID_type_check='symbol'
    if ID_type_check!=ID_type: #檢查ID_type對不對
        print("Invalid gene ID format in GEM data.")
        return

    if phenotype_bool:
        types = set(list((GEM_data.iloc[:,1:]).dtypes))
    else:
        types = set(list((GEM_data.iloc[:,1:]).dtypes)[1:])
    types = list(types)
    #if ID_type=='entrez':
    if not check_type(types): #check確認expresssion value都是數字
        print('invalid expression value')
        return
    
    del GEM_data
    del phenotype
    del types
    print('GEM....OK')
    
    #check DEG
    if not os.path.isfile(DEG): #確認檔案存在
        print('DEG file does not exist')
        return
    
    DEG_data = pd.read_csv(DEG, sep='\t', header=None)
    
    if len(list(DEG_data.keys()))!=2: #檢查是否只有兩個column
        print('false DEG data format')
        return
    
    DEG_bool = [str(x) for x in list(DEG_data[1])]
    if not check_list(DEG_bool): #檢查是否只有0跟1
        print('false DEG judge information')
        return
    
    #*************************************************#
    all_DEG = [str(x) for x in list(DEG_data[0])] #criteira
    query_list = [str(x) for x in list(DEG_data[DEG_data[1]==1][0])] #query
    #*************************************************#
    
    if len(set(all_DEG))!=len(all_DEG): #檢查DEG受否重複
        print('DEG duplicate')
        return
    
    if len(all_DEG)<3: #DEG數量不能小於3
        print('no enough DEG')
        return
    
    if len(set(whole_gene).intersection(all_DEG)) != len(all_DEG): #DEG是否都存在於GEM
        print('DEG loss in GEM')
        return
    
    if len(query_list)<3:
        print('no enough query') #檢查query數量
        return
    
    del DEG_data
    del DEG_bool
    del whole_gene
    print('DEG....OK')
    
    #check gene set
    gene_set_database_dir = 'Database/geneset/'
    gene_set_list = {'GO_BP','GO_CC','GO_MF','KEGG','Reactome'}
    
    if gene_set in gene_set_list:
        if species=='hsa':
            file_gene_set = open(gene_set_database_dir+gene_set+'/'+gene_set+'_homo_'+ID_type+'.txt',encoding="utf-8")
            gene_set_data = file_gene_set.read().strip().split('\n')
        elif species=='mmu':
            file_gene_set = open(gene_set_database_dir+gene_set+'/'+gene_set+'_mus_'+ID_type+'.txt',encoding="utf-8")
            gene_set_data = file_gene_set.read().strip().split('\n')
        elif species=='dre':
            file_gene_set = open(gene_set_database_dir+gene_set+'/'+gene_set+'_danio_'+ID_type+'.txt',encoding="utf-8")
            gene_set_data = file_gene_set.read().strip().split('\n')
        elif species=='dme':
            file_gene_set = open(gene_set_database_dir+gene_set+'/'+gene_set+'_drosophila_'+ID_type+'.txt',encoding="utf-8")
            gene_set_data = file_gene_set.read().strip().split('\n')
        elif species=='cel':
            file_gene_set = open(gene_set_database_dir+gene_set+'/'+gene_set+'_elegans_'+ID_type+'.txt',encoding="utf-8")
            gene_set_data = file_gene_set.read().strip().split('\n')
        elif species=='rno':
            file_gene_set = open(gene_set_database_dir+gene_set+'/'+gene_set+'_rat_'+ID_type+'.txt',encoding="utf-8")
            gene_set_data = file_gene_set.read().strip().split('\n')
        elif species=='sce':
            file_gene_set = open(gene_set_database_dir+gene_set+'/'+gene_set+'_saccharomyces_'+ID_type+'.txt',encoding="utf-8")
            gene_set_data = file_gene_set.read().strip().split('\n')
        else:
            print('Please input correct species ("hsa","mmu","dre","dme","cel","rno","sce").')
            return
    else:
        #user 自訂
        if not os.path.isfile(gene_set): #確認檔案存在
            print('Gene set file does not exist')
            return
        
        file_gene_set = open(gene_set, encoding="utf-8")
        gene_set_data = file_gene_set.read().strip().split('\n')
    file_gene_set.close()
    
    gene_set_dic = {}
    if len(gene_set_data)==0: #檢查是否空檔
        print('No gene set in file')
        return
    
    for pathway in gene_set_data:
        path_tmp = pathway.strip().split('\t')
        if len(path_tmp)==1: #檢查有沒有gene set 沒有gene
            print('Gene set should contain at least 1 gene')
            return
        gene_set_name = path_tmp[0]
        gene_set_gene = path_tmp[1:]
        if gene_set_name in gene_set_dic: #檢查是否有gene set重複
            print('Gene set duplicate')
            return
        
        ID_type_check = 'entrez'
        try:
            [int(x) for x in gene_set_gene]
        except:
            ID_type_check='symbol'
        if ID_type_check!=ID_type: #檢查ID_type對不對
            print("Invalid gene ID format in gene set data.")
            return
            
        #*************************************************#
        gene_set_dic[gene_set_name] = gene_set_gene
        #*************************************************#
    
    del gene_set_data
    print('Gene set....OK')
    
    #check pcc_cutoff
    try:
        test = pcc_cutoff<1
    except:
        print('invalid pcc_cutoff number')
        return
    
    if pcc_cutoff<0 or pcc_cutoff>1:
        print('invalid pcc_cutoff number')
        return
    
    print('Pcc cutoff....OK')
    
    #check criterion
    if criterion!='fdrq' and criterion!='pv':
        print('Please input correct criterion ("fdrq" or "pv").')
        return
    
    # check output folder
    if output_dir!=None:
        if not os.path.isdir(output_dir): #確認資料夾存在
            print('Output folder does not exist')
            return
    else:
        print('Please input the output directory')
        return
    
    print('Start running....')
    #running
    print('Building coexpression network....')
    coexp_network = coexp.correlation(GEM, all_DEG, all_case_bool, phenotype_bool)
    print('Enrichment analyzing....')
    individual_result_df, DEG_list_result_df, coexpress_detail_df, involved_dic = main.gscore_processing(all_DEG, query_list, coexp_network, pcc_cutoff, gene_set_dic,ID_type)
    
    #result sorting
    individual_result_df = individual_result_df.sort_values(['gene_ID','p_value'],ascending=True).groupby(['gene_ID']).head(len(individual_result_df))
    DEG_list_result_df = DEG_list_result_df.sort_values(['p_value'],ascending=True)
    
    #individual, DEG list result output
    individual_result_df.to_csv(os.path.join(output_dir,'Individual_DEG_sig.associations.txt'),sep='\t', index=False)
    DEG_list_result_df.to_csv(os.path.join(output_dir,'DEG_list_sig.associations.txt'),sep='\t', index=False)
    
    print('Complete')
    
    #coexpressed detail output
    if coexp_detail:
        print('Start getting coexpressed pair....')
        individual_detail_df, DEGlist_detail_df = codetail.get_detail(individual_result_df, DEG_list_result_df, coexpress_detail_df, criterion, query_list,ID_type)
        individual_detail_df.to_csv(os.path.join(output_dir,'Individual_gene_coexpressed_detail.txt'),sep='\t', index=False)
        DEGlist_detail_df.to_csv(os.path.join(output_dir,'DEG_list_coexpressed_detail.txt'),sep='\t', index=False)
        print('Complete')
    
    #ratio dotplot
    if ratio_plot:
        print('Start ploting....')
        save_dir = os.path.join(output_dir,'Ratio_dotplot.png')
        dplt.plot(DEG_list_result_df, involved_dic, criterion, save_dir)
        print('Complete')

    #coexpression network graph
    if coexp_graph:
        print('Network graph generating....')
        ng.gene_set_network(DEG_list_result_df, criterion, output_dir)
        print('Complete')

