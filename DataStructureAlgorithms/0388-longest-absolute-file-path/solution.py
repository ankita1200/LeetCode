class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            print(line)
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
            print(pathlen)
        return maxlen
