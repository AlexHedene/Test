"""
Solutions to module 1
Student: 
Mail:
Reviewed by:
Reviewed date:
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib function.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""




import time
import math

def multiply(m: int, n: int) -> int:  
    if m == 0 or n == 0:
        return 0
    else:
        return n + multiply(m-1,n)
    

def harmonic(n: int) -> float:              
    if n == 1 or n == 0:
        return 1
    else:
        return 1/n + harmonic(n-1)

def get_binary(x: int) -> str:         
    if x < 0:
        return "-" + get_binary(-x)
    if x == 0:
        return "0"
    elif x == 1:
        return "1"
    
    return get_binary(x//2) + str(x % 2)


def reverse_string(s: str) -> str: 
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s     
    else:
        return s[-1] + reverse_string(s[:-1])
              
def largest(a: iter):                   
    if len(a) == 1:
        return a[0]
    else:
        return a[0] if a[0] > largest(a[1:]) else largest(a[1:])

def count(x, s: list) -> int:                
    """ Counts the number of occurences of x on all levels in s"""
    if type(s) == list and len(s) == 0:
        return 0
    if s == x or type(s) != list:
        return 1 if s == x else 0    
    elif len(s) > 1:
        return count(x,s[0]) + count(x,s[1:])
    else:
         return count(x, s[0])
        


def bricklek(f: str, t: str, h: str, n: int) -> str:  
    """ Returns a string of instruction ow to move the tiles """
#       Write a function def bricklek(from, to, help, n) which returns a list of in-
#       structions on how to move the tiles. The parameters from, to and help are
#       strings that identify the different piles and n is the number of tiles.
#       The call bricklek(’f’, ’t’, ’h’, 2) should return the list
#       [’f->h’, ’f->t’, ’h->t’]
#       which should be read as
#       “move from f to h, move from f to t, move from h to t”.
#       Each element in the list is thus a string that indicates from which pile and to
#       which pile tiles should be moved. Since it is always the top tile that is to be
#       moved, no other information is needed.
#       It is important that the strings look exactly as in the example and do not
#       contain any blank spaces!
#       Hint: The function does not need more than 5 lines, including the def line!
# 1: f->t
# 2: f->h, f->t, h->t
# 2: bricklek(f, h, t, n-1) + bricklek(f, t, h, 1) + bricklek(h, t, f, n-1)
# 3: f->t, f->h, t->h, f->t, h->f, h->t, f->t # Ändra plats på f,t,h 
# 3: bricklek(f, h, t, n-1) + bricklek(f, t, h, 1) + bricklek(h, t, f, n-1)
# 4: 
    if n == 0:
        return []
    if n == 1:
        return [f + "->" + t]
    else:
        return bricklek(f, h, t, n-1) + bricklek(f, t, h, 1) + bricklek(h, t, f, n-1)
    
#print(bricklek('f','t','h',3))  


def fib(n: int) -> int:                      
    """ Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    # print('\nCode that demonstates my implementations\n')

    # print('\n\nCode for analysing fib and fib_mem\n')

    # print('\nBye!')
    1


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles:
  
  
  
  
  Exercise 9: Time for Fibonacci:


  
  
  Exercise 10: Time for fib_mem:
  
  
  
  
  
  Exercise 11: Comparison sorting methods:
  
  
  
  
  
  Exercise 12: Comparison Theta(n) and Theta(n log n)
  
  
"""
