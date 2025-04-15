import math
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Product


class Paginator:
    def __init__(self, array:list | tuple, page: int=1, per_page: int=1):
        self.array = array
        self.per_page = per_page
        self.page = page
        self.len = len(self.array)
        self.pages = math.ceil(self.len / self.per_page)

    
    def _get_slice(self):
        start = (self.page - 1) * self.per_page
        stop = start + self.per_page
        return self.array[start:stop]
    

    def get_page(self):
        page_items = self.__get_slice()
        return page_items

    



async def orm_add_product(session: AsyncSession, data: dict):

    obj = Product(
            name=data['name'],
            description=data['description'],
            price=float(data['price']),
            image=data['image'],
        )
    session.add(obj)
    await session.commit()


async def orm_get_products(session: AsyncSession):
    query = select(Product)
    result = await session.execute(query)
    return result.scalars().all()


async def orm_get_product(session: AsyncSession, product_id: int):
    query = select(Product).where(Product.id==product_id)
    result = await session.execute(query)
    return result.scalar()


async def orm_update_product(session: AsyncSession, product_id: int, data):
    query = update(Product).where(Product.id==product_id).values(
            name=data['name'],
            description=data['description'],
            price=float(data['price']),
            image=data['image'],
    )
    await session.execute(query)
    await session.commit()
    

async def orm_delete_product(session: AsyncSession, product_id: int):
    query = delete(Product).where(Product.id == product_id)
    await session.execute(query)
    await session.commit()