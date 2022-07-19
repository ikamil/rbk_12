import pandas as pd

from app.transformers.base import Transformer
from definitions import FULL_DATA_DIR


class SaverPreprocess(Transformer):
    def transform(self, input_data: pd.DataFrame, mode='train') -> pd.DataFrame:
        input_data.to_json(
            FULL_DATA_DIR / f'full_{mode}.json',
            orient='records',
            indent=2,
            force_ascii=False,
        )
        return input_data
