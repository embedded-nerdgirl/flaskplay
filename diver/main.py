# This is the main program, it communicates with the server backend directly
# This section is what handles all the good stuff like the cameras and utils.

import camera

import os
import time

def upload_content(): ...

def main():
    running = True
    print("\0")
    print("Starting visor services...")

    camera.start_camera()

    print("Starting loop...")
    while running:
        ...

if __name__ == "__main__":
    main()