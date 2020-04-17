from datetime import datetime
import time
import sys
from LemonBlocks import Bar, Block


# A Block that displays the current date and time
class Date(Block):
    # Refresh the current date
    def update(self):
        self.date = datetime.now().strftime('%H:%M')
    
    # Get content of the block
    def content(self):
        return f' {self.date} '


if __name__ == "__main__":
    # Create a bar
    b = Bar()

    # Add a date block to the bar
    b.add(Date("#ffffff", "#0a84ff"))
    
    # Main loop
    while True:
      # Write the string representation of the Bar to stdout
      sys.stdout.write(str(b) + "\n")
      sys.stdout.flush()

      # This bar will refresh after a second
      time.sleep(1)

