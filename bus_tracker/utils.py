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

def get_date_full():
    d = get_local_time()
    d = d[0:19]
    return d

def get_local_time(zone='Asia/Kolkata'):
    import datetime
    from pytz import timezone
    other_zone = timezone(zone)
    other_zone_time = datetime.datetime.now(other_zone)
    return str(other_zone_time)