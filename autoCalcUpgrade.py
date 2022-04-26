import os

dataLocation = "YOUR_RECEIPT_FOLDER"

def read_receipt(inFileName):
    with open(inFileName) as f:
        contents = f.readlines()
    
    payer = contents[0].split(":")[1].strip()
    
    results = {payer:0}
    nums = []
    people = []
    for i in range(1,len(contents)):
        temp = contents[i].strip().split()
        nums.append(float(temp[0]))
        people.append(temp[1].split(","))
    
    for i in range(len(nums)):
        for name in people[i]:
            if name not in results.keys():
                results[name] = 0
            results[name] += nums[i]/len(people[i])
    
    print("total of receipt {} = ${:.2f}".format(inFileName.split("\\")[-1], sum(results.values())))
    
    return payer, results
    
    
def read_all_receipts(folderName):
    aggregateData = []
    people = []
    for f in os.listdir(folderName):
        aggregateData.append(read_receipt(folderName + "\\" + f))
        
    results = {}
    for entry in aggregateData:
        payer = entry[0]
        if payer not in results.keys():
            if payer not in people:
                people.append(payer)
            results[payer] = {}
            
        for person in entry[1].keys():
            if person != payer:
                if person not in results[payer].keys():
                    if person not in people:
                        people.append(person)
                    results[payer][person] = entry[1][person]
                else:
                    results[payer][person] += entry[1][person]

    #print(aggregateData)
    return results, people

def display_owed(dataArray, names):
    completedNames = []
    for i in range(len(names)):
        for j in range(i+1,len(names)):
            if dataArray[i][j]-dataArray[j][i] == 0:
                continue
            elif dataArray[i][j] > dataArray[j][i]:
                print(names[j], "owes", names[i], ": ${:.2f}".format(dataArray[i][j]-dataArray[j][i]))
            else:
                print(names[i], "owes", names[j], ": ${:.2f}".format(dataArray[j][i]-dataArray[i][j]))

def convert_to_array(resultDict, nameList):
    result = list([0 for i in nameList] for j in nameList)
    for i in resultDict.keys():
        for j in resultDict[i].keys():
            result[nameList.index(i)][nameList.index(j)] = resultDict[i][j]

    return result

if __name__ == "__main__":
    receiptResults, allNames = read_all_receipts(dataLocation)
    resultArray = convert_to_array(receiptResults, allNames)
    print("----------------------------------")
    display_owed(resultArray, allNames)
