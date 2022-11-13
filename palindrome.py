def highestValuePalindrome(s, n, k):
    palin=list(s)
    strr1=list(s)
    lengt=n-1
    i=0
    totalchanges=k
    onetimechanges=0
    
    while(i<=lengt):

        if(strr1[i]!=strr1[lengt]):
            onetimechanges+=1
        lengt-=1
        i+=1
        
    lengt=n-1
    i=0
    if(onetimechanges<=totalchanges):
            while(totalchanges>=2 and onetimechanges<totalchanges and i<=lengt):
                if(palin[i]!=palin[lengt]):
                    palin[i]=palin[lengt]='9'
                    totalchanges-=2
                    onetimechanges-=1
                lengt-=1
                i+=1
                
            lengt=n-1
            i=0        
            while(i<=lengt and onetimechanges>0):
                if(palin[i]!=palin[lengt]):
                    palin[i]=palin[lengt]=max(palin[i],palin[lengt])
                    totalchanges-=1
                    onetimechanges-=1  
                if(i==lengt and onetimechanges>0):
                    palin[i]='9'
                    totalchanges-=1
                    onetimechanges-=1      
                lengt-=1
                i+=1

            lengt=n-1
            i=0 
            while(totalchanges>=2 and i<=lengt):
                if(palin[i]!='9'):
                    palin[i]=palin[lengt]='9'
                    totalchanges-=2
                lengt-=1
                i+=1
            
            lengt=n-1
            i=0 
            while(totalchanges>0 and i<=lengt):
                if(i==lengt):
                    if(palin[i]!='9'):
                        palin[i]='9'
                        totalchanges-=1
                lengt-=1
                i+=1





                    
            stringnew=''
            for iterate in palin:
                stringnew +=''+iterate
            return stringnew
    else:
            return "-1"
        
