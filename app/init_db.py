from .database import Base, engine
from .models import Task

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Done!")
