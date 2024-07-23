def encrypt(my_message, shift):
  message = ""
  for index, letter in enumerate(my_message):
      current_index = alpha.find(letter)
      new_index = (current_index + shift) % 26
      message += alpha[new_index]
  print(f"Your encrypted code is {message}")

def decrypt(my_message, shift):
  message = ""
  for index, letter in enumerate(my_message):
      current_index = alpha.find(letter)
      new_index = (current_index - shift) % 26
      message += alpha[new_index]
  print(f"Your encrypted code is {message}")

alpha = "abcdefghijklmnopqrstuvwxyz"

# Loop to repeatedly ask the user until they decide to stop
while True:
  choice = input("Encode or Decode:\n").lower()

  if choice == "encode":
      my_message = input("Type your message:\n")
      shift = int(input("Type shift number:\n"))
      encrypt(my_message, shift)

  elif choice == "decode":
      my_message = input("Type your message:\n")
      shift = int(input("Type shift number:\n"))
      decrypt(my_message, shift)

  else:
      print("Invalid choice. Please type 'encode' or 'decode'.")
      continue  # Restart the loop if the input is invalid

  ans = input("You wanna do it again? (y/n):\n").lower()
  if ans == 'n':
      break  # Exit the loop if the user inputs 'n'