from datetime import date, timedelta
from tabulate import tabulate


def analyse_inventory(today, stock_levels, stock_prices, stock_delivery):
    inventory_table_header = ['Product', 'Stock', 'Price (€)', 'Total Stock Value (€)', 'Delivery Date']
    inventory_table_data = []

    d = today.strftime("%d %b %Y") + " " + "(" + today.strftime("%d/%m/%Y") + ")"
    title = f"Stock Inventory: {d}"
    
    for stock_item, quantity in stock_levels.items():
        price = stock_prices.get(stock_item, 0.0)
        total_value = quantity * price
        delivery_date = stock_delivery.get(stock_item)
        price = price/100
        total_value = total_value/100
        record = [stock_item.title(), quantity, price, total_value, delivery_date.strftime("%d/%m/%Y")]
        inventory_table_data.append(record)

    
    print(f"\nStock Inventory Report as of {today.strftime("%d %b %Y")}:") 
    print(tabulate(inventory_table_data,
                   headers=inventory_table_header,
                   tablefmt='fancy_grid',
                   floatfmt=",.2f",
                   colalign=('left','right', 'right', 'right','left')
                   )
        )

today = date.today()
stock_levels = {
    'nails' : 12,
    'hammers' : 20,
    'wire' : 0,
    'pliers': 30
}

stock_prices = {
    'nails' : 340,
    'hammers' : 1255,
    'wire' : 399,
    'pliers': 1045
}

stock_delivery= {
    'nails' : today + timedelta(days=3),
    'hammers' : today + timedelta(days=14),
    'wire' : today + timedelta(days = 7),
    'pliers': today + timedelta(days=3)
}

analyse_inventory(today, stock_levels, stock_prices, stock_delivery)



