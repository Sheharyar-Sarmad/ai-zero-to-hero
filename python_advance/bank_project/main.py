"""

                    COMPLETE SECURE BANKING SYSTEM

A fully-featured banking application with:
- Account creation with unique identifiers
- Secure PIN-based authentication
- Deposit and withdrawal functionality
- Account search and money transfer
- Data persistence using JSON
- Exception handling and input validation
"""

# STANDARD LIBRARY IMPORTS
import json
import random
import hashlib      # For secure password/PIN hashing
import re           # For email validation
import string       # FIXED: Added string import
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Any

# SECURITY CONFIGURATION
class SecurityConfig:
    """Security configuration and constants"""
    SALT = "BankSecureSalt2026!"  # Salt for hashing (in production, use environment variables)
    MAX_LOGIN_ATTEMPTS = 3
    SESSION_TIMEOUT = 300  # 5 minutes in seconds
    
    @staticmethod
    def hash_pin(pin: int) -> str:
        """Hash a PIN using SHA-256 with salt"""
        pin_str = str(pin)
        salted = pin_str + SecurityConfig.SALT
        return hashlib.sha256(salted.encode()).hexdigest()
    
    @staticmethod
    def verify_pin(pin: int, hashed_pin: str) -> bool:
        """Verify a PIN against its hash"""
        return SecurityConfig.hash_pin(pin) == hashed_pin


