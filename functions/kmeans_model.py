def kmeans_model(PCs, clusters, title):
    '''Conduct K-means clustering, make elbow plot,
    clustering plot with PC1, PC2,
    and return clustering assignment'''
    from scipy import cluster
    # Use PC1 and PC2 for kmeans clustering, looping through 1 to 6 clusters
    df = [cluster.vq.kmeans(PCs[:, 0:2], i) for i in range(1, 7)]

    # Figure 1: Elbow plot
    figure1 = plt.scatter(x=list(range(1, 7)),
                          y=[var for (cent, var) in df])
    plt.xlabel('Number of clusters')
    plt.ylabel('Average Euclidean distance between \n observations and centroids')
    plt.show()

    # Figure 2: Visualize clusters with PC1 and PC2
    cent, var = df[clusters - 1]  # choose number of clusters
    # use vq() to get as assignment for each obs.
    assignment, cdist = cluster.vq.vq(PCs[:, 0:2], cent)
    plt.style.use('classic')
    figure2 = plt.scatter(PCs[:, 0], PCs[:, 1], c=assignment)  # Plot PC1 and PC2
    plt.xlabel('PC1', fontsize=18)
    plt.ylabel('PC2', fontsize=18)
    plt.title('Clustering for {}'.format(title), fontsize=18)

    return assignment