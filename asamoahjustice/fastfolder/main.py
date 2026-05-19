from fastapi import FastAPI

app = FastAPI()

@app.get("/page")
def main():
    return {"message": "Hello from FastAPI!"}


@app.get("/api")
def info():
      return["name", "age", "school"]


if __name__ == "__main__":
        main()
