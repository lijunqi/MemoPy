"""
python -Xfrozen_modules=off -m debugpy --listen localhost:5678 --pid 12456

launch.json
"configurations": [
        {
            "name": "Python Debugger: Remote Attach",
            "type": "debugpy",
            "request": "attach",
            "connect": {
                "host": "localhost",
                "port": 5678
            },
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}",
                    "remoteRoot": "."
                }
            ]
        }
    ]
"""
import os
import time

def main():
    cnt = 0
    while True:
        print(f"cnt = {cnt}")
        time.sleep(1)
        cnt += 1


if __name__ == "__main__":
    print("PID: ", os.getppid())
    main()
