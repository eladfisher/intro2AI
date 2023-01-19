#presents:Elad Fisher 213924624   ,Yehoshua Gronspect 332521103
import frontier
import stack
import state




def search(n): #DFS searching function to find the wanted state

   f = frontier.create(state.create(n))

   print(f[2]) #print the initial state

   while not frontier.is_empty(f):

       s=frontier.remove(f)

       if state.is_target(s):

           return [s,f[1],f[4]]

       ns = state.get_next(s) #check the next state

       for i in range(len (ns)): #f == next state

           frontier.insert(f, (ns[i]))



answer=search(4) #the moves needed to solve a 4x4 puzzle

print("Depth:",answer[1]) #print the amount of moves needed to solve the puzzle

print("number:",answer[2]) #print the amount of states checked

'''we runned the program for 2X2,3X3,4X4 and We see that as the
 size of the table grows the calculating time is longer, the tree
  is deeper and there are more pushes into the stack'''








