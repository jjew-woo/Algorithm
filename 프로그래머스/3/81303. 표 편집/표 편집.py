class Node :
    def __init__(self,left = None,right = None):
        self.remove = False
        self.left = left
        self.right = right
    
def solution(n, k, cmd):
    table = [Node(i-1,i+1) for i in range(n)]
    table[0].left= None
    table[n - 1].right = None
    delete = []
    
    for c in cmd:
        if c[0] == 'U':
            
            for _ in range(int(c[2:])):
                k = table[k].left

        elif c[0] == 'D':
            for _ in range(int(c[2:])):
                k = table[k].right

        elif c[0] == 'C':
            delete.append(k)
            table[k].remove = True
            l, r = table[k].left, table[k].right
            
            if l != None:
                table[l].right = r
            
            if r:
                table[r].left = l
                k = r
            else:
                k = l

        elif c[0] == 'Z':
            row = delete.pop()
            table[row].remove = False
            l, r = table[row].left, table[row].right

            if l:
                table[l].right = row
            if r:
                table[r].left = row

    return ''.join(['X' if n.remove else 'O' for n in table])