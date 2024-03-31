#!/usr/bin/env python3
import getpass
import os.path
import sys

from pypdf import PdfReader, PdfWriter


def pdf_util_filename_from_args() -> str:
    try:
        return sys.argv[1]
    except IndexError:
        print("Must have on argument 'filename'", file=sys.stderr)
        exit(1)


def pdf_util_decrypt_pdf():
    filename: str = pdf_util_filename_from_args()
    
    reader = PdfReader(filename)
    
    if reader.is_encrypted:
        password = getpass.getpass()
        if reader.decrypt(password) == 0:
            print("Unable to decrypt PDF, password was probably incorrect!")
            exit(1)
    else:
        exit(0)
        
    writer = PdfWriter(clone_from=reader)
    
    with open(filename, "wb") as f:
        writer.write(f)
    

def pdf_util_encrypt_pdf():
    filename: str = pdf_util_filename_from_args()
    
    reader = PdfReader(filename)
    if reader.is_encrypted:
        print(f"{filename} has already been encrypted", file=sys.stderr)
        exit(1)
        
    new_password: str = ""
    password_confirmed: bool = False
    while not password_confirmed:
        new_password = getpass.getpass("New Password:")
        confirm_new_password = getpass.getpass("Confirm New Password:")
        if new_password == confirm_new_password:
            password_confirmed = True
        else:
            print("Confirm Password does not match, try again", file=sys.stderr)
    
    writer = PdfWriter(clone_from=reader)
    writer.encrypt(new_password, algorithm='AES-256-R5')
    
    with open(filename, "wb") as f:
        writer.write(f)
        
        
def pdf_util_process():
    command_name = os.path.basename(sys.argv[0])
    if command_name == "pdf_util_decrypt":
        pdf_util_decrypt_pdf()
    elif command_name == "pdf_util_encrypt":
        pdf_util_encrypt_pdf()


pdf_util_process()
