import orm
import asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='password', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()

async def test_get(loop):
    await orm.create_pool(loop, user='root', password='password', db='awesome')
    U = await User().findAll()
    print(U)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [test(loop), test_get(loop)]
    loop.run_until_complete(asyncio.wait(tasks))
    print('Test finished!')