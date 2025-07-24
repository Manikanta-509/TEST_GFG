class Solution:
    def isSquare(self, x1, y1, x2, y2, x3, y3, x4, y4):
        def dist_sq(xa, ya, xb, yb):
            return (xa - xb) ** 2 + (ya - yb) ** 2

        points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
        dists = []

        for i in range(4):
            for j in range(i + 1, 4):
                dists.append(dist_sq(points[i][0], points[i][1], points[j][0], points[j][1]))

        dists.sort()

        if (
            dists[0] > 0 and
            dists[0] == dists[1] == dists[2] == dists[3] and
            dists[4] == dists[5] and
            dists[4] == 2 * dists[0]
        ):
            return "Yes"
        else:
            return "No"
