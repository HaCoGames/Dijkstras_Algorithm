import position
import connection
import connections

import copy


start = position.Position("A")
end = position.Position("C")


cons = copy.copy(connections.connections)


for c in cons:
    print(c)