from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


class Bert:
    def __init__(self):

        self.bert(self, data_cv, job_discr)

    def bert(cv, job_discr):
        sen = job_discr
        model = SentenceTransformer('bert-base-nli-mean-tokens')
        check_cv = cv
        check_embeddings = model.encode(check_cv)
        check_embeddings.shape
        sen_embeddings = model.encode(sen)
        sen_embeddings.shape
        return cosine_similarity([check_embeddings], sen_embeddings[0:])