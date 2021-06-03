alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def Caesar (start_text, shift_amount, chiper_direction) :
  end_text = ""
  if direction == 'decode':
    shift_amount *= -1 
  for letter in start_text:
    position = alphabet.index(letter)
    print(position)
    new_position = position + shift_amount
    print(new_position)
    end_text += alphabet[new_position]
    print(end_text)
  print(f' The {direction} text is {end_text}')
    
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

Caesar(start_text = text, shift_amount = shift, chiper_direction = direction)