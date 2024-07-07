import pyautogui
import time
import keyboard
import webbrowser

def disable_mouse():
    pyautogui.FAILSAFE = False 
    try:
        while True:
            pyautogui.moveTo(1, 1)  # Move mouse cursor to (1, 1)
            time.sleep(0)  # Adjust sleep time to prevent high CPU usage
    except pyautogui.FailSafeException:
        pass  


# Function to open a website in a web browser
def open_website(url):
    webbrowser.open(url)
def main():
    try:
        url = "https://www.youtube.com/watch?v=xvFZjo5PgG0"
        open_website(url)
        disable_mouse()
        
    except Exception as e:
        print(f"Error occurred: {e}")
        raise  # Re-raise the exception to ensure proper error handling

    finally:
        pyautogui.FAILSAFE = True  # Restore the pyautogui failsafe

if __name__ == "__main__":
    main()
