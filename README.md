# Fast Filesystem Search Tool

## Overview

This Python script is designed to quickly search for files and directories in a Linux filesystem, with a focus on optimizing the search in environments like WSL (Windows Subsystem for Linux). The script walks through the filesystem, applying filters to avoid known bottlenecks such as specific system directories and `.git` directories.

The tool provides an efficient way to locate files and directories by name and offers an optional parameter to limit the search depth, allowing users to fine-tune their search according to their needs.

### Features
- Fast and efficient filesystem search.
- Avoidance of known bottlenecks and system directories.
- Optional search depth limitation.
- Timer outputs for directories that take more than 1 second to search, aiding in identifying potential bottlenecks.
- Command-line interface for easy usage.

## Alternatives and Challenges

During the development of this tool, several alternative methods and tools were explored, but they presented various challenges, particularly in environments like WSL. Here are some of the tools that were considered and the issues encountered:

- **Ripgrep (rg)**
  - *Challenges*: Exhibited performance bottlenecks in WSL environments. Constructing queries with multiple glob exclusions proved to be challenging, resulting in errors or empty results.
- **Baloo**
  - *Challenges*: Primarily designed for KDE desktop environments. Faced issues such as being disabled by default and failing to open the index on headless servers.
- **The Silver Searcher (ag)**
  - *Challenges*: Did not provide the level of performance and flexibility required, particularly in avoiding system and git bottlenecks.
- **locate/mlocate**
  - *Challenges*: Relies on a database updated periodically, potentially lacking the most up-to-date information. Modifying the update frequency and adding new files only were not straightforward.
- **fzf**
  - *Challenges*: Did not offer optimized performance needed for searching large filesystems with depth limitations.
- **fsearch**
  - *Challenges*: Faced performance issues and did not return results as expected during testing.

Given the challenges with the aforementioned tools, a custom Python script was developed to address the specific needs and constraints of efficiently searching files and directories in Linux filesystems, especially in WSL environments.

## Usage

### Basic Usage
To use the script, navigate to the directory containing the script and execute it with the target file or directory name as a parameter:
```sh
./search_filesystem.py <target>

