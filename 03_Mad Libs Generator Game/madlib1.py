def madlib1():
    animal = input("Enter a animal name: ")
    proffesion = input("Enter a profession name: ")
    cloth = input("Enter a cloth: ")
    things = input("Enter a things name: ")
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    verb = input("Enter a verb: ")
    food = input("Enter a food: ")
    print("Say", food, "The photographer said as the camera flash!", name, "and I had gone to", place, "to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as",
          animal, "pretending to be a", proffesion, ". When we saw the second photo it was excatly what I wanted. We both looked like", things, "wearing", cloth, "and", verb, "--exactly what I had in my mind.")


def madlib2():
    points = ["adjective", "color-name", "thing-name", "place",
              "person", "adjective1", "insect", "food", "verb"]
    points[0] = input("enter an adjective: ")
    points[1] = input(f"Enter {points[1]}")


if __name__ == "__main__":
    story = madlib1
    madlibtwo = madlib2
    print(madlibtwo)
