import connection
import position

connections = [
    connection.Connection(position.Position("A"), position.Position("B"), 2),
    connection.Connection(position.Position("B"), position.Position("C"), 5),
    connection.Connection(position.Position("C"), position.Position("A"), 7),
    connection.Connection(position.Position("B"), position.Position("D"), 12),
    connection.Connection(position.Position("C"), position.Position("D"), 3),
]
