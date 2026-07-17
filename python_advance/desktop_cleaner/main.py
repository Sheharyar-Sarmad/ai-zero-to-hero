import os
import sys
import subprocess
import platform
import psutil
import ctypes
import shutil
import winreg
import tempfile
import threading
import time
import json
from datetime import datetime
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, Checkbutton, BooleanVar, Listbox, Scrollbar, EXTENDED, LabelFrame, Frame, Label, Button, Entry
from tkinter import font as tkfont
import winshell
from pathlib import Path

# ==================== SYSTEM DIAGNOSTICS ====================
class SystemDiagnostics:
    @staticmethod
    def check_system_health():
        """Check system for errors and issues"""
        issues = []
        
        try:
            # Check disk health
            for partition in psutil.disk_partitions():
                if 'C:' in partition.mountpoint:
                    usage = psutil.disk_usage(partition.mountpoint)
                    if usage.free / (1024**3) < 5:
                        issues.append("⚠️ Low disk space on C: drive")
        except:
            pass
        
        try:
            memory = psutil.virtual_memory()
            if memory.percent > 90:
                issues.append("⚠️ High memory usage (>90%)")
        except:
            pass
        
        try:
            result = subprocess.run(['wevtutil', 'qe', 'System', '/c:5', '/f:text'], 
                                  capture_output=True, text=True, timeout=5)
            if 'Error' in result.stdout:
                issues.append("⚠️ Recent system errors detected in Event Log")
        except:
            pass
        
        try:
            high_cpu = [p for p in psutil.process_iter(['name', 'cpu_percent']) 
                       if p.info['cpu_percent'] and p.info['cpu_percent'] > 50]
            if high_cpu:
                issues.append(f"⚠️ {len(high_cpu)} processes using high CPU")
        except:
            pass
        
        return issues if issues else ["✅ System is healthy - No issues detected"]

    @staticmethod
    def get_system_info():
        """Get detailed system information"""
        info = {}
        
        try:
            info['OS'] = platform.platform()
            info['OS Version'] = platform.version()
            info['Machine'] = platform.machine()
            info['Processor'] = platform.processor()
            info['CPU Cores'] = psutil.cpu_count()
            info['CPU Usage'] = f"{psutil.cpu_percent(interval=1)}%"
            
            memory = psutil.virtual_memory()
            info['Total RAM'] = f"{memory.total / (1024**3):.2f} GB"
            info['Available RAM'] = f"{memory.available / (1024**3):.2f} GB"
            info['RAM Usage'] = f"{memory.percent}%"
            
            for partition in psutil.disk_partitions():
                if 'C:' in partition.mountpoint:
                    usage = psutil.disk_usage(partition.mountpoint)
                    info['Total Disk'] = f"{usage.total / (1024**3):.2f} GB"
                    info['Used Disk'] = f"{usage.used / (1024**3):.2f} GB"
                    info['Free Disk'] = f"{usage.free / (1024**3):.2f} GB"
                    info['Disk Usage'] = f"{usage.percent}%"
                    break
            
            import socket
            hostname = socket.gethostname()
            info['Hostname'] = hostname
            try:
                info['IP Address'] = socket.gethostbyname(hostname)
            except:
                info['IP Address'] = "N/A"
            
            boot_time = datetime.fromtimestamp(psutil.boot_time())
            uptime = datetime.now() - boot_time
            days = uptime.days
            hours, remainder = divmod(uptime.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            info['System Uptime'] = f"{days}d {hours}h {minutes}m"
        except Exception as e:
            info['Error'] = str(e)
        
        return info

# ==================== SOFTWARE MANAGER ====================
class SoftwareManager:
    @staticmethod
    def get_installed_software():
        """Get list of installed software"""
        software = []
        
        try:
            registry_paths = [
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
            ]
            
            for reg_path in registry_paths:
                try:
                    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
                    i = 0
                    while True:
                        try:
                            subkey_name = winreg.EnumKey(key, i)
                            subkey = winreg.OpenKey(key, subkey_name)
                            try:
                                display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                if display_name and display_name.strip():
                                    version = ""
                                    publisher = ""
                                    try:
                                        version = winreg.QueryValueEx(subkey, "DisplayVersion")[0]
                                    except:
                                        pass
                                    try:
                                        publisher = winreg.QueryValueEx(subkey, "Publisher")[0]
                                    except:
                                        pass
                                    
                                    software.append({
                                        'name': display_name.strip(),
                                        'version': version if version else "",
                                        'publisher': publisher if publisher else ""
                                    })
                            except:
                                pass
                            i += 1
                        except WindowsError:
                            break
                except:
                    pass
        except:
            pass
        
        # Sort by name
        software.sort(key=lambda x: x['name'].lower())
        return software

    @staticmethod
    def uninstall_software(software_name):
        """Uninstall software by name"""
        try:
            registry_paths = [
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
            ]
            
            for reg_path in registry_paths:
                try:
                    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
                    i = 0
                    while True:
                        try:
                            subkey_name = winreg.EnumKey(key, i)
                            subkey = winreg.OpenKey(key, subkey_name)
                            try:
                                display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                if display_name and display_name.lower() == software_name.lower():
                                    try:
                                        uninstall_string = winreg.QueryValueEx(subkey, "UninstallString")[0]
                                        if uninstall_string:
                                            subprocess.Popen(uninstall_string, shell=True)
                                            return True, "Uninstaller launched successfully"
                                    except:
                                        pass
                            except:
                                pass
                            i += 1
                        except WindowsError:
                            break
                except:
                    pass
            return False, "Software not found"
        except Exception as e:
            return False, f"Error: {str(e)}"

# ==================== MAIN APPLICATION ====================
class ModernCleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧹 System Cleaner Pro")
        self.root.geometry("1300x900")
        self.root.configure(bg='#0a0e17')
        
        # Variables
        self.scanning = False
        self.cleaning = False
        self.files_found = []
        self.selected_files = []
        self.software_list = []
        self.selected_software = []
        self.system_issues = []
        self.initialized = False
        
        # Cleanup options
        self.clean_temp = BooleanVar(value=True)
        self.clean_windows_temp = BooleanVar(value=True)
        self.clean_prefetch = BooleanVar(value=False)
        self.clean_recycle = BooleanVar(value=True)
        self.clean_recent = BooleanVar(value=True)
        self.clean_desktop = BooleanVar(value=False)
        
        # Setup UI
        self.setup_ui()
        
        # Initial system check
        self.root.after(1000, self.check_system_health)
        self.root.after(500, self.load_software_list)
        
    def setup_ui(self):
        # Main container
        main_frame = tk.Frame(self.root, bg='#0a0e17')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_frame)
        
        # Content - Split into sections
        content_frame = tk.Frame(main_frame, bg='#0a0e17')
        content_frame.pack(fill=tk.BOTH, expand=True, pady=15)
        
        # Left section - Cleaning
        left_frame = tk.Frame(content_frame, bg='#0a0e17', width=450)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        left_frame.pack_propagate(False)
        
        # Right section - System Info
        right_frame = tk.Frame(content_frame, bg='#0a0e17')
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Create all sections
        self.create_stats_section(left_frame)
        self.create_options_section(left_frame)
        self.create_scan_section(left_frame)
        self.create_file_list_section(left_frame)
        
        # Right side sections
        self.create_system_info_section(right_frame)
        self.create_software_section(right_frame)
        self.create_diagnostics_section(right_frame)
        
        # Bottom - Log (create this before loading software)
        self.create_log_section(main_frame)
        
        # Mark as initialized
        self.initialized = True
        
        # Apply modern styling
        self.apply_modern_style()
    
    def create_header(self, parent):
        header_frame = tk.Frame(parent, bg='#0a0e17')
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Title and subtitle
        title_container = tk.Frame(header_frame, bg='#0a0e17')
        title_container.pack(side=tk.LEFT)
        
        title_label = tk.Label(
            title_container,
            text="🧹 System Cleaner Pro",
            font=('Segoe UI', 24, 'bold'),
            fg='#ffffff',
            bg='#0a0e17'
        )
        title_label.pack(anchor='w')
        
        subtitle_label = tk.Label(
            title_container,
            text="Advanced System Optimization & Cleanup Tool",
            font=('Segoe UI', 11),
            fg='#8899aa',
            bg='#0a0e17'
        )
        subtitle_label.pack(anchor='w')
        
        # System status indicator
        status_frame = tk.Frame(header_frame, bg='#0a0e17')
        status_frame.pack(side=tk.RIGHT)
        
        self.status_indicator = tk.Label(
            status_frame,
            text="🟢 System Running",
            font=('Segoe UI', 11),
            fg='#00ff88',
            bg='#0a0e17'
        )
        self.status_indicator.pack()
    
    def create_stats_section(self, parent):
        stats_frame = tk.Frame(parent, bg='#0a0e17')
        stats_frame.pack(fill=tk.X, pady=(0, 10))
        
        stats_data = [
            ("📁", "Files Found", "0", "#4fc3f7"),
            ("💾", "Total Size", "0 MB", "#ffb74d"),
            ("✅", "Selected", "0", "#81c784"),
            ("📊", "Free Space", "0 GB", "#ce93d8")
        ]
        
        self.stat_cards = []
        for icon, label, value, color in stats_data:
            card = tk.Frame(stats_frame, bg='#1a2332', relief=tk.FLAT, bd=1)
            card.pack(side=tk.LEFT, padx=3, fill=tk.BOTH, expand=True)
            card.configure(highlightbackground='#2a3a4e', highlightthickness=1)
            
            icon_label = tk.Label(card, text=icon, font=('Segoe UI', 16), bg='#1a2332', fg='#8899aa')
            icon_label.pack(pady=(8, 0))
            
            val_label = tk.Label(
                card,
                text=value,
                font=('Segoe UI', 16, 'bold'),
                fg=color,
                bg='#1a2332'
            )
            val_label.pack()
            
            label_label = tk.Label(
                card,
                text=label,
                font=('Segoe UI', 9),
                fg='#8899aa',
                bg='#1a2332'
            )
            label_label.pack(pady=(0, 8))
            
            self.stat_cards.append(val_label)
        
        self.update_free_space()
    
    def create_options_section(self, parent):
        options_frame = tk.LabelFrame(
            parent,
            text="🛡️ Cleanup Locations",
            bg='#0a0e17',
            fg='#ffffff',
            font=('Segoe UI', 11, 'bold'),
            relief=tk.FLAT
        )
        options_frame.pack(fill=tk.X, pady=(0, 10))
        
        options_inner = tk.Frame(options_frame, bg='#0a0e17')
        options_inner.pack(pady=10, padx=10)
        
        col1 = tk.Frame(options_inner, bg='#0a0e17')
        col1.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        col2 = tk.Frame(options_inner, bg='#0a0e17')
        col2.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        
        Checkbutton(col1, text="🗑️ User Temp Folder", variable=self.clean_temp,
                   bg='#0a0e17', fg='#ccddee', selectcolor='#1a2332',
                   font=('Segoe UI', 10)).pack(anchor='w', pady=3)
        
        Checkbutton(col1, text="💻 Windows Temp Folder", variable=self.clean_windows_temp,
                   bg='#0a0e17', fg='#ccddee', selectcolor='#1a2332',
                   font=('Segoe UI', 10)).pack(anchor='w', pady=3)
        
        Checkbutton(col1, text="🔄 Prefetch Files", variable=self.clean_prefetch,
                   bg='#0a0e17', fg='#ccddee', selectcolor='#1a2332',
                   font=('Segoe UI', 10)).pack(anchor='w', pady=3)
        
        Checkbutton(col2, text="♻️ Recycle Bin", variable=self.clean_recycle,
                   bg='#0a0e17', fg='#ccddee', selectcolor='#1a2332',
                   font=('Segoe UI', 10)).pack(anchor='w', pady=3)
        
        Checkbutton(col2, text="📄 Recent Documents", variable=self.clean_recent,
                   bg='#0a0e17', fg='#ccddee', selectcolor='#1a2332',
                   font=('Segoe UI', 10)).pack(anchor='w', pady=3)
        
        Checkbutton(col2, text="🖥️ Desktop Files", variable=self.clean_desktop,
                   bg='#0a0e17', fg='#ccddee', selectcolor='#1a2332',
                   font=('Segoe UI', 10)).pack(anchor='w', pady=3)
    
    def create_scan_section(self, parent):
        scan_frame = tk.Frame(parent, bg='#0a0e17')
        scan_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.progress_var = tk.DoubleVar()
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Custom.Horizontal.TProgressbar", 
                       background='#4fc3f7', 
                       troughcolor='#1a2332',
                       bordercolor='#0a0e17',
                       lightcolor='#4fc3f7',
                       darkcolor='#4fc3f7')
        
        self.progress_bar = ttk.Progressbar(
            scan_frame,
            variable=self.progress_var,
            length=100,
            mode='determinate',
            style="Custom.Horizontal.TProgressbar"
        )
        self.progress_bar.pack(fill=tk.X, pady=(0, 5))
        
        self.status_label = tk.Label(
            scan_frame,
            text="Ready to scan...",
            font=('Segoe UI', 10),
            fg='#8899aa',
            bg='#0a0e17'
        )
        self.status_label.pack()
        
        button_frame = tk.Frame(scan_frame, bg='#0a0e17')
        button_frame.pack(pady=10)
        
        self.scan_btn = self.create_modern_button(
            button_frame, "🔍 Scan", self.scan_files,
            '#4fc3f7', '#0d47a1'
        )
        self.scan_btn.pack(side=tk.LEFT, padx=5)
        
        self.clean_btn = self.create_modern_button(
            button_frame, "🧹 Delete Selected", self.clean_files,
            '#81c784', '#1b5e20', state=tk.DISABLED
        )
        self.clean_btn.pack(side=tk.LEFT, padx=5)
        
        self.cancel_btn = self.create_modern_button(
            button_frame, "❌ Cancel", self.cancel_operation,
            '#ef5350', '#b71c1c', state=tk.DISABLED
        )
        self.cancel_btn.pack(side=tk.LEFT, padx=5)
    
    def create_file_list_section(self, parent):
        list_frame = tk.LabelFrame(
            parent,
            text="📋 Found Files (Click to select/deselect)",
            bg='#0a0e17',
            fg='#ffffff',
            font=('Segoe UI', 10, 'bold'),
            relief=tk.FLAT
        )
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        list_inner = tk.Frame(list_frame, bg='#0a0e17')
        list_inner.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        scrollbar = Scrollbar(list_inner, bg='#1a2332')
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.file_listbox = Listbox(
            list_inner,
            selectmode=EXTENDED,
            yscrollcommand=scrollbar.set,
            font=('Consolas', 9),
            bg='#1a2332',
            fg='#ccddee',
            selectbackground='#4fc3f7',
            selectforeground='#0a0e17',
            relief=tk.FLAT,
            highlightthickness=0
        )
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.file_listbox.yview)
        self.file_listbox.bind('<ButtonRelease-1>', self.on_file_select)
        
        control_frame = tk.Frame(list_frame, bg='#0a0e17')
        control_frame.pack(fill=tk.X, pady=(0, 5))
        
        Button(control_frame, text="✅ Select All", command=self.select_all_files,
              bg='#1a2332', fg='#81c784', font=('Segoe UI', 9), 
              relief=tk.FLAT, cursor='hand2').pack(side=tk.LEFT, padx=5)
        
        Button(control_frame, text="❌ Deselect All", command=self.deselect_all_files,
              bg='#1a2332', fg='#ef5350', font=('Segoe UI', 9),
              relief=tk.FLAT, cursor='hand2').pack(side=tk.LEFT, padx=5)
    
    def create_system_info_section(self, parent):
        info_frame = tk.LabelFrame(
            parent,
            text="💻 System Information",
            bg='#0a0e17',
            fg='#ffffff',
            font=('Segoe UI', 11, 'bold'),
            relief=tk.FLAT
        )
        info_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.info_text = scrolledtext.ScrolledText(
            info_frame,
            height=8,
            font=('Consolas', 9),
            bg='#1a2332',
            fg='#ccddee',
            relief=tk.FLAT,
            wrap=tk.WORD
        )
        self.info_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Load system info
        self.load_system_info()
    
    def create_software_section(self, parent):
        software_frame = tk.LabelFrame(
            parent,
            text="📦 Installed Software",
            bg='#0a0e17',
            fg='#ffffff',
            font=('Segoe UI', 11, 'bold'),
            relief=tk.FLAT
        )
        software_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        search_frame = tk.Frame(software_frame, bg='#0a0e17')
        search_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(search_frame, text="Search:", bg='#0a0e17', fg='#8899aa',
                font=('Segoe UI', 9)).pack(side=tk.LEFT, padx=(0, 5))
        
        self.search_entry = Entry(search_frame, bg='#1a2332', fg='#ffffff',
                                  relief=tk.FLAT, font=('Segoe UI', 10))
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.search_entry.bind('<KeyRelease>', self.filter_software)
        
        Button(search_frame, text="🔄 Refresh", command=self.load_software_list,
              bg='#1a2332', fg='#4fc3f7', font=('Segoe UI', 9),
              relief=tk.FLAT, cursor='hand2').pack(side=tk.RIGHT)
        
        list_frame = tk.Frame(software_frame, bg='#0a0e17')
        list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=(0, 5))
        
        scrollbar = Scrollbar(list_frame, bg='#1a2332')
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.software_listbox = Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            font=('Segoe UI', 9),
            bg='#1a2332',
            fg='#ccddee',
            selectbackground='#81c784',
            selectforeground='#0a0e17',
            relief=tk.FLAT,
            height=6
        )
        self.software_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.software_listbox.yview)
        
        action_frame = tk.Frame(software_frame, bg='#0a0e17')
        action_frame.pack(fill=tk.X, padx=5, pady=(0, 5))
        
        Button(action_frame, text="🗑️ Uninstall Selected", command=self.uninstall_software,
              bg='#ef5350', fg='#ffffff', font=('Segoe UI', 9),
              relief=tk.FLAT, cursor='hand2', padx=15).pack(side=tk.LEFT, padx=5)
    
    def create_diagnostics_section(self, parent):
        diag_frame = tk.LabelFrame(
            parent,
            text="🔍 System Diagnostics",
            bg='#0a0e17',
            fg='#ffffff',
            font=('Segoe UI', 11, 'bold'),
            relief=tk.FLAT
        )
        diag_frame.pack(fill=tk.X, pady=(0, 10))
        
        diag_inner = tk.Frame(diag_frame, bg='#0a0e17')
        diag_inner.pack(fill=tk.X, padx=5, pady=5)
        
        self.diag_text = tk.Text(
            diag_inner,
            height=4,
            font=('Consolas', 9),
            bg='#1a2332',
            fg='#ccddee',
            relief=tk.FLAT,
            wrap=tk.WORD
        )
        self.diag_text.pack(fill=tk.BOTH, expand=True)
        
        Button(diag_frame, text="🔄 Run Diagnostics", command=self.check_system_health,
              bg='#1a2332', fg='#4fc3f7', font=('Segoe UI', 9),
              relief=tk.FLAT, cursor='hand2', padx=15).pack(pady=(0, 5))
    
    def create_log_section(self, parent):
        log_frame = tk.LabelFrame(
            parent,
            text="📋 Activity Log",
            bg='#0a0e17',
            fg='#ffffff',
            font=('Segoe UI', 10, 'bold'),
            relief=tk.FLAT
        )
        log_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            height=4,
            font=('Consolas', 9),
            bg='#1a2332',
            fg='#ccddee',
            relief=tk.FLAT,
            wrap=tk.WORD
        )
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Configure tags
        self.log_text.tag_config('info', foreground='#4fc3f7')
        self.log_text.tag_config('success', foreground='#81c784')
        self.log_text.tag_config('warning', foreground='#ffb74d')
        self.log_text.tag_config('error', foreground='#ef5350')
        
        self.log("🚀 System Cleaner Pro initialized", 'info')
        self.log("💡 Select cleanup options and click 'Scan' to begin", 'info')
    
    def create_modern_button(self, parent, text, command, color, hover_color, state=tk.NORMAL):
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg='#ffffff',
            font=('Segoe UI', 11, 'bold'),
            padx=20,
            pady=8,
            relief=tk.FLAT,
            cursor='hand2',
            state=state
        )
        
        def on_enter(e):
            btn.configure(bg=hover_color)
        def on_leave(e):
            btn.configure(bg=color)
        
        btn.bind('<Enter>', on_enter)
        btn.bind('<Leave>', on_leave)
        
        return btn
    
    def apply_modern_style(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background='#0a0e17', foreground='#ffffff')
        style.configure('TFrame', background='#0a0e17')
        style.configure('TLabelframe', background='#0a0e17', foreground='#ffffff')
    
    def log(self, message, tag='info'):
        """Add message to log with timestamp"""
        try:
            if hasattr(self, 'log_text') and self.log_text:
                timestamp = datetime.now().strftime('%H:%M:%S')
                self.log_text.insert(tk.END, f"[{timestamp}] {message}\n", tag)
                self.log_text.see(tk.END)
                self.root.update_idletasks()
        except:
            # Fallback to print if log_text not available
            print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")
    
    def update_free_space(self):
        try:
            for partition in psutil.disk_partitions():
                if 'C:' in partition.mountpoint:
                    usage = psutil.disk_usage(partition.mountpoint)
                    free_gb = usage.free / (1024**3)
                    if len(self.stat_cards) > 3:
                        self.stat_cards[3].configure(text=f"{free_gb:.1f} GB")
                    break
        except:
            pass
    
    def update_stats(self):
        try:
            total = len(self.files_found)
            size = sum(f.get('size', 0) for f in self.files_found)
            selected = len(self.selected_files)
            
            if len(self.stat_cards) > 0:
                self.stat_cards[0].configure(text=str(total))
            if len(self.stat_cards) > 1:
                self.stat_cards[1].configure(text=f"{size:.1f} MB")
            if len(self.stat_cards) > 2:
                self.stat_cards[2].configure(text=str(selected))
            self.update_free_space()
        except:
            pass
    
    def load_system_info(self):
        """Load system information into the info panel"""
        try:
            info = SystemDiagnostics.get_system_info()
            if hasattr(self, 'info_text') and self.info_text:
                self.info_text.delete(1.0, tk.END)
                for key, value in info.items():
                    self.info_text.insert(tk.END, f"{key}: ", 'info')
                    self.info_text.insert(tk.END, f"{value}\n", 'success')
        except:
            pass
    
    def load_software_list(self):
        """Load installed software list"""
        try:
            if not hasattr(self, 'software_listbox') or not self.software_listbox:
                return
                
            self.software_listbox.delete(0, tk.END)
            self.software_list = SoftwareManager.get_installed_software()
            
            if self.software_list:
                for sw in self.software_list[:200]:
                    display = f"{sw['name']}"
                    if sw['version']:
                        display += f" (v{sw['version']})"
                    self.software_listbox.insert(tk.END, display)
                self.log(f"✅ Loaded {len(self.software_list)} installed applications", 'success')
            else:
                self.software_listbox.insert(tk.END, "No software found or insufficient permissions")
                self.log("⚠️ No software found. Try running as administrator.", 'warning')
        except Exception as e:
            self.log(f"❌ Error loading software list: {str(e)}", 'error')
    
    def filter_software(self, event=None):
        """Filter software list based on search"""
        try:
            if not hasattr(self, 'software_listbox') or not self.software_listbox:
                return
                
            search_term = self.search_entry.get().lower()
            self.software_listbox.delete(0, tk.END)
            
            if not self.software_list:
                self.software_listbox.insert(tk.END, "No software found")
                return
                
            for sw in self.software_list:
                if search_term in sw['name'].lower():
                    display = f"{sw['name']}"
                    if sw['version']:
                        display += f" (v{sw['version']})"
                    self.software_listbox.insert(tk.END, display)
                    
            if self.software_listbox.size() == 0:
                self.software_listbox.insert(tk.END, "No matching software found")
        except:
            pass
    
    def uninstall_software(self):
        """Uninstall selected software"""
        try:
            if not hasattr(self, 'software_listbox') or not self.software_listbox:
                return
                
            selection = self.software_listbox.curselection()
            if not selection:
                messagebox.showwarning("No Selection", "Please select a software to uninstall")
                return
            
            idx = selection[0]
            if idx < len(self.software_list):
                sw = self.software_list[idx]
                
                response = messagebox.askyesno(
                    "⚠️ Confirm Uninstall",
                    f"This will uninstall:\n\n{sw['name']}\n\n"
                    "Are you sure you want to continue?",
                    icon='warning'
                )
                
                if response:
                    self.log(f"🗑️ Uninstalling: {sw['name']}", 'warning')
                    success, message = SoftwareManager.uninstall_software(sw['name'])
                    if success:
                        self.log(f"✅ {message}", 'success')
                        messagebox.showinfo("Success", f"Uninstaller launched for {sw['name']}")
                    else:
                        self.log(f"❌ {message}", 'error')
                        messagebox.showerror("Error", f"Could not uninstall {sw['name']}")
                    
                    self.load_software_list()
        except Exception as e:
            self.log(f"❌ Error during uninstall: {str(e)}", 'error')
    
    def check_system_health(self):
        """Run system diagnostics"""
        try:
            self.log("🔍 Running system diagnostics...", 'info')
            if hasattr(self, 'diag_text') and self.diag_text:
                self.diag_text.delete(1.0, tk.END)
                
                issues = SystemDiagnostics.check_system_health()
                
                for issue in issues:
                    if '✅' in issue:
                        self.diag_text.insert(tk.END, f"{issue}\n", 'success')
                        self.log(issue, 'success')
                    else:
                        self.diag_text.insert(tk.END, f"{issue}\n", 'warning')
                        self.log(issue, 'warning')
                
                if not issues:
                    self.diag_text.insert(tk.END, "✅ No issues detected!\n", 'success')
                
                if hasattr(self, 'status_indicator'):
                    if any('⚠️' in issue for issue in issues):
                        self.status_indicator.configure(text="🟡 Issues Detected", fg='#ffb74d')
                    else:
                        self.status_indicator.configure(text="🟢 System Healthy", fg='#81c784')
        except Exception as e:
            self.log(f"❌ Error running diagnostics: {str(e)}", 'error')
    
    def get_temp_paths(self):
        paths = []
        if self.clean_temp.get():
            temp = os.environ.get('TEMP', '')
            if temp:
                paths.append(('User Temp', temp))
            tmp = os.environ.get('TMP', '')
            if tmp and tmp != temp:
                paths.append(('User TMP', tmp))
        
        if self.clean_windows_temp.get():
            win_temp = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Temp')
            if os.path.exists(win_temp):
                paths.append(('Windows Temp', win_temp))
        
        if self.clean_prefetch.get():
            prefetch = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Prefetch')
            if os.path.exists(prefetch):
                paths.append(('Prefetch', prefetch))
        
        if self.clean_desktop.get():
            desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
            paths.append(('Desktop', desktop))
        
        if self.clean_recent.get():
            recent = os.path.join(os.environ['USERPROFILE'], 'Recent')
            if os.path.exists(recent):
                paths.append(('Recent Documents', recent))
            else:
                recent = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Recent')
                if os.path.exists(recent):
                    paths.append(('Recent Documents', recent))
        
        return paths
    
    def scan_files(self):
        if self.scanning:
            return
        
        self.scanning = True
        self.files_found = []
        self.selected_files = []
        
        self.file_listbox.delete(0, tk.END)
        self.scan_btn.configure(state=tk.DISABLED)
        self.clean_btn.configure(state=tk.DISABLED)
        self.cancel_btn.configure(state=tk.NORMAL)
        self.progress_var.set(0)
        self.status_label.configure(text="Scanning...", fg='#4fc3f7')
        
        self.log("=" * 50, 'info')
        self.log("🔍 Starting comprehensive scan...", 'info')
        
        thread = threading.Thread(target=self.scan_files_thread)
        thread.daemon = True
        thread.start()
    
    def scan_files_thread(self):
        try:
            paths = self.get_temp_paths()
            if not paths:
                self.root.after(0, lambda: self.log("⚠️ No scan locations selected!", 'warning'))
                self.root.after(0, self.scan_complete)
                return
            
            patterns = ['.tmp', '.temp', '.log', '.cache', '.bak', '~$', '.old', 
                       '.backup', '.chk', '.dmp', '.etl', '.evtx']
            total_paths = len(paths)
            
            for idx, (name, path) in enumerate(paths):
                if not self.scanning:
                    break
                
                self.log(f"📂 Scanning {name}: {path}", 'info')
                
                if os.path.exists(path):
                    try:
                        for root_dir, dirs, files in os.walk(path):
                            if not self.scanning:
                                break
                            for filename in files:
                                if filename.lower() in ['desktop.ini', 'thumbs.db']:
                                    continue
                                
                                should_delete = False
                                for pattern in patterns:
                                    if filename.lower().endswith(pattern) or pattern in filename.lower():
                                        should_delete = True
                                        break
                                
                                if not should_delete and any(x in filename.lower() for x in ['temp', 'tmp']):
                                    try:
                                        filepath = os.path.join(root_dir, filename)
                                        if time.time() - os.path.getctime(filepath) > 604800:
                                            should_delete = True
                                    except:
                                        pass
                                
                                if should_delete:
                                    try:
                                        filepath = os.path.join(root_dir, filename)
                                        file_size = os.path.getsize(filepath) / (1024 * 1024)
                                        
                                        if file_size < 0.001:
                                            continue
                                        
                                        self.files_found.append({
                                            'path': filepath,
                                            'name': filename,
                                            'size': file_size,
                                            'location': name
                                        })
                                        
                                        display_text = f"[{name}] {filename} ({file_size:.2f} MB)"
                                        self.root.after(0, lambda t=display_text: self.file_listbox.insert(tk.END, t))
                                        
                                    except:
                                        pass
                    except Exception as e:
                        self.log(f"⚠️ Error accessing {path}: {str(e)}", 'warning')
                
                self.root.after(0, lambda p=((idx+1)/total_paths)*100: self.progress_var.set(p))
                self.root.after(0, self.update_stats)
            
            # Check Recycle Bin
            if self.clean_recycle.get() and self.scanning:
                self.log("♻️ Checking Recycle Bin...", 'info')
                try:
                    recycle_size = 0
                    recycle_count = 0
                    for item in winshell.recycle_bin():
                        try:
                            if hasattr(item, 'size'):
                                size_mb = item.size / (1024 * 1024)
                                if size_mb > 0:
                                    recycle_size += size_mb
                                    recycle_count += 1
                        except:
                            pass
                    
                    if recycle_size > 0:
                        self.files_found.append({
                            'path': 'recycle_bin',
                            'name': f'Recycle Bin ({recycle_count} items)',
                            'size': recycle_size,
                            'location': 'Recycle Bin'
                        })
                        self.root.after(0, lambda: self.file_listbox.insert(
                            tk.END, f"[Recycle Bin] {recycle_count} items ({recycle_size:.2f} MB)"
                        ))
                        self.log(f"♻️ Found {recycle_count} items ({recycle_size:.1f} MB) in Recycle Bin", 'info')
                except Exception as e:
                    self.log(f"⚠️ Could not check Recycle Bin: {str(e)}", 'warning')
            
            self.root.after(0, self.scan_complete)
            
        except Exception as e:
            self.root.after(0, lambda: self.log(f"❌ Error: {str(e)}", 'error'))
            self.root.after(0, self.scan_complete)
    
    def scan_complete(self):
        self.scanning = False
        self.scan_btn.configure(state=tk.NORMAL)
        self.cancel_btn.configure(state=tk.DISABLED)
        self.progress_var.set(100)
        
        if self.files_found:
            self.clean_btn.configure(state=tk.NORMAL)
            total_size = sum(f['size'] for f in self.files_found)
            self.status_label.configure(
                text=f"✅ Found {len(self.files_found)} files ({total_size:.1f} MB)",
                fg='#81c784'
            )
            self.log(f"✅ Scan complete! Found {len(self.files_found)} files.", 'success')
            self.update_stats()
            self.select_all_files()
        else:
            self.clean_btn.configure(state=tk.DISABLED)
            self.status_label.configure(text="✅ No unnecessary files found!", fg='#81c784')
            self.log("🎉 No unnecessary files found! Your system is clean.", 'success')
    
    def on_file_select(self, event):
        try:
            selected = self.file_listbox.curselection()
            self.selected_files = []
            for idx in selected:
                if idx < len(self.files_found):
                    self.selected_files.append(self.files_found[idx])
            self.update_stats()
            
            if self.selected_files:
                self.clean_btn.configure(state=tk.NORMAL)
                total_size = sum(f['size'] for f in self.selected_files)
                self.status_label.configure(
                    text=f"✅ {len(self.selected_files)} files selected ({total_size:.1f} MB)",
                    fg='#81c784'
                )
            else:
                self.clean_btn.configure(state=tk.DISABLED)
                self.status_label.configure(text="No files selected", fg='#8899aa')
        except:
            pass
    
    def select_all_files(self):
        try:
            self.file_listbox.select_set(0, tk.END)
            self.selected_files = self.files_found.copy()
            self.update_stats()
            self.clean_btn.configure(state=tk.NORMAL)
            total_size = sum(f['size'] for f in self.selected_files)
            self.status_label.configure(
                text=f"✅ All {len(self.selected_files)} files selected ({total_size:.1f} MB)",
                fg='#81c784'
            )
        except:
            pass
    
    def deselect_all_files(self):
        try:
            self.file_listbox.selection_clear(0, tk.END)
            self.selected_files = []
            self.update_stats()
            self.clean_btn.configure(state=tk.DISABLED)
            self.status_label.configure(text="No files selected", fg='#8899aa')
        except:
            pass
    
    def clean_files(self):
        if self.cleaning or not self.selected_files:
            return
        
        total_size = sum(f['size'] for f in self.selected_files)
        response = messagebox.askyesno(
            "⚠️ Confirm Deletion",
            f"This will delete {len(self.selected_files)} files ({total_size:.1f} MB).\n\n"
            "Are you sure you want to continue?",
            icon='warning'
        )
        
        if not response:
            return
        
        self.cleaning = True
        self.clean_btn.configure(state=tk.DISABLED)
        self.scan_btn.configure(state=tk.DISABLED)
        self.cancel_btn.configure(state=tk.NORMAL)
        self.status_label.configure(text="🧹 Deleting files...", fg='#ffb74d')
        
        self.log("=" * 50, 'info')
        self.log("🧹 Starting deletion...", 'info')
        
        thread = threading.Thread(target=self.clean_files_thread)
        thread.daemon = True
        thread.start()
    
    def clean_files_thread(self):
        try:
            deleted = 0
            total = len(self.selected_files)
            
            for i, file_info in enumerate(self.selected_files):
                if not self.cleaning:
                    break
                
                try:
                    if file_info['path'] == 'recycle_bin':
                        try:
                            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                            deleted += 1
                            self.log(f"♻️ Emptied Recycle Bin", 'success')
                        except Exception as e:
                            self.log(f"⚠️ Could not empty Recycle Bin: {str(e)}", 'warning')
                    elif os.path.exists(file_info['path']):
                        try:
                            os.remove(file_info['path'])
                            deleted += 1
                            self.log(f"🗑️ Deleted: {file_info['name']}", 'success')
                        except PermissionError:
                            self.log(f"⚠️ Permission denied: {file_info['name']}", 'warning')
                        except Exception as e:
                            self.log(f"⚠️ Could not delete {file_info['name']}: {str(e)}", 'warning')
                except:
                    pass
                
                self.progress_var.set(((i + 1) / total) * 100)
                self.root.after(0, self.update_stats)
                time.sleep(0.01)
            
            self.root.after(0, lambda: self.clean_complete(deleted))
            
        except Exception as e:
            self.root.after(0, lambda: self.log(f"❌ Error: {str(e)}", 'error'))
            self.root.after(0, self.clean_complete)
    
    def clean_complete(self, deleted=0):
        self.cleaning = False
        
        for f in self.selected_files:
            if f in self.files_found:
                self.files_found.remove(f)
        
        self.selected_files = []
        self.file_listbox.delete(0, tk.END)
        
        for f in self.files_found:
            self.file_listbox.insert(tk.END, f"[{f['location']}] {f['name']} ({f['size']:.2f} MB)")
        
        self.scan_btn.configure(state=tk.NORMAL)
        self.clean_btn.configure(state=tk.DISABLED if not self.files_found else tk.NORMAL)
        self.cancel_btn.configure(state=tk.DISABLED)
        self.progress_var.set(0)
        
        if deleted > 0:
            self.status_label.configure(text=f"✅ Deleted {deleted} files!", fg='#81c784')
            self.log(f"🎉 Deleted {deleted} files successfully!", 'success')
            self.update_stats()
            self.update_free_space()
            
            messagebox.showinfo(
                "✅ Cleanup Complete",
                f"🧹 Deleted {deleted} files successfully!\n\n"
                f"💾 Freed up space on your system."
            )
        else:
            self.status_label.configure(text="❌ No files were deleted", fg='#ef5350')
            self.log("ℹ️ No files were deleted.", 'info')
    
    def cancel_operation(self):
        if self.scanning:
            self.scanning = False
            self.log("⏹️ Scan cancelled", 'warning')
            self.status_label.configure(text="⏹️ Scan cancelled", fg='#ef5350')
            self.scan_btn.configure(state=tk.NORMAL)
            self.cancel_btn.configure(state=tk.DISABLED)
            self.progress_var.set(0)
        
        if self.cleaning:
            self.cleaning = False
            self.log("⏹️ Deletion cancelled", 'warning')
            self.status_label.configure(text="⏹️ Deletion cancelled", fg='#ef5350')
            self.clean_btn.configure(state=tk.NORMAL)
            self.scan_btn.configure(state=tk.NORMAL)
            self.cancel_btn.configure(state=tk.DISABLED)
            self.progress_var.set(0)

# ==================== MAIN ====================
def main():
    root = tk.Tk()
    
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
    
    root.configure(bg='#0a0e17')
    app = ModernCleanerApp(root)
    
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    root.minsize(1200, 800)
    
    root.mainloop()

if __name__ == "__main__":
    required_packages = ['psutil', 'winshell']
    missing = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"⚠️ Installing required packages: {', '.join(missing)}")
        for package in missing:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print("✅ Packages installed! Restarting...")
        os.execv(sys.executable, [sys.executable] + sys.argv)
    
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        if not is_admin:
            print("⚠️ Running without administrator privileges. Some features may be limited.")
            print("   Right-click and select 'Run as administrator' for full functionality.")
    except:
        pass
    
    main()