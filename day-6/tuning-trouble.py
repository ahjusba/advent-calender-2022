def list_has_duplicates(previous_data: list) -> bool:
  #Worst case complexity n(log(n)) while possibility for a much lower complexity
  set_of_previous_data = set()
  for d in previous_data:
    if d in set_of_previous_data:
      return True
    else:
      set_of_previous_data.add(d)
  return False

def find_the_first_marker(input: str) -> int:
  file = open(input)
  data_stream = file.read()
  file.close()
  marker = 14
  
  for i in range(marker - 1, len(data_stream)):
    previous_data = []
    for j in range(marker):
      data = data_stream[i-j]
      previous_data.append(data)
    if list_has_duplicates(previous_data):
      continue
    else:
      return i + 1

  return print("There was no marker in the data stream!")
  
first_marker = find_the_first_marker("input.txt")
print("First marker at position", first_marker) #PART ONE ANSWER