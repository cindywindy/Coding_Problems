def arrayStringsAreEqual(word1, word2):
        
    string1 = ""
    string2 = ""
    
    #concatenate strings
    for i in word1:
        string1 += i
    for j in word2:
        string2 += j

    if string1==string2:
        return True

    return False

wordy = ["wxgdwznoledlfeoilewsjziotnncyebhwpdnnimcorzovuiig","lycfb"]

wordo = ["wxgdwznoledlfeoilewsjzio","tnncyebhwpdnnimcor","iigl","yc","f","b","hnjm"]

print(arrayStringsAreEqual(wordy,wordo))

