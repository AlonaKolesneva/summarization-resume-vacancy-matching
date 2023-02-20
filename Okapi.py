import numpy

class Okapi:
    def __init__(self):

        self.ranking_okapi_bm25(self, data_cv, job_discr)


    def ranking_okapi_bm25(cv, j_discr, b=0.75, k=1.2):
        m = len(j_discr)
        avdl = sum(sum(j_discr)) / float(m)
        dfw = sum(j_discr.astype(bool))
        idf = numpy.log((m + 1.0) / dfw)
        num = (k + 1.0) * j_discr
        dem = k * (1.0 - b + (b * (sum(j_discr.T) / avdl)))
        dem = numpy.matrix(dem)
        dem = j_discr + dem.T
        okapi = numpy.array(num / dem) * idf
        score = numpy.dot(cv, okapi.T)
        return score