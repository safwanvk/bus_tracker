from django.db import connection

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, cursor.fetchone()))

def execute(query,data=None,many=True):
        with connection.cursor() as cursor:
            cursor.execute(query,data)
            if many:
                return dictfetchall(cursor)
            else:
                return dictfetchone(cursor)