import platform
import time
import os

def main():
    print("--- Start Monitoring Application ---")

    system_info = platform.system()
    release_info = platform.release()
    host_name = platform.node()

    print(f"Host: {host_name}")
    print(f"System: {system_info} {release_info}")
    print("-" * 30)


    counter = 1
    while True:
        print(f"Log [{counter}]: The application is working properly... Server time: {time.ctime()}")
        counter += 1
        time.sleep(5)


if __name__ == "__main__":
    main()