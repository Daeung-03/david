import pandas as pd


def Serching_Analysis():
  structure = pd.read_csv('datafiles/area_struct.csv')
  category = pd.read_csv('datafiles/area_category.csv')
  map = pd.read_csv('datafiles/area_map.csv')

  category_dict = category.set_index(
      category.columns[0])[category.columns[1]].to_dict()
  category_dict.update({0: 'etc'})

  structure_id_column = structure.columns[2]
  structure[structure_id_column] = structure[structure_id_column].map(
      category_dict)

  merged_map_struct = map.merge(structure, on=['x', 'y'], how='outer')
  merged_sort = merged_map_struct.sort_values(by='area').reset_index(
      drop='True')

  filtered_data = merged_sort[merged_sort['area'] == 1].reset_index(
      drop='True')
  return filtered_data


def Print_Report(data):
  structure_stats = data.groupby('category').agg({
      'x': ['count', 'min', 'max'],
      'y': ['min', 'max'],
      'ConstructionSite': 'sum'
  }).round(2)

  print("구조물 종류별 상세 통계:")
  print(structure_stats)


Print_Report(Serching_Analysis())
