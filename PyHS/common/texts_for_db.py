from aiogram.utils.formatting import Bold, as_list, as_marked_section


categories = ['Еда', 'Напитки']

description_for_infp_pages = {
    'main': 'Добро пожаловать',
    'about': 'Пицерия такая',
    'payment': as_marked_section(
        Bold('Варианты оплаты'),
        "Картой в боте", 
        "При получении",
        "В заведении",
        marker="✅ ",
    ).as_html(),
    'shipping': as_list(
        as_marked_section(
            Bold('Варианты доставки'),
            "Курьер", 
            "Самовынос",
            "Покушаю у вас",
            marker="✅ ",
        ),
        as_marked_section(Bold("Нельзя"), 'Почта', 'Голубь', marker="✅ "),
        sep="\n-------------------\n",
    ).as_html(),
    'catalog': 'Категории',
    'cart': 'В корзине ничего нет',
}