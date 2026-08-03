from database.db import Db # importing Db class 
from database.security_config import SecurityConfig # importing SecurityConfig class
from dotenv import load_dotenv # imorting load_dotenv function or method
import os # import os module for getenv method
import bcrypt # for hashing plain password into any salting algorithm
import re # for validating email and phone number


load_dotenv() # calling the load_dotenv method or function

mongo_uri = os.getenv("MONGO_URI") # creating container mongo_uri to save the connection string
db = Db(mongo_uri) # Creating object of db

db.create_collection("admin") # creating collection and named as "admin"

admin = db["admin"] # storing admin collection inside an "admin" container

class AdminAuth:
    # Initializing variables:
    def __init__(self, name, email, password, phonenumber):
        self.name = name
        self.email = email
        self.password = password
        self.phonenumber = phonenumber
        self.success = False
        self.can_make_account = False
     
    # Validate name
    def validate_name(self) -> bool:  
        # failing if minimum age requirement is not fullfilled
        if len(self.name) < 2: 
            return False

        # failing if maximum age requirement is not fullfilled
        elif len(self.name) >= 50: 
            return False     

        # returning True if requirements are true
        return True      

    # Validate email
    def validate_email(self) -> bool:
        # Regex
        EMAIL_REGEX = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
 
        # failing if minimum lenght is not fullfilled
        if len(self.email) < 6: 
            return False

        # failing if maximum length is not fullfilled
        elif len(self.email) > 254:
            return False

        # checking before split on the bases of "@"
        elif len(self.email.split("@")[0]) > 64:
            return False
        
        # returning regex evaluation into boolean
        return bool(re.match(EMAIL_REGEX, self.email)) 

    # Validate password length
    def validate_password_length(self) -> bool:
        # Checking password
        if len(self.password) < 8 or len(self.password) > 50: 
            return False

        # returning True if password length is valid
        return True

    # Validate phonenumber with regex and lenght
    def validate_phonenumber(self) -> bool: 
        PHONE_REGEX = r"^(?:\+92|92|0)?3[0-9]{2}[0-9]{7}$"
        phone = self.phonenumber.replace(" ","").replace("-", "")

        if len(phone) not in [10,11,12,13]:
            return False

        return bool(re.match(PHONE_REGEX, phone))

    # hashing plain password into bcypt using salt algorithm
    def hash_password(self) -> bytes: 
        # making password into bytes
        password_bytes = self.password.encode("utf-8")

        # generating random password
        salt = bcrypt.gensalt()

        # hashing password
        hashed_password = bcrypt.hashpw(
            password_bytes,
            salt
        )

        return hashed_password

    # Compare plain password by hashed password stored in database
    def check_password(self, hashed_password) -> bool:

        password_bytes = self.password.encode("utf-8")

        match_pass = bcrypt.checkpw(
            password_bytes,
            hashed_password
        )

        return bool(match_pass)

    # Creating admin after several checkings
    def signup(self): 
        try: 
           count = admin.count_documents({})

           # Checking user's count
           if count >= 2: 
               print("\nYou are not authorized to create an account!\n")
               self.success = False
               self.can_make_account = False
               return self.success

           # Db query for finding it
           already_exists = admin.find_one({
               "$or": [{"name": self.name}, {"email": self.email}]
           },
           { 
               "password": 0, 
               "name": 1,
               "email": 1
           })

           # Checking if admin already exists
           if already_exists:
               print("\nYou are not authorized to create an account!\n")
               self.success = False
               self.can_make_account = False
               return self.success

           # Validating name length
           if not self.validate_name(): 
               print("\nName must be more than 2 characters and maximum 50\n")
               self.success = False
               self.can_make_account = False
               return self.success

           # Validating password length
           if not self.validate_password_length(): 
               print("\nPassword length must be atleast 8 characters and maximum 50\n")
               self.success = False
               self.can_make_account = False
               return self.success

           # Validating email type and its length
           if not self.validate_email(): 
               print("\nInvalid email!\n")
               self.success = False
               self.can_make_account = False
               return self.success

           # Validating phonenumber type and its length
           if not self.validate_phonenumber(): 
               print("\nInvalid phonenumber!\n")
               self.success = False
               self.can_make_account = False
               return self.success

           admin_doc = admin.insert_one({
               "name": self.name,
               "email": self.email,
               "password": self.hash_password(),
               "phonenumber": self.phonenumber
            })

           SecurityConfig.create_session(
               str(admin_doc.inserted_id),
               self.name,
               self.email
            )

           self.success = True

           return {
               "success": self.success,
               "message": "\nAdmin account created successfully!\n",
               "_id": str(admin_doc.inserted_id)
           }
           
        except Exception as err:
            print(f"\nSignup error occur: {err}\n")
            self.success = False
            self.can_make_account = False
            return self.success

    # Login to admin account after several checkings
    def login(self):
        try:
            is_exists = admin.find_one(
            {"email": self.email}
            , {
                "password": 1,
                "_id": 1,
                "name": 1,
                "email": 1
            })

            if not is_exists: 
                print("\nAdmin with these credentials did'nt exists!\n")
                self.success = False
                return self.success 

            if not self.check_password(is_exists["password"]): 
                print("\nWrong credentials!\n")
                self.success = False
                return self.success

            if is_exists and self.check_password(is_exists["password"]):
                SecurityConfig.create_session(
                    str(is_exists["_id"]),
                    is_exists["name"],
                    is_exists["email"]
                )

                self.success = True

            return {
                "success": self.success, 
                "message": "\nLogin successfully!\n"
            }

        except Exception as err:
            print(f"\nLogin error occur: {err}")
            self.success = False
            return self.success

    # Logout and destroy session
    def logout(self): 
        try: 
            SecurityConfig.destroy_session()

            self.success = True
            return {
                "success": True,
                "message": "Logout Successfully!",
            }
        
        except Exception as err: 
            print(f"\nLogout error occur: {err}\n") 
            self.success = False
            return self.success

    # Sending details of logged in admin after validating session
    def details(self): 
        try: 
            if not SecurityConfig.validate_session(): 
                print("\nLogin first to see details!")
                self.success = False
                return self.success

            data = SecurityConfig.get_session()

            self.success = True
            return {
                "success": self.success, 
                "message": "\nDetails delivered successfully!\n", 
                "data": {
                    "_id": data["_id"], 
                    "name": data["name"],
                    "email": data["email"]
                }
            }
             
        except Exception as err: 
            print(f"\nDetails error occur: {err}")
            self.success = False
            return self.success