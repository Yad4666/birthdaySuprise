#Angel.

import time
import os


def birthday_surprise():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display a loading effect
    for i in range(3):
        print("Preparing your surprise" + "." * i)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

    # Print the birthday message
    print("""
        🎉🎉🎉 HAPPY BIRTHDAY! 🎉🎉🎉

        Dear [frishta],

        Roses are red,
        Violets are blue,
        This little surprise,
        Is just for you!

        🎂 Have the best day ever! 🎂
    """)

    # Add some ASCII art
    print("""
          ,,,,,,,,,,,,
        ,;;;;;;;;;;;;;;;;;;;,
       ;;;;;;;;;;;;;;;;;;;;;;;
       ;;;;;;@;;;;;;;;;;@;;;;;;
       ;;;;;;;;;;;;;;;;;;;;;;;;;
        ;;;;;;;;;;;;;;;;;;;;;;;
         `;;;;;;;;;;;;;;;;;;;'
           `;;;;;;;;;;;;;;;'
              `;;;;;;;;;'

         🎵 🎶 Play a song 🎶 🎵
    """)

    # Optional: Play a Happy Birthday song (requires `playsound` module)
    try:
        from playsound import playsound
        playsound('happy_birthday.mp3')  # Ensure you have a "happy_birthday.mp3" file in the same directory
    except ImportError:
        print("Install the 'playsound' library to enable sound.")
    except Exception as e:
        print(f"Could not play the sound. Error: {e}")


if __name__ == "__main__":
    birthday_surprise()


