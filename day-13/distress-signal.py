def parse_line(line: str) -> list:  
    packet = []
    current_list = packet
    parents = []
    nesting = 1
    int_str = ""

    for i in range(1, len(line)):
      char = line[i]

      if char == "[":
        nesting += 1
        nested_list = []
        parents.append(current_list)
        current_list = nested_list

      elif char == ',':
        if int_str != "":
            current_list.append(int(int_str))
            int_str = ""

      elif char == "]":
        nesting -= 1
        if int_str != "":
            current_list.append(int(int_str))
            int_str = ""
        if len(parents) > 0:
          parents[-1].append(current_list)
          current_list = parents[-1]
          parents.pop()

      else:
        if char == "T":
          char = "10"
        int_str += char
    
    return packet

def parse_input(input: str) -> list:
  file = open(input)
  input_text = list(file)
  file.close()  
  packets = []

  for line in input_text:
    line = line.replace("\n", "")
    line = line.replace("10", "T") #Make tens easier to parse
    if line == "":
      continue
    
    packet = parse_line(line)
    packets.append(packet)
  
  return packets
  
def count_packets_in_right_order(packets: list) -> int:

  right_packet_index_sum = 0

  for i in range(0, len(packets), 2):
    left = packets[i]
    right = packets[i + 1]        
    result = compare(left, right)
    if result:
      right_packet_index_sum += i // 2 + 1
  return right_packet_index_sum

def sort_packets_with_dividers(packets: list) -> list:

  sorted_packets = [packets[0]]
  for i in range(1, len(packets)):

    for j in range(len(sorted_packets)):

      result = compare(packets[i], sorted_packets[j])

      if result == False:
        sorted_packets.insert(j, packets[i])
        break

      if j == len(sorted_packets) - 1:
        sorted_packets.append(packets[i])

  sorted_packets.reverse()

  for packet in sorted_packets:
    print(packet)

  return sorted_packets

def add_dividers_to_packets(sorted_packets: list) -> int:
  d1 = [[2]]
  d2 = [[6]]

  d1_index = 0
  d2_index = 0
  #Start with the lower one as it would otherwise affect the index of the higher one

  for i in range(len(sorted_packets)):
    result = compare(sorted_packets[i], d1)
    if result == False:
      sorted_packets.insert(i, d1)
      d1_index = i + 1
      break
    if i == len(sorted_packets) - 1:
      sorted_packets.append(packets[i])

  for i in range(len(sorted_packets)):
    result = compare(sorted_packets[i], d2)
    if result == False:
      sorted_packets.insert(i, d2)
      d2_index = i + 1
      break
    if i == len(sorted_packets) - 1:
      sorted_packets.append(packets[i])

  return d1_index * d2_index

def compare(left: list, right: list) -> bool | None:
    for i in range(max(len(left), len(right))):
        if i == len(left):
            return True
        
        if i == len(right):
            return False

        if type(left[i]) is int and type(right[i]) is int:
            if left[i] is not right[i]:
                return left[i] < right[i]
        else:
            result = compare(left[i] if type(left[i]) is list else [left[i]], right[i] if type(right[i]) is list else [right[i]])

            if result is not None:
                return result

input = "input.txt"
packets = parse_input(input)
number = count_packets_in_right_order(packets)

print(number)

sorted_packets = sort_packets_with_dividers(packets)
decoder_key = add_dividers_to_packets(sorted_packets)
print(f"Part 2: {decoder_key}")

