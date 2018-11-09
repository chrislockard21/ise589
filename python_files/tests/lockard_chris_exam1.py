# -*- coding: utf-8 -*-
"""
@author: bstarly

"""
#add any import modules over here below


#1.	Print the sum of the entire contents of the list without the use of the
#   for-loop. (5 points)
def findsum(numberList):
    return sum(numberList)

#2.	Write a function that accepts a word and returns back a string in its
#   reverse form. For example – If the word – ‘EXAM’ is passed to the function,
#   it must return back the string ‘MAXE”. If the word ‘Exam’ is sent, it must
#   return, the exact case back as well – ‘maxE’ (5 points)
def reversestring(word):
    return word[::-1]

#3.	Given a list, write code that computes the sum of all even numbers in the
#   list. (5 points)
def sumeven(numberList):
    return sum([number for number in numberList if number%2 == 0])

#4.	Given a list of strings, write code that performs the following:
#   a) Sorts the given list based on the length of each string in the list to create a new string;
#   b) Sorts a given sentence based on the lower case conversion of all strings
#      in the sentence to create a new sentence string. (10 points)
def sortsString(teststr):
    # Based on length of words
    sort_length = teststr.split()
    # Sorts list based on word length
    sort_length.sort(key=len)

    # Sorts based on the lowecase spelling of the word
    sort_lower = teststr.split()
    sort_lower.sort(key=str.lower)

    return (' '.join(sort_length), ' '.join(sort_lower))

#5.	Write a list comprehension code where strings that contain the alphabet ‘a’ or ‘A’
#   in the list is first changed to lowercase and then add the ‘+++’ string to
#   each filtered word in the list. The new list will contain only the words
#   that contain ‘a’ or ‘A’ in lowercase with +++ assigned to it. (10 points)
def AStr(testList):
    return [
        '{}+++'.format(word.lower()) for word in testList
        if 'a' in word.lower()
    ]

#6.	Given a list of numbers in a list, return a new list where all adjacent
#   elements have been reduced to a single element, so [1,10,10, 3, 5, 5]
#   reduces to the new list [1, 10, 3, 5] (5 points)
def reduceList(numList):
    # Loops and deletes next number if it is duplicated
    for ind, num in enumerate(numList):
        if numList[ind] == numList[ind + 1]:
            del numList[ind + 1]
    return numList

#7  Ethan is fond of playing with strings. He discovered his own kind of
#   string called Ethan’s String Test. If the string is split in the middle,
#   the two halves will have the same exact characters and appear in the same frequency.
#   If the number of characters is even, such as ‘papa’ and ‘mama’, there is an
#   exact split and each half passes the Ethan’s String Test. If the string has
#   odd number of characters such as ‘pappa’ and ‘mamma’, this also passes the
#   Ethan’s string test, since the middle character – p and m are omitted..and
#   the two halves are exactly the same. Note that strings like ‘lala’, ‘eegege’,
#   ‘pqooqp’, ‘acdca’ also pass Ethan’s String Test. Given an input string list,
#   write a python program that passes Ethan’s String Test. (20 points)
def EthanStringTest(testWList):
    from collections import Counter
    result = []
    for word in testWList:
        # Finds the splitting point of words
        div_word = int(len(word)/2)

        # Sets the first and last parts of the word based on word remainder
        first = word[:div_word].lower()
        if len(word) % 2 == 0:
            last = word[div_word:].lower()
        else:
            last = word[div_word + 1:]

        # Creates Counter objects to count the frequency of letters in the
        # strings and compare them for equality
        first_dict = Counter(first)
        last_dict = Counter(last)
        if first_dict == last_dict:
            result.append('Pass')
        else:
            result.append('Fail')
    return result

#8  Write code that computes the conversion from gallons to liters and from
#   liters to gallons. The user inputs the string: a number followed by a space
#   and then “gallons” or “liters”; the model then computes the corresponding conversion.
#   Also ensure that your program takes care of output errors to the user if
#   negative numbers or alphabetical characters are received by the program in
#   the place of numbers. (1 gallon = 3.785 liters and 1 liter = 0.264 gallons) (10 points)
def conversion(inputstr):
    # Handles errors for the input
    try:
        input_split = inputstr.split()
        if len(input_split) > 1:
            num = float(input_split[0])
        else:
            num = None
    except:
        num = None

    # Performs the conversion is the number exists and is greater than 0
    if num != None and num >= 0:
        unit = input_split[1].lower()
        if unit == 'gallons':
            new_num, new_unit = num*3.785, 'liters'
            return '{} {}'.format(new_num, new_unit)
        elif unit == 'liters':
            new_num, new_unit = num*0.264, 'gallons'
            return '{} {}'.format(new_num, new_unit)
        else:
            # Hangles errors based on input
            print('Sorry please check input')
            return None
    else:
        # Handles errors based on the input
        print('Sorry please check input')
        return None

