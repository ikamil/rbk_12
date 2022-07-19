import datetime

import holidays
import numpy as np
import pandas as pd

from app.transformers.base import Transformer

russia_holidays_list = holidays.Russia(years=[2021, 2022]).items()
russia_holidays_list = [str(x[0]) for x in russia_holidays_list]


def get_part_day(x):
    if (x > 4) and (x <= 8):
        return 'Early Morning'
    elif (x > 8) and (x <= 12):
        return 'Morning'
    elif (x > 12) and (x <= 16):
        return 'Noon'
    elif (x > 16) and (x <= 20):
        return 'Evening'
    elif (x > 20) and (x <= 24):
        return 'Night'
    elif x <= 4:
        return 'Late Night'


class DatetimeTransformer(Transformer):
    def transform(self, input_data: pd.DataFrame, mode='train') -> pd.DataFrame:
        input_data['publish_date'] = pd.to_datetime(
            input_data['publish_date']
        ) + datetime.timedelta(hours=3)
        input_data['minute'] = input_data['publish_date'].dt.minute
        input_data['hour'] = input_data['publish_date'].dt.hour
        input_data['part_of_the_day'] = (
            input_data['hour'].apply(get_part_day).astype('category')
        )
        # input_data['DATE'] = input_data['publish_date'].dt.date
        # input_data['DATE'] = input_data['DATE'].astype(str).astype('category')
        input_data['dayofweek'] = input_data['publish_date'].dt.dayofweek
        input_data['is_weekend'] = np.where(
            input_data['publish_date']
            .dt.day_name()
            .isin(['Sunday', 'Saturday']),
            1,
            0,
        )
        input_data['year'] = input_data['publish_date'].dt.year
        input_data['day'] = input_data['publish_date'].dt.day
        input_data['month'] = input_data['publish_date'].dt.month

        input_data['is_after_24_february'] = input_data[
            'publish_date'
        ] > datetime.datetime(2022, 2, 24)
        #
        input_data['quarter'] = input_data['publish_date'].dt.quarter

        input_data['time_sec'] = (
            input_data['publish_date'].dt.hour * 3600
            + input_data['publish_date'].dt.minute * 60
            + input_data['publish_date'].dt.second
        )
        return input_data
