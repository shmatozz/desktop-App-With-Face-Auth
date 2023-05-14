import psycopg2


def connect_to_db():
    """
    Establish connection with users database.
    """
    return psycopg2.connect(host="db.dkadcfuknosrclhomisf.supabase.co",
                            user="postgres",
                            password="verifacetion123",
                            database="postgres")
