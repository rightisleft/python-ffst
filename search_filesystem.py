#!/usr/bin/env python3
import os
import sys
import time
import argparse

def search_filesystem(target, maxdepth=None):
    # Define directories to exclude
    exclude_dirs = set([
        "/proc",
        "/sys",
        "/mnt",
        "/dev",
        "/snap",
        "/var",
        "/.git",  # Exclude .git directories to avoid git bottlenecks
    ])
    
    # Walk through the filesystem starting from the root directory
    for root, dirs, files in os.walk("/", topdown=True):
        # Modify dirs in-place to skip excluded directories
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_dirs]
        
        # Calculate the current depth
        depth = root.count(os.path.sep)
        
        # Skip directories deeper than maxdepth
        if maxdepth is not None and depth > maxdepth:
            del dirs[:]
            continue
        
        # Start the timer
        start_time = time.time()
        
        # Check if the current directory name matches the target
        if os.path.basename(root) == target:
            print(root)
        
        # Check if any file in the current directory matches the target
        for file in files:
            if file == target:
                print(os.path.join(root, file))
        
        # End the timer and check the elapsed time
        elapsed_time = time.time() - start_time
        if elapsed_time > 1:
            print(f"Searching in {root} took {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for files and directories matching the target.")
    parser.add_argument("target", help="The name of the file or directory to search for.")
    parser.add_argument("--maxdepth", type=int, help="The maximum depth to search.")
    args = parser.parse_args()
    
    search_filesystem(args.target, args.maxdepth)

