"""
Digital Clock (Command-Line Version)
-----------------------------------------
This simple program displays the current time
and updates every second like a live clock.

Concepts used:
- Python's time module
- Infinite loops
- String formatting
- Real-time screen updates using '\r' (carriage return)
"""

import time  # Provides time-related functions like sleep() and localtime()

def digital_clock():
    """Displays the current time continuously until the user stops the program."""
    print("⏰ Digital Clock Started! (Press Ctrl+C to stop)\n")
    
    try:
        while True:
            # Get the current local time as a struct_time object
            current_time = time.localtime()

            # Format time as HH:MM:SS using strftime()
            formatted_time = time.strftime("%H:%M:%S", current_time)

            # Print time on the same line using '\r' to overwrite previous output
            print(f"\r🕒 Current Time: {formatted_time}", end="")

            # Wait for 1 second before updating again
            time.sleep(1)

    except KeyboardInterrupt:
        # Graceful exit message when user presses Ctrl+C
        print("\n🛑 Clock stopped by user. Goodbye!")


# Entry point of the program
if __name__ == "__main__":
    digital_clock()
