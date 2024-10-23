import heapq
from time import time
edge_sum = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
all = {}


with open(f"hw6/Dict.txt", "r") as a_file:
    #reads the file one line at a time, and repeats following code for each line
    for line in a_file:
        #creates a variable row, and saves the data in list form, split by comma
        row = (line.strip().split(","))
        #the row is appended to the list
        all[row[0]] = []
        # print(row)

for word in all.keys():
    for i in range(len(word)):
        for letter in alphabet:
            possible_word = word[:i] + letter + word[i+1:]
            if possible_word == word:
                continue
            if possible_word in all:
                new_node = (word, possible_word, abs(ord(letter) - ord(word[i])))
                all[word].append(new_node)
                edge_sum += 1

# this is our value for infinity, the sum of all the edges + 1
edge_sum += 1




def Relax(d, p, node):
    if d[node[0]] + node[2] < d[node[1]]:
        d[node[1]] = d[node[0]] + node[2]
        p[node[1]] = node[0]


def absolute_letter_difference(word1, word2):
    # Ensure both words have the same length
    if len(word1) != len(word2):
        return "Words must have the same length"

    # Initialize total difference
    total_difference = 0

    # Loop through each character pair
    for char1, char2 in zip(word1, word2):
        # Calculate absolute difference between ASCII values
        difference = abs(ord(char1) - ord(char2))
        # Add the absolute difference to the total
        total_difference += difference

    return total_difference


def DijkstraA(start,end,dict, huer):
    if len(start) != len(end):
        return "Your entries are of unequel length."
    if start not in all:
        return f"{start} is not a valid word."
    if end not in all:
        return f"{end} is not a valid word."
    if end == start:
        return "Enter two different words."
    Q = []
    S = set()
    distances = {item: edge_sum for item in dict}
    predicessors = {item: None for item in dict}
    distances[start] = 0
    heapq.heappush(Q, (0, start))
    node_searched = 0
    while len(Q) > 0:
        u = heapq.heappop(Q)
        node_searched += 1
        S.add(u[1])
        for child in dict[u[1]]:
            before = distances[child[1]]
            Relax(distances, predicessors, child)
            after = distances[child[1]]
            if after < before:
                heapq.heappush(Q, (distances[child[1]] + (huer * absolute_letter_difference(end,child[1])), child[1]))
                # heapq.heappush(Q, (distances[child[1]], child[1]))
            

        if end in S:
            count = 1
            
            to_print = predicessors[end]
            final_printable = f"{end}"
            while to_print != start:
                final_printable = f"{to_print} -> {final_printable}"
                count += 1
                to_print = predicessors[to_print]
            final_printable = f"{start} -> {final_printable}"
            return node_searched
    return "The path does not exist."
        

 
def Dijkstra(start,end,dict):
    if len(start) != len(end):
        return "Your entries are of unequel length."
    if start not in all:
        return f"{start} is not a valid word."
    if end not in all:
        return f"{end} is not a valid word."
    if end == start:
        return "Enter two different words."
    Q = []
    S = set()
    distances = {item: edge_sum for item in dict}
    predicessors = {item: None for item in dict}
    distances[start] = 0
    heapq.heappush(Q, (0, start))
    node_searched = 0
    while len(Q) > 0:
        u = heapq.heappop(Q)
        node_searched += 1
        S.add(u[1])
        for child in dict[u[1]]:
            before = distances[child[1]]
            Relax(distances, predicessors, child)
            after = distances[child[1]]
            if after < before:
                # heapq.heappush(Q, (distances[child[1]] + absolute_letter_difference(end,child[1]), child[1]))
                heapq.heappush(Q, (distances[child[1]], child[1]))
            

        if end in S:
            count = 1
            
            to_print = predicessors[end]
            final_printable = f"{end}"
            while to_print != start:
                final_printable = f"{to_print} -> {final_printable}"
                count += 1
                to_print = predicessors[to_print]
            final_printable = f"{start} -> {final_printable}"

            return node_searched
    return "The path does not exist."
           
# new_dict = {"car": [("car", "cad", 14)], "cad":[("cad", "car", 14), ("cad", "mad", 10)], "mad":[("mad", "cad", 10)] }





# cont = True
# while cont:
#     word1 = input("Enter your your beginning word: ").strip()
#     word2 = input("Enter your your ending word: ").strip()
#     print((DijkstraA(word1,word2,all)))
#     print((Dijkstra(word1,word2,all)))
#     cont = input("Do you want to continue? y/n: ").strip()
#     if cont == "y":
#             cont = True
#     elif cont == "n":
#         cont = False
#     while cont != True and cont != False:
#         cont = input("Enter a valid answer, y/n: ").strip()
#         if cont == "y":
#             cont = True
#         elif cont == "n":
#             cont = False
    

words = [("to", "me"), ("red", "for"), ("bath", "boom"), ("earth", "blows")]

def ply_timer(function = object):
    
    for word in words:
        #the toops of each column are printed
        #n will take on these in a loop
        lowest = 100000000
        lowestN = 8008
        for n in range(150,300):
            n/=100
            #for however many trials there are...
            nodes = function(word[0], word[1], all, n)

            if nodes < lowest:
                lowest = nodes
                lowestN = n
            #the times are printed
            # print(f"{n} {nodes}")
        print(f"The lowest n for a word size {len(word)} is {lowestN}, which looked at {lowest} nodes.")

        
ply_timer(DijkstraA)