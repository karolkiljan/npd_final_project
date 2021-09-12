import pandas as pd

from nypd.nypd.prepare import split_index_into_districts, connect_dataframes, get_preferred_schools
from pandas._testing import assert_frame_equal


def test_change_age_into_year_of_birth():
    df = pd.DataFrame({
        '7': [1, 1],
        '6': [1, 1],
        '5': [1, 1]
    })

    result = pd.DataFrame({
        '2013': [1, 1],
        '2014': [1, 1],
        '2015': [1, 1],
    })

    assert_frame_equal(df, result)

def test_split_index_into_districts():
    df = pd.DataFrame({'test': [10, 20, 30, 40, 50]}, index =['1234567', '1122334', '1112223', '1010102', '3012123'])
    result = pd.DataFrame({'test': [10, 20, 30, 40, 50], 'woj': ['12', '11', '11', '10', '30'], 'pow': ['34', '22', '12', '10', '12'], 'gm': ['56', '33', '22', '10', '12']})
    assert_frame_equal(split_index_into_districts(df), result)

def test_connect_dataframes():
    df1 = pd.DataFrame({'test1': [10, 20, 30, 40, 50], 'woj': ['12', '11', '11', '10', '30'], 'pow': ['34', '22', '12', '10', '12'], 'gm': ['56', '33', '22', '10', '12']})
    df2 = pd.DataFrame({'test2': [10, 20, 30, 40, 50], 'woj': ['12', '11', '11', '10', '30'], 'pow': ['34', '22', '12', '10', '12'], 'gm': ['56', '33', '22', '10', '12']})
    result = pd.DataFrame({'test1': [10, 20, 30, 40, 50], 'test2': [10, 20, 30, 40, 50], 'woj': ['12', '11', '11', '10', '30'], 'pow': ['34', '22', '12', '10', '12'], 'gm': ['56', '33', '22', '10', '12']})
    assert_frame_equal(connect_dataframes(df1, df2), result)

def test_get_preferred_schools():
    pass

def test_distribute_teachers_from_zesp():
    pass

def test_change_type_of_area_to_float():
    pass