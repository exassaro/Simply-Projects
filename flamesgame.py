# This is popular Flames game we used to plat to predict the relationship status


#function for removing common characters with their respective occurences
def  remov_match_char(lst1,lst2):
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            
            # if common character is found
            # then remove that character
            # and return list of concatenated
            # list with True Flag
            
            if lst1[i]==lst2[j]:
                c=lst1[i]
                
                # remove character from the list
                lst1.remove(c)
                lst2.remove(c)
                
                # concatenation of two list elements with *
                # * is act as border mark here
                lst3=lst1+["*"]+lst2
                
                # return the concatenated list with True flag
                return [lst3,True]
    
    # no common characters is found
    # return the concatenated list with False flag
    lst3=lst1+["*"]+lst2
    return [lst3,False]

if __name__=="__main__":
    p1=input("player 1 name: ")
    p1.lower()
    p1.replace(" ","")
    
    p1_list=list(p1)
    
    p2=input("Player 2 name: ")
    p2=p2.lower()
    p2.replace(" ","")
    p2_list=list(p2)
    
    proceed=True

    while proceed:
        # function calling and store return value
        ret_list=remov_match_char(p1_list,p2_list)
        
        # take out concatenated list from return list
        con_list=ret_list[0]
        
        # take out flag value from return list
        proceed=ret_list[1]
        
        # find the index of "*" / border mark
        star_index=con_list.index("*")
        
        # list slicing perform

        # all characters before * store in p1_list
        p1_list=con_list[:star_index]
        
        # all characters after * store in p2_list
        p2_list=con_list[star_index+1:]
        
    
    # count total remaining characters    
    count=len(p1_list)+len(p2_list)
    
    result=["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    
    # keep looping until only one item
    # is not remaining in the result list
    while len(result)>1:
        
        # store that index value from
        # where we have to perform slicing.
        split_index=(count%len(result)-1)
        
        # this steps is done for performing
        # anticlock-wise circular fashion counting.
        if split_index>=0:
            right=result[split_index+1:]
            left=result[:split_index]
            
            result=right+left  
            
        else:
            result=result[:len(result)-1]
            
    print("Relationship status : ",result[0]) 
    
            