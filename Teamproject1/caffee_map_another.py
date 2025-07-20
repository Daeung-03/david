import pandas as pd

def searching_analysis():
    # 데이터 로드
    structure = pd.read_csv("dataFiles/area_struct.csv")
    category = pd.read_csv("dataFiles/area_category.csv")
    map_data = pd.read_csv("dataFiles/area_map.csv")
    
    # 카테고리 매핑 (한 줄로 단축)
    category_dict = {**category.set_index(category.columns[0])[category.columns[1]].to_dict(), 0: " etc"}
    
    # 카테고리 매핑 적용 및 병합, 정렬을 체이닝으로 처리
    merged_data = (map_data
                   .merge(structure.assign(**{structure.columns[2]: structure[structure.columns[2]].map(category_dict)}), 
                          on=["x", "y"], how="outer")
                   .sort_values("area")
                   .reset_index(drop=True))
    
    # Area1 데이터 필터링 및 저장
    merged_data[merged_data["area"] == 1].reset_index(drop=True).to_csv(
        'dataFiles/mas_map.csv', index=False, encoding='utf-8-sig')
    
    return merged_data

def print_report(data):
    print("구조물 종류별 개수:")
    print(data["category"].value_counts().sort_index())

if __name__ == "__main__":
    print_report(searching_analysis())
