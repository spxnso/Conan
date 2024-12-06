# Benchmarking for potential problems
import os
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from modules.usernames.socials import *

_SUCCESS = 0
_TOTAL_TIME = 0.0


def binstagram():
    global _SUCCESS, _TOTAL_TIME
    try:
        start_time = time.time()
        c = instagram("nintendo", True)
        end_time = time.time()

        elapsed_time = end_time - start_time

        if c:
            _SUCCESS += 1
            _TOTAL_TIME += elapsed_time
            print("[✓] Instagram")
    except Exception as e:
        print(f"[X] Instagram: {e}")


def btiktok():
    global _SUCCESS, _TOTAL_TIME
    try:
        start_time = time.time()
        c = tiktok("nintendo", True)
        end_time = time.time()

        elapsed_time = end_time - start_time

        if c:
            _SUCCESS += 1
            _TOTAL_TIME += elapsed_time
            print("[✓] Tiktok")
    except Exception as e:
        print(f"[X] Tiktok: {e}")


def bsnapchat():
    global _SUCCESS, _TOTAL_TIME
    try:
        start_time = time.time()
        c = snapchat("nintendo", True)
        end_time = time.time()

        elapsed_time = end_time - start_time

        if c:
            _SUCCESS += 1
            _TOTAL_TIME += elapsed_time
            print("[✓] Snapchat")
    except Exception as e:
        print(f"[X] Snapchat: {e}")

def bx():
    global _SUCCESS, _TOTAL_TIME
    try:
        start_time = time.time()
        c = twitter("nintendo", True)
        end_time = time.time()

        elapsed_time = end_time - start_time

        if c:
            _SUCCESS += 1
            _TOTAL_TIME += elapsed_time
            print("[✓] X")
    except Exception as e:
        print(f"[X] X: {e}")

def benchmark():
    bsnapchat()
    btiktok()
    binstagram()
    bx()
    print(f"Success count: {_SUCCESS}/{COUNT}")
    print(f"Total elapsed time: {_TOTAL_TIME:.6f} seconds")
    _TIME = f"{_TOTAL_TIME:.6f}"
    return _SUCCESS, _TIME