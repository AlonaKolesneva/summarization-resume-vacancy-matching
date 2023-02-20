from google.colab import drive
import numpy
from Bert import Bert
from Okapi import Okapi
from Normalize import Normalize

class Okapi_without_sum:

    def __init__(self):

        self.calculate(self, data_cv, job_discr)




    drive.mount('content')





    # path_txt = os.path.join(os.getcwd(), ' MyDrive', 'results', 'bert.txt')
    def calculate(self, data_cv, job_discr):
        with open('okapi_withoutsum.txt', "w", encoding='utf-8') as file:

            for i in range(len(data_cv)):
                bert_array = (Bert(data_cv[i], job_discr))
                results_df['bert'] = bert_array[0]
                ranking = results_df.sort_values('bert', ascending=False)
                num_rows = ranking.count()[0]
                quantity_rows = 10000
                new_indexes = [i for i in range(quantity_rows)]
                ranking.index = new_indexes
                file.write('\n______________________________________\n')
                file.write(doc.loc[doc['processed_text'] == data_cv[i]].values[0][0])
                file.write("\n ")
                # first_place = get_summary((ranking.iloc[0][0]))
                file.write("\n 1st place:" + ((ranking.iloc[0][0])))
                file.write("\n  ")
                file.write("\n 3rd place:" + ((ranking.iloc[2][0])))
                file.write("\n  ")
                file.write("\n 5th place:" + ((ranking.iloc[4][0])))
                file.write("\n  ")
                file.write("\n middle place:" + ((ranking.iloc[num_rows // 2][0])))
                file.write("\n  ")
                file.write("\n last place:" + ((ranking.iloc[num_rows - 1][0])))
                okapi_score = Normalize((Okapi((data_cv[i], job_discr))))

                results_df_okapi['Okapi_score'] = okapi_score

                ranking1 = results_df_okapi.sort_values('Okapi_score', ascending=False)
                num_rows = ranking1.count()[0]
                ranking1.index = new_indexes
                rank_1 = (numpy.array2string([ranking1.loc[ranking1['job_description'] == (ranking.iloc[0][0])].index][0][0]))
                score_1 = str(ranking1.loc[ranking1['job_description'] == (ranking.iloc[0][0])].values[0][3])
                first_line = ('\n 1st place in bert = ' + rank_1 + " " + score_1 + ' in Okapi without summary')
                file.write(first_line)
                rank_3 = (numpy.array2string([ranking1.loc[ranking1['job_description'] == (ranking.iloc[2][0])].index][0][0]))
                score_3 = str(ranking1.loc[ranking1['job_description'] == (ranking.iloc[2][0])].values[0][3])
                second_line = ('\n 3rd bert in bert:' + rank_3 + " " + score_3 + ' in Okapi without summary')
                file.write(second_line)
                rank_5 = (numpy.array2string([ranking1.loc[ranking1['job_description'] == (ranking.iloc[4][0])].index][0][0]))
                score_5 = str(ranking1.loc[ranking1['job_description'] == (ranking.iloc[4][0])].values[0][3])
                third_line = ('\n 5th place in bert:' + rank_5 + " " + score_5 + ' in Okapi without summary')
                file.write(third_line)
                rank_middle = ((numpy.array2string(([ranking1.loc[ranking1['job_description'] == (ranking.iloc[4999][0])].index][0][0]))))
                score_middle = str(ranking1.loc[ranking1['job_description'] == (ranking.iloc[4999][0])].values[0][3])
                fourth_line = ('\n middle place in bert:' + rank_middle + " " + score_middle + ' in Okapi without summary')
                file.write(fourth_line)
                rank_last = (numpy.array2string([ranking1.loc[ranking1['job_description'] == (ranking.iloc[9999][0])].index][0][0]))
                score_last = str(ranking1.loc[ranking1['job_description'] == (ranking.iloc[9999][0])].values[0][3])
                fifth_line = ('\n last place in bert:' + rank_last + " " + score_last + ' in Okapi without summary')
                file.write(fifth_line)
            file.close()
            return file
