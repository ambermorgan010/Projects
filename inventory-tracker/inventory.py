"""
FUNCTION: Creates an inventory file containing items and their updated daily sales.

AUTHOR: Amber Morgan
"""


def read_inventory(filename):
    """
    Reads the lines in the given file and puts them in a dictionary using the item
    as the key and the quantity as the value. Returns the dictionary.
    """
    inventory = open(filename)
    inventory_dict = {}
    for line in inventory:
        product, quantity = line.strip().split(",")
        inventory_dict[product] = int(quantity)
    inventory.close()
    return inventory_dict


def update_inventory(inventory, filename):
    """
    Reads the given file and turns the lines into a dictionary with the product as the
    key and the amount sold as the value. Then, if the item exists, the amount sold is
    subtracted from the inventory dictionary to reflect the remaining quantity. If the
    item does not exist in the inventory, it is disregarded. Returns the updated
    inventory dictionary.
    """
    sales = open(filename)
    sold = {}
    for line in sales:
        products = line[6:]
        products_lst = products.split(",")
        for pair in products_lst:
            item, amount_sold = pair.split(":")
            if item not in sold:
                sold[item] = 0
            sold[item] += int(amount_sold)
    for item in sold:
        if item in inventory:
            inventory[item] -= int(sold[item])
    sales.close()
    return inventory


def save_inventory(inventory, filename):
    """
    Creates a new file. Prints the updated inventory, separating the item and quantity
    with a comma, in the file.
    """
    new_inv = open(filename, "w")
    for item in inventory:
        print(item, inventory[item], sep=",", file=new_inv)
    new_inv.close()


def main():
    inventory = read_inventory("fruits.csv")
    inventory = update_inventory(inventory, "sales.txt")
    save_inventory(inventory, "updated_inventory.csv")


if __name__ == "__main__":
    main()
