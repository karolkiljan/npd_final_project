import pandas as pd
from pandas._testing import assert_frame_equal

from nypd.nypd.calculate import calculate_kids_per_teacher, calculate_statistics_for_years, \
    calculate_statistics_kids_per_teacher


def test_calculate_kids_per_teacher():
    df = pd.DataFrame({
        'Uczniowie, wychow., słuchacze': [10, 10, 10],
        'Nauczyciele pełnozatrudnieni': [1, 1, 1],
        'Nauczyciele niepełnozatrudnieni (stos.pracy)': [9, 1, 4],
    })
    sr = pd.Series([1, 5, 2])

    assert_frame_equal(calculate_kids_per_teacher(df), sr)


def test_calculate_kids_per_school_by_year():
    df = pd.DataFrame({
        'Lp.': [0, 1, 2, 3, 4, 5, 6, 7],
        'Uczniowie, wychow., słuchacze': [10, 10, 10, 10, 10, 10, 10, 10],
        'Nauczyciele pełnozatrudnieni': [1, 1, 1, 1, 1, 1, 1, 1],
        'Typ gminy': ['Gm', 'M', 'M', 'Gm', 'M-Gm', 'Gm', 'M-Gm', 'M'],
        'Nauczyciele niepełnozatrudnieni (stos.pracy)': [1, 1, 1, 1, 1, 1, 1, 1],
        'Nazwa typu': ['Przedszkole', 'Szkoła podstawowa', 'Gimnazjum', 'Sześcioletnia szkoła muzyczna I stopnia',
                       'Liceum ogólnokształcące', 'Technikum', 'Czteroletnie liceum plastyczne', 'Punkt przedszkolny'],
        '1999': [1, 1, 1, 1, 1, 1, 1, 1],
        '2000': [1, 1, 1, 1, 1, 1, 1, 1],
        '2001': [1, 1, 1, 1, 1, 1, 1, 1],
        '2002': [1, 1, 1, 1, 1, 1, 1, 1],
        '2003': [1, 1, 1, 1, 1, 1, 1, 1],
        '2004': [1, 1, 1, 1, 1, 1, 1, 1],
        '2005': [1, 1, 1, 1, 1, 1, 1, 1],
        '2006': [1, 1, 1, 1, 1, 1, 1, 1],
        '2007': [1, 1, 1, 1, 1, 1, 1, 1],
        '2008': [1, 1, 1, 1, 1, 1, 1, 1],
        '2009': [1, 1, 1, 1, 1, 1, 1, 1],
        '2010': [1, 1, 1, 1, 1, 1, 1, 1],
        '2011': [1, 1, 1, 1, 1, 1, 1, 1],
        '2012': [1, 1, 1, 1, 1, 1, 1, 1],
        '2013': [1, 1, 1, 1, 1, 1, 1, 1],
        '2014': [1, 1, 1, 1, 1, 1, 1, 1],
        '2015': [1, 1, 1, 1, 1, 1, 1, 1],
    })
    result = pd.DataFrame(
        {'Lp.': [0, 1, 2, 3, 4, 5, 6, 7], 'Uczniowie, wychow., słuchacze': [10, 10, 10, 10, 10, 10, 10, 10],
         'Nauczyciele pełnozatrudnieni': [1, 1, 1, 1, 1, 1, 1, 1],
         'Typ gminy': ['Gm', 'M', 'M', 'Gm', 'M-Gm', 'Gm', 'M-Gm', 'M'],
         'Nauczyciele niepełnozatrudnieni (stos.pracy)': [1, 1, 1, 1, 1, 1, 1, 1],
         'Nazwa typu': ['Przedszkole', 'Szkoła podstawowa', 'Gimnazjum', 'Sześcioletnia szkoła muzyczna I stopnia',
                        'Liceum ogólnokształcące', 'Technikum', 'Czteroletnie liceum plastyczne', 'Punkt przedszkolny'],
         1999: [-1.0, -1.0, -1.0, -1.0, -1.0, 2.5, 2.5, -1.0],
         2000: [-1.0, -1.0, -1.0, -1.0, 3.3333333333333335, 2.5, 2.5, -1.0],
         2001: [-1.0, -1.0, -1.0, -1.0, 3.3333333333333335, 2.5, 2.5, -1.0],
         2002: [-1.0, -1.0, -1.0, -1.0, 3.3333333333333335, 2.5, 2.5, -1.0],
         2003: [-1.0, -1.0, 3.3333333333333335, -1.0, -1.0, -1.0, -1.0, -1.0],
         2004: [-1.0, -1.0, 3.3333333333333335, -1.0, -1.0, -1.0, -1.0, -1.0],
         2005: [-1.0, -1.0, 3.3333333333333335, -1.0, -1.0, -1.0, -1.0, -1.0],
         2006: [-1.0, 1.6666666666666667, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0],
         2007: [-1.0, 1.6666666666666667, -1.0, 1.6666666666666667, -1.0, -1.0, -1.0, -1.0],
         2008: [-1.0, 1.6666666666666667, -1.0, 1.6666666666666667, -1.0, -1.0, -1.0, -1.0],
         2009: [-1.0, 1.6666666666666667, -1.0, 1.6666666666666667, -1.0, -1.0, -1.0, -1.0],
         2010: [-1.0, 1.6666666666666667, -1.0, 1.6666666666666667, -1.0, -1.0, -1.0, -1.0],
         2011: [-1.0, 1.6666666666666667, -1.0, 1.6666666666666667, -1.0, -1.0, -1.0, -1.0],
         2012: [2.5, -1.0, -1.0, 1.6666666666666667, -1.0, -1.0, -1.0, 2.5],
         2013: [2.5, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 2.5], 2014: [2.5, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 2.5],
         2015: [2.5, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 2.5]}
    )

    assert (calculate_kids_per_teacher(df).equals(result))


