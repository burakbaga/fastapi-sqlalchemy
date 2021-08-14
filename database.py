from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Veritabanına erişmek için bir engine oluşturuyoruz. 
engine = create_engine("postgresql://postgres:admin@localhost/university",echo=True)

# Tabloları oluşturmak için declaritive_base e ihtiyacımız var. Yeni tanımlanmış tablo neselerinin toplandığı bir metada içerir. 
Base = declarative_base()

# Veritabanı ile etkileşime girmek için session oluşturmamız gerekiyor. Bunu sessionmaker ile sağlıyoruz. 
Session = sessionmaker(bind=engine)




