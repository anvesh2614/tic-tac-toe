import random                                                        #LIBRARY ALREADY DEFINED IN PYTHON

b="#"                                                                #USED # TO REPRESENT EMPTY SPACE ON BOARD
column=0                                                             
row=0                                                                
row1=[b,b,b]                                                         
row2=[b,"0",b]                                                         
row3=[b,b,b]                                                         #HAS USED LIST OF LIST TO FORM ROWS AND COLUMNS
lst=[row1,row2,row3]                                                   
a=1                                                                  
p1=0                                                                 
p2=0                                                                 
p3=0                                                                 
count=0                                                                
moves_available=[[1,1],[1,2],[1,3],[2,1],[2,3],[3,1],[3,2],[3,3]]    #POSSIBLE MOVES OF THE USER AND COMPUTER IN FORMAT [ROW,COLUMN]
for i in range(20):
    
    


    
    if a==0 or a==2 or a==4 or a==6 or a==8:                         #COMPUTER RANDOM INPUT FOR 0 
        print("\n\ncomputer input")                                 
        X_O="0"
        temprow=random.randint(1,3)

        tempcolumn=random.randint(1,3)
        #print("\n","row is:",temprow,"\tcolumn is",tempcolumn)
        row=temprow
        column=tempcolumn
            
        
                
    else:                                                             #USER INPUT FOR X
        X_O="X"
        print("\n\nenter the position for x")
        temprow=int(input("enter row number"))
        tempcolumn=int(input("enter column number"))
        if temprow==2 and tempcolumn==2:
            print("already defined")
            temprow=int(input("enter row number"))
            tempcolumn=int(input("enter column number"))

        row=temprow
        column=tempcolumn
        
        
    
    

    if [row,column] in  moves_available:                              #TO CHECK WHETHER THIS MOVE IS POSSIBNLE OR NOT
        moves_available.remove([temprow,tempcolumn])                  #THIS STEP IS USED TO REMOVE THE STEPS THAT HAVE ALREADY BEEN USED
        column=column-1
    

        if row==1:
            
            row1.insert(column,X_O)                                   #INSERTION OF X OR 0 IN ROW1 
            row1.pop(column+1)
            
            
            
        elif row==2:                                                  
        
            row2.insert(column,X_O)                                   #INSERTION OF X OR 0 IN ROW2
            row2.pop(column+1)
            
            
        else:
        
            row3.insert(column,X_O)                                   #INSERTION OF X OR 0 IN ROW3
            row3.pop(column+1)
            
            
        a=a+1
        print("\n")
        print("GAMEPLAY ON BOARD")
        print(row1[0]," ",row1[1]," ",row1[2])                        # STRUCTURE OF BOARD DEFINITION
        print(row2[0]," ",row2[1]," ",row2[2])
        print(row3[0]," ",row3[1]," ",row3[2])
        for i in row1:
            if row1[0]==row1[1]==row1[2]=="X":                        #TO CHECK THE CONDITION FOR WIN
                print("x wins")
                exit(1)
        for i in row2:
            if row2[0]==row2[1]==row2[2]=="X":
                print("x wins")
                exit(1)
        for i in row1:
            if row3[0]==row3[1]==row3[2]=="X":
                print("x wins")
                exit(1)
        

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if row1[i]=="X" and row2[i]=="X" and row3[i]=="X":
                        p1=i+1
                        p2=j+1
                        p3=k+1
                        if ((p1+p2+p2)%3==0):
                            print("X WINS")
                            exit(1)
                                     
                        


        #print("\n\nMOVES AVIALABLE:")                                  #REMAINING MOVES AVAILABLE FOR THIS GAME
        #print(moves_available)
        
        
        

        if a==10:
            break
        
    #else:
                                                                       #IF THE MOVE ENTERED IS OUT OF BOUND THEN THIS STEP IS USED
        #print("\n\nERROR")
        #print("THIS MOVE IS NOT VALID IN THIS GAME\n\n")
        



                 













    
                
