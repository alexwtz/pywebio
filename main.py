from pywebio.input import input, NUMBER
from pywebio.output import put_text, use_scope
from pywebio.exceptions import SessionClosedException

def demo():
    

    put_text("Hello")
    age = input("What is your name? ")
    put_text(f"Hello {age}")
    #put_text("You are old")
    while age != 2:
        age = input("Enter your age: ", type=NUMBER)
        with use_scope('scope2', clear=True):  # enter the existing scope and clear the previous content
            put_text(f"you have selected {age}")
    put_text("you win")
    
if __name__ == "__main__":
    try:
        demo()
    except SessionClosedException:
        print("The session was closed unexpectedly")