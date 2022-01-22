class Garden:
    STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

    def __init__(self, diagram, students=STUDENTS):
        garden = diagram.splitlines()
        self.first_half_row = garden[0]
        self.second_half_row = garden[1]

        self.students = sorted(students)

    def plants(self, student):
        index = self.students.index(student)
        first_column = index * 2
        second_columun = index * 2 + 1

        plant_list = []
        plant_list.append(self.first_half_row[first_column])
        plant_list.append(self.first_half_row[second_columun])
        plant_list.append(self.second_half_row[first_column])
        plant_list.append(self.second_half_row[second_columun])

        table = str.maketrans({
            'V': 'Violets',
            'R': 'Radishes',
            'G': 'Grass',
            'C': 'Clover',
        })

        plant_list = [plant.translate(table) for plant in plant_list]

        return plant_list
