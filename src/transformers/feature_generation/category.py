import pandas as pd

from app.transformers.base import Transformer


class CategoryTransformer(Transformer):
    def transform(self, input_data: pd.DataFrame, mode='train') -> pd.DataFrame:
        input_data['category'] = input_data['category'].astype('category')
        input_data['category_parsed'] = input_data['category'].astype(
            'category'
        )
        input_data['category_from_title'] = input_data[
            'category_from_title'
        ].isna()
        return input_data
