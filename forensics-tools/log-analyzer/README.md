# Log Analyzer — Forensics Tool

## What It Does
Scans any log file for suspicious keywords.
Flags matching lines with exact line numbers.
Prints a summary of total matches per keyword.

## Forensic Use Case
Investigators search log files for failed login attempts,
unknown users, and suspicious IP addresses on seized systems.
This tool automates that search across any log file.

## How to Run
python3 log_analyzer.py

## Example Output
8 10.0.0.55 - unknown - GET /admin failed
9 10.0.0.55 - unknown - GET /admin failed

Total unknown attempts: 6
Total failed attempts: 10
