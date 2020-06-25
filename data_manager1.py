
import matplotlib.pyplot as plt
from agent import agent



meeting=[]
n=0
no=[]
nodes=[]

def takeSecond(elem):
    return elem[1]


def find_events(num_of_agent,events):#find all events and add it to corresponding person
    global n
    for i in range(num_of_agent):
        for j in range(i+1,num_of_agent):
            for p in range(len(events[i])):
                for q in range(len(events[j])):
                    if events[i][p]==events[j][q]:
                        n+=1
                        #m[i].append(['M',i,j,m[i][p][1]])
                        #m[j].append(['M',i,j,m[i][p][1]])
                        meeting.append(['M',i,j,events[i][p][1]])
                        print(['M',i,j,events[i][p][1]])




def graph(events):# use all the meeting events to draw a graph using L-∞ norm
    for i in range(n):
        mk=[]
        for j in range(len(events[meeting[i][1]])):
            if events[meeting[i][1]][j][1]<meeting[i][3]:
                p=events[meeting[i][1]][j]
            elif events[meeting[i][1]][j][1]>meeting[i][3]:
                q=events[meeting[i][1]][j]
                break
        meeting.append(p)
        meeting.append(q)
        mk.append(meeting[i])
        mk.append([n+4*(i+1)-4,abs(p[1]-meeting[i][3])])
        mk.append([n+4*(i+1)-3,abs(q[1]-meeting[i][3])])
        for j in range(len(events[meeting[i][2]])):
            if events[meeting[i][2]][j][1]<meeting[i][3]:
                p=events[meeting[i][2]][j]
            elif events[meeting[i][2]][j][1]>meeting[i][3]:
                q=events[meeting[i][2]][j]
                break
        meeting.append(p)
        meeting.append(q)
        mk.append([n+4*(i+1)-2,abs(p[1]-meeting[i][3])])
        mk.append([n+4*(i+1)-1,abs(q[1]-meeting[i][3])])
        nodes.append(mk)

    for i in range(n,5*n):
        tmp=[]
        j=(i-n)//4
        k=(i-n-4*j)//2+1
        tmp.append(['G',meeting[j][k],meeting[i][1],meeting[i][2][0]])
        tmp.append([j,abs(meeting[i][1]-meeting[j][3])])
        nodes.append(tmp)


    return nodes




