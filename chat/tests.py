from django.test import TestCase

# Create your tests here.
import asyncio


async def async_task(name):
    print(f"Starting {name}")
    await asyncio.sleep(2)  # Simulate a blocking operation, like reading from a file or making an API call
    print(f"Completed {name}")

async def main():
    await asyncio.gather(
        async_task("Task 1"),
        async_task("Task 2")
    )

if __name__ == "__main__":
    asyncio.run(main())
    
    
    