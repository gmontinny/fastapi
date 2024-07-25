my_list = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "title of post 2", "content": "content of post 2", "id": 2}
]

def find_post(id: int):
    for post in my_list:
        if post["id"] == id:
            return post
    return None

def find_index_post(id: int):
    for index, post in enumerate(my_list):
        if post["id"] == id:
            return index
    return None