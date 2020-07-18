#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^2)

b)O(n log n)
first line is constant
for loop is linear
while loop is logarithmic
When i take away the constants from O(1 + n + log(n)) im left with O(n log n)

c)O(n)
The function is dependent of how many bunnies there are

## Exercise II

Using Binary_search the top would be n-story and bottom would be 1. Finding the middle of the building devide top by 2 and store in variable middle. Drop an egg from the middle variable if it doesn't break move bottom to floor above the previous middle. If it does break move top variable to be -1 of previous middle floor. Repeating the process until the egg doesn't break and there you have your floor that the egg doesn't break.

O(logn)
The number of floors can increase so it's dependent on the n number of floors or n input
