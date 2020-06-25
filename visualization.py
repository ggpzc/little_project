import matplotlib.pyplot as plt


"""
hit rate = 1.0
accuracy = 0.23333333333333334
hit rate = 0.9047619047619048
accuracy = 0.3064516129032258

hit rate = 1.0
accuracy = 0.2692307692307692
hit rate = 0.9047619047619048
accuracy = 0.34545454545454546

hit rate = 1.0
accuracy = 0.22674418604651161
hit rate = 0.9743589743589743
accuracy = 0.3333333333333333

hit rate = 0.9722222222222222
accuracy = 0.3125
hit rate = 0.9444444444444444
accuracy = 0.4857142857142857

hit rate = 1.0
accuracy = 0.5454545454545454
hit rate = 1.0
accuracy = 0.8571428571428571
"""


def Graph(Nodes):
    x=[]
    y=[]
    for i in range(len(Nodes)):
        if Nodes[i][0][0]=='G':

            plt.plot(Nodes[i][0][1],Nodes[i][0][2],'o',markersize=4 ,color='b')

        if Nodes[i][0][0]=='M':
            plt.plot(Nodes[i][0][1],Nodes[i][0][3],'o',markersize=4 ,color='r')

    plt.show()

plt.ylim(0,1)
x=[1,2,3,4,5]
plt.plot(x,[0.23333333333333334,0.2692307692307692,0.22674418604651161,0.3125,0.5454545454545454],linewidth=2,linestyle=':',label='Jay income', marker='o')
plt.plot(x,[0.3064516129032258,0.34545454545454546,0.3333333333333333,0.4857142857142857,0.8571428571428571],linewidth=2,linestyle=':',label='Jay income', marker='+')
plt.show()