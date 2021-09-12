import numpy as np


def calculate_kids_per_teacher(df):
    """Calculates number of kids per teacher in one school

    Parameters
    ----------
    df : pandas.DataFrame
        dataframe with data
        

    Returns
    -------
    df : pandas.Series
        Series with result of calculations

    """
    kids = df['Uczniowie, wychow., słuchacze']
    teachers = df[['Nauczyciele pełnozatrudnieni', 'Nauczyciele niepełnozatrudnieni (stos.pracy)']].sum(axis=1)
    df_result = kids.divide(teachers)
    df_result = df_result.replace(np.Infinity, 0)
    df_result = df_result.replace(np.nan, 0)
    df_result = df_result.apply(lambda x: round(x))
    return df_result


def calculate_kids_per_school_by_year(df):
    """Calculates number of kids per school in one year of birth

    Parameters
    ----------
    df : pandas.DataFrame
        

    Returns
    -------
    df : pandas.DataFrame
        dataframe with result of calculations

    """
    kids_years = {
        "Przedszkole": [2012, 2013, 2014, 2015],
        "Punkt przedszkolny": [2012, 2013, 2014, 2015],
        "Szkoła podstawowa": [2011, 2010, 2009, 2008, 2007, 2006],
        "Gimnazjum": [2005, 2004, 2003],
        "Liceum ogólnokształcące": [2002, 2001, 2000],
        "Technikum": [2002, 2001, 2000, 1999],
        "Sześcioletnia szkoła muzyczna I stopnia": [2012, 2011, 2010, 2009, 2008, 2007],
        "Czteroletnie liceum plastyczne": [2002, 2001, 2000, 1999],
    }
    years_range = range(1999, 2016)

    for row in df.iterrows():
        years = kids_years[row[1]['Nazwa typu']]
        sum_of_kids_in_school = 0
        for year in years:
            sum_of_kids_in_school += row[1][year]
        kids = row[1]['Uczniowie, wychow., słuchacze']
        for year in years_range:
            if year not in years:
                df.loc[df['Lp.'] == row[1]['Lp.'], year] = -1
            else:
                if (sum_of_kids_in_school == 0):
                    df.loc[df['Lp.'] == row[1]['Lp.'], year] = 0
                else:
                    df.loc[df['Lp.'] == row[1]['Lp.'], year] = (kids * row[1][year]) / sum_of_kids_in_school
    return df


def calculate_statistics_kids_per_teacher(df, value, group_columns, list_of_statistics):
    """Calculates statistics for kids per teacher in one school value

    Parameters
    ----------
    df : pandas.DataFrame
        dataframe with data

    value : str
        name of column with data to calculate statistics

    group_columns : list of str
        list with names of columns to group by

    list_of_statistics : list of str
        list of statistic names to calculate
        

    Returns
    -------
    df : pandas.DataFrame
        dataframe with result of calculations

    """
    result = df.groupby(group_columns)[value].agg(list_of_statistics)
    if ('mean' in list_of_statistics):
        result['mean'] = result['mean'].apply(lambda x: round(x))
    return result


def calculate_statistics_for_years(df, value, group_columns, list_of_statistics):
    """Calculates statistics for kids per school in one year of birth value

    Parameters
    ----------
    df : pandas.DataFrame
        dataframe with data

    value : str
        name of column with data to calculate statistics

    group_columns : list of str
        list with names of columns to group by

    list_of_statistics : list of str
        list of statistic names to calculate

    Returns
    -------
    df: pandas.DataFrame
        dataframe with result of calculations

    """

    def calc_min(col):
        """Calculates min from non negative values

        Parameters
        ----------
        col : array of float64


        Returns
        -------
        value: int
            rounded min non negative number from given array

        """
        values = list(filter(lambda x: x >= 0, list(col)))
        if len(values) == 0:
            return 0
        return round(min(values))

    def calc_max(col):
        """Calculates max from non negative values

        Parameters
        ----------
        col : array of float64


        Returns
        -------
        value: int
            rounded max non negative number from given array

        """
        values = list(filter(lambda x: x >= 0, list(col)))
        if len(values) == 0:
            return 0
        return round(max(values))

    def calc_mean(col):
        """Calculates mean from non negative values

        Parameters
        ----------
        col : array of float64


        Returns
        -------
        value: int
            rounded mean of non negative numbers from given array

        """
        values = list(filter(lambda x: x >= 0, list(col)))
        if len(values) == 0:
            return 0
        return round(sum(values) / len(values))

    funcs = {
        'min': calc_min,
        'max': calc_max,
        'mean': calc_mean
    }
    methods = [funcs[method] for method in list_of_statistics]

    return df.groupby(group_columns)[value].agg(methods)
