import math

import numpy as np
import pandas as pd


def drop_first_row(df):
    """Drops first row


        Parameters
        ----------
        df : pandas.Dataframe
            dataframe with data


        Returns
        -------
        df : pandas.DataFrame
            dataframe with deleted first row of original dataframe


        """
    return df.drop(index=0)

def extract_data_from_subsheets(sheets):
    """Extract data from all subsheets

    Dataframe is taken from all subsheets of sheet given as a pandas ExcelFile Object

    Parameters
    ----------
    sheets : pandas.ExcelFile
        ExcelFile object with data


    Returns
    -------
    df : pandas.DataFrame
        dataframe with concatenated data from all pages of ExcelFile


    """
    districts = sheets.sheet_names
    dfs = []
    for district in districts:
        df = pd.read_excel(sheets, sheet_name=district, skiprows=8, header=None)
        filterer = df[1][1]
        not_null_id_rows = df[df[1] != filterer].index.values.tolist()
        indexes_len = len(not_null_id_rows)
        for iter in range(indexes_len - 1):
            df_part = df.iloc[not_null_id_rows[iter]:not_null_id_rows[iter + 1], 0:3]
            df_part[0] = df_part[0].str.strip()
            code = df.iloc[not_null_id_rows[iter], 1]
            df_part = df_part[df_part[0].str.match(r'^[0-9]*$') == True]
            df_new = pd.DataFrame([list(df_part[2])], index=[code], columns=list(df_part[0]))
            dfs.append(df_new)
    result = pd.concat(dfs)
    return result


def change_age_into_year_of_birth(df):
    """Change age into year of birth

    Function changes dataframe column with ages into year of birth starting from 2020

    Parameters
    ----------
    df : pandas.DataFrame
        dataframe with data
        

    Returns
    -------
    df : pandas.DataFrame
        dataframe with changed column names
    """
    years = df.columns
    years = [2020 - int(year) for year in years]
    df.columns = years
    return df


def split_index_into_districts(df):
    """Add three new columns with voivodeship ,county ,district id

    Function takes index column which is also district id from dataframe
    and splits it into three columns:
    1st concatenated with 2nd number from code is voivodeship code
    3rd concatenated with 4th number from code is county code
    5rd concatenated with 6th number from code is district code
    7th dropped

    Parameters
    ----------
    df : pandas.DataFrame
        dataframe with data
        

    Returns
    -------
    df : pandas.DataFrame
        dataframe with new three columns

    """
    indexes = df.index.values
    indexes = [str(index) for index in indexes]
    woj = [x[0:2] for x in indexes]
    pow = [x[2:4] for x in indexes]
    gm = [x[4:6] for x in indexes]
    df = df.assign(woj=woj)
    df = df.assign(pow=pow)
    df = df.assign(gm=gm)
    return df


def connect_dataframes(df_schools, df_years):
    """Adds years columns from df_year dataframe to df_schools dataframe

    Function joins data about kids from every year into data about schools.
    Data are merged by voivodeship ,county ,district ids

    Parameters
    ----------
    df_schools : pandas.DataFrame
        dataframe with data about kids in schools
        
    df_years : pandas.DataFrame
        dataframe with data about kids in a given year

    Returns
    -------
    df : pandas.DataFrame
        dataframe

    """
    return pd.merge(df_schools, df_years, on=['woj', 'pow', 'gm'], how="left")


