from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.pool import QueuePool
banco = SQLAlchemy(engine_options={"pool_size": 10, "poolclass":QueuePool, "pool_pre_ping":True})
