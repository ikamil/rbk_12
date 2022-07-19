import pandas as pd

from app.transformers.base import Transformer


class TagsTransformer(Transformer):
    def transform(self, input_data: pd.DataFrame, mode='train') -> pd.DataFrame:
        # input_data['amount_of_tags'] = input_data['tags_parsed'].apply(
        #     lambda x: len(x) if isinstance(x, list) else 0
        # )
        return input_data
