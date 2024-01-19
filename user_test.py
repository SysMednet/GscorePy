from gscorepy import gscore

gscore(GEM='test_input/GSE157103.txt', 
        DEG='test_input/allDEG.txt', 
        pcc_cutoff=0.7, 
        criterion='pv', 
        gene_set='KEGG', 
        species='hsa', 
        ID_type='entrez',
        output_dir = 'test_output/',
        coexp_detail=True,
        ratio_plot=True,
        coexp_graph=True)
