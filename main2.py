#https://stackoverflow.com/questions/58309184/is-it-possible-to-capture-websocket-traffic-using-selenium-and-python

import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(
        headless=True,
        args=['--no-sandbox'],
        autoClose=False
    )
    page = await browser.newPage()
    await page.goto('https://www.tradingview.com/symbols/BTCUSD/')
    cdp = await page.target.createCDPSession()
    await cdp.send('Network.enable')
    await cdp.send('Page.enable')

    def printResponse(response):
        print(response)

    cdp.on('Network.webSocketFrameReceived', printResponse)  # Calls printResponse when a websocket is received
    cdp.on('Network.webSocketFrameSent', printResponse)  # Calls printResponse when a websocket is sent
    await asyncio.sleep(100)


# loop =
loop.run_until_complete(main())