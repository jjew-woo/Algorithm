def solution(brown, yellow):
    size = brown + yellow
    for i in range(3, int(size**0.5)+1):
        if size % i == 0:
            h = i
            w = size // i
            if yellow == (h-2) * (w-2):
                return [w,h]