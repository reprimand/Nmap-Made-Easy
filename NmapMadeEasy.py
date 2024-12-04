import subprocess

def explain_timing_template():
    print("""
--- Timing Templates (T1–T5) ---
1. T1 (Paranoid): Very slow scan, used to avoid detection on IDS/IPS.
2. T2 (Sneaky): Slow scan, less likely to be detected.
3. T3 (Normal): Default timing, balanced between speed and stealth.
4. T4 (Aggressive): Faster scans, might trigger alarms.
5. T5 (Insane): Very fast scans, likely to trigger alarms.
""")

def explain_scan_types():
    print("""
--- Scan Types ---
1. Ping Scan (-sn): Checks if hosts are up without scanning ports.
2. Service and Version Detection (-sV): Detects services running on open ports.
3. Vulnerability Scan (--script vuln): Runs vulnerability checks using Nmap's scripting engine.
4. Full Port Scan (-p-): Scans all 65535 ports on the target.
5. Custom Scan: Manually enter your own flags for a custom scan.
""")

def wizard():
    print("Welcome to the Nmap Made Easy")
    print("This tool will guide you through creating and executing an Nmap scan step by step. I would want you to slowly move away from using this tool so take notes of everything you do and you'll slowly be able to transition away from using it\n")

    # Step 1: Enter target(s)
    targets = input("Enter target(s) (e.g., IP, hostname, or CIDR): ").strip()
    if not targets:
        print("No target entered. Exiting.")
        return

    # Step 2: Choose timing template
    explain_timing_template()
    timing_choice = input("Select a timing template (1-5): ").strip()
    timing_template = f"-T{timing_choice}" if timing_choice in ["1", "2", "3", "4", "5"] else "-T3"
    print(f"Timing template set to: {timing_template}\n")

    # Step 3: Choose scan type
    explain_scan_types()
    scan_choice = input("Select a scan type (1-5): ").strip()
    if scan_choice == "1":
        scan_type = "-sn"
    elif scan_choice == "2":
        scan_type = "-sV"
    elif scan_choice == "3":
        scan_type = "--script vuln"
    elif scan_choice == "4":
        scan_type = "-p-"
    elif scan_choice == "5":
        scan_type = input("Enter custom Nmap options: ").strip()
    else:
        print("Invalid choice. Defaulting to Ping Scan (-sn).")
        scan_type = "-sn"
    print(f"Scan type set to: {scan_type}\n")

    # Step 4: Add advanced options
    print("""
--- Advanced Options ---
1. Enable OS Detection (--osscan-guess)
2. Save results to a file (-oN or -oX)
3. Skip additional options
""")
    advanced_options = ""
    advanced_choice = input("Select an advanced option (1-3): ").strip()
    if advanced_choice == "1":
        advanced_options = "--osscan-guess"
    elif advanced_choice == "2":
        file_format = input("Choose file format: 1. Normal (-oN) or 2. XML (-oX): ").strip()
        file_name = input("Enter the file name to save results (e.g., results.txt): ").strip()
        if file_format == "1":
            advanced_options = f"-oN {file_name}"
        elif file_format == "2":
            advanced_options = f"-oX {file_name}"
        else:
            print("Invalid choice. Skipping save option.")
    print(f"Advanced options set to: {advanced_options}\n")

    # Step 5: Review and confirm command
    command = f"nmap {timing_template} {scan_type} {advanced_options} {targets}"
    print(f"\n--- Command Review ---")
    print(f"Generated Nmap Command: {command}")
    confirm = input("Would you like to run this command? (y/n): ").strip().lower()

    if confirm == "y":
        print("\nRunning the command...\n")
        try:
            subprocess.run(command, shell=True)
        except Exception as e:
            print(f"Error executing command: {e}")
    else:
        print("Command not executed. Exiting.")

if __name__ == "__main__":
    wizard()
