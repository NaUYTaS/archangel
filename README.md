# 🛡️ Archangel (archangel.py)

A lightweight Cyber-Security and Network Monitoring script written in Python. It acts as a digital guardian for your PC, analyzing outbound traffic, identifying hidden heavy processes (like crypto-miners), and checking Windows startup registry keys for unauthorized persistence.
___
/   \
|  X  |
_         _/         _
/ \          |          / 
/   \        /|\        /   
/     _/ | ___/     
/       \    /  |  \    /       
/   /\    \  /   |   \  /    /\   \
|   /  \    /    |    /    /  \   |
|  /    \   /     |     \   /    \  |
| /      _/      |      _/      \ |
|/                |                |
|
|
[-]
| |
| |
v

## ✨ Features
* 🌐 **Network Traffic Monitoring:** Scans active `ESTABLISHED` connections to show you exactly where your internet traffic is going.
* ⚙️ **Process Analysis:** Detects hidden or suspicious applications consuming high amounts of RAM or CPU (potential miners or malware).
* 🔑 **Windows Registry Check:** Audits startup (`Run` and `RunOnce`) keys to see what launches automatically behind your back.
* 🎨 **Visual Interface:** Beautiful ASCII-art and color-coded terminal outputs (Green for safe, Red for warnings).

## 🚀 How to Run

1. Clone this repository or download `archangel.py`.
2. Install the required library via terminal:
   ```bash
   pip install psutil
   ```
3. Run the script (Run as **Administrator** for full network access):
   ```bash
   python archangel.py
   ```

## 🛠️ Future Improvements (Roadmap)
I am a beginner developer passionate about cybersecurity. I want to improve Archangel by adding:
* 🗺️ IP Geolocation (showing which country the traffic goes to).
* 📁 Automated scans of the `Temp` folder for dropped malware.
* 🛑 A feature to instantly terminate/block suspicious processes.

*If you like this project, please leave a ⭐ Star! It helps a lot!*
