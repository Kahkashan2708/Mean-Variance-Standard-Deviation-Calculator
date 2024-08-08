import numpy as np
i = input("Enter elements of the list separated by space: ")  
  
lst = i.split()  
lst = [int(num) for num in lst]  
if len(lst)<9:
    print("List must contain nine elements")
else:
    print("List:", lst)

def Calculator():    
    arr=np.array(lst)
    arr1=np.reshape(arr,(3,3))

    a1=np.mean(arr1,axis=0)
    a2=np.mean(arr1,axis=1)
    a3=np.mean(arr)

    b1=np.var(arr1,axis=0)
    b2=np.var(arr1,axis=1)
    b3=np.var(arr)

    c1=np.std(arr1,axis=0)
    c2=np.std(arr1,axis=1)
    c3=np.std(arr)

    d1=np.min(arr1,axis=0)
    d2=np.min(arr1,axis=1)
    d3=np.min(arr)

    e1=np.max(arr1,axis=0)
    e2=np.max(arr1,axis=1)
    e3=np.max(arr)

    f1=np.sum(arr1,axis=0)
    f2=np.sum(arr1,axis=1)
    f3=np.sum(arr)
    
    a1=a1.tolist()
    a2=a2.tolist()
    a3=a3.tolist()
    
    b1=b1.tolist()
    b2=b2.tolist()
    b3=b3.tolist()
    
    c1=c1.tolist()
    c2=c2.tolist()
    c3=c3.tolist()
    
    d1=d1.tolist()
    d2=d2.tolist()
    d3=d3.tolist()
    
    e1=e1.tolist()
    e2=e2.tolist()
    e3=e3.tolist()
    
    f1=f1.tolist()
    f2=f2.tolist()
    f3=f3.tolist()
    


    dect={'Mean': [a1,a2,a3] ,'Variance': [b1,b2,b3] ,'Standard Deviation': [c1,c2,c3] ,'Min': [d1,d2,d3] ,'Max': [e1,e2,e3] ,'Sum': [f1,f2,f3] }
    print(dect)
Calculator()