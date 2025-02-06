# def is_valid_post_format(posts):

#     if not posts or len(posts) <= 1:
#         return False

#     stk = []

#     validator_dict = {")":"(", "]":"[", "}": "{"}

#     for symbols in posts:

#         if symbols in validator_dict.values():
#             stk.append(symbols)
#         elif symbols in validator_dict:
#             if stk and validator_dict[symbols] == stk[-1]:
#                 stk.pop()
#             else:
#                 return False
#         else:
#             return False
            
#     if not stk:
#         return True
#     else:
#         return False
    

# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))


# """
# Match Patterns:
#     Using a stack and queue

# 1. initialize an empty stack

# 2. loop through comments

#     3. check if comments are empty:
#         return comments array as is
#     4. check if not length of stk is == to the length of comments array
#         add the current item to the stk in the last position

# 5. Return stk
# """

# def reverse_comments_queue(comments):
#     if not comments:
#         return comments
#     new_comments = []
#     size = len(comments)
#     for comment in range(size):

#         new_comments.append(comments.pop())

#     return new_comments

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

# """
# 1. make the title var lowercase
# 2. check if the string is empty or if the first and last characters are Equal
# 3. make a left pointer and right pointer set at beginning:End
# 4. While Loop where it continues while left less than right pointer
# 5. if left pointer == a space:
#     left_pointer += 1
# 6. elif right pointer == a space:
#     right pointer -= 1
# 5. elif left pointer value == to right pointer value
#     add one to left pointer and right pointer
# 6. else:
#     return False

# 7. Return True
# """
# def is_symmetrical_title(title):
#     title = title.lower()
#     if not title or title[0] != title[-1]:
#         return False
    
#     lp = 0
#     rp = len(title) - 1

#     while lp < rp:
#         if title[lp] == " ":
#             lp += 1
#         elif title[rp] == " ":
#             rp -= 1
#         elif title[lp] == title[rp]:
#             lp += 1
#             rp -= 1
#         else:
#             return False
#     return True

# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media")) 


# def engagement_boost(engagements):
#     squared_engagements = [] # Initialize empty list for squared engagements
    
#     for i in range(len(engagements)): # iterate through engagements list
#         squared_engagement = engagements[i] * engagements[i] # making a square of each item for every iteration
#         squared_engagements.append((squared_engagement, i)) # adding the squared item to the squared_engagments list
    
#     squared_engagements.sort(reverse=True) # sorting every item in the squared_engagements list but flipping it
    
#     result = [0] * len(engagements) # making new list out of 0's that will be the same len as engagements list
#     position = len(engagements) - 1 # setting position to start at the end of the targeted list
    
#     for square, original_index in squared_engagements: # iterating for items and index in squared_engagements
#         result[position] = square # setting last item in results list to current square
#         position -= 1 # moving position back one to go the next item to the left
    
#     return result # returning the list of engagements squared

# """
# 1. what if it is 1 char or empty

# 1. stack

# stk = []
# cleansed_post = ""

# for every item and index in post:
#     elif stk not empty:
#         if not at the end of string:
#             if current item does not equal last item in stk:
#                 then add to stk
#             else:
#                 continue
#     else:
#         add item to stk

# retrun a joined string of the items in the stk
# """

# def clean_post(post):
#   if not post or len(post) <= 1:
#       return post
#   stk = []

#   for item in post:
#     if stk and stk[-1] != item and stk[-1].lower() == item.lower():
#         stk.pop()
#     else:
#         stk.append(item)
  
#   return "".join(stk)

# print(clean_post("poOost")) 
# print(clean_post("abBAcC"))
# print(clean_post("s")) 
      
                

# """
# 1. add to queue until we reach a space or end of string
# 2. when reaching a space load current queue into string from top to bottom
# 3. then continue
# """
# from collections import deque
# def edit_post(post):
  
#   queue = deque()
#   new_post = ""

#   for item in post:
      
#       if item != " ":
#           queue.appendleft(item)
#       else:
#          new_post += "".join(queue.popleft() for _ in range(len(queue))) + " "
#   new_post += "".join(queue.popleft() for _ in range(len(queue))) # catch last word

#   return new_post

# print(edit_post("Boost your engagement with these tips")) 
# print(edit_post("Check out my latest vlog")) 

"""
1. two new strings
2. when theres a hashtag we remove past items in stk
3. multiple hashtags mean remove multiple items in the stk
"""

def post_compare(draft1, draft2):
  
  stk1 = []
  stk2 = []

  for char1, char2 in zip(draft1, draft2):
     print(stk1, stk2)
     if char1 != "#":
        stk1.append(char1)
     if char2 != "#":
        stk2.append(char2)
     if char1 == "#":
        stk1.pop()
     if char2 == "#":
        stk2.pop()
  return stk1 == stk2


print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 