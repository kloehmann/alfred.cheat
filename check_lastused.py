import sys, os, time

MAX_OFFSET = 3000

if __name__ == "__main__":
    lastused = sys.argv[1]
    last_access = os.stat(lastused).st_mtime
    now = time.time()
    offset = round(now - last_access)
    if offset > MAX_OFFSET:
        os.remove(lastused)
        print("")
    else:
        f = open(lastused)
        print(f.read(), end="")
        f.close()
