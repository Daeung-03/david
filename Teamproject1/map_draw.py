import pandas as pd
import matplotlib as plt
from coffe_map import Serching_Analysis

def setup_coordinate_system(ax, data):
    """
    좌표계 설정: 좌측 상단이 (1,1), 우측 하단이 가장 큰 좌표
    """
    
    # 데이터 범위 확인
    x_min, x_max = data['x'].min(), data['x'].max()
    y_min, y_max = data['y'].min(), data['y'].max()
    
    # y축을 뒤집어서 작은 값이 위쪽에 오도록 설정
    ax.invert_yaxis()
    
    # 축 범위 설정 (여백 0.5 추가)
    ax.set_xlim(x_min - 0.5, x_max + 0.5)
    ax.set_ylim(y_max + 0.5, y_min - 0.5)
    
    # 축 라벨 및 제목 설정
    ax.set_xlabel('X 좌표 (서쪽 ← → 동쪽)')
    ax.set_ylabel('Y 좌표 (북쪽 ↑ ↓ 남쪽)')
    
    # 격자 표시
    ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    
    return x_min, x_max, y_min, y_max

def visualize_map(data):
    # matplotlib 한글 폰트 설정
    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.rcParams['axes.unicode_minus'] = False
    
    # 플롯 생성
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # 좌표계 설정
    x_min, x_max, y_min, y_max = setup_coordinate_system(ax, data)
    
    # 일반 좌표점 (건설현장 제외)
    normal_points = data[data['ConstructionSite'] == 0]
    construction_sites = data[data['ConstructionSite'] == 1]
    
    # 일반 좌표점 표시
    ax.scatter(normal_points['x'], normal_points['y'], 
              c='lightblue', s=50, alpha=0.6, 
              label=f'일반 지점 ({len(normal_points)}개)')
    
    # 건설현장 강조 표시
    ax.scatter(construction_sites['x'], construction_sites['y'], 
              c='red', s=100, alpha=0.8, marker='s',
              label=f'건설현장 ({len(construction_sites)}개)')
    
    # 좌표계 확인용 모서리 점 표시
    corners = [(x_min, y_min), (x_max, y_min), (x_min, y_max), (x_max, y_max)]
    corner_labels = ['좌측상단', '우측상단', '좌측하단', '우측하단']
    
    for i, (x, y) in enumerate(corners):
        ax.plot(x, y, 'ko', markersize=8)
        ax.annotate(f'{corner_labels[i]}\n({x},{y})', 
                   (x, y), xytext=(10, 10), 
                   textcoords='offset points', 
                   fontsize=8, ha='left')
    
    # 범례 표시
    ax.legend(loc='upper right', bbox_to_anchor=(1.0, 1.0))
    
    # 레이아웃 조정
    plt.tight_layout()
    
    return fig, ax

def main():
    ori_data = Serching_Analysis()

if __name__ == '__main__':
    main()