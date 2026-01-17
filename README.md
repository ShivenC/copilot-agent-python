# copilot-agent-python

A Python utility repository containing various diagnostic and helper scripts.

## System Diagnostics Utility

The `system_diagnostics.py` script provides a simple way to view system information.

### Usage

Run the script directly from the command line:

```bash
python3 system_diagnostics.py
```

Or import and use the functions in your own code:

```python
from system_diagnostics import get_os_name, get_python_version, get_current_directory

print(f"OS: {get_os_name()}")
print(f"Python: {get_python_version()}")
print(f"Directory: {get_current_directory()}")
```

### Output

The script displays:
- **OS Name**: The operating system (e.g., Linux, Windows, Darwin for macOS)
- **Python Version**: The Python interpreter version currently in use
- **Current Working Directory**: The directory from which the script is executed