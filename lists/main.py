# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
# List of film names
film_names = [
    "Star Wars",
    "Jurassic Park",
    "Harry Potter",
    "E.T.",
    "Indiana Jones"
]

# Function to sort films alphabetically
def alphabetical_order(films):
    return sorted(films)

# Test the function
print(alphabetical_order(film_names))
# List of Golden Globe winning films
golden_globes = [
    "jaws",
    "e.t.",
    "schindler's list",
    "star wars"
]

# Function to check if a film won a Golden Globe
def won_golden_globe(film_name):
    film_name = film_name.lower()
    return film_name in golden_globes


# Test examples
print(won_golden_globe("Jaws"))          # True
print(won_golden_globe("Harry Potter")) # False
print(won_golden_globe("STAR WARS"))    # True
