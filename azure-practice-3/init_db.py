from db import get_connection

SCHEMA = "MikitaMalafei"

conn = get_connection()
cursor = conn.cursor()

cursor.execute(f"""
IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = '{SCHEMA}')
EXEC('CREATE SCHEMA {SCHEMA}')
""")


cursor.execute(f"""
IF OBJECT_ID('{SCHEMA}.chef', 'U') IS NULL
CREATE TABLE {SCHEMA}.chef (
    chefId INT PRIMARY KEY,
    name NVARCHAR(100),
    rating FLOAT
)
""")

cursor.execute(f"""
IF OBJECT_ID('{SCHEMA}.class', 'U') IS NULL
CREATE TABLE {SCHEMA}.class (
    classId INT PRIMARY KEY,
    title NVARCHAR(100),
    chefId INT,
    date DATETIME,
    capacity INT
)
""")

cursor.execute(f"""
IF OBJECT_ID('{SCHEMA}.booking', 'U') IS NULL
CREATE TABLE {SCHEMA}.booking (
    bookingId INT PRIMARY KEY,
    classId INT,
    userId INT,
    status NVARCHAR(50)
)
""")

cursor.execute(f"""
IF OBJECT_ID('{SCHEMA}.feedback', 'U') IS NULL
CREATE TABLE {SCHEMA}.feedback (
    feedbackId INT PRIMARY KEY,
    classId INT,
    rating INT,
    comment NVARCHAR(255)
)
""")

cursor.execute("""
INSERT INTO MikitaMalafei.chef (chefId, name, rating)
VALUES (1,'Gordon Ramsay',4.9)
""")

cursor.execute("""
INSERT INTO MikitaMalafei.chef (chefId, name, rating)
VALUES (2,'Jamie Oliver',4.5)
""")

cursor.execute("""
INSERT INTO MikitaMalafei.class (classId, title, chefId, date, capacity)
VALUES (1,'Italian Cooking',1,'2026-04-20',10)
""")

cursor.execute("""
INSERT INTO MikitaMalafei.class (classId, title, chefId, date, capacity)
VALUES (2,'Baking Basics',2,'2026-04-22',8)
""")

cursor.execute("""
INSERT INTO MikitaMalafei.booking (bookingId, classId, userId, status)
VALUES (1,1,101,'active')
""")

cursor.execute("""
INSERT INTO MikitaMalafei.booking (bookingId, classId, userId, status)
VALUES (2,2,102,'cancelled')
""")

cursor.execute("""
INSERT INTO MikitaMalafei.feedback (feedbackId, classId, rating, comment)
VALUES (1,1,5,'Amazing')
""")

cursor.execute("""
INSERT INTO MikitaMalafei.feedback (feedbackId, classId, rating, comment)
VALUES (2,2,4,'Good')
""")

conn.commit()
conn.close()

print("DB initialized")