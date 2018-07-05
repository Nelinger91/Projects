def is_balanced(s):
    counterstart=0
    counterend=0
    begining=[]
    end=[]
    check=0
    for i in range(0,len(s)):
        if "("==s[i]:
            counterstart+=1
            begining.append(i)
        elif ")"==s[i]:
            counterend+=1
            end.append(i)
    if counterend!=counterstart:
        return False
    elif counterend==0:
        return True
    else:
        for j in range(0,len(begining)):
            if end[j]>begining[j]:
                check+=1
        if check==len(begining):
            return True

                
def bracket_to_dist(s,counter):
    last=len(s)-1
    for i in range(0,len(s)):
        if s[last-i]==")":
            closeB=last-i
        elif s[last-i]=="(":
            openB=last-i
            s[closeB]=openB-closeB
            s[openB]=closeB-openB
            counter-=1
            if counter==0:
                return s
            else:
                return bracket_to_dist(s,counter)

            
            


def match_brackets(s):
    slist=[]
    counter=0
    if is_balanced(s)==False:
        return -1
    for i in range(0,len(s)):
        if s[i]==")"or s[i]=="(":
            slist.append(s[i])
            counter+=1
        else:
            slist.append(0)
    return bracket_to_dist(slist,(counter/2))

s="(dsc(gf))v"
a=match_brackets(s)
print(a)
                            
            
        
