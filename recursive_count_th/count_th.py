'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    matches = 0
    if len(word) >= 2: #check if word is 2 or more characters
        if word[:2] == 'th': #check if first 2 elements == th if so + 1 match
            matches += 1
            return count_th(word[1:]) + matches #run func again without firts element in word until it hits base case less than 2
        else:
            return count_th(word[1:]) #taking first element off each time func is called again looking for a match of next 2 elements
    else:
        return matches #if len(word) at begining is less than 2 return 0 matches--- none possible

