def barplot(data, title):
    '''Function to make customized bar plot'''
    figure = sns.barplot(y='ShortName', x='Importance', data=data)
    plt.ylabel('Features')
    plt.xlim(0, 0.5)
    plt.title('Feature importance for {}'.format(title))
    plt.show()