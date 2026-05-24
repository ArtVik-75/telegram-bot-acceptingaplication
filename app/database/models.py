import aiosqlite


async def create_db():

    async with aiosqlite.connect("database.db") as db:

        await db.execute("""
            CREATE TABLE IF NOT EXISTS applications (
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         name TEXT,
                         phone TEXT,
                         comment TEXT
                    )
                """)
        
        await db.commit()