#9.	Read the file grades.txt or grades.rtf. Write code that finds and displays
#   the 5 student IDs who received the lowest grades in the class (10 points).
def lowgrades(filename):
    import operator
    # Opens file
    # **Note** I changed the file in main() to .rtf because that was the only
    # file I could find in the zip
    with open(filename, 'r') as f:
        key_dict = {}
        lines = f.readlines()
        # Deletes header
        del lines[0]
        # Splits each line and sorts the created dictionary by the value of keys
        for line in lines:
            split_line = line.split()
            key_dict[split_line[0]] = int(split_line[1])
        dict_sorted = sorted(key_dict.items(), key=operator.itemgetter(1))
        display_list = [
            'Student ID {}: {}'.format(item[0], item[1]) for item in dict_sorted
        ]
        return display_list

#10. Read the file “FTEGroup.txt” or “FTEGroup.rtf”. Write code that provides
#    information on the following aspect (20points):
#    a) Total Members
#    b) List the names that have not provided a biosketch (Items marked ‘x’ have not provided a biosketch)
#    c) How many members joined in 2018
#    d) How many members joined between Year  2013 and Year 2015
def FTEGroupSlice(filename):
    from datetime import datetime as dt
    with open(filename, 'r') as f:
        lines = f.readlines()
        split_lines = [line.split(',') for line in lines]
        # Deletes header
        del split_lines[0]
        # Assigns counters
        total = 0
        nobio = []
        newFac = 0
        twoYear = 0
        for line in split_lines:
            if line[1].lower() == 'x':
                nobio.append(line[0])
            # Converts time to datetime object
            time = dt.strptime(line[2], '%m/%d/%Y')
            if time.year == 2018:
                newFac += 1
            # Compares dates
            if time >= dt(2013, 1, 1, 0, 0) and time <= dt(2015, 12, 31, 23, 0):
                twoYear += 1
            if (line[4].startswith('FTE')
                or line[5].startswith('FTE')
                or line[6].startswith('FTE')):
                total += 1
    return total, nobio, newFac, twoYear

#11. Find the max points and the name of the person with the maximum points from the given dictionary
def findmaxdict(points):
    # Returns the key with the maximum value and then calls that keys value
    # from the dictionary
    return max(points, key=points.get), points[max(points, key=points.get)]

#DO NOT ALTER CODE BELOW Except for Adding Name Below. SIMPLY EXECUTE CODE TO CHECK RESULTS
def main():
    numList=[10,10,21,32,32,44,51,60,71,71,83,91,2,1,0,12,34,56,32,77,22,21,21]
    teststr="This is a Test String provided for Exam One by Avi Adam"
    testAnimList=["lion", "Tiger", "Bear", "Gorilla", "ANTS", "AARDVARK", "Scorpion", "Blue Whale"]
    choice=0

    while choice!=12:
        print("\n************ FIRST EXAM CHRISTOPHER LOCKARD**************")
        print("1 : Find Sum")
        print("2 : Reverse String")
        print("3 : Find Sum of Even Numbers")
        print("4 : Sorts the String")
        print("5 : Find A or a")
        print("6 : Reduce List")
        print("7 : Ethan's String Test")
        print("8 : Convert Volume from G to L or L to G")
        print("9 : 5 Low Grade List")
        print("10: FTE Group Data")
        print("11: EXIT")

        choice=int(input("Enter Choice: "))

        if (choice==1):
            sum=findsum(numList)
            print ("The Sum of the number list is :",sum)
        elif (choice==2):
            word=input("Enter the word:")
            reversed = reversestring(word)
            print("The reversed word string is: ", reversed)

        elif (choice==3):
            sum = sumeven(numList)
            print("The sum of the even numbers are:", sum)

        elif (choice==4):
            sortStrLen, sortStrLower = sortsString(teststr)
            print("The Sort String on Length:", sortStrLen)
            print("The Sort String on Lowercase:", sortStrLower)

        elif (choice==5):
            newStr=AStr(testAnimList)
            print("The new modified string is ", newStr)

        elif (choice==6):
            newList=reduceList(numList)
            print("The new modified list is ", newList)

        elif (choice==7):
            testWList=['papa', 'paapaaa', 'Mama', 'eefffe','danda', 'paattaa', 'lala', 'eefefe', 'abdba', 'RoaaoR','Ululu','Ratatat']
            answerList=EthanStringTest(testWList)
            print("Pass or Fail List : ", answerList)

        elif (choice==8):
            inputstr=input("Enter the volume to convert:")
            convertstr=conversion(inputstr)
            print("The converted volume is", convertstr)

        elif (choice==9):
            gradeList=lowgrades("grades.rtf")
            print("The 5 lowest grades are", gradeList[:5])

        elif (choice==10):
            total, nobio, newFac, twoYear = FTEGroupSlice("NCSUFTEGroup.csv")
            print('Total members in FTE group are:', total)
            print('Total without a Biosketch:', nobio)
            print('Total Faculty joined in in 2018:', newFac)
            print('Total Faculty between 2013 and 2015:', twoYear)

        elif (choice==11):
            points= {'John': 51, 'Binil': 52, 'Sally': 12, 'Ethan': 43, 'Starly':99}
            maxVal=findmaxdict(points)
            print(f"The max points was won by {maxVal[0]} with {maxVal[1]}")

        elif (choice==12):
            print("Good Bye! Thanks for coding!")

if __name__ == main():
    main()
