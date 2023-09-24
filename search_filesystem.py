#!/usr/bin/env python3
import os
import sys
import time

def is_excluded_directory(dir):
    excluded_directories = ['/proc', '/sys', '/mnt', '/dev', '/snap', '/var', '.git']
    for excluded_dir in excluded_directories:
        if dir.startswith(excluded_dir):
            return True
    return False

def search_filesystem(target, max_depth, root='/'):
    for root, dirs, files in os.walk(root):
        depth = root.count(os.path.sep)
        if depth > max_depth:
            del dirs[:]
            continue
        if is_excluded_directory(root):
            del dirs[:]
            continue
        if target in files or target in dirs:
            print(os.path.join(root, target))
        for dir in dirs:
            start_time = time.time()
            if os.path.isdir(os.path.join(root, dir)):
                if time.time() - start_time > 0.1:
                    print(f"Skipping {os.path.join(root, dir)} due to timeout")
                    dirs.remove(dir)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: search_filesystem.py <target> [--maxdepth <max_depth>]")
        sys.exit(1)
    target = sys.argv[1]
    max_depth = int(sys.argv[3]) if '--maxdepth' in sys.argv else float('inf')
    search_filesystem(target, max_depth)

