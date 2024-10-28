import asyncio
from robinhood.robinhood_integration import RobinhoodIntegration
from venmo.venmo_integration import VenmoIntegration

async def main():
    venmo = VenmoIntegration("d6fcf9f51a2dd189dfe7b7f395d106b803c485f2a318293467cbad7366de0c3d")
    await venmo.initialize()
    # print(await venmo.get_balance())
    # await venmo.pay_user("Richard-F-zhang", 1, "test")
    print(await venmo.get_user("Richard-F-zhang"))
    # robinhood = RobinhoodIntegration("YOUR_ACCESS_TOKEN")
    # await robinhood.get_tax_documents()

if __name__ == "__main__":
    asyncio.run(main())
