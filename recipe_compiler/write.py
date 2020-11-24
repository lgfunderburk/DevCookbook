import os


def write_home_page(home_page: str):
    """Writes the home_page HTML to file

    Args:
        home_page (str): A string of HTML to be written to file
    """

    with open("./docs/index.html", "w+") as f:
        f.write(home_page)


def write_recipe_page(recipe_slug: str, recipe_page: str):
    """Writes the recipe_page HTML to file

    Args:
        recipe_page (str): A string of HTML to be written to file
    """

    assert recipe_slug != "index"

    if not os.path.exists(f"./docs/{recipe_slug}"):
        os.makedirs(f"./docs/{recipe_slug}")

    with open(f"./docs/{recipe_slug}/index.html", "w+") as f:
        f.write(recipe_page)
