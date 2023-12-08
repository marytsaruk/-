def find_times(file_path, user_value):
  with open(file_path, 'r', encoding = 'utf-8') as file:
      for line in file:
          time, measurement = line.split()
          if float(measurement) > float(user_value):
              print(time)
              
user_value = input('Введіть значення: ')
find_times('file.txt', user_value)