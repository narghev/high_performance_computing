# HPC Homework 2

## Setup
Make files in the /src directory and fill them with random data.
```bash
dd if=/dev/random of=src/a.txt count=1024000
dd if=/dev/random of=src/b.txt count=1024000
dd if=/dev/random of=src/c.txt count=1024000
dd if=/dev/random of=src/d.txt count=1024000
```

## Running
Call `copy.py`, `multiprocess_copy.py`, `multithread_copy.py` like
```bash
time python3 <filename>.py
```

This will run the command and time it.