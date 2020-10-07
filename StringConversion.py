import time


def StringToInt ():
    """
    This program prompts the user for a string and converts
    it to a integer if applicable. 
    """

    string = input('Desired Number:')
    print('The current state:\nString:',string,' ->', type(string))

    if string == '': #handle no input
        raise Exception ('Invalid input!') #throws exception
    elif '-' in string: #handle non-positive inputs
        raise Exception('No negative numbers') # throws exception
    else:
        num=0 #initialize int value of string 
        string =string[::-1] #reverse the string
        var = 1 #placeholder
        #print (isinstance(string,str)) #precaution to check if the string is a string
        
        for x in range (len(string)): # determine the number of places
            if x is 0:
                num += int(string[x])
            else:
                num += int(string[x]) * var
            
            var = var * 10 #concatenate placeholder
            
        #print (isinstance(num,int)) #precaution to check if the string is converted to is a integer
        print('\nConverting your string.....')
        time.sleep(len(string)/2)
        print('\nConverted State: \nNum:', num,'->', type(num))
StringToInt()
