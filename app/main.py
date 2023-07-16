from fastapi import FastAPI
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# def startup():
#     redis_cache = FastApiRedisCache()
#     redis_cache.init(
#         host_url=os.environ.get("REDIS_URL", LOCAL_REDIS_URL),
#         prefix="fastapiC-cache",
#         response_header="X-FastAPI-Cache",
#         ignore_arg_types=[Request,Response,Session]
#     )

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
#             {"title": "favorate food", "content": "I like Pizza", "id": 2}]


# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "welcome to my API!!"}