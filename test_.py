import random

def recommend(data,weight):
    weight_ = weight/4
    a,b,c,d,e = 0.2,0.2,0.2,0.2,0.2
    r = random.random()  
    if r < a:  
        return ""
    elif r < a+b:  
        print("第二个参数被选中")  
    elif r < a+b+c:  
        print("第三个参数被选中")  
    elif r < a+b+c+d:  
        print("第四个参数被选中")  
    else:  
        print("第五个参数被选中")