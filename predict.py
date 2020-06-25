import time

def location(nodes,bound,num_of_agents): # predict location for every agent
    method=int(input("please select method: \n1.dijkstra\n2.alpha\n"))

    if method:
        print("starting dijkstra's algorithm")

        start_time=time.time()
        res_1 = [[] for i in range(num_of_agents)]
        GPS_event=[]
        for i in range(len(nodes)):
            if nodes[i][0][0]=='G':
                GPS_event.append(i)

        cur=GPS_event[:]
        r_most=[bound for i in range(len(nodes))] # corresponding to each node
        detected=[]
        for i in GPS_event:
            r_most[i]=nodes[i][0][3]

        print("initializing GPS events")
        print(r_most)

        while(len(detected)!=len(nodes)):
            tmp=[]
            for i in cur:
                for j in range(1,len(nodes[i])):
                    r_most[nodes[i][j][0]]=min(r_most[i]+nodes[i][j][1],r_most[nodes[i][j][0]])
                    if nodes[i][j][0] not in detected and nodes[i][j][0] not in tmp:
                        tmp.append(nodes[i][j][0])

                detected.append(i)

            cur=tmp



        cur=GPS_event[:]
        l_most = [bound for i in range(len(nodes))]  # corresponding to each node
        detected = []
        for i in GPS_event:
            l_most[i] = bound-nodes[i][0][3]

        print("initializing GPS events")
        print(l_most)

        while (len(detected) != len(nodes)):
            tmp = []
            for i in cur:
                for j in range(1, len(nodes[i])):
                    l_most[nodes[i][j][0]] = min(l_most[i] + nodes[i][j][1], l_most[nodes[i][j][0]])
                    if nodes[i][j][0] not in detected and nodes[i][j][0] not in tmp:
                        tmp.append(nodes[i][j][0])

                detected.append(i)

            cur = tmp
        for i in range(len(l_most)):
            l_most[i] = bound - l_most[i]


        for i in range(len(nodes)):
            if nodes[i][0][0]=='G':
                res_1[nodes[i][0][1]].append([nodes[i][0][2]]+[l_most[i],r_most[i]])


            if nodes[i][0][0] =='M':
                res_1[nodes[i][0][1]].append([nodes[i][0][3]]+[l_most[i],r_most[i]])
                res_1[nodes[i][0][2]].append([nodes[i][0][3]]+[l_most[i],r_most[i]])

        end_time=time.time()
        print("finish! Time used: {}".format(end_time-start_time))



    if method:
        print("starting alpha's algorithm")
        alpha=0.7

        start_time = time.time()
        res = [[] for i in range(num_of_agents)]
        GPS_event = []
        for i in range(len(nodes)):
            if nodes[i][0][0] == 'G':
                GPS_event.append(i)

        cur = GPS_event[:]
        r_most = [bound for i in range(len(nodes))]  # corresponding to each node
        detected = []
        for i in GPS_event:
            r_most[i] = nodes[i][0][3]

        print("initializing GPS events")
        print(r_most)

        while (len(detected) != len(nodes)):
            tmp = []
            for i in cur:
                for j in range(1, len(nodes[i])):
                    r_most[nodes[i][j][0]] = min(int(r_most[i] + nodes[i][j][1]*alpha), r_most[nodes[i][j][0]])
                    if nodes[i][j][0] not in detected and nodes[i][j][0] not in tmp:
                        tmp.append(nodes[i][j][0])

                detected.append(i)

            cur = tmp

        cur = GPS_event[:]
        l_most = [bound for i in range(len(nodes))]  # corresponding to each node
        detected = []
        for i in GPS_event:
            l_most[i] = bound - nodes[i][0][3]

        print("initializing GPS events")
        print(l_most)

        while (len(detected) != len(nodes)):
            tmp = []
            for i in cur:
                for j in range(1, len(nodes[i])):
                    l_most[nodes[i][j][0]] = min(int(l_most[i] + nodes[i][j][1]*alpha), l_most[nodes[i][j][0]])
                    if nodes[i][j][0] not in detected and nodes[i][j][0] not in tmp:
                        tmp.append(nodes[i][j][0])

                detected.append(i)

            cur = tmp
        for i in range(len(l_most)):
            l_most[i] = bound - l_most[i]

        for i in range(len(nodes)):
            if nodes[i][0][0] == 'G':
                res[nodes[i][0][1]].append([nodes[i][0][2]] + [l_most[i], r_most[i]])

            if nodes[i][0][0] == 'M':
                res[nodes[i][0][1]].append([nodes[i][0][3]] + [l_most[i], r_most[i]])
                res[nodes[i][0][2]].append([nodes[i][0][3]] + [l_most[i], r_most[i]])

        end_time = time.time()
        print("finish! Time used: {}".format(end_time - start_time))
        return res_1,res



def hit_rate(agent_set,predict_set): # calculate the hit rate for an agent
    cor_rate=0
    acc_rate=0

    hit=0
    miss=0
    area=0
    for i in range(len(predict_set)):
        for j in range(len(predict_set[i])):
            time=predict_set[i][j][0]
            left=predict_set[i][j][1]
            right=predict_set[i][j][2]

            area+=max((right-left+1),0)

            if left<=agent_set[i].track[time][0]<=right:
                hit+=1
            else:
                miss+=1

    cor_rate=hit/(hit+miss)
    acc_rate=hit/area

    print()
    print("hit rate = {}".format(cor_rate))
    print("accuracy = {}".format(acc_rate))

    return cor_rate,acc_rate


'''

def hit_rate(agent_set,predict_x_set,predict_y_set): # calculate the hit rate for an agent
    cor_rate=0
    acc_rate=0

    hit=0
    miss=0
    area=0
    for i in range(len(predict_x_set)):
        for j in range(len(predict_x_set)):
            time=predict_x_set[i][j][0]
            left=predict_x_set[i][j][1][0]
            right=predict_x_set[i][j][1][1]
            down=predict_y_set[i][j][1][0]
            up=predict_y_set[i][j][1][1]

            area+=max((right-left)*(up-down),0)

            if left<=agent_set[i].track[time][0]<=right and down<=agent_set[i].track[time][1]<= up:
                hit+=1
            else:
                miss+=1

    cor_rate=hit/(hit+miss)
    acc_rate=hit/area

    print()
    print("hit rate = {}".format(cor_rate))
    print("accuracy = {}".format(acc_rate))

    return cor_rate,acc_rate
'''


# [G,agent, time, position]
# [M, agent, agent, time]

"""
nodes=[[['G',0,1,1],[1,3]],
       [['M',0,1,4],[0,3],[2,2],[3,1]],
       [['G',1,2,3],[1,2]],
      [['M',2,1,5],[1,1]]]


print(location(nodes,10,3))

"""