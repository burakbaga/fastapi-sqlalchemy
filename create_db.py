from database import engine,Base
from models import Student

# metada kullanarak db de 
print("Cretating Database...")
Base.metadata.create_all(engine)