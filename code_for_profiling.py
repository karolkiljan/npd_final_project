import pandas as pd
from nypd.nypd.prepare import drop_first_row, get_preferred_schools, distribute_teachers_from_zesp, \
    extract_data_from_subsheets, change_age_into_year_of_birth, split_index_into_districts, \
    change_type_of_area_to_float, connect_dataframes
from nypd.nypd.calculate import calculate_kids_per_teacher, calculate_statistics_kids_per_teacher, \
    calculate_kids_per_school_by_year, calculate_statistics_for_years

#Subtask A
df_schools = pd.read_excel('./data/Wykaz_szkół_i_placówek_wg_stanu_na_30.IX._2018_w.5.xlsx')
df_schools = drop_first_row(df_schools)

schools = ['Przedszkole', 'Szkoła podstawowa', 'Gimnazjum', 'Sześcioletnia szkoła muzyczna I stopnia',
                          'Liceum ogólnokształcące', 'Technikum', 'Czteroletnie liceum plastyczne', 'Punkt przedszkolny']

df_schools = get_preferred_schools(df_schools, schools)
df_schools = distribute_teachers_from_zesp(df_schools)

df_schools['Nauczyciele/uczniowie'] = calculate_kids_per_teacher(df_schools)

df_result_1 = calculate_statistics_kids_per_teacher(
    df_schools,
    'Nauczyciele/uczniowie',
    ['Gmina', 'woj', 'pow', 'gm', 'Nazwa typu'],
    ['min', 'max', 'mean']
)
df_result_2 = calculate_statistics_kids_per_teacher(
    df_schools,
    'Nauczyciele/uczniowie',
    ['Typ gminy', 'Nazwa typu'],
    ['min', 'max', 'mean']
)

df_result_1.to_csv('./result_kids_per_teacher_a')
df_result_2.to_csv('./result_kids_per_teacher_b')

#Subtask B
sheets = pd.ExcelFile('./data/tabela12.xls')
df_years = extract_data_from_subsheets(sheets)
df_years = change_age_into_year_of_birth(df_years)
df_years = split_index_into_districts(df_years)

df_schools = change_type_of_area_to_float(df_schools)
df_years = change_type_of_area_to_float(df_years)

df_merged = connect_dataframes(df_schools, df_years)

df_calc_kids_by_year = calculate_kids_per_school_by_year(df_merged)

years = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
df_result_B = calculate_statistics_for_years(df_calc_kids_by_year, years, ['Typ gminy'], ['min', 'max', 'mean'])

columns = df_result_B.columns
columns = [column.replace('calc_', '') for column in columns]
df_result_B.columns = columns
df_result_B.to_csv('./result_kids_per_school')




