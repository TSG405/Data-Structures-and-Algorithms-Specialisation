>>
import sys


class DisjointSet(object):
        def __init__(self,n,lines):
            self.n = n
            self.lines = [0] + lines
            self.rank = [0] * (n + 1)
            self.parent = list(range(0, n + 1))
            self.max = max(self.lines)

        def get_parent(self, x):
            parents_to_update = []

            root = x
            while root != self.parent[root]:
                parents_to_update.append(self.parent[root])
                root = self.parent[root]

            for i in parents_to_update:
                self.parent[i] = root

            return root

        def merge(self, dest, src):
            src_root = self.get_parent(src)
            dest_root = self.get_parent(dest)
            
            if src_root == dest_root:
                return

            if self.rank[src_root] >= self.rank[dest_root]:
                self.parent[src_root] = dest_root
            else:
                self.parent[dest_root] = src_root
                if self.rank[src_root] == self.rank[dest_root]:
                    self.rank[src_root] += 1

            self.lines[dest_root] += self.lines[src_root]
            self.lines[src_root] = 0

            if self.max < self.lines[dest_root]:
                self.max = self.lines[dest_root]

        def get_max_lines(self):
            return self.max


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lines = list(map(int, sys.stdin.readline().split()))

    ds = DisjointSet(n, lines)
    
    for i in range(m):
        destination, source = map(int, sys.stdin.readline().split())
        ds.merge(destination, source)
        print(ds.get_max_lines())
        
        
        
@ CODED BY TSG405, 2021
