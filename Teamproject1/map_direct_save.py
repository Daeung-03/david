import pandas as pd
import matplotlib.pyplot as plt
from collections import deque
from caffee_map import Serching_Analysis
from map_draw import visualize_map, mask_overlap, setup_coordinate_system


class GridPathfinder:

  def __init__(self, data):
    """
      그리드 최단 경로 탐색기 초기화
      """
    self.data = data.copy()
    self.grid_map = {}
    self.setup_grid()

  def setup_grid(self):
    """
      데이터를 그리드 맵으로 변환하고 시작점, 도착점 설정
      """
    # 그리드 맵 생성 - 각 좌표에 대한 정보 저장
    for _, row in self.data.iterrows():
      coord = (row['x'], row['y'])
      self.grid_map[coord] = {
          'category': row['category'].strip(),
          'construction_site': row['ConstructionSite'],
          'walkable': row['ConstructionSite'] == 0  # 건설현장이 아니면 통행 가능
      }

    # 시작점과 도착점 찾기
    self.start = None
    self.goals = []  # 여러 커피점이 있을 수 있음

    for coord, info in self.grid_map.items():
      category = info['category'].strip()  # 공백 제거
      if category == 'MyHome':
        self.start = coord
      elif category == 'BandalgomCoffee':
        self.goals.append(coord)

    if not self.start:
      raise ValueError("시작점(MyHome)을 찾을 수 없습니다.")
    if not self.goals:
      raise ValueError("목표점(BandalgomCoffee)을 찾을 수 없습니다.")

    print(f"시작점: {self.start}")
    print(f"목표점들: {self.goals}")

  def find_shortest_path_to_nearest_cafe(self):
    """
    가장 가까운 커피점까지의 최단 경로 찾기
    """
    shortest_path = None
    shortest_distance = float('inf')
    target_cafe = None

    # 모든 커피점에 대해 최단 경로 탐색
    for cafe_pos in self.goals:
      path = self.bfs_shortest_path(self.start, cafe_pos)
      if path and len(path) < shortest_distance:
        shortest_distance = len(path)
        shortest_path = path
        target_cafe = cafe_pos

    if shortest_path:
      print(f"최단 경로를 찾았습니다!")
      print(f"목표 커피점: {target_cafe}")
      print(f"경로 길이: {len(shortest_path) - 1} 단계")
      print(f"경로: {shortest_path}")
    else:
      print("경로를 찾을 수 없습니다. 모든 커피점이 차단되었을 수 있습니다.")

    return shortest_path, target_cafe

  def bfs_shortest_path(self, start, goal):
    """
    BFS를 사용하여 시작점에서 목표점까지의 최단 경로 찾기
    """
    if start == goal:
      return [start]

    # BFS 초기화 - 큐와 방문 체크
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
      current_pos, path = queue.popleft()

      # 상하좌우 이웃 탐색
      for neighbor in self.get_neighbors(current_pos):
        if neighbor not in visited:
          new_path = path + [neighbor]

          if neighbor == goal:
            return new_path

          visited.add(neighbor)
          queue.append((neighbor, new_path))

    return None

  def get_neighbors(self, pos):
    """
    주어진 위치의 유효한 이웃 좌표들 반환 (상하좌우 이동)
    """
    x, y = pos
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상, 하, 우, 좌
    neighbors = []

    for dx, dy in directions:
      new_pos = (x + dx, y + dy)
      # 그리드 범위 내에 있고 통행 가능한 위치인지 확인
      if new_pos in self.grid_map and self.grid_map[new_pos]['walkable']:
        neighbors.append(new_pos)

    return neighbors


def visualize_map(data, path, save_path='map_final.png'):

  # 플롯 생성
  fig, ax = plt.subplots(figsize=(10, 10))

  # 좌표계 설정
  x_min, x_max, y_min, y_max = setup_coordinate_system(ax, data)

  # 카테고리별 데이터 저장
  apartments_buildings = data[data['category'].isin(['Apartment', 'Building'])]
  shops = data[data['category'] == 'BandalgomCoffee']
  home = data[data['category'] == 'MyHome']
  construction_sites = data[data['ConstructionSite'] == 1]

  # 아파트·빌딩 -> 갈색 원형
  ax.scatter(apartments_buildings['x'],
             apartments_buildings['y'],
             c='saddlebrown',
             marker='o',
             s=100,
             label=f"apartments and bulidings ({len(apartments_buildings)})")

  # 반달곰 커피점 -> 녹색 사각형
  ax.scatter(shops['x'],
             shops['y'],
             c='limegreen',
             marker='s',
             s=120,
             label=f"bandalgom coffee ({len(shops)})")

  # 집 -> 녹색 삼각형
  ax.scatter(home['x'],
             home['y'],
             c='green',
             marker='^',
             s=120,
             label="my_home")

  # 건설현장 -> 회색 사각형
  ax.scatter(construction_sites['x'],
             construction_sites['y'],
             c='lightgrey',
             s=140,
             alpha=0.8,
             marker='s',
             label=f'construction_sites ({len(construction_sites)})',
             zorder=5)

  # 범례 표시
  ax.legend(loc='upper right', bbox_to_anchor=(1.0, 1.0))

  # 이미지 저장
  fig.savefig('map.png', bbox_inches=None, dpi=300)

  # 최단경로 저장
  if path:
    path_x = [p[0] for p in path]
    path_y = [p[1] for p in path]
    ax.plot(path_x,
            path_y,
            'r-',
            linewidth=3,
            alpha=0.8,
            label='shortest path')
    ax.scatter(path_x, path_y, c='red', s=50, alpha=0.7)

  ax.legend()
  fig.savefig(save_path, bbox_inches=None, dpi=300)
  plt.tight_layout()
  plt.show()

  # 레이아웃 조정
  plt.tight_layout()
  plt.show()
  return fig, ax


def main():
  # 지도 데이터 불러오기
  ori_data = Serching_Analysis()
  ori_data['category'] = ori_data['category'].str.strip()
  data_masked = mask_overlap(ori_data)

  # 경로탐색기 인스턴스 생성
  pathfinder = GridPathfinder(data_masked)

  # 집 → 카페 최단 경로 탐색
  path, target_cafe = pathfinder.find_shortest_path_to_nearest_cafe()

  # 최단 경로가 존재하면 CSV 저장 및 시각화
  if path:
    # 경로 CSV 저장
    path_df = pd.DataFrame([{
        'step': i,
        'x': pos[0],
        'y': pos[1]
    } for i, pos in enumerate(path)])
    path_df.to_csv("home_to_cafe.csv", index=False, encoding='utf-8-sig')
    print("경로가 'home_to_cafe.csv' 파일로 저장되었습니다.")

    # 지도와 경로 시각화 + 파일 저장
    visualize_map(ori_data, path, save_path='map_final.png')
  else:
    print("최단 경로를 찾을 수 없습니다.")
    # 경로 없이 지도만 시각화
    visualize_map(ori_data, path=None, save_path='map_final.png')


if __name__ == '__main__':
  main()
