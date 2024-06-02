print("""
  ____                             ____ _       _               
 / ___|__ _  ___  ___  ___ _ __   / ___(_)_ __ | |__   ___ _ __ 
| |   / _` |/ _ \/ __|/ _ \ '__| | |   | | '_ \| '_ \ / _ \ '__|
| |__| (_| |  __/\__ \  __/ |    | |___| | |_) | | | |  __/ |   
 \____\__,_|\___||___/\___|_|     \____|_| .__/|_| |_|\___|_|   
                                         |_|                    
      """)

def encode():
    message = input("Type your message: ")
    shift_value = int(input("Enter the shift key: "))
    shift_char = []
    for i in message:
        charTOaskii = ord(i)
        askiiTochar = chr(charTOaskii + shift_value)
        shift_char.append(askiiTochar)
    return ''.join(shift_char)
def decode():
    message = input("Type your message: ")
    shift_value = int(input("Enter the shift key: "))
    shift_char = []
    for i in message:
        charTOaskii = ord(i)
        askiiTochar = chr(charTOaskii - shift_value)
        shift_char.append(askiiTochar)
    return ''.join(shift_char)
while True:
    userInterest = input("Do you want to encode or decode?(press enter to quit) ")
    if userInterest.lower() == "encode":
        print(encode())
    elif userInterest.lower() == "decode":
        print(decode())
    if userInterest == '':
        break
