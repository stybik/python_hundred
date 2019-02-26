
test_list = [12,24,35,24,88,120,155,88,120,155] 
print ("The original list is : " +  str(test_list)) 
   
test_list = list(set(test_list)) 
  
print ("The list after removing duplicates : " + str(test_list)) 