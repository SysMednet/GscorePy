import pandas as pd

def get_detail(individual_result_df, DEG_list_result_df, coexpress_detail_df, criterion, interest_DEG, ID_type):
    #individual detail
    if criterion=='fdrq':
        enrich_individual_df = individual_result_df[individual_result_df['FDR_q_value']<0.05]
    else:
        enrich_individual_df = individual_result_df[individual_result_df['p_value']<0.05]
        
    if ID_type=='entrez':
        type_label = 'Entrez ID'
    else:
        type_label = 'Gene symbol'
    
    individual_detail_dic = {type_label+' of the individual DEG':[],type_label+' in the gene set':[],'Gene set':[],"Pearson's r":[]}
    for ind in enrich_individual_df.index:
        DEG_list_gene_ID = enrich_individual_df.loc[ind]['gene_ID']
        gene_set = enrich_individual_df.loc[ind]['GeneSet']
        tmp_df = coexpress_detail_df[(coexpress_detail_df[type_label+' in the DEG list']==DEG_list_gene_ID) & (coexpress_detail_df['Gene set']==gene_set)]
        for ind2 in tmp_df.index:
            individual_detail_dic[type_label+' of the individual DEG'].append(tmp_df.loc[ind2][type_label+' in the DEG list'])
            individual_detail_dic[type_label+' in the gene set'].append(tmp_df.loc[ind2][type_label+' in the gene set'])
            individual_detail_dic['Gene set'].append(tmp_df.loc[ind2]['Gene set'])
            individual_detail_dic["Pearson's r"].append(tmp_df.loc[ind2]["Pearson's r"])
    
    individual_detail_df = pd.DataFrame(individual_detail_dic)
    individual_detail_df = individual_detail_df.sort_values([type_label+' of the individual DEG','Gene set',"Pearson's r"],ascending=False).groupby([type_label+' of the individual DEG','Gene set']).head(len(coexpress_detail_df))
    
    #DEG list detail
    if criterion=='fdrq':
        enrich_DEGlist_df = DEG_list_result_df[DEG_list_result_df['FDR_q_value']<0.05]
    else:
        enrich_DEGlist_df = DEG_list_result_df[DEG_list_result_df['p_value']<0.05]
    
    enrich_path = list(enrich_DEGlist_df['GeneSet'])
    DEGlist_detail_df = coexpress_detail_df[(coexpress_detail_df['Gene set'].isin(enrich_path)) & (coexpress_detail_df[type_label+' in the DEG list'].isin(interest_DEG))]
    DEGlist_detail_df = DEGlist_detail_df.sort_values(['Gene set',"Pearson's r"],ascending=False).groupby(['Gene set']).head(len(DEGlist_detail_df))

    return individual_detail_df, DEGlist_detail_df
