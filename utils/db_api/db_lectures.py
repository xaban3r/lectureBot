import asyncio

import asyncpg

from data import config


class Database:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                user=config.PQUSER,
                password=config.PQPASSWORD,
                host=config.IP
            )
        )
    async def create_table_lectures(self):
        sql = """
        CREATE TABLE IF NOT EXISTS lectures (
        subject_name VARCHAR(255) NOT NULL,
        video_id text[],
        PRIMARY KEY (subject_name))
        """
        await self.pool.execute(sql)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters, start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_lecture(self, subject_name, video_id):
        print(video_id)
        sql = "UPDATE lectures SET video_id = $2 WHERE subject_name = $1"
        return await self.pool.execute(sql, subject_name, video_id)

    async def select_subject(self, **kwargs):
        sql = "SELECT * FROM lectures WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetchrow(sql, *parameters)

    async def delete_subject(self):
        await self.pool.execute("DELETE FROM lectures WHERE True")
