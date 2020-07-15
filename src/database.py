import sqlite3

conn = sqlite3.connect("mstore.db")

c = conn.cursor()


def create_tables():
    c.execute(
        """CREATE TABLE IF NOT EXISTS transactions (
              id integer primary key autoincrement,
              amount integer,
              comment text,
              date integer
              )"""
    )

    c.execute(
        """CREATE TABLE IF NOT EXISTS tags (
              id integer primary key autoincrement,
              tag text
              )"""
    )

    c.execute(
        """CREATE TABLE IF NOT EXISTS tags_by_transactions (
              id integer primary key autoincrement,
              transaction_id integer references transactions(id),
              tag_id integer references tags(id)
              )"""
    )


def drop_tables():
    c.execute("DROP TABLE tags_by_transactions")
    c.execute("DROP TABLE transactions")
    c.execute("DROP TABLE tags")


def insert_tables():
    c.execute(
        """INSERT INTO transactions (amount, comment, date)
              VALUES (100, "blaaa", 1235465464)"""
    )
    c.execute("""INSERT INTO tags (tag) VALUES ("food")""")
    c.execute(
        """INSERT INTO tags_by_transactions (transaction_id, tag_id)
              VALUES (1, 1)"""
    )
    conn.commit()


def add_new_transaction(amount, comment, date):
    c.execute(
        """INSERT INTO transactions (amount, comment, date) VALUES (?, ?, ?)""",
        (amount, comment, date),
    )
    conn.commit()
    return c.lastrowid


def add_new_tag(tag):
    c.execute("""INSERT INTO tags (tag) VALUES (?)""", (tag,))
    conn.commit()
    return c.lastrowid


def add_new_tag_by_transaction(transaction, tag):
    c.execute(
        """INSERT INTO tags_by_transactions (transaction_id, tag_id) VALUES (?, ?)""",
        (transaction, tag),
    )
    conn.commit()


def select():
    c.execute("SELECT * FROM tags")
    r = c.fetchall()
    print(r)


def find_tag(tag):
    c.execute("SELECT * FROM tags WHERE tag=?", (tag,))
    result = c.fetchall()
    if not result:
        return add_new_tag(tag)
    else:
        return result[0][0]
