#lecture 6
#Bisection search - square root for all x values

x = 0.5
epsilon = 0.01
if x >= 1:
low = 1.0
high = x
else:
low = x
high = 1.0
guess = (high + low)/2
while abs(guess**2 - x) >= epsilon:
if guess**2 < x:
low = guess
else:
high = guess
guess = (high + low)/2.0
print(f'{str(guess)} is close to square root of {str(x)}')


#The optimised program 

x = 0.5
epsilon = 0.01
n = 0
if x>= 1:
    low = 1
    high = x
else:
    low = x
    high = 1
guess = (low+high)/2
while abs(guess**2-x)>=epsilon :
    if guess**2<x:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2
    n += 1
print(f"No.of guesses: {n}")
print(f"square root of {x} is close to {guess}")

#write code to do Bisection search to find cube root of a positive cubes

cube = 27
epsilon = 0.01
n=0
if cube>=1:
    low = 1
    high = cube
else:
    high = 1
    low = cube
guess = (high + low)/2
while abs(guess**3- cube) > epsilon:
    if guess**3>cube:
        high = guess
    else:
        low = guess
    n+= 1
    guess = (high + low) / 2
print(f"No.of guesses: {n}")
print(f"cube root of {cube} is close to {guess}")

#newton-raphson root finder 

epsilon = 0.01
k = 24.0
guess = k/2.0
num_guesses = 0

while abs(guess*guess -k)>=epsilon:
    num_guesses +=1
    guess -= (guess**2-k)/(2*guess)
print("num_guesses = "+str(num_guesses))
print("square root of " + str(k) + 'is about' + str(guess))
