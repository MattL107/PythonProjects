# primeFactorDecomposer.py

from math import floor

def primeChecker(number):
    if number == 2 or number == 3:
        return True
    rootNum = floor(number**0.5)
    prime = True
    for i in range(2, rootNum + 1):
        if number % i == 0:
            prime = False
    return prime

def firstDivisorPair(number):
    rootNum = floor(number**0.5)
    for i in range(2, rootNum + 1):
        if number % i == 0:
            return [i, int(number/i)]
    return [1, number]

def primeFactorDecomposition(num):
    fdp = firstDivisorPair(num) # first divisor pair is always a prime num, and some other num
    primeFactorList = []
    primeFactorList.append(fdp[0]) # append the prime num to the prime factor list
    while not primeChecker(fdp[1]): # when second num is not prime, repeat process until it is
        fdp = firstDivisorPair(fdp[1])
        primeFactorList.append(fdp[0])
    primeFactorList.append(fdp[1]) # finally when 2nd num is prime, we add it to list and we done
    uniquePrimeFactors = []
    factorPowers = []
    for i in range(len(primeFactorList)):
        if primeFactorList[i] not in uniquePrimeFactors:
            factorPowers.append([primeFactorList[i],primeFactorList.count(primeFactorList[i])])
            uniquePrimeFactors.append(primeFactorList[i])
    returnString = ''
    for i in range(len(factorPowers)-1):
        returnString += f'{factorPowers[i][0]}^{factorPowers[i][1]} * '
    returnString += f'{factorPowers[-1][0]}^{factorPowers[-1][1]}'
    return returnString

# The process:
# 1) Write a function which is passed a whole number and returns True if it is prime and
#    False if it is not prime
# 2) Write a function which returns the first divisor pair of a number passed to it. A list
#    of the smaller number (always prime) and the larger number (potentially not prime)
#    is returned
# 3) Find the first divisor pair of the num passed to primeFactorDecomposition(). The first
#    number in the list produced is a prime which can be added to the final list of prime
#    factors. The second number is potentially not prime. If it *is* prime, we can add it to
#    the list and we are done. If it is *not* prime, we must keep repeating this process of
#    using the firstDivisorPair() function to 'extract' a small prime number one loop cycle
#    at a time until we are left with a secondary number that *is* prime. At this point, we
#    can exit the while loop and append this number to our primes list. We are now technically
#    done, and just need to work on the formatting from here onwards.
# 4) Look through the list of primes and for each new prime that is found, append it to a new
#    list along with the number of times it appears using the .count() function. then, to stop
#    looking at this number if/when it appears again, add it to a list of uniqueFactors, and if
#    a number appears in that list, that means we have already considered it and it can be
#    skipped over.
# 5) Finally, create the string by looping through the list of [number,power] and taking
#    index0^index1 and adding these strings together via concatenation. Note, only go up to
#    final index - 1 with the for loop, so that the last number doesn't have a * appear after it










