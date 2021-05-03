import sys
import pandas as pd

def find_possible(line):
    """
    Function to find all Possible Kmers:

    Takes in a single line as an argument and outputs the possible kmers for each value k
    Computes this by finding the minimum of the length of the string minus k plus 1, and 4^k 

    Returns a list of all possible kmers for the given string
    """
    #initialize empty list to hold all possible kmers
    poss_k = []
    #loop through the line and find all possible kmers, append kmer to the list 
    for i in range(len(line)):
        n = (len(line) - (i+1)) + 1
        m = 4 ** (i+1)
        if(n < m):
            poss_k.append(n)
        else:
            poss_k.append(m)
    return poss_k

def find_observed(line, k):
    """
    Function to find the observed kmers for a given line with size k.

    Takes in as arguments, the line to find kmers on, and the size of k
    Returns a single integer, which is the number of kmers observed
    """
    #temp_k will hold current iteration of characters, length of k
    temp_k = ""
    #will hold already found kmers so not double counting
    obs_k = []
    #the number of kmers observed, returned at the end 
    count = 0
    #a copy of the line, will be deleting from it and dont want to delete the original line
    tracker = list(line)
    for i in range(len(line)):
        temp_k = ""
        #make sure wont go out of range
        if(i + k <= len(line)):
            #get new kmer and check if a new unique one or not
            for j in range(k):
                temp_k += tracker[j]
            if(temp_k not in obs_k):
                obs_k.append(temp_k)
                count += 1
        del(tracker[0])
    return count

def comp_complexity(obs, poss_k):
    """
    Function to compute the linguistic complexity 

    Takes in as arguments a list of observed kmers and list of possible kmers 
    Divides the sum of observed kmers by possible kmers and returns this number
    """
    top = 0
    bot = 0
    #add together all observed kmers
    for i in range(len(obs)):
        top += obs[i]
    
    #add together all possible kmers
    for i in range(len(poss_k)):
        bot += poss_k[i]

    return (top/bot)

def create_df(obs, poss_k):
    """
    Function to create a pandas dataframe containing, all possible ks, all observed kmers, and all possible kmers
    
    Takes in as arguments, a list of all possible kmers and all observed kmers
    Creates a new list of all possible k and then converts the three lists into a pandas dataframe before returning it
    """
    #create a list of all possible k
    ks = []
    for i in range(len(obs)):
        ks.append(i+1)
    #convert to a pandas dataframe
    dict = {'k': ks, 'Observed kmers': obs, 'Possible kmers': poss_k}
    df = pd.DataFrame(dict)

    return df

def main():
    """
    The main function of our program
    Will read in a file from the command line, and split it by each line 
    
    It will loop through each line and call all of the functions on them
    Prints a dataframe to a different file for each line contained within the file
    Will print to the command line the linguistic complexity of each line
    """

    #open file and split file
    filename = sys.argv[1]
    datas = []
    with open(filename, 'r') as f:
        text = f.read()
        text = text.split()
    j = 0
    #loop through every line, get possible kmers for the line
    for line in text:
        j += 1
        obs = []
        poss_k = find_possible(line)
        #loop through the line to get observed kmers of every possible k
        for i in range(len(line)):
            i += 1
            num = find_observed(line, i)
            obs.append(num)
        #create dataframe and append to list of dataframes
        df = create_df(obs, poss_k)
        datas.append(df)
        #loop through list of dataframes, and print each one to a different file
        for i in range(len(datas)):
            letter = str(i)
            filename = ("Output_" + letter + ".txt")
            with open(filename, 'w') as f:
                print(datas[i], file=f)
        #compute linguistic complexity and print it to the command line
        comp = comp_complexity(obs, poss_k)
        print("Linguistic Complexity of Line", j, "is:", comp)

if __name__=="__main__":
    main()
