import numpy as np
import pandas as pd

from definitions import AUTHORS_DIR
from src.transformers.base import Transformer


class AuthorsTransformer(Transformer):
    def transform(self, input_data: pd.DataFrame, mode='train') -> pd.DataFrame:
        if self.kwargs.get('target_variable') != 'depth':
            input_data['amount_of_authors'] = input_data[
                'authors_parsed'
            ].apply(lambda x: len(x) if isinstance(x, list) else 0)

        if self.kwargs.get('target_variable') == 'full_reads_percent':
            input_data['is_author_na'] = input_data['authors_parsed'].isna()

            o = {'м': True, 'ж': False}
            authors = pd.read_json(AUTHORS_DIR / 'authors.json').T
            p = []
            p1 = []
            p2 = []
            p4 = []
            p5 = []
            for i in input_data['authors_parsed']:

                if i is None:
                    p.append(i)
                    p1.append(i)
                    p2.append(i)
                    p4.append(i)
                    p5.append(i)
                else:
                    a = []
                    b = []
                    for j in i:
                        a.append(authors.loc[j]['публикации'])
                        b.append(authors.loc[j]['пол'])
                    if len(set(b)) == 1 and b[0] == 'м':
                        p1.append(0)
                    elif len(set(b)) == 1 and b[0] == 'ж':
                        p1.append(1)
                    else:
                        p1.append(2)
                    p.append(np.sum(a))
                    p2.append(np.mean(a))
                    p4.append(np.sum(np.array(b) == 'м'))
                    p5.append(np.sum(np.array(b) == 'ж'))
            input_data['amount_of_publication_sum'] = p
            input_data['amount_of_publication_mean'] = p2
            input_data['number_of_man_in_authors'] = p4
            input_data['number_of_woman_in_authors'] = p5
            input_data['type_of_authors'] = p1
            # input_data['type_of_authors'] = input_data[
            #     'type_of_authors'].astype(
            #     'category'
            # )

        return input_data
