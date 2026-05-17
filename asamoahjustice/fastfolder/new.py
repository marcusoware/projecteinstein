# def main(f):
#     def wrapper():
#         print("before")
#         f()
#         print("after")
#     return wrapper


# @main
# def secfun():
#     print("hello from second")

# secfun()


# def main(me):
#     def call():
#         print("Now i understand")
#         me()
#         print("don't I?")
#     return call

# @main
# def calling():
#     print("Are you sure you do understand it?")

# calling()

from fastapi import FastAPI

new_app = FastAPI()

@new_app.get("/come")
def see():
    return {"message1": "Hellow there!",
            "message2": "welcome, it seems i know finally understoon fastapi basic syntax",
            "message3": "ain't that awesome?"
            }

if __name__ == "__main__":
    see()
