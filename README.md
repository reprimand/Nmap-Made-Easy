# Nmap Made Easy

**Nmap Made Easy** is a Python based Nmap tool that simplifies network scanning. Made for beginners, it guides you step-by-step through the process of creating and executing  Nmap commands.

## Requirements

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **Nmap**: Install Nmap, as this tool builds commands that rely on it.

### Installing Nmap
- **Linux**: `sudo apt install nmap` (Debian/Ubuntu)
- **Windows**: Download and install from [https://nmap.org/download.html](https://nmap.org/download.html)

---

## Usage

1. **Enter target(s):** Provide the target IP, hostname, or CIDR range.
   - Examples:
     - IP: `192.168.0.1`
     - Hostname: `example.com`
     - CIDR: `192.168.0.0/24`

2. **Select a scan type:** Choose from options like ping scan, service detection, or vulnerability scan.

3. **Choose a timing template (T1–T5):** Control scan speed and stealth.
   - T1: Very slow, stealthy.
   - T3: Default, balanced speed.
   - T5: Very fast, less stealthy.

4. **Add optional advanced flags:** Options include OS detection (`--osscan-guess`) or saving results to a file (`-oN results.txt`).

5. **Review and execute the command.** The tool shows the full Nmap command before running, giving you complete control.

---

## Disclaimer

**Nmap Made Easy is intended for educational purposes only.** This tool is designed to help users learn and understand network scanning using Nmap. It should only be used in environments where you have explicit permission to scan, such as your own networks or networks where you have proper authorization.

Unauthorized scanning of networks is illegal and may result in severe consequences, including fines or imprisonment. The creators and contributors of this tool are not responsible for any misuse, legal issues, or damages caused by its use.

By using this tool, you agree to take full responsibility for ensuring your actions comply with all applicable laws and regulations.
