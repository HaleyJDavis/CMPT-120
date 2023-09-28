def main():
  
  #set this to any double
  doubleValue = 97.45
  
  #set this to any int
  intValue = 86
  
  #print out addition, subtraction, multiplication, and division of these two values
  print(doubleValue + intValue)
  print(doubleValue - intValue)
  print(doubleValue * intValue)
  print(doubleValue / intValue)
  
  #populate this list
  myFriends = ["Tori", "Carlie", "Emma", "Haylie"]
  
  #print out your friends at index 2 and index 3
  print(myFriends[2])
  print(myFriends[3])

  #populate this list with five numbers
  fiveNumbers = [73, 902, 64, 26, 3]
  
  #do each of the four equations with different numbers each time.
  print(fiveNumbers[0] + fiveNumbers[1])
  print(fiveNumbers[1] - fiveNumbers[2])
  print(fiveNumbers[2] * fiveNumbers[3])
  print(fiveNumbers[3] / fiveNumbers[4])

  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  print(fiveNumbers)
  fiveNumbers[4] = 603
  fiveNumbers[3] = 89
  #print out the list
  print(fiveNumbers)
  
main()
