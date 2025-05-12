from colorama import Fore, init
import random
import time

init(autoreset=True)
message = (
    "This Encryption By @D8N8D\n Decode This And Send Source At @TalkToShridharBot\n"
)

colors = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.WHITE,
]

for char in message:
    print(random.choice(colors) + char, end="", flush=True)
    time.sleep(0.1)


for i in range(21):
    bar = "[" + "#" * i + " " * (20 - i) + "]"
    print(Fore.YELLOW + f"\rLoading {bar}", end="", flush=True)
    time.sleep(0.2)

key = "bQbp_TP%~P4z"

# Decode By @SoukPy // @SoukTool
