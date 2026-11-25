import sys
from parce import parse

def main():
    parse("src/config.json")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)