import asyncio
import aiosqlite

async def async_fetch_users():
        """Fetch all users asynchronously."""
            async with aiosqlite.connect("users.db") as conn:
                        async with conn.execute("SELECT * FROM users") as cursor:
                                        return await cursor.fetchall()

                                    async def async_fetch_older_users():
                                            """Fetch users older than 40 asynchronously."""
                                                async with aiosqlite.connect("users.db") as conn:
                                                            async with conn.execute("SELECT * FROM users WHERE age > 40") as cursor:
                                                                            return await cursor.fetchall()

                                                                        async def fetch_concurrently():
                                                                                """Run multiple database queries concurrently."""
                                                                                    users, older_users = await asyncio.gather(
                                                                                                    async_fetch_users(),
                                                                                                            async_fetch_older_users()
                                                                                                                )
                                                                                        print("All users:", users)
                                                                                            print("Users older than 40:", older_users)

                                                                                            # Run the concurrent fetch
                                                                                            asyncio.run(fetch_concurrently())
