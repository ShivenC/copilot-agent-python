#!/usr/bin/env python3
"""
System Diagnostics Utility

This module provides a simple utility to print system diagnostic information
including the operating system name, Python version, and current working directory.
"""

import os
import platform
import sys


def get_os_name():
    """
    Get the operating system name.
    
    Returns:
        str: The name of the operating system.
    """
    return platform.system()


def get_python_version():
    """
    Get the Python version.
    
    Returns:
        str: The Python version in use.
    """
    return sys.version


def get_current_directory():
    """
    Get the current working directory.
    
    Returns:
        str: The current working directory path.
    """
    return os.getcwd()


def print_diagnostics():
    """
    Print system diagnostic information.
    
    Displays the OS name, Python version, and current working directory.
    """
    print("=== System Diagnostics ===")
    print(f"OS Name: {get_os_name()}")
    print(f"Python Version: {get_python_version()}")
    print(f"Current Working Directory: {get_current_directory()}")
    print("==========================")


if __name__ == "__main__":
    print_diagnostics()
