'''
present: Elad Fisher 213924624, Yehoshua Gronspect 332521103
coclusion:
2. it take bilions of checks in order to solve the puzzle of 4X4 and many checks for 3X3
and it took more than an half hour somtimes to solve the puzzle and
this is very bad way to solve this problem

4. the problem solved a lot quicker and it doesn't took us hours to solve the 4X4
puzzle so we gues that this is more effective way to solve this problem

6. the problem solved really quick without a lot cheks. the program
less than 1000 check most of the time.
this is very good way to solve this problem and it really quicker than the previus 2
programs in question 2 and 4.

 the funcion of quetion 3:
  def hdistance(s):  # the heuristic value of s
    #the hdistance of qution 3:
    counter = 0

    for i in range(len(s[0])):
        if not  i  == s[0][i]:
            counter = counter + 1

    return counter
'''

import state_quetion_5
import frontier

def search(n): #DFS searching function to find the wanted state

   f = frontier.create(state_quetion_5.create(n))
   print(f[0])
 #  print(f[2]) #print the initial state

   while not frontier.is_empty(f):

       s=frontier.remove(f)

       if state_quetion_5.is_target(s):

           return [s,f[1],f[2]]

       ns = state_quetion_5.get_next(s) #check the next state

       for i in range(len (ns)): #f == next state
           frontier.insert(f, (ns[i]))

print(search(4))