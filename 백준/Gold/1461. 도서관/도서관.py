N, M = map(int, input().split())
plus = []; minus = []
max_coord = 0

for c in list(map(int, input().split())):
    max_coord = max(max_coord, abs(c))
    minus.append(c) if c < 0 else plus.append(c) 
minus.sort(); plus.sort(reverse=True)

ans = 0
m_idx, p_idx = 0, 0
while(m_idx < len(minus) or p_idx < len(plus)):
    idx = min(m_idx+M, len(minus))
    ans += ((abs(min(minus[m_idx:idx])) if m_idx != idx else 0)*2)
    m_idx = idx
    idx = min(p_idx+M, len(plus))
    ans += ((max(plus[p_idx:idx]) if p_idx != idx else 0)*2)
    p_idx = idx

print(ans-max_coord)