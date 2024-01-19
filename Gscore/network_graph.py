import numpy as np
import os
import shutil
import pkg_resources

def json_generate(data_df,node_num):
    tmp_df = data_df.head(node_num)
    
    maxvalue = list(tmp_df['p_log'])[0]
    minvalue = list(tmp_df['p_log'])[-1]
    if maxvalue == minvalue:
        minvalue = maxvalue - 0.01
    # output javascript file
    op = '[\n'
    # Genelist position
    op+='\t'*9+'{"group":"nodes", "data": { "id": "DEG list","shape": "diamond","color":"#ACD6FF"} },\n'
    for j in range(len(tmp_df)):
        op+='\t'*9+'{"group":"nodes", "data": { "id": "' + list(tmp_df['GeneSet'])[j] + '","shape": "roundrectangle","color":"#FF9797"}},\n'
        op+='\t'*9+'{"group":"edges", "data": { "id": "e' + str(j) + '", "source": "DEG list", "target": "' + list(tmp_df['GeneSet'])[j] + '","width": "' + str("%.2f" % ((10*(list(tmp_df['p_log'])[j]-minvalue)/(maxvalue-minvalue))+3)) + '" }}'
        if j != (len(tmp_df)-1):
            op+=',\n'
    op+="]\n"
    
    return op

def gene_set_network(DEG_list_result_df, criterion, output_dir):
    if criterion=='fdrq':
        legend_figure = 'graph_files/legend_fdrq.png'
        enrich_DEGlist_df = DEG_list_result_df[DEG_list_result_df['FDR_q_value']<0.05]
        enrich_DEGlist_df['p_log'] = [-np.log10(x) for x in enrich_DEGlist_df['FDR_q_value']]
        rank_by_tag = '(ranked by FDR <i>q</i> value)'
    else:
        legend_figure = 'graph_files/legend_rawp.png'
        enrich_DEGlist_df = DEG_list_result_df[DEG_list_result_df['p_value']<0.05]
        enrich_DEGlist_df['p_log'] = [-np.log10(x) for x in enrich_DEGlist_df['p_value']]
        rank_by_tag = '(ranked by raw <i>p</i> value)'
    
    if len(enrich_DEGlist_df)<=10:
        total_select=[len(enrich_DEGlist_df)]
        function_list = ['one']
        html_selection = '<option value=1 selected>'+str(len(enrich_DEGlist_df))+'</option>\n'
    elif len(enrich_DEGlist_df)>10 and len(enrich_DEGlist_df)<=25:
        total_select=[10,len(enrich_DEGlist_df)]
        function_list = ['one','two']
        html_selection = '<option value=1 selected>10</option>\n'
        html_selection += '\t'*2+'<option value=2>'+str(len(enrich_DEGlist_df))+'</option>\n'
    elif len(enrich_DEGlist_df)>25 and len(enrich_DEGlist_df)<=50:
        total_select=[10,25,len(enrich_DEGlist_df)]
        function_list = ['one','two','three']
        html_selection = '<option value=1 selected>10</option>\n'
        html_selection += '\t'*2+'<option value=2>25</option>\n'
        html_selection += '\t'*2+'<option value=3>'+str(len(enrich_DEGlist_df))+'</option>\n'
    elif len(enrich_DEGlist_df)>50 and len(enrich_DEGlist_df)<=100:
        total_select=[10,25,50,len(enrich_DEGlist_df)]
        function_list = ['one','two','three','four']
        html_selection = '<option value=1 selected>10</option>\n'
        html_selection += '\t'*2+'<option value=2>25</option>\n'
        html_selection += '\t'*2+'<option value=3>50</option>\n'
        html_selection += '\t'*2+'<option value=4>'+str(len(enrich_DEGlist_df))+'</option>\n'
    else:
        total_select=[10,25,50,100]
        function_list = ['one','two','three','four']
        html_selection = '<option value=1 selected>10</option>\n'
        html_selection += '\t'*2+'<option value=2>25</option>\n'
        html_selection += '\t'*2+'<option value=3>50</option>\n'
        html_selection += '\t'*2+'<option value=4>100</option>\n'
    
    #copy graph need files
    graph_files_database = pkg_resources.resource_filename('gscorepy', 'Database/graph_files')
    if not os.path.isdir(os.path.join(output_dir,'graph_files')):
        shutil.copytree(graph_files_database, os.path.join(output_dir,'graph_files'))
    
    #write html file
    fileo_html = open(os.path.join(output_dir,'GeneSet_network_graph.html'),'w')
    ###html backbone
    filef1_html_path = pkg_resources.resource_filename('gscorepy', 'Database/graph_code_fragment/html_f1.txt')
    filef1_html = open(filef1_html_path)
    html_f1 = filef1_html.read()
    filef1_html.close()
    
    filef2_html_path = pkg_resources.resource_filename('gscorepy', 'Database/graph_code_fragment/html_f2.txt')
    filef2_html = open(filef2_html_path)
    html_f2 = filef2_html.read()
    filef2_html.close()
    
    filef3_html_path = pkg_resources.resource_filename('gscorepy', 'Database/graph_code_fragment/html_f3.txt')
    filef3_html = open(filef3_html_path)
    html_f3 = filef3_html.read()
    filef3_html.close()
    
    fileo_html.write(html_f1)
    fileo_html.write(legend_figure)
    fileo_html.write(html_f2)
    fileo_html.write(html_selection)
    fileo_html.write('\t</select>\n\tgene sets\n')
    fileo_html.write('\t&emsp;&emsp;\n\t<button onclick="reset()">Refresh graph</button>\n')
    fileo_html.write('\t<br />\n\t'+rank_by_tag+'\n')
    fileo_html.write(html_f3)
    fileo_html.close()

    #write js file
    fileo_js = open(os.path.join(output_dir,'graph_files/script.js'),'w')
    ###js backbone
    filef1_js_path = pkg_resources.resource_filename('gscorepy', 'Database/graph_code_fragment/js_f1.txt')
    filef1_js = open(filef1_js_path)
    js_f1 = filef1_js.read()
    filef1_js.close()
    
    filef2_js_path = pkg_resources.resource_filename('gscorepy', 'Database/graph_code_fragment/js_f2.txt')
    filef2_js = open(filef2_js_path)
    js_f2 = filef2_js.read()
    filef2_js.close()
    
    filet1_cyto_path = pkg_resources.resource_filename('gscorepy', 'Database/graph_code_fragment/cyto_t1.txt')
    filet1_cyto = open(filet1_cyto_path)
    cyto_t1 = filet1_cyto.read()
    filet1_cyto.close()
    
    filet2_cyto_path = pkg_resources.resource_filename('gscorepy', 'Database/graph_code_fragment/cyto_t2.txt')
    filet2_cyto = open(filet2_cyto_path)
    cyto_t2 = filet2_cyto.read()
    filet2_cyto.close()
    
    fileo_js.write(js_f1)
    for node_num,func_name in zip(total_select,function_list):
        fileo_js.write('\t'*4+func_name+cyto_t1)
        json = json_generate(enrich_DEGlist_df, node_num)
        fileo_js.write(json)
        fileo_js.write(cyto_t2)
        if node_num!=total_select[-1]:
            fileo_js.write(',')
        fileo_js.write('\n')
    fileo_js.write(js_f2)
    fileo_js.close()
    