def get_preferred_schools(df, schools):
    """Gets only data about schools from schools list

    Function filters dataframe and returns only data about schools passed in list plus data about "Zespoly szkol"

    Parameters
    ----------
    df : pandas.DataFrame
        dataframe with data
        
    schools : list of str
        list with names of schools considered in the analysis
        

    Returns
    -------
    df : pandas.DataFrame
        dataframe with data about schools considered in the analysis

    """
    # refy szkół
    refs = df[df['Nazwa typu'].isin(schools)]['Nr RSPO jednostki sprawozdawczej'].dropna().unique()

    if ('Zespół szkół i placówek oświatowych' in schools):
        schools.remove('Zespół szkół i placówek oświatowych')

    # refy zespołów szkół
    zesp_refs = df[df['Nazwa typu'] == 'Zespół szkół i placówek oświatowych'][
        'Nr RSPO jednostki sprawozdawczej'].dropna().unique()
    zesp_refs_set = set(zesp_refs)

    # Brane są tylko pod uwagę zespoły szkół, które mają współny ref z schools
    refs_intersection = list(zesp_refs_set.intersection(refs))

    teachers_in_zesp_from_intersection = \
        df[(df['Nazwa typu'] == 'Zespół szkół i placówek oświatowych') & df['Nr RSPO jednostki sprawozdawczej'].isin(
            refs_intersection)]['Nauczyciele pełnozatrudnieni'].sum() + \
        df[(df['Nazwa typu'] == 'Zespół szkół i placówek oświatowych')
           & df['Nr RSPO jednostki sprawozdawczej'].isin(refs_intersection)][
            'Nauczyciele niepełnozatrudnieni (stos.pracy)'].sum()

    df_schools = df[df['Nazwa typu'].isin(schools)]
    number_of_all_children = df['Uczniowie, wychow., słuchacze'].sum()
    number_of_lost_children = number_of_all_children - df_schools['Uczniowie, wychow., słuchacze'].sum()
    number_of_all_teachers = df['Nauczyciele pełnozatrudnieni'].sum() + df[
        'Nauczyciele niepełnozatrudnieni (stos.pracy)'].sum()
    print(f'all {number_of_all_teachers}')
    number_of_accepted_teachers = df_schools['Nauczyciele pełnozatrudnieni'].sum() + df_schools[
        'Nauczyciele niepełnozatrudnieni (stos.pracy)'].sum() + teachers_in_zesp_from_intersection
    print(f'acc {number_of_accepted_teachers}')

    print(
        f"Lost {number_of_lost_children} children from {number_of_all_children} and it is {(number_of_lost_children * 100) / number_of_all_children}% loss\n")
    print(
        f"Lost {number_of_all_teachers - number_of_accepted_teachers} teachers from {number_of_all_teachers} and it is {((number_of_all_teachers - number_of_accepted_teachers) * 100) / number_of_all_teachers}% loss\n")

    return pd.concat([df_schools, df[
        (df['Nazwa typu'] == 'Zespół szkół i placówek oświatowych') & df['Nr RSPO jednostki sprawozdawczej'].isin(
            refs_intersection)]])


def distribute_teachers_from_zesp(df):
    """Distribute teachers to schools

    Function takes teachers from Zespoly szkol and distributes them to other schools with the same RSPO number
    Each school recieves teachers according to the number of kids

    Parameters
    ----------
    df : pandas.DataFrame
        dataframe with data
        

    Returns
    -------
    df : pandas.DataFrame
        dataframe with data distributed into schools and removed "Zespoly szkol"

    """
    refs = list(
        df[df['Nazwa typu'] == 'Zespół szkół i placówek oświatowych']['Nr RSPO jednostki sprawozdawczej'].unique())
    for rspo in refs:
        df_sub = df[df['Nr RSPO jednostki sprawozdawczej'] == rspo]
        teachers_from_zesp = df_sub[df_sub['Nazwa typu'] == 'Zespół szkół i placówek oświatowych'][
                                 'Nauczyciele niepełnozatrudnieni (stos.pracy)'].sum() + \
                             df_sub[df_sub['Nazwa typu'] == 'Zespół szkół i placówek oświatowych'][
                                 'Nauczyciele pełnozatrudnieni'].sum()

        df_no_zesp = df_sub[df_sub['Nazwa typu'] != 'Zespół szkół i placówek oświatowych']

        sum_of_children_from_schools = df_no_zesp['Uczniowie, wychow., słuchacze'].sum()
        if (sum_of_children_from_schools > 0):
            free_teachers = teachers_from_zesp
            indexes = df_no_zesp.index.values.tolist()
            for i in range(len(indexes) - 1):
                teachers = math.floor((float(df_no_zesp.loc[df_no_zesp.index == indexes[
                    i], 'Uczniowie, wychow., słuchacze']) / sum_of_children_from_schools) * teachers_from_zesp)
                df[df['Lp.'] == indexes[i]]['Nauczyciele pełnozatrudnieni'] += teachers
                free_teachers -= teachers
            df[df['Lp.'] == indexes[-1]]['Nauczyciele pełnozatrudnieni'] += free_teachers

    return df[df['Nazwa typu'] != 'Zespół szkół i placówek oświatowych']


def change_type_of_area_to_float(df):
    """Change type to float64

    Function changes type of values in woj, pow and gm columns to float64 type.

    Parameters
    ----------
    df : pandas.DataFrame
        dataframe with data

    Returns
    -------
    df : pandas.DataFrame
        dataframe with changed type of values in columns

    """
    df['gm'] = df['gm'].astype(np.float64)
    df['pow'] = df['pow'].astype(np.float64)
    df['woj'] = df['woj'].astype(np.float64)
    return df
