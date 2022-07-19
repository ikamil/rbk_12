import pandas as pd

from app.transformers.base import Transformer


class TitleTransformer(Transformer):
    def transform(self, input_data: pd.DataFrame, mode='train') -> pd.DataFrame:
        input_data['title_parsed_from_yandex_is_na'] = input_data[
            'title_parsed_from_yandex'
        ].isna()
        input_data['news_inline_titles_parsed_is_na'] = input_data[
            'news_inline_titles_parsed'
        ].isna()
        input_data['num_words_title'] = (
            input_data['title_preprocessed'].str.split().apply(lambda x: len(x))
        )
        return input_data
