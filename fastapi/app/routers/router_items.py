from fastapi import APIRouter
from app.classes.models import Item, ItemNoId
from app.database.db import connect

router = APIRouter(prefix="/items")

async def execute_query(query, values=None):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, values)
    response = cursor.fetchall()
    conn.commit()
    conn.close()
    return response

@router.get("/", response_model=list[Item])
async def get_items():
    query = "SELECT id, name, description FROM items"
    response = await execute_query(query)
    return [Item(**dict(zip(["id", "name", "description"], row))) for row in response]

@router.post("/")
async def post_items(item: ItemNoId):
    query = "INSERT INTO items (name, description) VALUES (%s, %s)"
    values = [item.name, item.description]
    await execute_query(query, values)
    return await execute_query("SELECT LAST_INSERT_ID()")[0][0]

@router.get("/{id}")
async def get_item_by_id(id: int):
    query = "SELECT id, name, description FROM items WHERE id=%s"
    values = [id]
    response = await execute_query(query, values)
    return Item(**dict(zip(["id", "name", "description"], response[0])))