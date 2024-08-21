import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import importlib
importlib.reload(matplotlib); importlib.reload(plt); importlib.reload(sns)

def plot(DEG_list_result_df, involved_dic, criterion, save_dir):
    if criterion=='fdrq':
        figure_df = DEG_list_result_df[DEG_list_result_df['FDR_q_value']<=0.05]
    else:
        figure_df = DEG_list_result_df[DEG_list_result_df['p_value']<=0.05]
    
    figure_df['ratio'] = DEG_list_result_df['m']/DEG_list_result_df['n']
    involved_num_list = []
    for ID in figure_df['GeneSet']:
        involved_num_list.append(len(involved_dic[ID]))
    figure_df['Involved DEG count'] = involved_num_list
    figure_df = figure_df.sort_values(['ratio'],ascending=False)
    
    if len(figure_df)>100:
        figure_df = figure_df.head(100)
    
    x_value = max(list(figure_df['ratio']))*100
    y_value = len(figure_df)
    
    sns.set(font_scale=x_value/8, style='whitegrid')
    ax = plt.figure(dpi = 300, figsize=(x_value,y_value+2)) #
    if criterion=='fdrq':
        ax = sns.scatterplot(data=figure_df, x="ratio", y="GeneSet", hue="FDR_q_value",palette='coolwarm_r',hue_norm=(0,0.05),size="Involved DEG count"
                             , sizes=(10*x_value,100*x_value))
    else:
        ax = sns.scatterplot(data=figure_df, x="ratio", y="GeneSet", hue="p_value",palette='coolwarm_r',hue_norm=(0,0.05),size="Involved DEG count"
                             , sizes=(10*x_value,100*x_value))
        
    handles, labels = ax.get_legend_handles_labels()
    handles = handles[labels.index('Involved DEG count')+1:]
    labels = labels[labels.index('Involved DEG count')+1:]
    leg = plt.legend(title='Involved DEG count',title_fontsize=52,handles=handles, labels=labels, bbox_to_anchor=(1.03, 1), loc="upper left",prop={'size': 52})
    leg._legend_box.align = "left"
    
    #colorbar
    norm = plt.Normalize(0,0.05)
    sm = plt.cm.ScalarMappable(cmap='coolwarm_r',norm=norm)
    ##(x,y,寬度,高度)
    axins = ax.inset_axes((1+(1.3/x_value),1-(24/y_value),1/x_value,12.5/y_value)) #2 sets
    clb = plt.colorbar(sm,cax=axins, orientation="vertical") #,label='FDR q-value/\nNominal p-value'
    clb_text = {'fontsize':52}
    if criterion=='fdrq':
        clb.ax.set_title('FDR $\it{q}$ value\n', loc='left',**clb_text)
    else:
        clb.ax.set_title('$\it{p}$ value\n', loc='left',**clb_text)
    clb.ax.tick_params(labelsize=50)
    
    ax.set(ylim=(len(figure_df),-1))
    plt.ylabel('')
    plt.xlabel('Ratio fo coexpressed DEG pairs (m/n)',size=52, weight='bold')
    plt.xticks(size=52)
    plt.yticks(size=52)
    
    plt.savefig(save_dir, bbox_inches='tight', dpi=300)
    plt.show()
    
