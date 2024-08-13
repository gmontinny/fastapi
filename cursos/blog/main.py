from random import randrange

from fastapi import FastAPI, HTTPException, status
from database import my_list, find_post, find_index_post
from openapi import CustomOpenApi
from schemas import Post

app = FastAPI()

@app.get("/posts")
async def get_all_posts():
    return {"data": my_list}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_list.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/latest")
async def get_latest_post():
    post = my_list[-1]
    return {"post_detail": post}

@app.get("/posts/{id}")
async def get_post_by_id(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID {id} not found")
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    indx = find_index_post(id)
    if indx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID {id} does not exist")
    my_list.pop(indx)
    return {"message": f"Post with ID {id} successfully deleted"}

@app.put("/posts/{id}")
async def update_post(id: int, post: Post):
    indx = find_index_post(id)
    if indx is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID {id} does not exist")
    post_dict = post.dict()
    post_dict['id'] = id
    my_list[indx] = post_dict
    return {"message": f"Post with ID {id} successfully updated"}

custom_schema = CustomOpenApi(app)
custom_schema.custom_openapi()