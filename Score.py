scores=[]
print("Enter 4 scores:")
for i in range(4):
    s=int(input(f"scores {i+1}: "))
    scores.append(s)
total=sum(scores)
average=total/4
print("\nscores:",scores)
print("total:",total)
print("Average:",average)
