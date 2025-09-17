# your method definition here
def array_of_names(persons):
  full_names = []
  for first_name, last_name in persons.items():
    capitalized_first = first_name.capitalize()
    capitalized_last = last_name.capitalize()
    full_names.append(f"{capitalized_first} {capitalized_last}")
  return full_names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))