def summarize_chars(str):
     upper_count, lower_count, number_count, special_count = 0, 0, 0, 0
     for i in range(len(str)):
          if str[i] >= 'A' and str[i] <= 'Z': upper_count += 1
          elif str[i] >= 'a' and str[i] <= 'z': lower_count += 1
          elif str[i] >= '0' and str[i] <= '9': number_count += 1
          else: special_count += 1
     return upper_count, lower_count, number_count, special_count

if __name__ == '__main__':
    file_data = open("inputFile.txt", "r")
    input_string = file_data.read()
    print("File data:\n",input_string)
    print("\nSummary of file data:")
    upper, lower, number, special = summarize_chars(input_string)
    print('\nUpper case characters: ',upper)
    print('Lower case characters: ',lower)
    print('Number case: ',number)
    print('Special case characters: ',special)
