from google.colab import drive
from N_grams_chars import N_GRAMS_WORDS
from Bert import Bert
from Normalize import Normalize
import numpy
from Summarize_matrix import Summarize_matrix




class Bert_ngrams_words_with_sum:

    def __init__(self):

        self.calculate(self, data_cv, job_discr)



    drive.mount('content')



    def calculate(self, data_cv, job_discr):
        with open('Bert_ngrams_words_withsummary.txt', "w", encoding='utf-8') as file:
            for i in range(len(data_cv)):
                bert_array = (Bert(data_cv[i], job_discr))
                results_df['bert'] = bert_array[0]
                ranking = results_df.sort_values('bert', ascending=False)
                num_rows = ranking.count()[0]
                quantity_rows = 10000
                new_indexes = [i for i in range(quantity_rows)]
                print(i)
                ranking.index = new_indexes
                file.write('\n______________________________________\n')
                file.write(doc.loc[doc['processed_text'] == data_cv[i]].values[0][0])
                file.write("\n ")
                file.write("\n 1st place:" + ((ranking.iloc[0][0])))
                file.write("\n  ")
                file.write("\n 3rd place:" + ((ranking.iloc[2][0])))
                file.write("\n  ")
                file.write("\n 5th place:" + ((ranking.iloc[4][0])))
                file.write("\n  ")
                file.write("\n middle place:" + ((ranking.iloc[num_rows // 2][0])))
                file.write("\n  ")
                file.write("\n last place:" + ((ranking.iloc[num_rows - 1][0])))
                file.write("\n ")




                n_grams_array = Normalize(N_GRAMS_WORDS(data_cv[i], job_discr))
                Bert_ngrams_matrix_sum = Summarize_matrix(bert_array, n_grams_array)
                results_df_bert_n_grams_word['bert-n-grams'] = Bert_ngrams_matrix_sum
                ranking1 = results_df_n_grams_word.sort_values('bert-n-grams', ascending=False)
                num_rows = ranking1.count()[0]
                quantity_rows = 10000
                new_indexes = [i for i in range(quantity_rows)]
                ranking1.index = new_indexes

                rank_1 = (numpy.array2string([ranking1.loc[ranking1['job_description'] == (ranking.iloc[0][0])].index][0][0]))

                score_1 = str(ranking1.loc[ranking1['job_description'] == (ranking.iloc[0][0])].values[0][4])

                first_line = ('\n 1st place in bert = ' + rank_1 + " " + score_1 + ' in Bert + ngrams(words) with summary')
                file.write(first_line)
                rank_3 = (numpy.array2string([ranking1.loc[ranking1['job_description'] == (ranking.iloc[2][0])].index][0][0]))

                score_3 = str(ranking1.loc[ranking1['job_description'] == (ranking.iloc[2][0])].values[0][4])

                second_line = ('\n 3rd bert in bert:' + rank_3 + " " + score_3 + ' in Bert + ngrams(words) with summary')
                file.write(second_line)
                rank_5 = (numpy.array2string([ranking1.loc[ranking1['job_description'] == (ranking.iloc[4][0])].index][0][0]))

                score_5 = str(ranking1.loc[ranking1['job_description'] == (ranking.iloc[4][0])].values[0][4])

                third_line = ('\n 5th place in bert:' + rank_5 + " " + score_5 + ' in Bert + ngrams(words) with summary')
                file.write(third_line)
                rank_middle = ((numpy.array2string(([ranking1.loc[ranking1['job_description'] == (ranking.iloc[4999][0])].index][0][0]))))

                score_middle = str(ranking1.loc[ranking1['job_description'] == (ranking.iloc[4999][0])].values[0][4])

                fourth_line = ('\n middle place in bert:' + rank_middle + " " + score_middle + ' in Bert + ngrams(words) with summary')
                file.write(fourth_line)
                rank_last = (numpy.array2string([ranking1.loc[ranking1['job_description'] == (ranking.iloc[9999][0])].index][0][0]))

                score_last = str(ranking1.loc[ranking1['job_description'] == (ranking.iloc[9999][0])].values[0][4])

                fifth_line = ('\n last place in bert:' + rank_last + " " + score_last + ' in Bert + ngrams(words) with summary')
                file.write(fifth_line)

            file.close()
            return file