#michelia's python playground

animal_dict = {
    "giraffe": "all giraffes have unique spots",
    'peacock/fowl':'only male peacocks have the colorful feathers',
    'penguins':"penguins are the closest relative to the albatross"
}

print("What is your favorite animal?")
print('peacock, giraffe, or penguins.')

favanimal_string=input()

print(favanimal_string)
print(animal_dict[favanimal_string])


