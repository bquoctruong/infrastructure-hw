import asyncio
from client import client

# Function main runs client utilzing asyncio
def main():
    asyncio.run(client())

if __name__ == "__main__":
    main()
