from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QToolBar, QAction, QMessageBox,
    QTabWidget, QWidget, QVBoxLayout
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl, QSize
import sys, os

# -------------------------
# History
HISTORY_FILE = "files_8/Practice_Set/history.txt"
os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w") as f:
        pass

def save_history(url):
    with open(HISTORY_FILE, "a") as f:
        f.write(url + "\n")

def show_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return f.read().splitlines()
    except:
        return []

def delete_history():
    with open(HISTORY_FILE, "w") as f:
        pass

# -------------------------
# Browser Tab
class BrowserTab(QWidget):
    def __init__(self, url="https://www.google.com"):
        super().__init__()
        self.layout = QVBoxLayout()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)

        # Fullscreen support
        self.browser.page().fullScreenRequested.connect(self.handle_fullscreen)

    def handle_fullscreen(self, request):
        request.accept()
        if request.toggleOn():
            self.showFullScreen()
        else:
            self.showNormal()

# -------------------------
# Main Window
class MiniBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Opera Browser")
        self.setGeometry(100, 100, 1200, 800)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        # Open first tab
        self.add_new_tab("https://www.google.com", "New Tab")

        # Navigation toolbar
        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(30, 30))
        self.addToolBar(navtb)

        # Back
        back_btn = QAction(QIcon.fromTheme("go-previous"), "Back", self)
        back_btn.triggered.connect(lambda: self.current_browser().back())
        navtb.addAction(back_btn)

        # Forward
        forward_btn = QAction(QIcon.fromTheme("go-next"), "Forward", self)
        forward_btn.triggered.connect(lambda: self.current_browser().forward())
        navtb.addAction(forward_btn)

        # Reload
        reload_btn = QAction(QIcon.fromTheme("view-refresh"), "Reload", self)
        reload_btn.triggered.connect(lambda: self.current_browser().reload())
        navtb.addAction(reload_btn)

        # Address bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.url_bar)

        # New Tab
        new_tab_btn = QAction(QIcon.fromTheme("tab-new"), "New Tab", self)
        new_tab_btn.triggered.connect(lambda: self.add_new_tab())
        navtb.addAction(new_tab_btn)

        # History
        history_btn = QAction(QIcon.fromTheme("document-open-recent"), "History", self)
        history_btn.triggered.connect(self.display_history)
        navtb.addAction(history_btn)

        # Delete history
        delete_btn = QAction(QIcon.fromTheme("edit-delete"), "Clear History", self)
        delete_btn.triggered.connect(delete_history)
        navtb.addAction(delete_btn)

        # Theme toggle
        theme_btn = QAction(QIcon.fromTheme("preferences-desktop-theme"), "Toggle Theme", self)
        theme_btn.triggered.connect(self.toggle_theme)
        navtb.addAction(theme_btn)

        self.dark_theme = False

        # Update URL when tab changes
        self.tabs.currentChanged.connect(self.update_url)
        self.current_browser().urlChanged.connect(self.update_url)

    # -------------------------
    def current_browser(self):
        return self.tabs.currentWidget().browser

    def add_new_tab(self, url="https://www.google.com", label="New Tab"):
        new_tab = BrowserTab(url)
        index = self.tabs.addTab(new_tab, label)
        self.tabs.setCurrentIndex(index)
        new_tab.browser.urlChanged.connect(lambda q, tab=new_tab: self.update_tab_url(tab, q))

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if "." not in url:
            # Treat as search
            url = "https://www.google.com/search?q=" + url.replace(" ", "+")
        elif not url.startswith("http"):
            url = "http://" + url
        self.current_browser().setUrl(QUrl(url))

    def update_url(self, _=None):
        url = self.current_browser().url().toString()
        self.url_bar.setText(url)
        save_history(url)

    def update_tab_url(self, tab, q):
        index = self.tabs.indexOf(tab)
        self.tabs.setTabText(index, tab.browser.title()[:15])
        save_history(q.toString())

    def display_history(self):
        hist = show_history()
        if hist:
            QMessageBox.information(self, "History", "\n".join(hist[-20:]))
        else:
            QMessageBox.information(self, "History", "No history found!")

    def toggle_theme(self):
        if self.dark_theme:
            self.setStyleSheet("")
            self.dark_theme = False
        else:
            self.setStyleSheet(
                "QMainWindow {background-color: #2b2b2b; color: white;} "
                "QLineEdit {background-color: #3b3b3b; color: white;} "
                "QToolBar {background-color: #3b3b3b;}"
            )
            self.dark_theme = True

# -------------------------
app = QApplication(sys.argv)
window = MiniBrowser()
window.show()
sys.exit(app.exec_())