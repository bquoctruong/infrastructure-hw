import asyncio
from server import server

# Function main runs client utilzing asyncio
def main():
    asyncio.run(server())

if __name__ == "__main__":
    main()
