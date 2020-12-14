def salt_password(password):
  #For every 2 characters, insert a 'Bob'
  iterations = 0
  password_array = []

  for char in password:
    iterations += 1
    password_array.append(char)
    if iterations % 2 == 0:
      password_array.append('Bob')

  return ''.join(password_array)