def test_calculate_statistics_kids_per_teacher():
    df = pd.DataFrame({
        'Uczniowie, wychow., słuchacze': [10, 10, 10],
        'Nauczyciele pełnozatrudnieni': [1, 1, 1],
        'Nauczyciele niepełnozatrudnieni (stos.pracy)': [9, 1, 4],
        'Nauczyciele/uczniowie': [1, 5, 2],
        'Typ gminy': ['M', 'G', 'M']
    })
    result = pd.DataFrame({'min': [5, 1], 'max': [5, 2], 'mean': [5, 2]})

    assert_frame_equal(calculate_statistics_kids_per_teacher(df, 'Nauczyciele/uczniowie', ['Typ gminy'],
                                                  ['min', 'max', 'mean']),result)


def test_calculate_statistics_for_years():
    df = pd.DataFrame(
        {'Lp.': [0, 1, 2, 3, 4, 5, 6, 7], 'Uczniowie, wychow., słuchacze': [10, 10, 10, 10, 10, 10, 10, 10],
         'Nauczyciele pełnozatrudnieni': [1, 1, 1, 1, 1, 1, 1, 1],
         'Typ gminy': ['Gm', 'M', 'M', 'Gm', 'M-Gm', 'Gm', 'M-Gm', 'M'],
         'Nauczyciele niepełnozatrudnieni (stos.pracy)': [1, 1, 1, 1, 1, 1, 1, 1],
         'Nazwa typu': ['Przedszkole', 'Szkoła podstawowa', 'Gimnazjum', 'Sześcioletnia szkoła muzyczna I stopnia',
                        'Liceum ogólnokształcące', 'Technikum', 'Czteroletnie liceum plastyczne', 'Punkt przedszkolny'],
         1999: [-1.0, -1.0, -1.0, -1.0, -1.0, 2.5, 2.5, -1.0],
         2000: [-1.0, -1.0, -1.0, -1.0, 3.3333333333333335, 2.5, 2.5, -1.0],
         2001: [-1.0, -1.0, -1.0, -1.0, 3.3333333333333335, 2.5, 2.5, -1.0],
         2002: [-1.0, -1.0, -1.0, -1.0, 3.3333333333333335, 2.5, 2.5, -1.0],
         2003: [-1.0, -1.0, 3.3333333333333335, -1.0, -1.0, -1.0, -1.0, -1.0],
         2004: [-1.0, -1.0, 3.3333333333333335, -1.0, -1.0, -1.0, -1.0, -1.0],
         2005: [-1.0, -1.0, 3.3333333333333335, -1.0, -1.0, -1.0, -1.0, -1.0],
         2006: [-1.0, 1.6666666666666667, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0],
         2007: [-1.0, 1.6666666666666667, -1.0, 1.6666666666666667, -1.0, -1.0, -1.0, -1.0],
         2008: [-1.0, 1.6666666666666667, -1.0, 1.6666666666666667, -1.0, -1.0, -1.0, -1.0],
         2009: [-1.0, 1.6666666666666667, -1.0, 1.6666666666666667, -1.0, -1.0, -1.0, -1.0],
         2010: [-1.0, 1.6666666666666667, -1.0, 1.6666666666666667, -1.0, -1.0, -1.0, -1.0],
         2011: [-1.0, 1.6666666666666667, -1.0, 1.6666666666666667, -1.0, -1.0, -1.0, -1.0],
         2012: [2.5, -1.0, -1.0, 1.6666666666666667, -1.0, -1.0, -1.0, 2.5],
         2013: [2.5, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 2.5], 2014: [2.5, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 2.5],
         2015: [2.5, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 2.5]}
    )
    result = pd.DataFrame(
        {(1999, 'calc_min'): [2, 0, 2], (1999, 'calc_max'): [2, 0, 2], (1999, 'calc_mean'): [2, 0, 2],
         (2000, 'calc_min'): [2, 0, 2], (2000, 'calc_max'): [2, 0, 3], (2000, 'calc_mean'): [2, 0, 3],
         (2001, 'calc_min'): [2, 0, 2], (2001, 'calc_max'): [2, 0, 3], (2001, 'calc_mean'): [2, 0, 3],
         (2002, 'calc_min'): [2, 0, 2], (2002, 'calc_max'): [2, 0, 3], (2002, 'calc_mean'): [2, 0, 3],
         (2003, 'calc_min'): [0, 3, 0], (2003, 'calc_max'): [0, 3, 0], (2003, 'calc_mean'): [0, 3, 0],
         (2004, 'calc_min'): [0, 3, 0], (2004, 'calc_max'): [0, 3, 0], (2004, 'calc_mean'): [0, 3, 0],
         (2005, 'calc_min'): [0, 3, 0], (2005, 'calc_max'): [0, 3, 0], (2005, 'calc_mean'): [0, 3, 0],
         (2006, 'calc_min'): [0, 2, 0], (2006, 'calc_max'): [0, 2, 0], (2006, 'calc_mean'): [0, 2, 0],
         (2007, 'calc_min'): [2, 2, 0], (2007, 'calc_max'): [2, 2, 0], (2007, 'calc_mean'): [2, 2, 0],
         (2008, 'calc_min'): [2, 2, 0], (2008, 'calc_max'): [2, 2, 0], (2008, 'calc_mean'): [2, 2, 0],
         (2009, 'calc_min'): [2, 2, 0], (2009, 'calc_max'): [2, 2, 0], (2009, 'calc_mean'): [2, 2, 0],
         (2010, 'calc_min'): [2, 2, 0], (2010, 'calc_max'): [2, 2, 0], (2010, 'calc_mean'): [2, 2, 0],
         (2011, 'calc_min'): [2, 2, 0], (2011, 'calc_max'): [2, 2, 0], (2011, 'calc_mean'): [2, 2, 0],
         (2012, 'calc_min'): [2, 2, 0], (2012, 'calc_max'): [2, 2, 0], (2012, 'calc_mean'): [2, 2, 0],
         (2013, 'calc_min'): [2, 2, 0], (2013, 'calc_max'): [2, 2, 0], (2013, 'calc_mean'): [2, 2, 0],
         (2014, 'calc_min'): [2, 2, 0], (2014, 'calc_max'): [2, 2, 0], (2014, 'calc_mean'): [2, 2, 0],
         (2015, 'calc_min'): [2, 2, 0], (2015, 'calc_max'): [2, 2, 0], (2015, 'calc_mean'): [2, 2, 0]})

    years = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]

    assert_frame_equal(calculate_statistics_for_years(df, years, ['Typ gminy'], ['min', 'max', 'mean']),result)
