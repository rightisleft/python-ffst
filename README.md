# Fast Filesystem Search Tool

## Overview

This Python script is designed to quickly search for files and directories in a Linux filesystem, with a focus on optimizing the search in environments like WSL (Windows Subsystem for Linux). The script navigates through the filesystem, applying filters to avoid known bottlenecks such as specific system directories and `.git` directories.

The tool provides an efficient way to locate files and directories by name and offers an optional parameter to limit the search depth, allowing users to fine-tune their search according to their needs.

### Features
- Fast and efficient filesystem search.
- Avoidance of known bottlenecks and system directories.
- Optional search depth limitation.
- Timer outputs for directories that take more than 1 second to search, aiding in identifying potential bottlenecks.
- Command-line interface for easy usage.

## Alternatives and Challenges

During the development of this tool, several alternative methods and tools were explored, but they presented various challenges, particularly in environments like WSL. Here are some of the tools that were considered and the issues encountered:

### Ripgrep (rg)
**Challenges:** Ripgrep is a powerful search tool, but it exhibited performance bottlenecks in WSL environments. Additionally, constructing queries with multiple glob exclusions proved to be challenging, and certain queries resulted in errors or empty results.

### Baloo
**Challenges:** Baloo is a file indexing and search service for Linux, but it is primarily designed for KDE desktop environments. During testing, Baloo presented challenges such as being disabled by default and failing to open the index on headless servers.

### The Silver Searcher (ag)
**Challenges:** The Silver Searcher is a code-searching tool similar to ack, but faster. However, it did not provide the level of performance and flexibility required for this specific use case, particularly in avoiding system and git bottlenecks.

### locate/mlocate
**Challenges:** The `locate` command is a quick way to find the location of files and directories on Linux. However, it relies on a database that is updated periodically, which means it might not always have the most up-to-date information. Additionally, modifying the update frequency and adding new files only were not straightforward.

### fzf
**Challenges:** `fzf` is a general-purpose command-line fuzzy finder, but it did not offer the optimized performance needed for searching large filesystems, especially with depth limitations.

### fsearch
**Challenges:** `fsearch` is a fast file search utility for Unix-like systems, but it also faced performance issues and did not return results as expected during testing.

Given the challenges with the aforementioned tools, the decision was made to develop a custom Python script to address the specific needs and constraints of searching files and directories efficiently in Linux filesystems, especially in WSL environments.

## Usage

### Basic Usage
To use the script, navigate to the directory containing the script and execute it with the target file or directory name as a parameter:
```sh
./search_filesystem.py <target_name>

