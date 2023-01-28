from app import ctx_db
from datetime import datetime, timedelta
from .queries__mongodb import Queries
from .command__mongodb import Command

class Blacklist:

    def add(tk: dict, ttl: float) -> bool:
        """Add a JWT to the blacklist"""
        Command(ctx_db = ctx_db, db_name = 'app_alexpddd', cl_name='blacklist').create_index_expires("expiresAfterSeconds", 20)

        expiry_date = datetime.utcnow() + timedelta(seconds=int(ttl))
        query={'token': tk, "expiresAfterSeconds": expiry_date}
        return Command(ctx_db = ctx_db, db_name = 'app_alexpddd', cl_name='blacklist').insert_one(query)

    def is_blacklisted(tk: str) -> bool:
        """Check if a tk is in the blacklist"""
        query={'token': tk}
        return bool(Queries(ctx_db = ctx_db, db_name = 'app_alexpddd', cl_name='blacklist').find_one(query))