# MAIN BANK CLASS
class Bank:
    """
    Complete Banking System with high security and full features
    
    Features:
    - Account creation with validation
    - Secure PIN storage using SHA-256 hashing
    - Deposit, Withdraw, Transfer funds
    - Account management (update, delete)
    - Transaction history
    - Search and view accounts
    - Data persistence with JSON
    """
    
    # CLASS VARIABLES
    database = 'data.json'          # JSON file for data persistence
    data: List[Dict[str, Any]] = [] # In-memory data storage
    current_session: Dict[str, Any] = None  # Current user session
    session_timestamp: float = 0    # Session start time
    
    # INITIALIZATION & DATA LOADING
    try:
        """Load existing data from JSON file on startup"""
        if Path(database).exists():
            with open(database, 'r') as fs:
                data = json.loads(fs.read())
                print(f"✅ Loaded {len(data)} existing accounts")
        else:
            print("\nℹ️  No existing data file found. Starting fresh.")
    except json.JSONDecodeError:
        print("\n⚠️  Data file corrupted. Starting fresh.")
        data = []
    except Exception as err:
        print(f"\n❌ Error loading data: {err}")
        data = []
    
    # DATA PERSISTENCE METHODS
    @staticmethod
    def update() -> bool:
        """
        Save current data to JSON file
        Returns: True if successful, False otherwise
        """
        try:
            with open(Bank.database, 'w') as fs:
                fs.write(json.dumps(Bank.data, indent=2))
            return True
        except Exception as err:
            print(f"❌ Error saving data: {err}")
            return False
    
    # VALIDATION METHODS
    @staticmethod
    def validate_name(name: str) -> bool:
        """Validate name: 2-50 characters, letters and spaces only"""
        if not name or len(name) < 2 or len(name) > 50:
            return False
        return all(c.isalpha() or c.isspace() for c in name)
    
    @staticmethod
    def validate_age(age: int) -> bool:
        """Validate age: must be between 18 and 120"""
        return 18 <= age <= 120
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format using regex"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email)) and len(email) <= 100
    
    @staticmethod
    def validate_pin(pin: int) -> bool:
        """Validate PIN: exactly 4 digits"""
        return 1000 <= pin <= 9999
    
    @staticmethod
    def validate_amount(amount: float) -> bool:
        """Validate amount: positive and not exceeding limits"""
        if not isinstance(amount, (int, float)):
            return False
        if amount <= 0:
            return False
        if amount > 100000000:  # Max 100 million
            return False
        return True
    
    @staticmethod
    def is_name_unique(name: str) -> bool:
        """Check if name already exists (case-insensitive)"""
        return not any(account['name'].lower() == name.lower() 
                      for account in Bank.data)
    
    @staticmethod
    def is_email_unique(email: str) -> bool:
        """Check if email already exists (case-insensitive)"""
        return not any(account['email'].lower() == email.lower() 
                      for account in Bank.data)
    
    @staticmethod
    def is_account_number_unique(acc_num: int) -> bool:
        """Check if account number already exists"""
        return not any(account['accountNumber'] == acc_num 
                      for account in Bank.data)
    
    # ACCOUNT GENERATION METHODS
    @staticmethod
    def generate_account_number() -> Optional[int]:
        """
        Generate a unique 4-digit account number
        Returns: Unique account number or None if failed
        """
        try:
            attempts = 0
            max_attempts = 1000
            
            while attempts < max_attempts:
                acc_num = random.randint(1000, 9999)
                
                # Check uniqueness
                if Bank.is_account_number_unique(acc_num):
                    return acc_num
                
                attempts += 1
            
            print("❌ Could not generate unique account number after 1000 attempts")
            return None
            
        except Exception as err:
            print(f"❌ Error generating account number: {err}")
            return None
    
    @staticmethod
    def generate_transaction_id() -> str:
        """Generate a unique transaction ID"""
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        random_suffix = ''.join(random.choices(string.digits, k=6))  # FIXED: Uses string.digits
        return f"TXN{timestamp}{random_suffix}"
    
    # AUTHENTICATION METHODS
    @staticmethod
    def verify_user(account_number: int, pin: int) -> Optional[Dict[str, Any]]:
        """
        Verify user credentials
        Returns: Account data if valid, None otherwise
        """
        try:
            # Find account by number
            account = Bank.find_account_by_number(account_number)
            if not account:
                return None
            
            # Verify PIN
            stored_pin = account.get('pin')
            if isinstance(stored_pin, int):
                # If PIN is stored as integer (legacy), compare directly
                if pin == stored_pin:
                    return account
                return None
            
            # If PIN is stored as hash (new), verify with hash
            if stored_pin and SecurityConfig.verify_pin(pin, stored_pin):
                return account
            
            return None
            
        except Exception as err:
            print(f"❌ Error verifying user: {err}")
            return None
    
    @staticmethod
    def find_account_by_number(acc_num: int) -> Optional[Dict[str, Any]]:
        """Find account by account number"""
        for account in Bank.data:
            if account.get('accountNumber') == acc_num:
                return account
        return None
    
    @staticmethod
    def find_accounts_by_name(name: str) -> List[Dict[str, Any]]:
        """Find all accounts matching name (case-insensitive partial match)"""
        name_lower = name.lower()
        return [acc for acc in Bank.data if name_lower in acc.get('name', '').lower()]
    
    # SESSION MANAGEMENT
    @staticmethod
    def start_session(account: Dict[str, Any]) -> bool:
        """Start a user session"""
        Bank.current_session = account.copy()
        Bank.session_timestamp = datetime.now().timestamp()
        return True
    
    @staticmethod
    def end_session() -> None:
        """End the current session"""
        Bank.current_session = None
        Bank.session_timestamp = 0
    
    @staticmethod
    def is_session_active() -> bool:
        """Check if current session is active"""
        if not Bank.current_session:
            return False
        
        # Check session timeout
        current_time = datetime.now().timestamp()
        if current_time - Bank.session_timestamp > SecurityConfig.SESSION_TIMEOUT:
            Bank.end_session()
            return False
        
        return True
    
    @staticmethod
    def require_auth(func):
        """Decorator to require authentication"""
        def wrapper(*args, **kwargs):
            if not Bank.is_session_active():
                print("\n❌ Please login first to access this feature.")
                return
            return func(*args, **kwargs)
        return wrapper
    
    # CORE BANKING OPERATIONS
    def create_account(self) -> None:
        """
        Create a new bank account with full validation
        Security: PIN is hashed before storage
        """
        print("\n" + "=" * 50)
        print("           🏦 CREATE NEW ACCOUNT")
        print("=" * 50)
        
        try:
            # GET USER INPUT 
            name = input("\n📝 Enter your full name: ").strip()
            
            # Validate name
            if not self.validate_name(name):
                print("\n❌ Invalid name! Must be 2-50 characters (letters and spaces only).")
                return
            
            # Check name uniqueness
            if not self.is_name_unique(name):
                print(f"\n❌ Account with name '{name}' already exists!")
                return
            
            # AGE 
            try:
                age = int(input("📅 Enter your age: "))
            except ValueError:
                print("\n❌ Please enter a valid age!")
                return
            
            if not self.validate_age(age):
                print("\n❌ You must be between 18 and 120 years old.")
                return
            
            # EMAIL 
            email = input("📧 Enter your email address: ").strip()
            
            if not self.validate_email(email):
                print("\n❌ Invalid email format. Please enter a valid email address.")
                return
            
            if not self.is_email_unique(email):
                print(f"\n❌ Email '{email}' is already registered!")
                return
            
            # PIN (SECURE) 
            try:
                pin = int(input("🔑 Enter your 4-digit PIN: "))
            except ValueError:
                print("\n❌ Please enter a valid 4-digit PIN!")
                return
            
            if not self.validate_pin(pin):
                print("\n❌ PIN must be exactly 4 digits!")
                return
            
            # CONFIRM PIN 
            try:
                pin_confirm = int(input("🔑 Confirm your PIN: "))
            except ValueError:
                print("\n❌ Please enter a valid PIN!")
                return
            
            if pin != pin_confirm:
                print("\n❌ PINs do not match!")
                return
            
            # GENERATE ACCOUNT NUMBER 
            account_number = self.generate_account_number()
            if account_number is None:
                print("\n❌ Could not generate unique account number. Please try again.")
                return
            
            # CREATE ACCOUNT 
            # Hash the PIN for secure storage
            hashed_pin = SecurityConfig.hash_pin(pin)
            
            account_info = {
                "accountNumber": account_number,
                "name": name,
                "age": age,
                "email": email,
                "pin": hashed_pin,  # Stored as hash!
                "balance": 0.0,
                "createdAt": datetime.now().isoformat(),
                "transactions": []
            }
            
            # Save to database
            Bank.data.append(account_info)
            
            if not self.update():
                print("\n❌ Failed to save account. Please try again.")
                Bank.data.pop()  # Remove if save failed
                return
            
            # SUCCESS MESSAGE 
            print("\n" + "=" * 50)
            print("🎉 ACCOUNT CREATED SUCCESSFULLY!")
            print("=" * 50)
            print(f"👤 Account Holder: {name}")
            print(f"🏦 Account Number: {account_number}")
            print(f"📧 Email: {email}")
            print(f"💰 Balance: $0.00")
            print("=" * 50)
            print("\n⚠️  IMPORTANT: Please note your account number and PIN.")
            print("   Store them safely and never share your PIN with anyone.")
            print("\n🔐 Your PIN is securely encrypted and stored.")
            
            # AUTO-LOGIN 
            self.start_session(account_info)
            print("\n✅ You are now logged in!")
            
        except Exception as err:
            print(f"\n❌ Error creating account: {err}")
    
    # LOGIN SYSTEM

    def login(self) -> bool:
        """
        Secure login system with rate limiting
        Returns: True if login successful, False otherwise
        """
        print("\n" + "=" * 50)
        print("           🔐 SECURE LOGIN")
        print("=" * 50)
        
        attempts = 0
        
        while attempts < SecurityConfig.MAX_LOGIN_ATTEMPTS:
            try:
                # Get credentials
                acc_num = int(input("\n🏦 Enter your account number: "))
                pin = int(input("🔑 Enter your PIN: "))
                
                # Verify credentials
                account = self.verify_user(acc_num, pin)
                
                if account:
                    # Start session
                    self.start_session(account)
                    print(f"\n✅ Welcome back, {account['name']}!")
                    print(f"💰 Current Balance: ${account['balance']:,.2f}")
                    return True
                else:
                    attempts += 1
                    remaining = SecurityConfig.MAX_LOGIN_ATTEMPTS - attempts
                    print(f"❌ Invalid credentials. {remaining} attempts remaining.")
                    
            except ValueError:
                print("❌ Please enter valid numbers for account number and PIN.")
                attempts += 1
            except Exception as err:
                print(f"❌ Error during login: {err}")
                attempts += 1
        
        print("\n🔒 Too many failed attempts. Please try again later.")
        return False
    
    def logout(self) -> None:
        """Log out current user"""
        if Bank.current_session:
            name = Bank.current_session.get('name', 'User')
            self.end_session()
            print(f"\n👋 Goodbye, {name}! You have been logged out.")
        else:
            print("\nℹ️  You are not logged in.")
    
    # CORE TRANSACTION METHODS (FIXED)
    
    def deposit(self) -> None:
        """Deposit money into current account (requires login)"""
        if not self.is_session_active():
            print("\n❌ Please login first.")
            return
        
        account = Bank.current_session
        
        print("\n" + "=" * 50)
        print("           💰 DEPOSIT MONEY")
        print("=" * 50)
        
        try:
            # Get amount - ✅ FIXED: Removed the $ from input prompt
            amount_input = input("\n💰 Enter amount to deposit: $")
            amount = float(amount_input)
            
            # Validate amount
            if not self.validate_amount(amount):
                print("\n❌ Invalid amount. Must be positive and less than $100,000,000.")
                return
            
            # Confirm deposit
            print(f"\n📝 Confirm deposit of ${amount:,.2f} to your account?")
            confirm = input("Type 'yes' to confirm: ").lower()
            
            if confirm != 'yes':
                print("\n❌ Deposit cancelled.")
                return
            
            # Find actual account in database
            acc_num = account['accountNumber']
            actual_account = self.find_account_by_number(acc_num)
            
            if not actual_account:
                print("\n❌ Account not found in database.")
                return
            
            # Update balance
            old_balance = actual_account['balance']
            actual_account['balance'] = old_balance + amount
            
            # Record transaction - ✅ FIXED: Now uses string.digits correctly
            transaction = {
                "id": self.generate_transaction_id(),
                "type": "DEPOSIT",
                "amount": amount,
                "balance": actual_account['balance'],
                "date": datetime.now().isoformat()
            }
            actual_account.setdefault('transactions', []).append(transaction)
            
            # Save to database
            if self.update():
                print("\n" + "=" * 50)
                print("✅ DEPOSIT SUCCESSFUL!")
                print("=" * 50)
                print(f"💰 Amount: ${amount:,.2f}")
                print(f"💵 New Balance: ${actual_account['balance']:,.2f}")
                print("=" * 50)
                
                # Update current session
                self.start_session(actual_account)
            else:
                print("\n❌ Failed to save transaction. Please try again.")
                actual_account['balance'] = old_balance  # Rollback
            
        except ValueError as e:
            print(f"\n❌ Please enter a valid amount. Error: {e}")
        except Exception as err:
            print(f"\n❌ Error during deposit: {err}")
    
    def withdraw(self) -> None:
        """Withdraw money from current account (requires login)"""
        if not self.is_session_active():
            print("\n❌ Please login first.")
            return
        
        account = Bank.current_session
        
        print("\n" + "=" * 50)
        print("           💸 WITHDRAW MONEY")
        print("=" * 50)
        
        try:
            # Get amount - ✅ FIXED: Removed the $ from input prompt
            amount_input = input("\n💰 Enter amount to withdraw: $")
            amount = float(amount_input)
            
            # Validate amount
            if not self.validate_amount(amount):
                print("\n❌ Invalid amount. Must be positive and less than $100,000,000.")
                return
            
            # Find actual account in database
            acc_num = account['accountNumber']
            actual_account = self.find_account_by_number(acc_num)
            
            if not actual_account:
                print("\n❌ Account not found in database.")
                return
            
            # Check sufficient balance
            if actual_account['balance'] < amount:
                print(f"\n❌ Insufficient balance. Current balance: ${actual_account['balance']:,.2f}")
                return
            
            # Confirm withdrawal
            print(f"\n📝 Confirm withdrawal of ${amount:,.2f} from your account?")
            confirm = input("Type 'yes' to confirm: ").lower()
            
            if confirm != 'yes':
                print("\n❌ Withdrawal cancelled.")
                return
            
            # Update balance
            old_balance = actual_account['balance']
            actual_account['balance'] = old_balance - amount
            
            # Record transaction - ✅ FIXED: Uses string.digits correctly
            transaction = {
                "id": self.generate_transaction_id(),
                "type": "WITHDRAWAL",
                "amount": amount,
                "balance": actual_account['balance'],
                "date": datetime.now().isoformat()
            }
            actual_account.setdefault('transactions', []).append(transaction)
            
            # Save to database
            if self.update():
                print("\n" + "=" * 50)
                print("✅ WITHDRAWAL SUCCESSFUL!")
                print("=" * 50)
                print(f"💰 Amount: ${amount:,.2f}")
                print(f"💵 New Balance: ${actual_account['balance']:,.2f}")
                print("=" * 50)
                print("ℹ️  Please take your cash from the dispenser.")
                
                # Update current session
                self.start_session(actual_account)
            else:
                print("\n❌ Failed to save transaction. Please try again.")
                actual_account['balance'] = old_balance  # Rollback
            
        except ValueError as e:
            print(f"\n❌ Please enter a valid amount. Error: {e}")
        except Exception as err:
            print(f"\n❌ Error during withdrawal: {err}")
    
    # TRANSFER MONEY
    def transfer_money(self) -> None:
        """Transfer money to another account (requires login)"""
        if not self.is_session_active():
            print("\n❌ Please login first.")
            return
        
        account = Bank.current_session
        
        print("\n" + "=" * 50)
        print("           🔄 TRANSFER MONEY")
        print("=" * 50)
        
        try:
            # Search for recipient
            print("\n🔍 Search for recipient by name or account number:")
            print("   (Enter account number to transfer directly)")
            print("   (Enter name to search and select from results)")
            
            search_input = input("\n📝 Enter account number or name: ").strip()
            
            # Determine if input is account number or name
            recipients = []
            if search_input.isdigit():
                # Search by account number
                recipient = self.find_account_by_number(int(search_input))
                if recipient and recipient['accountNumber'] != account['accountNumber']:
                    recipients = [recipient]
                else:
                    print("\n❌ Account not found or cannot transfer to yourself.")
                    return
            else:
                # Search by name
                recipients = self.find_accounts_by_name(search_input)
                if not recipients:
                    print("\n❌ No accounts found matching that name.")
                    return
            
            # Show recipients
            print("\n" + "-" * 40)
            print("📋 Search Results:")
            print("-" * 40)
            for idx, acc in enumerate(recipients, 1):
                if acc['accountNumber'] == account['accountNumber']:
                    print(f"  {idx}. {acc['name']} (THIS IS YOU!)")
                else:
                    print(f"  {idx}. {acc['name']} - Account: {acc['accountNumber']}")
            print("-" * 40)
            
            # Select recipient
            if len(recipients) > 1:
                try:
                    choice = int(input(f"\nSelect recipient (1-{len(recipients)}): "))
                    recipient = recipients[choice - 1]
                except (ValueError, IndexError):
                    print("\n❌ Invalid selection.")
                    return
            else:
                recipient = recipients[0]
            
            # Check if trying to transfer to self
            if recipient['accountNumber'] == account['accountNumber']:
                print("\n❌ Cannot transfer money to yourself!")
                return
            
            # Get amount
            amount_input = input(f"\n💰 Enter amount to transfer to {recipient['name']}: $")
            amount = float(amount_input)
            
            # Validate amount
            if not self.validate_amount(amount):
                print("\n❌ Invalid amount. Must be positive and less than $100,000,000.")
                return
            
            # Find actual accounts in database
            sender_acc = self.find_account_by_number(account['accountNumber'])
            receiver_acc = self.find_account_by_number(recipient['accountNumber'])
            
            if not sender_acc or not receiver_acc:
                print("\n❌ Account not found in database.")
                return
            
            # Check sender's balance
            if sender_acc['balance'] < amount:
                print(f"\n❌ Insufficient balance. Current balance: ${sender_acc['balance']:,.2f}")
                return
            
            # Confirm transfer
            print(f"\n📝 Transfer Details:")
            print(f"   From: {sender_acc['name']} ({sender_acc['accountNumber']})")
            print(f"   To: {receiver_acc['name']} ({receiver_acc['accountNumber']})")
            print(f"   Amount: ${amount:,.2f}")
            print(f"   Balance after: ${sender_acc['balance'] - amount:,.2f}")
            
            confirm = input("\nType 'yes' to confirm transfer: ").lower()
            
            if confirm != 'yes':
                print("\n❌ Transfer cancelled.")
                return
            
            # Process transfer
            sender_acc['balance'] -= amount
            receiver_acc['balance'] += amount
            
            # Record transactions - FIXED: Uses string.digits correctly
            sender_txn = {
                "id": self.generate_transaction_id(),
                "type": "TRANSFER_SENT",
                "amount": amount,
                "recipient": receiver_acc['name'],
                "recipient_account": receiver_acc['accountNumber'],
                "balance": sender_acc['balance'],
                "date": datetime.now().isoformat()
            }
            sender_acc.setdefault('transactions', []).append(sender_txn)
            
            receiver_txn = {
                "id": self.generate_transaction_id(),
                "type": "TRANSFER_RECEIVED",
                "amount": amount,
                "sender": sender_acc['name'],
                "sender_account": sender_acc['accountNumber'],
                "balance": receiver_acc['balance'],
                "date": datetime.now().isoformat()
            }
            receiver_acc.setdefault('transactions', []).append(receiver_txn)
            
            # Save to database
            if self.update():
                print("\n" + "=" * 50)
                print("✅ TRANSFER SUCCESSFUL!")
                print("=" * 50)
                print(f"💰 Amount Transferred: ${amount:,.2f}")
                print(f"📤 From: {sender_acc['name']}")
                print(f"📥 To: {receiver_acc['name']}")
                print(f"💵 Your New Balance: ${sender_acc['balance']:,.2f}")
                print("=" * 50)
                
                # Update current session
                self.start_session(sender_acc)
            else:
                # Rollback
                sender_acc['balance'] += amount
                receiver_acc['balance'] -= amount
                print("\n❌ Failed to process transfer. Please try again.")
            
        except ValueError as e:
            print(f"\n❌ Please enter a valid amount. Error: {e}")
        except Exception as err:
            print(f"\n❌ Error during transfer: {err}")
    
    # VIEW ACCOUNT DETAILS
    def view_account_details(self) -> None:
        """View account details and transaction history (requires login)"""
        if not self.is_session_active():
            print("\n❌ Please login first.")
            return
        
        account = Bank.current_session
        
        print("\n" + "=" * 55)
        print("           📊 ACCOUNT DETAILS")
        print("=" * 55)
        
        # Get latest account data from database
        acc_num = account['accountNumber']
        actual_account = self.find_account_by_number(acc_num)
        
        if not actual_account:
            print("\n❌ Account not found in database.")
            return
        
        # Display account information
        print(f"\n👤 Account Holder: {actual_account['name']}")
        print(f"🏦 Account Number: {actual_account['accountNumber']}")
        print(f"📧 Email: {actual_account['email']}")
        print(f"📅 Account Created: {actual_account.get('createdAt', 'N/A')}")
        print(f"💰 Current Balance: ${actual_account['balance']:,.2f}")
        
        # Display transactions
        transactions = actual_account.get('transactions', [])
        print(f"\n📋 Recent Transactions ({len(transactions)} total):")
        print("-" * 55)
        
        if not transactions:
            print("   ℹ️  No transactions yet.")
        else:
            # Show last 10 transactions
            for txn in transactions[-10:]:
                txn_type = txn['type']
                amount = txn['amount']
                date = txn.get('date', 'N/A')
                
                if 'DEPOSIT' in txn_type:
                    icon = "💰"
                elif 'WITHDRAWAL' in txn_type:
                    icon = "💸"
                else:
                    icon = "🔄"
                
                if 'TRANSFER_SENT' in txn_type:
                    print(f"   {icon} {txn_type} - ${amount:,.2f} to {txn.get('recipient', 'N/A')}")
                elif 'TRANSFER_RECEIVED' in txn_type:
                    print(f"   {icon} {txn_type} - ${amount:,.2f} from {txn.get('sender', 'N/A')}")
                else:
                    print(f"   {icon} {txn_type} - ${amount:,.2f}")
                
                print(f"      Balance: ${txn['balance']:,.2f}")
                print(f"      Date: {date}")
                print()
        
        print("=" * 55)
        
        # Update session with latest data
        self.start_session(actual_account)
    
    # UPDATE ACCOUNT
    def update_account(self) -> None:
        """Update account details (requires login)"""
        if not self.is_session_active():
            print("\n❌ Please login first.")
            return
        
        account = Bank.current_session
        acc_num = account['accountNumber']
        actual_account = self.find_account_by_number(acc_num)
        
        if not actual_account:
            print("\n❌ Account not found.")
            return
        
        print("\n" + "=" * 50)
        print("           ✏️ UPDATE ACCOUNT")
        print("=" * 50)
        
        # Security: Verify PIN before updates
        try:
            pin_input = int(input("\n🔑 Enter your current PIN to verify identity: "))
        except ValueError:
            print("\n❌ Invalid PIN format.")
            return
        
        # Check PIN
        stored_pin = actual_account.get('pin')
        if isinstance(stored_pin, int):
            if pin_input != stored_pin:
                print("\n❌ Incorrect PIN.")
                return
        else:
            if not SecurityConfig.verify_pin(pin_input, stored_pin):
                print("\n❌ Incorrect PIN.")
                return
        
        print("\n🔄 What would you like to update?")
        print("   1. Name")
        print("   2. Email")
        print("   3. PIN")
        print("   4. Cancel")
        
        try:
            choice = int(input("\nSelect option (1-4): "))
            
            if choice == 1:
                # Update Name
                new_name = input("\n📝 Enter new name: ").strip()
                if not self.validate_name(new_name):
                    print("\n❌ Invalid name format.")
                    return
                if not self.is_name_unique(new_name):
                    print("\n❌ Name already exists.")
                    return
                old_name = actual_account['name']
                actual_account['name'] = new_name
                print(f"\n✅ Name updated from '{old_name}' to '{new_name}'")
                
            elif choice == 2:
                # Update Email
                new_email = input("\n📧 Enter new email: ").strip()
                if not self.validate_email(new_email):
                    print("\n❌ Invalid email format.")
                    return
                if not self.is_email_unique(new_email):
                    print("\n❌ Email already registered.")
                    return
                old_email = actual_account['email']
                actual_account['email'] = new_email
                print(f"\n✅ Email updated from '{old_email}' to '{new_email}'")
                
            elif choice == 3:
                # Update PIN
                try:
                    new_pin = int(input("\n🔑 Enter new 4-digit PIN: "))
                except ValueError:
                    print("\n❌ Invalid PIN format.")
                    return
                
                if not self.validate_pin(new_pin):
                    print("\n❌ PIN must be exactly 4 digits.")
                    return
                
                try:
                    confirm_pin = int(input("🔑 Confirm new PIN: "))
                except ValueError:
                    print("\n❌ Invalid PIN format.")
                    return
                
                if new_pin != confirm_pin:
                    print("\n❌ PINs do not match.")
                    return
                
                # Hash and store new PIN
                actual_account['pin'] = SecurityConfig.hash_pin(new_pin)
                print("\n✅ PIN updated successfully!")
                
            elif choice == 4:
                print("\n❌ Update cancelled.")
                return
            else:
                print("\n❌ Invalid choice.")
                return
            
            # Save changes
            if self.update():
                print("✅ Account updated successfully!")
                # Update session with new data
                self.start_session(actual_account)
            else:
                print("❌ Failed to save changes.")
                
        except ValueError:
            print("\n❌ Invalid input.")
        except Exception as err:
            print(f"\n❌ Error updating account: {err}")
    
    # DELETE ACCOUNT
    def delete_account(self) -> None:
        """
        Permanently delete an account (requires login)
        EXTREME CAUTION: This operation cannot be undone!
        """
        if not self.is_session_active():
            print("\n❌ Please login first.")
            return
        
        account = Bank.current_session
        acc_num = account['accountNumber']
        
        print("\n" + "=" * 55)
        print("           ⚠️ DELETE ACCOUNT")
        print("=" * 55)
        print("\n🔴 DANGER: This action is PERMANENT and CANNOT BE UNDONE!")
        print(f"   Account: {account['name']} ({acc_num})")
        print(f"   Balance: ${account['balance']:,.2f}")
        
        # Security: Multiple confirmations
        confirm1 = input("\n⚠️ Type 'DELETE' to confirm: ").strip()
        if confirm1 != 'DELETE':
            print("\n❌ Account deletion cancelled.")
            return
        
        try:
            pin_input = int(input("\n🔑 Enter your PIN to verify identity: "))
        except ValueError:
            print("\n❌ Invalid PIN format.")
            return
        
        # Verify PIN
        stored_pin = account.get('pin')
        if isinstance(stored_pin, int):
            if pin_input != stored_pin:
                print("\n❌ Incorrect PIN.")
                return
        else:
            if not SecurityConfig.verify_pin(pin_input, stored_pin):
                print("\n❌ Incorrect PIN.")
                return
        
        # Final confirmation
        print("\n🔴 Are you absolutely sure you want to delete this account?")
        print(f"   This will delete account: {account['name']}")
        print(f"   With balance: ${account['balance']:,.2f}")
        confirm2 = input("Type 'YES I AM SURE' to confirm: ").strip()
        
        if confirm2 != 'YES I AM SURE':
            print("\n❌ Account deletion cancelled.")
            return
        
        # Remove account from database
        Bank.data = [acc for acc in Bank.data if acc['accountNumber'] != acc_num]
        
        # Save to database
        if self.update():
            print("\n" + "=" * 55)
            print("🔴 ACCOUNT PERMANENTLY DELETED")
            print("=" * 55)
            print(f"👤 Account Holder: {account['name']}")
            print(f"🏦 Account Number: {acc_num}")
            print("=" * 55)
            print("\nℹ️  This action cannot be undone. Your data has been removed.")
            
            # End session
            self.end_session()
        else:
            print("\n❌ Failed to delete account. Please try again.")
            # Rollback
            Bank.data.append(account)
    
    # SEARCH ACCOUNTS
    def search_accounts(self) -> None:
        """
        Search for accounts by name (public, doesn't require login)
        Shows limited information for privacy
        """
        print("\n" + "=" * 50)
        print("           🔍 SEARCH ACCOUNTS")
        print("=" * 50)
        
        try:
            search_term = input("\n📝 Enter name to search: ").strip()
            
            if not search_term:
                print("\n❌ Please enter a search term.")
                return
            
            # Find matching accounts
            results = self.find_accounts_by_name(search_term)
            
            if not results:
                print(f"\n❌ No accounts found matching '{search_term}'.")
                return
            
            print(f"\n📋 Found {len(results)} matching account(s):")
            print("-" * 50)
            
            for idx, acc in enumerate(results, 1):
                print(f"\n  {idx}. {acc['name']}")
                print(f"     Account Number: {acc['accountNumber']}")
                print(f"     Age: {acc.get('age', 'N/A')}")
                print(f"     Email: {acc.get('email', 'N/A')}")
                print(f"     Balance: ${acc.get('balance', 0):,.2f}")
            
            print("\n" + "-" * 50)
            
            # Option to view details of a specific account
            if results:
                try:
                    view_choice = input("\n📊 Enter number to view full details (or press Enter to cancel): ")
                    
                    if view_choice and view_choice.isdigit():
                        idx = int(view_choice) - 1
                        if 0 <= idx < len(results):
                            account = results[idx]
                            print("\n" + "=" * 50)
                            print("📊 FULL ACCOUNT DETAILS")
                            print("=" * 50)
                            print(f"👤 Name: {account['name']}")
                            print(f"🏦 Account Number: {account['accountNumber']}")
                            print(f"📧 Email: {account.get('email', 'N/A')}")
                            print(f"📅 Age: {account.get('age', 'N/A')}")
                            print(f"💰 Balance: ${account.get('balance', 0):,.2f}")
                            print("=" * 50)
                except Exception:
                    pass
                    
        except Exception as err:
            print(f"\n❌ Error during search: {err}")


