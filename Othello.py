import os
import time
import sys,getopt
import operator
import copy
import numpy

##################################################
#Alpha Beta Pruning
##################################################


def minimax_alpha_beta(initialStates,depth,maxPlayer):
    v=-9999999999
    value=[]
    finalvalue=[]
    alpha=-9999999999
    beta=9999999999
    filewrite.write("root"+","+str(0)+","+"-Infinity,"+"-Infinity,"+"Infinity"+"\n")
    actions,alphabetlist=action(initialStates,maxPlayer)

    for a,alphabet in zip(actions,alphabetlist):

        temp,state= (min_value_alpha_beta(a,1,minPlayer,alphabet,alpha,beta))
        v=max(v,temp)
        alpha=max(alpha,v)
        tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
        filewrite.write("root"+","+str('0')+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
        value.append(temp)
        finalvalue.append(state)

    nextState=finalvalue[numpy.argmax(value)]
    if(taskNumber!=4):
        nextWrite=open('next_state.txt','w+')
        for i in range(0,5):
            for j in range(0,5):
                nextWrite.write(nextState[i][j])
            nextWrite.write("\n")
    else:
        nextWrite=open(os.devnull,'w+')
    return nextState

#Min Value inside Alphabeta

def min_value_alpha_beta(initialStates,depth,minPlayer,node,alpha,beta):

    #raw_input()
    v=9999999999
    if (cutoff(depth)):

        evalval= evaluate(initialStates)
        tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,evalval)
        filewrite.write(node+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
        return evalval,initialStates
    if(gameend(initialStates)):
        evalval= evaluate(initialStates)
        tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,evalval)
        filewrite.write(node+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
        return evalval,initialStates

    actions,alphabetlist=action(initialStates,minPlayer)
    state=actions[0]
    for a,alphabet in zip(actions,alphabetlist):
        tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
        filewrite.write(node+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
        value1,state1=max_value_alpha_beta(a,depth+1,maxPlayer,alphabet,alpha,beta)
        if(value1<v and depth==1):
            state=initialStates

        v=min(v,value1)
        if(v<=alpha):
            tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
            filewrite.write(node+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
            return v,state
        beta=min(beta,v)


    tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
    filewrite.write(node+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
    return v,state

#Max value inside Alpha Beta
def max_value_alpha_beta(initialStates,depth,maxPlayer,node,alpha,beta):
    
    v=-9999999999
    if (cutoff(depth) ):
        evalval= evaluate(initialStates)
        tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,evalval)
        filewrite.write(node+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
        return evalval,initialStates

    if(gameend(initialStates)):

        evalval= evaluate(initialStates)
        tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,evalval)
        filewrite.write(node+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
        return evalval,initialStates


    actions,alphabetlist=action(initialStates,maxPlayer)
    state=actions[0]
    for a,alphabet in zip(actions,alphabetlist):


        tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
        filewrite.write(node+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")

        value1,state1=min_value_alpha_beta(a,depth+1,minPlayer,alphabet,alpha,beta)
        if value1>v and depth==1:
            state=initialStates



        v=max(v,value1)
        if(v>=beta):
            tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
            filewrite.write(node+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
            return v,state
        alpha=max(alpha,v)

    tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
    filewrite.write(node+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
    return v,state

#End of AlphaBeta

######################################
#MiniMax Algorithm
######################################

def minimax(initialStates,depth,maxPlayer):
    v=-9999999999
    value=[]
    finalvalue=[]

    filewrite.write("root"+","+str(0)+","+"-Infinity"+"\n")
    actions,alphabetlist=action(initialStates,maxPlayer)

    for a,alphabet in zip(actions,alphabetlist):

        temp,state= (min_value(a,1,minPlayer,alphabet))
        v=max(v,temp)
        tempv=gettempvalues(v)
        filewrite.write("root"+","+str('0')+","+str(tempv)+"\n")
        value.append(temp)
        finalvalue.append(state)

    #print "next state",finalvalue[numpy.argmax(value)]
    nextState=finalvalue[numpy.argmax(value)]
    if(taskNumber!=4):
        nextWrite=open('next_state.txt','w+')
        for i in range(0,5):
            for j in range(0,5):
                nextWrite.write(nextState[i][j])
            nextWrite.write("\n")
    else:
        nextWrite=open(os.devnull,'w+')
    return nextState

#Min Value inside minimax
def min_value(initialStates,depth,minPlayer,node):
    #print "min function"
    #print "depth",depth
    #print "player",minPlayer
    #print "action considered ",initialStates
    #raw_input()
    v=9999999999
    if (cutoff(depth)):

        evalval= evaluate(initialStates)
        tempv=gettempvalues(evalval)
        filewrite.write(node+","+str(depth)+","+str(tempv)+"\n")
        return evalval,initialStates
    if(gameend(initialStates)):
        evalval= evaluate(initialStates)
        tempv=gettempvalues(evalval)
        filewrite.write(node+","+str(depth)+","+str(tempv)+"\n")
        return evalval,initialStates

    actions,alphabetlist=action(initialStates,minPlayer)
    state=actions[0]
    for a,alphabet in zip(actions,alphabetlist):
        tempv=gettempvalues(v)
        filewrite.write(node+","+str(depth)+","+str(tempv)+"\n")
        value1,state1=max_value(a,depth+1,maxPlayer,alphabet)
        if(value1<v and depth==1):
            state=initialStates
        v=min(v,value1)

    tempv=gettempvalues(v)
    filewrite.write(node+","+str(depth)+","+str(tempv)+"\n")
    return v,state

#Max Value inside minimax
def max_value(initialStates,depth,maxPlayer,node):
    #print "max function"
    #print "player",maxPlayer
    #print "action considered ",initialStates
    #print "depth",depth
    #raw_input()
    v=-9999999999
    if (cutoff(depth) ):
        evalval= evaluate(initialStates)
        tempv=gettempvalues(evalval)
        filewrite.write(node+","+str(depth)+","+str(tempv)+"\n")

        return evalval,initialStates

    if(gameend(initialStates)):

        evalval= evaluate(initialStates)
        tempv=gettempvalues(evalval)
        filewrite.write(node+","+str(depth)+","+str(tempv)+"\n")
        return evalval,initialStates

    actions,alphabetlist=action(initialStates,maxPlayer)
    state=actions[0]
    for a,alphabet in zip(actions,alphabetlist):
        tempv=gettempvalues(v)
        filewrite.write(node+","+str(depth)+","+str(tempv)+"\n")
        value1,state1=min_value(a,depth+1,minPlayer,alphabet)
        if value1>v and depth==1:
            state=initialStates
        v=max(v,value1)
    tempv=gettempvalues(v)
    filewrite.write(node+","+str(depth)+","+str(tempv)+"\n")
    return v,state
# End of Minimax


###############################################
# Greedy Best First Search
###############################################

def greedy(initialStates,depth,maxPlayer):
    v=-9999999999
    value=[]
    finalvalue=[]

    actions,alphabetlist=action(initialStates,maxPlayer)

    for a,alphabet in zip(actions,alphabetlist):
        #print "minimax"


        temp,state= (min_value_greedy(a,1,minPlayer,alphabet))
        v=max(v,temp)

        value.append(temp)
        finalvalue.append(state)

    #print "next state",finalvalue[numpy.argmax(value)]
    nextState=finalvalue[numpy.argmax(value)]
    if(taskNumber!=4):
        nextWrite=open('next_state.txt','w+')
        for i in range(0,5):
            for j in range(0,5):
                nextWrite.write(nextState[i][j])
            nextWrite.write("\n")
    else:
        nextWrite=open(os.devnull,'w+')
    #print nextState
    return nextState

#Min Value inside minimax
def min_value_greedy(initialStates,depth,minPlayer,node):
    #print "min function"
    #print "depth",depth
    #print "player",minPlayer
    #print "action considered ",initialStates
    #raw_input()
    v=9999999999
    if (cutoff(depth)):

        evalval= evaluate(initialStates)

        return evalval,initialStates
    if(gameend(initialStates)):
        evalval= evaluate(initialStates)

        return evalval,initialStates

    actions,alphabetlist=action(initialStates,minPlayer)
    state=actions[0]
    for a,alphabet in zip(actions,alphabetlist):
        filewrite.write(node+","+str(depth)+","+str(v)+"\n")
        value1,state1=max_value_greedy(a,depth+1,maxPlayer,alphabet)
        if(value1<v and depth==1):
            state=initialStates
        v=min(v,value1)

    return v,state

#Max Value inside minimax
def max_value_greedy(initialStates,depth,maxPlayer,node):
    #print "max function"
    #print "player",maxPlayer
    #print "action considered ",initialStates
    #print "depth",depth
    #raw_input()
    v=-9999999999
    if (cutoff(depth) ):
        evalval= evaluate(initialStates)

        return evalval,initialStates

    if(gameend(initialStates)):

        evalval= evaluate(initialStates)

        return evalval,initialStates

    actions,alphabetlist=action(initialStates,maxPlayer)
    state=actions[0]
    for a,alphabet in zip(actions,alphabetlist):

        value1,state1=min_value(a,depth+1,minPlayer,alphabet)
        if value1>v and depth==1:
            state=initialStates
        v=max(v,value1)

    return v,state

##########End of Greedy########


#Construction of Search Tree

def action(initialStates,playeri):
    #print "inside action"
    #print "playeri ",playeri
    actions=[]
    states=[]
    alphabetlist=[]
    temp1=list(initialStates)
    if(playeri=='X'):
        for i in range(0,5):
            for j in range(0,5):

                temp = copy.deepcopy(temp1)
                #print "temp outside if",temp
                #print "initial state",initialStates
                if(temp[i][j]=='*'):
                    temp[i][j]='X'


                    if(((i!=0 and temp[i-1][j]=='X') or (i!=4 and temp[i+1][j] =='X') or (j!=0 and temp[i][j-1]=='X')) and (j!=4 and temp[i][j+1]=='O') ):
                        #print "raid"
                        temp[i][j+1]='X'
                    if( ((i!=0 and temp[i-1][j]=='X') or (j!=4 and temp[i][j+1] =='X') or ( j!=0 and temp[i][j-1]=='X'))  and (i !=4 and temp[i+1][j]=='O')):
                        #print "raid"
                        temp[i+1][j]='X'
                    if(((j!=4 and temp[i][j+1]=='X') or (i!=4 and temp[i+1][j] =='X') or (j!=0 and temp[i][j-1]=='X' )) and (i!=0 and temp[i-1][j]=='O')):
                        #print "raid"
                        temp[i-1][j]='X'
                    if(((i!=0 and temp[i-1][j]=='X') or (i!=4 and temp[i+1][j] =='X') or (j!=4 and temp[i][j+1]=='X')) and (j!=0 and temp[i][j-1]=='O')):
                        #print "raid"
                        temp[i][j-1]='X'
                    tempj=i+1
                    if(j==0):
                        stri=str('A')+str(tempj)
                    elif(j==1):
                        stri=str('B')+str(tempj)
                    elif(j==2):
                        stri=str('C')+str(tempj)
                    elif(j==3):
                        stri=str('D')+str(tempj)
                    else:
                        stri=str('E')+str(tempj)
                    alphabetlist.append(stri)
                        #print "temp",temp
                    actions.append(temp)
                    #print actions
                        #print "actions",actions
    if(playeri=='O'):
        for i in range(0,5):
            for j in range(0,5):

                temp = copy.deepcopy(temp1)
                #print "temp outside if",temp
                #print "initial state",initialStates
                if(temp[i][j]=='*'):
                    temp[i][j]='O'

                    if(((i!=0 and temp[i-1][j]=='O') or (i!=4 and temp[i+1][j] =='O') or (j!=0 and temp[i][j-1]=='O')) and (j!=4 and temp[i][j+1]=='X') ):
                        #print "raid"
                        temp[i][j+1]='O'
                    if( ((i!=0 and temp[i-1][j]=='O') or (j!=4 and temp[i][j+1] =='O') or ( j!=0 and temp[i][j-1]=='O'))  and (i !=4 and temp[i+1][j]=='X')):
                        #print "raid"
                        temp[i+1][j]='O'
                    if(((j!=4 and temp[i][j+1]=='O') or (i!=4 and temp[i+1][j] =='O') or (j!=0 and temp[i][j-1]=='O' )) and (i!=0 and temp[i-1][j]=='X')):
                        #print "raid"
                        temp[i-1][j]='O'
                    if(((i!=0 and temp[i-1][j]=='O') or (i!=4 and temp[i+1][j] =='O') or (j!=4 and temp[i][j+1]=='O')) and (j!=0 and temp[i][j-1]=='X')):
                        #print "raid"
                        temp[i][j-1]='O'
                    tempi=i+1
                    if(j==0):
                        stri="A"+str(tempi)
                    elif(j==1):
                        stri=str('B')+str(tempi)
                    elif(j==2):
                        stri=str('C')+str(tempi)
                    elif(j==3):
                        stri=str('D')+str(tempi)
                    else:
                        stri=str('E')+str(tempi)

                    alphabetlist.append(stri)
                    #print "temp",temp
                    actions.append(temp)
    #print actions
    return actions,alphabetlist

#Evaluation of Players

def evaluate(initialStates):
    #print "inside evaluate"
    sum1=0
    sum2=0
    if maxPlayer=='X':
        for i in range(0,5):
            for j in range(0,5):
                if initialStates[i][j]=='X':
                    sum1+=int(initialValues[i][j])
                elif initialStates[i][j]=='O':
                    sum2+=int(initialValues[i][j])
    if maxPlayer=='O':
        for i in range(0,5):
            for j in range(0,5):
                if initialStates[i][j]=='O':
                    sum1+=int(initialValues[i][j])
                elif initialStates[i][j]=='X':
                    sum2+=int(initialValues[i][j])
    #print "sum1,sum2 ",sum1,sum2
    #print sum1-sum2
    return sum1-sum2

#Game End
def gameend(initialStates):
    flag=1
    for i in range(0,5):
        for j in range(0,5):
            if(initialStates[i][j]=='*'):
                flag=0
                return flag
    return flag
#Cut off Depth

def cutoff(depth):
    if depth==maindepth:
        return True
    return False

#Alpha Beta values if Infinity
def gettempvaluesalphabeta(alpha,beta,v):
    if(alpha==9999999999):
        tempalpha="Infinity"
    elif(alpha==-9999999999):
        tempalpha="-Infinity"
    else:
        tempalpha=alpha
    if(beta==9999999999):
        tempbeta="Infinity"
    elif(beta==-9999999999):
        tempbeta="-Infinity"
    else:
        tempbeta=beta
    if(v==9999999999):
        tempv="Infinity"
    elif(v==-9999999999):
        tempv="-Infinity"
    else:
        tempv=v
    return tempalpha,tempbeta,tempv

def gettempvalues(v):
    if(v==9999999999):
        tempv="Infinity"
    elif(v==-9999999999):
        tempv="-Infinity"
    else:
        tempv=v
    return tempv

##################################################
#Main Function
##################################################
f=open( "input.txt","r")
initialValues=[]
initialStates=[]
taskNumber = int(f.readline().strip())
nextState = []


if taskNumber==1:
    print "greedy"
    player=(f.readline().strip())
    depth=int(f.readline().strip())
    for i in range(0,5):
        temp=[]
        temp=f.readline().strip()
        temp=temp.split(" ")
        initialValues.append(temp)
    for i in range(0,5):
        temp=[]
        temp=f.readline().strip()
        temp=list(temp)
        initialStates.append(temp)

    maindepth=depth
    if(player=='X'):
        maxPlayer='X'
        minPlayer='O'
    else:
        maxPlayer='O'
        minPlayer='X'


    nextState=greedy(initialStates,1,maxPlayer)
    print "Completed"


elif taskNumber==2:
    print "minimax"
    player=(f.readline().strip())
    depth=int(f.readline().strip())
    for i in range(0,5):
        temp=[]
        temp=f.readline().strip()
        temp=temp.split(" ")
        initialValues.append(temp)
    for i in range(0,5):
        temp=[]
        temp=f.readline().strip()
        temp=list(temp)
        initialStates.append(temp)

    maindepth=depth
    if(player=='X'):
        maxPlayer='X'
        minPlayer='O'
    else:
        maxPlayer='O'
        minPlayer='X'
    filewrite=open('traverse_log.txt','w+')
    filewrite.write("Node,"+"Depth,"+"Value"+"\n")
    minimax(initialStates,depth,maxPlayer)
    print "Completed!"


elif taskNumber==3:
    print "alphabeta"
    player=(f.readline().strip())
    depth=int(f.readline().strip())
    for i in range(0,5):
        temp=[]
        temp=f.readline().strip()
        temp=temp.split(" ")
        initialValues.append(temp)
    for i in range(0,5):
        temp=[]
        temp=f.readline().strip()
        temp=list(temp)
        initialStates.append(temp)

    maindepth=depth
    if(player=='X'):
        maxPlayer='X'
        minPlayer='O'
    else:
        maxPlayer='O'
        minPlayer='X'
    filewrite=open('traverse_log.txt','w+')
    filewrite.write("Node,"+"Depth,"+"Value"+"Alpha,"+"Beta"+"\n")
    minimax_alpha_beta(initialStates,depth,maxPlayer)
    print "Completed!"



elif taskNumber==4:
    print "Simulation"
    player1=(f.readline().strip())
    player1Algo = int(f.readline().strip())
    player1Depth = int(f.readline().strip())
    player2=(f.readline().strip())
    player2Algo = int(f.readline().strip())
    player2Depth = int(f.readline().strip())
    for i in range(0,5):
        temp=[]
        temp=f.readline().strip()
        temp=temp.split(" ")
        initialValues.append(temp)
    for i in range(0,5):
        temp=[]
        temp=f.readline().strip()
        temp=list(temp)
        initialStates.append(temp)
    filewrite=open(os.devnull,'w+')
    nextWrite=open(os.devnull,'w+')



    nextState = copy.deepcopy(initialStates)
    nextTrace=open('trace_state.txt','w+')
    while (gameend(nextState)==0):

        if(player1Algo==1):
            minPlayer=player2
            maxPlayer=player1
            maindepth=player1Depth
            nextState = copy.deepcopy(greedy(nextState,1,maxPlayer))
            #print "while if",nextState

            for i in range(0,5):
                for j in range(0,5):
                    nextTrace.write(nextState[i][j])
                nextTrace.write("\n")

        elif(player1Algo==2):
            minPlayer=player2
            maxPlayer=player1
            maindepth=player1Depth
            nextState = copy.deepcopy(minimax(nextState,maindepth,maxPlayer))

            for i in range(0,5):
                for j in range(0,5):
                    nextTrace.write(nextState[i][j])
                nextTrace.write("\n")

        elif(player1Algo==3):
            minPlayer=player2
            maxPlayer=player1
            maindepth=player1Depth
            nextState = copy.deepcopy(minimax_alpha_beta(nextState,maindepth,maxPlayer))

            for i in range(0,5):
                for j in range(0,5):
                    nextTrace.write(nextState[i][j])
                nextTrace.write("\n")

        if(gameend(nextState)!=0):
            continue
        if(player2Algo==1):
            minPlayer=player1
            maxPlayer=player2
            maindepth=player2Depth
            nextState = copy.deepcopy(greedy(nextState,1,maxPlayer))

            for i in range(0,5):
                for j in range(0,5):
                    nextTrace.write(nextState[i][j])
                nextTrace.write("\n")

        elif(player2Algo==2):
            minPlayer=player1
            maxPlayer=player2
            maindepth=player2Depth
            nextState = copy.deepcopy(minimax(nextState,maindepth,maxPlayer))

            for i in range(0,5):
                for j in range(0,5):
                    nextTrace.write(nextState[i][j])
                nextTrace.write("\n")

        elif(player2Algo==3):
            minPlayer=player1
            maxPlayer=player2
            maindepth=player2Depth
            nextState = copy.deepcopy(minimax_alpha_beta(nextState,maindepth,maxPlayer))

            for i in range(0,5):
                for j in range(0,5):
                    nextTrace.write(nextState[i][j])
                nextTrace.write("\n")
    print "Completed!"


















