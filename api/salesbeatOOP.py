class TrainStation:

    def __init__(self, stat_name, platforms=None):
        self.station_name = stat_name

        if platforms is None:
            self.plaforms = []
        else:
            self.platforms = platforms

    def add_platform(self, plat):
        if plat not in self.plaforms:
            self.plaforms.append(plat)


class Platform:

    def __init__(self, plat_name, train=None):
        self.platform_name = plat_name
        self.train = train

    def accept_train(self, train):
        self.train = train


class ICE:

    def __init__(self, train_name, sections=None):
        self.train_name = train_name

        if sections is None:
            self.sections = []
        else:
            self.sections = sections

    def dock_section(self, section):
        if not section in self.sections:
            self.sections.append(section)

    def print_sections(self):
        for i in self.sections:
            print(i.sectionname)

    def show_current_passengers(self):
        for i in self.sections:
            for x in i.people:
                print('{} {}'.format(x.name, x.lastname))

    def count_passengers(self):
        count = 0
        for i in self.sections:
            count += len(i.people)
        print(count)


class TrainSection:

    def __init__(self, sectionname, people=None):
        self.sectionname = sectionname

        if people is None:
            self.people = []
        else:
            self.people = people

    def get_on_train(self, person):
        if person not in self.people:
            self.people.append(person)
            print('{} {} is on the train now'.format(person.name, person.lastname))

    def get_off_train(self, person):
        if person in self.people:
            self.people.remove(person)
            print('{} {} left the train'.format(person.name, person.lastname))


class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


# create a train station
platform = Platform('platform 1')
train_station = TrainStation('Linz')
train_station.add_platform(platform)
# create a train
train_1 = ICE('ICE 1')
platform.accept_train(train_1)
train_section_1 = TrainSection('First section')
train_section_2 = TrainSection('Second section')
train_section_3 = TrainSection('Third section')
train_1.dock_section(train_section_1)
train_1.dock_section(train_section_2)
train_1.dock_section(train_section_3)
train_1.print_sections()
# create a train
train_1 = ICE('ICE 1')
platform.accept_train(train_1)
train_section_1 = TrainSection('First section')
train_section_2 = TrainSection('Second section')
train_section_3 = TrainSection('Third section')
train_1.dock_section(train_section_1)
train_1.dock_section(train_section_2)
train_1.dock_section(train_section_3)
train_1.print_sections()
# Expected output: First section – Second section – Third section
# create persons
person_1 = Person('Franz', 'Mair')
person_2 = Person('Michael', 'Schuh')
person_3 = Person('Herbert', 'Sailer')
person_4 = Person('Michaela', 'Mader')
train_section_1.get_on_train(person_1)
# Expected output: Franz Mair is on the train now
train_section_1.get_on_train(person_2)
# Expected output: Michael Schuh is on the train now
train_section_2.get_on_train(person_3)
# Expected output: Herbert Sailer is on the train now
train_section_3.get_on_train(person_4)
# Expected output: Michaela Mader is on the train now
train_section_2.get_off_train(person_3)
# Expected output: Herbert Sailer has left the train
# query passengers
train_1.show_current_passengers()
# Expected output: Franz Mair, Michel Schuh, Michaela Mader
train_1.count_passengers()
# Expected output: 3