from dotenv import load_dotenv
import os

print("Start")

if __name__ == "__main__":
    load_dotenv()
    print("Hello Hamza!")
    print(os.environ['OPENAI_API_KEY'])

print("End")
