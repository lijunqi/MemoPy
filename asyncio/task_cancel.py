import asyncio
import time

async def cancel_me():
    print('[Start]cancel_me(): before sleep')
#    try:
    for i in range(10):
#        time.sleep(1)
        await asyncio.sleep(1)
        print('cancel_me sleep: ', i)
#    except asyncio.CancelledError:
#        print('[Catch]cancel_me(): cancel sleep')

#    try:
#        # Wait for 1 hour
#        await asyncio.sleep(3600)
#    except asyncio.CancelledError:
#        print('[Catch]cancel_me(): cancel sleep')
#    finally:
#        print('[Finally]cancel_me(): after sleep')

async def main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    print('sleeping...')
    await asyncio.sleep(3)
    print('sleep done')

    print('call cancel')
    task.cancel()
    print('call cancel done')
#    print('cancel again')
#    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())

# Expected output:
#
#     cancel_me(): before sleep
#     cancel_me(): cancel sleep
#     cancel_me(): after sleep
#     main(): cancel_me is cancelled now
