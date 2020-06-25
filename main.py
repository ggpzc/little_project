import agent
import time
import data_manager1
import predict
import visualization as vis


def main():
    agents = []

    events=[]
    for i in range(500):
        a = agent.agent(i, 100, 100)
        e=a.event
        agents.append(a)
        e.sort(key=data_manager1.takeSecond)
        events.append(e)

    data_manager1.find_events(500,events)

    v = data_manager1.graph(events)
    for i in range(len(v)):
        print(v[i])

    vis.Graph(v)


    predict_set_1,predict_set_2=predict.location(v,100,500)
    print(predict_set_1)
    print(predict_set_2)
    
    for i in range(len(predict_set_1)):
        for j in range(len(predict_set_1[i])):
            print("{}'th agent: predict time {} locate at [{},{}]".format(i,predict_set_1[i][j][0],predict_set_1[i][j][1],predict_set_1[i][j][2]))
            print(agents[i].track)
            print("real location: {}".format(agents[i].track[predict_set_1[i][j][0]]))

            print("{}'th agent: predict time {} locate at [{},{}]".format(i, predict_set_2[i][j][0],
                                                                          predict_set_2[i][j][1],
                                                                          predict_set_2[i][j][2]))
            print("real location: {}".format(agents[i].track[predict_set_2[i][j][0]]))

    predict.hit_rate(agents,predict_set_1)
    predict.hit_rate(agents,predict_set_2)

if __name__=="__main__":
    main()

'''
['M', 173, 228, 83]
['M', 179, 276, 662]
[['M', 173, 228, 83], [2, 3], [3, 31], [4, 2], [5, 11]]
[['M', 179, 276, 662], [6, 3], [7, 2], [8, 24], [9, 6]]
[['G', 173, 80, 78], [0, 3]]
[['G', 173, 114, 76], [0, 31]]
[['G', 228, 81, 80], [0, 2]]
[['G', 228, 94, 80], [0, 11]]
[['G', 179, 659, 49], [1, 3]]
[['G', 179, 664, 52], [1, 2]]
[['G', 276, 638, 52], [1, 24]]
[['G', 276, 668, 53], [1, 6]]
please select method: 
1.dijkstra
2.alpha
1
starting dijkstra's algorithm
initializing GPS events
[100, 100, 78, 76, 80, 80, 49, 52, 52, 53]
initializing GPS events
[100, 100, 22, 24, 20, 20, 51, 48, 48, 47]
finish! Time used: 0.0
starting alpha's algorithm
initializing GPS events
[100, 100, 78, 76, 80, 80, 49, 52, 52, 53]
initializing GPS events
[100, 100, 22, 24, 20, 20, 51, 48, 48, 47]
finish! Time used: 0.0
[[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [[83, 78, 81], [80, 78, 78], [114, 76, 76]], [], [], [], [], [], [[662, 50, 52], [659, 49, 49], [664, 52, 52]], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [[83, 78, 81], [81, 80, 80], [94, 80, 80]], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [[662, 50, 52], [638, 52, 52], [668, 53, 53]], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
[[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [[83, 79, 80], [80, 78, 78], [114, 76, 76]], [], [], [], [], [], [[662, 51, 51], [659, 49, 49], [664, 52, 52]], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [[83, 79, 80], [81, 80, 80], [94, 80, 80]], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [[662, 51, 51], [638, 52, 52], [668, 53, 53]], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
173'th agent: predict time 83 locate at [78,81]
real location: [79, 66]
173'th agent: predict time 83 locate at [79,80]
real location: [79, 66]
173'th agent: predict time 80 locate at [78,78]
real location: [78, 66]
173'th agent: predict time 80 locate at [78,78]
real location: [78, 66]
173'th agent: predict time 114 locate at [76,76]
real location: [76, 68]
173'th agent: predict time 114 locate at [76,76]
real location: [76, 68]
179'th agent: predict time 662 locate at [50,52]
real location: [51, 65]
179'th agent: predict time 662 locate at [51,51]
real location: [51, 65]
179'th agent: predict time 659 locate at [49,49]
real location: [49, 66]
179'th agent: predict time 659 locate at [49,49]
real location: [49, 66]
179'th agent: predict time 664 locate at [52,52]
real location: [52, 64]
179'th agent: predict time 664 locate at [52,52]
real location: [52, 64]
228'th agent: predict time 83 locate at [78,81]
real location: [79, 66]
228'th agent: predict time 83 locate at [79,80]
real location: [79, 66]
228'th agent: predict time 81 locate at [80,80]
real location: [80, 65]
228'th agent: predict time 81 locate at [80,80]
real location: [80, 65]
228'th agent: predict time 94 locate at [80,80]
real location: [80, 64]
228'th agent: predict time 94 locate at [80,80]
real location: [80, 64]
276'th agent: predict time 662 locate at [50,52]
real location: [51, 65]
276'th agent: predict time 662 locate at [51,51]
real location: [51, 65]
276'th agent: predict time 638 locate at [52,52]
real location: [52, 68]
276'th agent: predict time 638 locate at [52,52]
real location: [52, 68]
276'th agent: predict time 668 locate at [53,53]
real location: [53, 65]
276'th agent: predict time 668 locate at [53,53]
real location: [53, 65]

hit rate = 1.0
accuracy = 0.5454545454545454

hit rate = 1.0
accuracy = 0.8571428571428571'''

"""
hit rate = 1.0
accuracy = 0.23333333333333334

hit rate = 0.9047619047619048
accuracy = 0.3064516129032258


"""