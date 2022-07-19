import pandas as pd

from app.transformers.base import Transformer


class CTRTransformer(Transformer):
    def transform(self, input_data: pd.DataFrame, mode='train') -> pd.DataFrame:
        X = input_data['ctr']
        input_data['is_na_ctr'] = X.isna()
        # input_data['ctr_normal_distribution'] = (X - np.mean(X)) / np.std(X)

        # eps = self.kwargs.get('eps') or 0.5
        # start = 0
        # end = 40

        # for i, j in zip(
        #     np.arange(start, end, eps), np.arange(start + eps, end + eps, eps)
        # ):
        #     input_data[f'ctr_{i}_{j}'] = X.apply(
        #         lambda x: (x >= i) & (x < j)
        #     )
        return input_data
