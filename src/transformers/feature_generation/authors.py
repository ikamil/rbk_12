import pandas as pd

from app.transformers.base import Transformer


class AuthorsTransformer(Transformer):
    def transform(self, input_data: pd.DataFrame, mode='train') -> pd.DataFrame:
        # input_data['is_author_na'] = input_data['authors_parsed'].isna()
        # input_data['amount_of_authors'] = input_data['authors_parsed'].apply(
        #     lambda x: len(x) if isinstance(x, list) else 0
        # )
        return input_data
