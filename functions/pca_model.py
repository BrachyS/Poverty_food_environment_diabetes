def pca_model(data, components):
    '''Run PCA analysis and make plots'''
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    pca = PCA(n_components = components)
    pca_features = pca.fit_transform(scaled_data)
    features = range(pca.n_components_)

    ## Plot variance explained
    tally = 0
    scree = [0]
    for percent in pca.explained_variance_ratio_:
        tally += percent
        scree.append(tally)

    plt.figure(figsize=(5,5))
    plt.plot(scree)
    plt.xlabel('Number of Principal Components')
    plt.ylabel('Fraction Variance Explained')
    plt.ylim(0,1)

    print('Variance explained by first {} components:'.format(components),scree[-1]) # pring total variance explained by n components

    return pca_features