import __main__



def same_input(value:list[str]) -> str:
    dict1 = dict(100)
    for i in value: 
        for y, rez in enumerate(i[::-1]):
            dict1[y] += rez
            rez > 10;
            return
 
if __name__  == __main__:
     input = ["10000001","10000002","10000003","10000004"]
     print(same_input(input))       
     
