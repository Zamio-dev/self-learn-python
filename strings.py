print('This program let you under stand about string ops')
print('-------------------------------------------------\n')
message="""
hi how are you
i think things will get better
"""
print(f"{message=} {message}")
print(f"{message[:10]=}")
print(f"{message[5:]=}")
print(f"{message[-5:]=}")
print(f"{message[-1:-7]=}")
print(f"{message.upper()=}")
print(f"{message.lower()=}")
print(f"{message.title()=}")
print(f"{message.strip()=}")
print(f"{message.find('will')=}")
print(f"{message.replace('will','may')=}")
print(f"{'you' in message=}")
print(f"{'you' not in message=}")
