import RtreeQuery
import SequentialQuery
import KDTree

def testKNN(enc_dataset, image_query, k_values):
    # KNN - Secuencial
    seq_query = SequentialQuery.SequentialQuery(enc_dataset)
    print(seq_query.knn_query(image_query, k_values))
    
    # KNN - RTree
    rtree_query = RtreeQuery.RtreeQuery(enc_dataset)
    print(rtree_query.knn_query(image_query, k_values))
    
    # KNN - HighD
    kdtree_query = KDTree.KDTree(enc_dataset)
    print(kdtree_query.knn_query(image_query, k_values))


# testKNN('dict_encoding12800.pickle', '../lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg', 8)
