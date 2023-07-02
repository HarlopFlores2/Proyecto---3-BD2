import RtreeQuery
import SequentialQuery
# test knn_query
rtree_query = RtreeQuery.RtreeQuery(100)
print(rtree_query.knn_query('/mnt/c/proyecto3-bd2/lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg', 5))

# test range_query sequentially
sequential_query = SequentialQuery.SequentialQuery()
print(sequential_query.range_query('/mnt/c/proyecto3-bd2/lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg', 0.6))

# test knn_query sequentially
print(sequential_query.knn_query('/mnt/c/proyecto3-bd2/lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg', 5))