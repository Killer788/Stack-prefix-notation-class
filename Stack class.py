#THIS CODE IS WRITTEN BY Killer788
#I HOPE IT HELPS YOU WHEN YOU NEED IT

class Stack:
    def __init__(self):
        #define a list of operands
        self.operands=["^","*","/","+","-"]

    def prefix(self,lstf):
        x=""
        o_priority={}
        #prioritize operands
        for i in range(len(self.operands)):
            for j in range(len(lstf)):
                if lstf[j]==self.operands[i]:
                    o_priority[j]=lstf[j]
        print(o_priority)
        #replace the used variables in lstf with x(result) and return the final result
        consumed=[]
        for k,v in o_priority.items():
            x=lstf[k]+lstf[k-1]+lstf[k+1]
            consumed.append(k)
            consumed.append(k-1)
            consumed.append(k+1)
            for item in consumed:
                lstf[item]=x
            print(lstf)
        return x

    def parentheses_deleter(self,lst):
        while True:
            parentheses = {}
            p_priority = {}
            #create a list of parentheses
            for i in range(len(lst)):
                if lst[i]=="(" or lst[i]==")":
                    parentheses[i]=lst[i]
            print(parentheses)
            #if there are no paretheses left in the problem then there is no need to continue this function
            if len(parentheses)==0:
                break
            #choose priority of parentheses,the inner parentheses have higher priorities
            p=0
            for k,v in parentheses.items():
                if v!=")" and k>=p:
                    p_priority.clear()
                    p_priority[k]=v
                    p=k
                    open=k
                else:
                    p_priority[k]=v
                    close=k
                    break
            print(p_priority)
            #create a smaller list containing the inside of parentheses which gets cleared after each round of for
            inside=[]
            counter=0
            for i in range(open,close+1):
                if lst[i]!="(" or lst[i]!=")":
                    inside.append(lst[i])
                lst[i]="null"
                counter+=i
            print(lst)
            #we need to know the index of the center variant of the parentheses we are calculating so we can put change it to the result and delete nulls
            avg=int(counter/len(inside))
            #send the inside of the parentheses to be changed into prefix notation
            result=(self.prefix(inside))
            #replace the middle of parentheses whith the result
            lst[avg]=result

            lst2=[]
            for item in lst:
                if item!="null":
                    lst2.append(item)
            lst=lst2.copy()
            print(lst2,"\n","--------------------------------------------------------------------")


        #print the final result
        print("--------------------------------------------------------------------","\n","--------------------------------------------------------------------")
        result=self.prefix(lst)
        print("--------------------------------------------------------------------","\n",result)
        return result

    def Stack_Calc(self,lsts):
        stack=[]
        #create index of the top of the stack
        top=-1

        for item in lsts:
            if item in self.operands:
                stack.append(item)
                top+=1

            else:
                if stack[top] not in self.operands:
                    stack[top - 1] = "(" + stack[top] + stack[top - 1] + item + ")"
                    stack.pop()
                    top -= 1
                    if (stack[top - 1] not in self.operands) and top-2>-1:
                        stack[top - 2] = "(" + stack[top-1] + stack[top - 2] + stack[top] + ")"
                        stack.pop()
                        stack.pop()
                        top -= 2

                else:
                    stack.append(item)
                    top+=1

        stack=list(stack[0])
        stack.pop()
        stack.pop(0)
        cnt=""
        for item in stack:
            cnt+=item
        print(cnt)


#get input and turn it into a list
q=input("Please enter your problem using variants: ")
lst1=list(q)
print(lst1,"\n","--------------------------------------------------------------------")
stack1=Stack()
fresult=stack1.parentheses_deleter(lst1)

#create a list of prefix notation
lst3=list(fresult)
print(lst3,"\n","--------------------------------------------------------------------")

stack1.Stack_Calc(lst3)

print("Good Luck :)")