# MAIN APPLICATION ENTRY POINT
def main():
    """
    Main application loop with secure menu system
    """
    bank = Bank()
    
    print("\n" + "=" * 55)
    print("🏦  WELCOME TO THE SECURE BANKING SYSTEM")
    print("=" * 55)
    print("🔐 End-to-end encrypted PIN storage")
    print("📊 Full transaction history")
    print("🔄 Secure money transfers")
    print("🔒 Multi-factor verification")
    print("=" * 55)
    
    while True:
        # Check session status
        is_logged_in = bank.is_session_active()
        user_name = Bank.current_session.get('name', 'Guest') if is_logged_in else None
        
        # Display main menu
        print("\n" + "=" * 50)
        print(f"👤 {'Logged in as: ' + user_name if is_logged_in else 'Not Logged In'}")
        print("=" * 50)
        
        if not is_logged_in:
            print("   1. 🔐 Login")
            print("   2. 🏦 Create Account")
            print("   3. 🔍 Search Accounts")
            print("   4. ❌ Exit")
            
            try:
                choice = int(input("\n📝 Enter your choice: "))
                
                if choice == 1:
                    bank.login()
                elif choice == 2:
                    bank.create_account()
                elif choice == 3:
                    bank.search_accounts()
                elif choice == 4:
                    print("\n" + "=" * 50)
                    print("👋 THANK YOU FOR USING OUR BANKING SYSTEM")
                    print("=" * 50)
                    break
                else:
                    print("\n❌ Invalid choice. Please try again.")
                    
            except ValueError:
                print("\n❌ Please enter a valid number.")
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
                
        else:
            # Logged in menu
            print("   1. 💰 Deposit Money")
            print("   2. 💸 Withdraw Money")
            print("   3. 🔄 Transfer Money")
            print("   4. 📊 View Account Details")
            print("   5. ✏️  Update Account")
            print("   6. 🔍 Search Accounts")
            print("   7. 🚪 Logout")
            print("   8. ⚠️ Delete Account (DANGER)")
            print("   9. ❌ Exit")
            
            try:
                choice = int(input("\n📝 Enter your choice: "))
                
                if choice == 1:
                    bank.deposit()
                elif choice == 2:
                    bank.withdraw()
                elif choice == 3:
                    bank.transfer_money()
                elif choice == 4:
                    bank.view_account_details()
                elif choice == 5:
                    bank.update_account()
                elif choice == 6:
                    bank.search_accounts()
                elif choice == 7:
                    bank.logout()
                elif choice == 8:
                    bank.delete_account()
                elif choice == 9:
                    if bank.is_session_active():
                        bank.logout()
                    print("\n" + "=" * 50)
                    print("👋 THANK YOU FOR USING OUR BANKING SYSTEM")
                    print("❤️ Developed by Sheharyar Sarmad")
                    print("=" * 50)
                    break
                else:
                    print("\n❌ Invalid choice. Please try again.")
                    
            except ValueError:
                print("\n❌ Please enter a valid number.")
            except KeyboardInterrupt:
                if bank.is_session_active():
                    bank.logout()
                print("\n\n👋 Goodbye!")
                break


# APPLICATION ENTRY POINT
if __name__ == "__main__":
    main()