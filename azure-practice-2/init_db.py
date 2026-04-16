from db import get_connection

PREFIX = "s20230535"

conn = get_connection()
cursor = conn.cursor()

cursor.execute(f"""
IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = '{PREFIX}_classes')
EXEC('CREATE SCHEMA {PREFIX}_classes')
""")

cursor.execute(f"""
IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = '{PREFIX}_chefs')
EXEC('CREATE SCHEMA {PREFIX}_chefs')
""")

cursor.execute(f"""
IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = '{PREFIX}_feedbacks')
EXEC('CREATE SCHEMA {PREFIX}_feedbacks')
""")


cursor.execute(f"""
IF OBJECT_ID('{PREFIX}_chefs.chef', 'U') IS NULL
CREATE TABLE {PREFIX}_chefs.chef (
    chefId INT PRIMARY KEY,
    name NVARCHAR(100),
    rating FLOAT
)
""")

cursor.execute(f"""
IF OBJECT_ID('{PREFIX}_classes.class', 'U') IS NULL
CREATE TABLE {PREFIX}_classes.class (
    classId INT PRIMARY KEY,
    title NVARCHAR(100),
    chefId INT,
    date DATETIME,
    capacity INT
)
""")

cursor.execute(f"""
IF OBJECT_ID('{PREFIX}_classes.booking', 'U') IS NULL
CREATE TABLE {PREFIX}_classes.booking (
    bookingId INT PRIMARY KEY,
    classId INT,
    userId INT,
    status NVARCHAR(50)
)
""")

cursor.execute(f"""
IF OBJECT_ID('{PREFIX}_feedbacks.feedback', 'U') IS NULL
CREATE TABLE {PREFIX}_feedbacks.feedback (
    feedbackId INT PRIMARY KEY,
    classId INT,
    rating INT,
    comment NVARCHAR(255)
)
""")


cursor.execute(f"INSERT INTO {PREFIX}_chefs.chef VALUES (1,'Gordon Ramsay',4.9)")
cursor.execute(f"INSERT INTO {PREFIX}_chefs.chef VALUES (2,'Jamie Oliver',4.5)")

cursor.execute(f"INSERT INTO {PREFIX}_classes.class VALUES (1,'Italian Cooking',1,'2026-04-20',10)")
cursor.execute(f"INSERT INTO {PREFIX}_classes.class VALUES (2,'Baking Basics',2,'2026-04-22',8)")

cursor.execute(f"INSERT INTO {PREFIX}_classes.booking VALUES (1,1,101,'active')")
cursor.execute(f"INSERT INTO {PREFIX}_classes.booking VALUES (2,2,102,'cancelled')")

cursor.execute(f"INSERT INTO {PREFIX}_feedbacks.feedback VALUES (1,1,5,'Amazing')")
cursor.execute(f"INSERT INTO {PREFIX}_feedbacks.feedback VALUES (2,2,4,'Good')")

conn.commit()
conn.close()

print("DB initialized successfully")