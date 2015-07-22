import json

def processData():

    ped = {"name":"Tota Ram", "children": [],"gender":"M"}
    with open('ped.csv') as f:
        for line in f.readlines():
            lineData = line.strip().split(',')
            currPosn = 2
            curr = int(lineData[currPosn])
            parentNode = ped
            prev = curr
            flag = 1
            while curr != 0:
                if flag == 1:
                    currPosn += 1
                    curr = int(lineData[currPosn])
                    flag = 0
                    continue
               
                
                reqGenderCounter = 0
                childCounter = 0
                reqChild = 0
                while childCounter < len(parentNode['children']):
                    if parentNode['children'][childCounter]['gender']== ('M' if lineData[0]=='MP' else 'F'):
                        reqGenderCounter += 1
                        
                    if reqGenderCounter == prev:
                        reqChild = childCounter
                        break
                    childCounter += 1

                parentNode = parentNode['children'][reqChild]
                prev = curr
                currPosn += 1
                curr = int(lineData[currPosn])

            parentNode['children'].append({"name":lineData[11],"children":[], "gender":lineData[1]})

    with open('newdata.json','w+') as out:
        print >>out, json.dumps(ped)

if __name__=="__main__":
    processData()
