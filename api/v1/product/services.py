from contextlib import closing

from django.db import connection


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_all(requests):
    sql = 'Select * from index_product'
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        result = dictfetchall(cursor)
    return result


def get_one(requests, pk):
    sql = 'Select * from index_product where id=%s'
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])
        result = dictfetchone(cursor)
    return result