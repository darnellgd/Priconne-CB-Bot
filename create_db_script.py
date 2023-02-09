import sqlite3

conn = sqlite3.connect('priconne_database.db')
cur = conn.cursor()

cur.execute("""DROP TABLE IF EXISTS Clan""")
cur.execute("""DROP TABLE IF EXISTS Player""")
cur.execute("""DROP TABLE IF EXISTS ClanPlayer""")
cur.execute("""DROP TABLE IF EXISTS ClanBattle""")
cur.execute("""DROP TABLE IF EXISTS PlayerCBDayInfo""")
cur.execute("""DROP TABLE IF EXISTS TeamComposition""")
cur.execute("""DROP TABLE IF EXISTS CBDay""")
cur.execute("""DROP TABLE IF EXISTS Boss""")
cur.execute("""DROP TABLE IF EXISTS BossBooking""")

cur.execute("""
        CREATE TABLE Clan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """)

cur.execute("""
        CREATE TABLE Player (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            discord_id INTEGER NOT NULL
        )
    """)
cur.execute("""
        CREATE TABLE ClanPlayer (
            clan_id INTEGER,
            player_id INTEGER,
            FOREIGN KEY (clan_id) REFERENCES Clan(id), 
            FOREIGN KEY (player_id) REFERENCES Player(id),
            UNIQUE (clan_id, player_id)
        )
    """)

cur.execute("""
        CREATE TABLE ClanBattle (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            lap INTEGER NOT NULL,
            tier INTEGER NOT NULL,
            clan_id INTEGER,
            FOREIGN KEY (clan_id) REFERENCES Clan(id)
        )
    """)
cur.execute("""
        CREATE TABLE PlayerCBDayInfo(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            overflow INTEGER NOT NULL,
            ovf_time TEXT ,
            hits INTEGER NOT NULL,
            reset INTEGER NOT NULL,
            player_id INTEGER,
            cb_id INTEGER,
            FOREIGN KEY (player_id) REFERENCES PLayer(id),
            FOREIGN KEY (cb_id) REFERENCES ClanBattle(id)
        )
    """)
cur.execute("""
        CREATE TABLE TeamComposition(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            used INTEGER NOT NULL,
            pcdi_id INTEGER,
            FOREIGN KEY (pcdi_id) REFERENCES PlayerCBDayInfo(id)

        )
    """)
cur.execute("""
        CREATE TABLE Boss (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            boss_number INTEGER NOT NULL,
            ranking INTEGER,
            active INTEGER NOT NULL,
            cb_id INTEGER,
            FOREIGN KEY (cb_id) REFERENCES ClanBattle(id)
        )
    """)
cur.execute("""
        CREATE TABLE BossBooking (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lap INTEGER NOT NULL,
            overflow INTEGER,
            ovf_time TEXT,
            comp_name TEXT NOT NULL,
            exp_damage INTEGER,
            boss_id INTEGER,
            player_id INTEGER,
            FOREIGN KEY (boss_id) REFERENCES Boss(id),
            FOREIGN KEY (player_id) REFERENCES Player(id)
        )
    """)
conn.commit()
conn.close()
