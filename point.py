class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __repr__(self):
    return "(%.1f, %.1f)" %(self.x, self.y)

def edist(pt1, pt2):
  dx=pt1.x-pt2.x ## distance of 'x' between pt1 and pt2
  dy=pt1.y-pt2.y ## distance of 'y' between pt1 and pt2
  ## the Euclidean distance between pt1 and pt2 is
  ## the square root of the sum of squares of the distances
  ed = (dx**2+dy**2)**0.5
  return ed

if __name__ == "__main__" :
    import sys
    pt1 = Point(float(sys.argv[1]), float(sys.argv[2]))
    pt2 = Point(float(sys.argv[3]), float(sys.argv[4]))
    ed = edist(pt1, pt2)
    print(ed)

