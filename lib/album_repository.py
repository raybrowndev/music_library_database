from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection 

    def all(self):
        table_rows = self._connection.execute('SELECT * FROM albums')
        all_items = []
        for i in table_rows:
            each_item = (i['id'], i['title'], i['release_year'], i['artist_id'])
            all_items.append(each_item)
        return all_items

    def create(self, new_album):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [new_album.title, new_album.release_year, new_album.artist_id])
        return None

    def delete(self, del_id):
        self._connection.execute('DELETE FROM albums WHERE id = %s', [del_id])
        return None 

