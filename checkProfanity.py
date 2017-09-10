import urllib

# define function to read file to be checked
def readFile():
    # open function is used to access files
    quotes = open('C:\Users\pushk\Desktop\pb\Data Science\Udacity\Intro to Python\movie_quotes.txt')
    content = quotes.read() # read file into the content variable
    #print content
    quotes.close() # good habit to close all open files
    checkCurses(content) # call function to check curses 

def checkCurses(text2check):
    # open the web address which has a program to check curses
    # and store the response in connection
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text2check)
    output = connection.read()
    #print("\n"+output)
    connection.close()
    
    # if else loop to improve readability
    
    if "false" in output :
        print "No curse words in the doc"
        
    elif "true" in output: 
        print "Profanity alert, please correct your doc"
    
    else: 
        print "Unable to scan correctly"
readFile() #call function to check profanity