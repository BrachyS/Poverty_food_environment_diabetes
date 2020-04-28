def scatterplot(data):
    '''Make customized scatterplot'''
    plt.style.use('classic')
    plt.scatter(pca_features_shortlist15[:, 0], df.PCT_DIABETES_ADULTS13, s=6)
    plt.xlabel('PC1', fontsize=18)
    plt.ylabel('Adult Diabetes Rate (%) in 2013', fontsize=18)
    plt.savefig('Figs/PC1_diabetes.png')