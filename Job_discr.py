import datadotworld as dw
import stanza

stanza.download('en')
nlp = stanza.Pipeline('en')

class job_discription:

    def __init__(self):
        self.jb_discr(self)


    def forming_jb(self):
        select = 'SELECT job_description, job_title, uniq_id FROM software_developer_united_states_1971_20191023_1  Limit' + ' ' + str(10000)
        results = dw.query('jobspikr/software-developer-job-listings-from-usa', select)

        results_df = results.dataframe
        job_descriptions = dict(zip(results_df.uniq_id, results_df.job_description))
        job_descriptions_titles_dict = dict(zip(results_df.uniq_id, results_df.job_title))
        return results_df

    def jb_discr(results_df):
        job_discr = []
        for j in range(len(results_df.values)):
            job_discr.append(nlp((results_df.values[j][0])))
        return job_discr