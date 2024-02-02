# Define the list of numbers
dupnums = [1,5,2,9,4,3,100,6,56,89,12,5000]

# Define the selection sort function
def selection_sort(list):
  # Loop through the entire list
  for i in range(len(list)):
    # Find the index of the smallest element in the unsorted part of the list
    min_index = i
    for j in range(i + 1, len(list)):
      if list[j] < list[min_index]:
        min_index = j
    # Swap the smallest element with the first element in the unsorted part of the list
    # Break this line into two lines using a temporary variable
    temp = list[i]
    list[i] = list[min_index]
    list[min_index] = temp
  # Return the sorted list
  return list

# Call the selection sort function and print the result
print(selection_sort(dupnums))
