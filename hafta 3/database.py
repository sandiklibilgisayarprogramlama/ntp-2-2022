from sqlite3 import connect


class DB:
    def __init__(self, db_name):
        self.connection = connect(db_name)

    def tum_verileri_getir(self, table_name):
        query = "select * from "+table_name
        cur = self.connection.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        return rows

    def veri_ekle(self, table_name, eklenecekler):
        tuple_eklenecek = (
            eklenecekler.id, eklenecekler.ad, eklenecekler.soyad, eklenecekler.yas)
        sql = 'INSERT INTO ' + table_name+' VALUES(?,?,?,?) '
        cur = self.connection.cursor()
        cur.execute(sql, tuple_eklenecek)
        self.connection.commit()
