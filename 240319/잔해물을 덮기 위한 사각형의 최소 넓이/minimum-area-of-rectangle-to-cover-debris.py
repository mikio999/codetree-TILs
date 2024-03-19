def calculate_area(x1,y1,x2,y2,m1,k1,m2,k2):
  overlap_x1 = max(x1,m1)
  overlap_y1 = max(y1,k1)
  overlap_x2 = min(m2,k2)
  overlap_y2 = min(y2,k2)

  overlap_width = max(0, overlap_x2 - overlap_x1)
  overlap_height = max(0, overlap_y2 - overlap_y1)
  overlap_area = overlap_width * overlap_height

  first_area = (x2-x1) * (y2-y1)
  remaining_area = first_area - overlap_area
  return remaining_area

x1,y1,x2,y2 = map(int, input().split())
m1,k1,m2,k2 = map(int, input().split())

OFFSET = 1000
x1 += OFFSET
y1 += OFFSET
x2 += OFFSET
y2 += OFFSET
m1 += OFFSET
k1 += OFFSET
m2 += OFFSET
k2 += OFFSET

print(calculate_area(x1, y1, x2, y2, m1, k1, m2, k2))