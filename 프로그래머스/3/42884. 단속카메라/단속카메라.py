def solution(routes):
    routes.sort()
    camera = [routes[0]]
    for i in range(1, len(routes)):
        install = False
        for j in range(len(camera)):
            if (camera[j][0] <= routes[i][0] <= camera[j][1]) or (camera[j][0] <= routes[i][1] <= camera[j][1]):
                install = True
                camera[j] = (camera[j]+routes[i])
                camera[j].remove(max(camera[j]))
                camera[j].remove(min(camera[j]))
                camera[j].sort()
                break
                
        if not install:
            camera.append(routes[i])

    return len(camera)