from lib.album import Album
from lib.album_repository import AlbumRepository

def test_create(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)

    repo.create(Album(None, "Good Album", 2023, 3))
    assert repo.all() == [
        (1, 'Doolittle', 1989, 1),
        (2, 'Good Album', 2023, 3)
    ]


def test_delete(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)

    repo.create(Album(2, "Good Album", 2023, 3))
    repo.create(Album(3, "Bad Album", 2022, 3))
    repo.delete(2)
    assert repo.all() == [
        (1, 'Doolittle', 1989, 1),
        (3, 'Bad Album', 2022, 3)
    ]


