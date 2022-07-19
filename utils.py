from datetime import datetime


def str_to_date(date_in: str):
    """
    function convert string from <input type="datetime-local"> to datetime python
    :param date_in: '2022-07-19T03:40'
    :return: 2022-07-19 03:40:00
    """
    date_processing = date_in.replace('T', '-').replace(':', '-').split('-')
    date_processing = [int(v) for v in date_processing]
    date_out = datetime(*date_processing)
    return date_out
