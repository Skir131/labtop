__author__ = 'Minsuk Heo'

vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]
graphs = (vertexList, edgeList)

def dfs(graph, start):
    vertexList, edgeList = graph
    visitedVertex = [] #방문한 숫자를 체크하는 리스트
    stack = [start] #방문할 함수를 가지는 리스트
    adjacencyList = [[] for vertex in vertexList] #트리에 있는 숫자만큼 리스트 생성
    

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1]) #0번째 숫자에서 연결된 숫자 알려주는 리스트

    while stack: #처음엔 [0] #두번째 스택 [1,2]
        current = stack.pop() #처음에 0을 스택에서 꺼낸다. #current = 2
        for neighbor in adjacencyList[current]: #[1,2]를 꺼낸다.
            if not neighbor in visitedVertex: #방문한 요소가 없으므로 진행
                stack.append(neighbor) #스택에 1,2를 넣는다
        visitedVertex.append(current) #0을 방문했으므로 0을 집어 넣는다.
    return visitedVertex 

print(dfs(graphs, 0))