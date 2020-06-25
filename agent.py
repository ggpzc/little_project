import random




class agent: # record the track of an agent and the events he meet


    def __init__(self,id,m,n):
        self.event=[]
        self.track=[]
        self.id=id
        time=random.randint(0,m*n//10)
        start_position=[random.randint(0,m),random.randint(0,n)]

        self.track.append([start_position[0],start_position[1]])

        for i in range(time-1):
            dir=random.randint(0,3) # up, down, left, right
            if(dir==0):
                if(start_position[0]>0):
                    start_position[0]-=1
                else:
                    start_position[0]+=1

            if (dir == 1):
                if (start_position[1] < n-1):
                    start_position[1] += 1
                else:
                    start_position[1] -= 1

            if (dir == 2):
                if (start_position[0] < m-1):
                    start_position[0] += 1
                else:
                    start_position[0] -= 1

            if (dir == 3):
                if (start_position[1] > 0):
                    start_position[1] -= 1
                else:
                    start_position[1] += 1
            self.track.append([start_position[0],start_position[1]])


        GPS_time=[]
        for i in range(random.randint(0,time//10)): # GPS event
            t=random.randint(0,time-1)
            if t not in GPS_time:
                GPS_time.append(t)
            else:
                i-=1

        for i in range(len(GPS_time)):
            tmp=['G']
            tmp.append(GPS_time[i])
            tmp.append(self.track[GPS_time[i]])

            self.event.append(tmp)

        print("Successfully random create agent{}:".format(self.id))
        print("the track of the agent is\n",self.track)
        print("randomly choose {} GPS events:".format(len(GPS_time)))
        print(self.event)
        print()




