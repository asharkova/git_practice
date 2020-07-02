class CellSrc:
    # Source Cell Class
    def __init__(self, x=0, y=0, destination=1):
        self.x = x
        self.y = y
        self.destination = destination


def exists_on_board(x, y, map_size):
    # Checks if element exists on the chess board
    if 0 <= x <= map_size['map_height']-1 and 0 <= y <= map_size['map_width']-1:
        return True
    return False


def solution(map):
    map_size = {'map_width': len(map[0]),
                'map_height': len(map)}

    shortest_escape_path = map_size['map_width'] + map_size['map_height'] - 1

    length = find_path(map, map_size)
    if not length or shortest_escape_path < length:
        length = 99999999999999999
        for y in range(map_size['map_width']):
            for x in range(map_size['map_height']):
                if map[x][y] == 1:
                    map[x][y] = 0
                    current_length = find_path(map, map_size)
                    map[x][y] = 1
                    if current_length and shortest_escape_path == current_length:
                        return current_length
                    elif current_length and current_length < length:
                        length = current_length
    return length


def find_path(map, map_size):
    # Determine all possible movements of bunny:
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    # Creating empty queue and put bunny at the starting position
    prison_door = CellSrc()
    escape_door = (CellSrc(x=map_size['map_height']-1, y=map_size['map_width']-1))
    queue = [prison_door]

    # Define all cells on the board as not visited
    visited_cells = [[False for y in range(map_size['map_width'])] for x in range(map_size['map_height'])]

    # Mark started position as visited (prison_door)
    visited_cells[prison_door.x][prison_door.y] = True

    # Loop until we have element in the queue
    while len(queue) > 0:

        # Read element from queue and then empty queue
        queue_element = queue[0]
        queue.pop(0)

        # If queue cell coordinates equal to destination coordinates
        # return destination
        if queue_element.x == escape_door.x and\
                queue_element.y == escape_door.y:
            return queue_element.destination

        # Iterate through all possible movements:
        for move_num in range(len(dx)):

            x = queue_element.x + dx[move_num]
            y = queue_element.y + dy[move_num]

            # Check if new coordinates are on the board and not visited yet:
            if exists_on_board(x, y, map_size) and not visited_cells[x][y] and map[x][y] != 1:
                visited_cells[x][y] = True
                queue.append(CellSrc(x=x, y=y, destination=queue_element.destination + 1))


if __name__ == '__main__':
    # print(solution(map=[[0, 0, 0, 0],
    #                     [1, 1, 0, 0],
    #                     [0, 0, 0, 1],
    #                     [0, 1, 1, 1],
    #                     [0, 0, 1, 0]]))
    #
    # print(solution(map=([[0, 1, 1, 0],
    #                      [0, 0, 0, 1],
    #                      [1, 1, 0, 0],
    #                      [1, 1, 1, 0]])))
    #
    # print(solution(
    #     map=[[0, 0, 0, 0, 0, 0],
    #          [0, 1, 1, 1, 1, 0],
    #          [0, 0, 0, 0, 0, 0],
    #          [0, 1, 1, 1, 1, 1],
    #          [0, 1, 1, 1, 1, 1],
    #          [0, 0, 0, 0, 1, 0]]))
    #
    # print(solution(map=[[0, 0, 0, 0, 0, 0, 0, 0],
    #                     [1, 1, 1, 1, 1, 0, 0, 0],
    #                     [0, 0, 0, 0, 1, 0, 0, 0],
    #                     [1, 1, 1, 1, 1, 0, 0, 0],
    #                     [0, 0, 0, 0, 0, 0, 1, 1],
    #                     [0, 1, 1, 1, 1, 1, 1, 1],
    #                     [0, 1, 1, 1, 1, 1, 1, 1],
    #                     [0, 0, 0, 0, 1, 0, 0, 0]]))
    #
    print(solution(map=([[0, 0, 0, 0, 0, 0],
                         [1, 1, 1, 1, 1, 0],
                         [1, 0, 0, 0, 0, 0],
                         [0, 0, 1, 0, 1, 1],
                         [0, 1, 1, 1, 1, 1],
                         [0, 0, 0, 0, 0, 0]])))
    # THIS
    print(solution(map=([[0, 0, 0, 0, 0, 0],
                         [1, 1, 1, 1, 1, 0],
                         [1, 1, 0, 0, 0, 0],
                         [0, 0, 1, 0, 1, 1],
                         [0, 1, 1, 1, 1, 1],
                         [0, 0, 0, 0, 0, 0]])))

    # print(solution(map=[[0, 0],
    #                     [0, 0]]))
    #
    # print(solution(map=[[0, 1],
    #                     [0, 0]]))
    #
    # print(solution(map=[[0, 1, 1],
    #                     [0, 0, 0]]))

    # print(solution(map=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                     [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #                     [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]]))
