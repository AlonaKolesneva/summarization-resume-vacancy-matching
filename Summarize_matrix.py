from scipy.sparse import coo_matrix, hstack

class Summarize_matrix:
    def __init__(self):

        self.matrix_sum(self, matrixA, matrixB)
    def matrix_sum(matrixA, matrixB):
        prepared_for_hstack_matrixA = coo_matrix(matrixA)
        prepared_for_hstack_matrixB = coo_matrix(matrixB)

        summary_matrix = hstack([prepared_for_hstack_matrixA, prepared_for_hstack_matrixB]).toarray()
        return summary_matrix