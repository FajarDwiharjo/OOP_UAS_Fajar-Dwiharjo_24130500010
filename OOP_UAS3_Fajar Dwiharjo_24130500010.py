class Person:
    def __init__(self, personId, firstName, lastName, dateOfBirth, nationality):
        self.personId = personId
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.nationality = nationality

    def getFullName(self):
        return f"{self.firstName} {self.lastName}"


class Player(Person):
    def __init__(self, personId, firstName, lastName, dateOfBirth, nationality,
                 playerId, jerseyNumber, marketValue, teamId, position, status):
        super().__init__(personId, firstName, lastName, dateOfBirth, nationality)
        self.playerId = playerId
        self.jerseyNumber = jerseyNumber
        self.marketValue = marketValue
        self.teamId = teamId
        self.position = position
        self.status = status

    def train(self):
        pass

    def playMatch(self):
        pass


class Coach(Person):
    def __init__(self, personId, firstName, lastName, dateOfBirth, nationality,
                 coachId, licenseLevel, teamId, role):
        super().__init__(personId, firstName, lastName, dateOfBirth, nationality)
        self.coachId = coachId
        self.licenseLevel = licenseLevel
        self.teamId = teamId
        self.role = role

    def conductTraining(self):
        pass

    def selectSquad(self):
        pass


class Sponsor:
    def __init__(self, sponsorId, name, contactPerson, phone, email, contractValue, contractStartDate, contractEndDate):
        self.sponsorId = sponsorId
        self.name = name
        self.contactPerson = contactPerson
        self.phone = phone
        self.email = email
        self.contractValue = contractValue
        self.contractStartDate = contractStartDate
        self.contractEndDate = contractEndDate

    def renewContract(self, newDate, newValue):
        self.contractEndDate = newDate
        self.contractValue = newValue


class Team:
    def __init__(self, teamId, league, division, clubId, name):
        self.teamId = teamId
        self.league = league
        self.division = division
        self.clubId = clubId
        self.name = name
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def removePlayer(self, player):
        self.players.remove(player)

    def scheduleTraining(self, session):
        pass


class Club:
    def __init__(self, clubId, name, foundingDate, budget, league, stadiumId):
        self.clubId = clubId
        self.name = name
        self.foundingDate = foundingDate
        self.budget = budget
        self.league = league
        self.stadiumId = stadiumId
        self.teams = []
        self.sponsors = []

    def manageBudget(self):
        pass

    def signSponsor(self, sponsor):
        self.sponsors.append(sponsor)

    def getTeams(self):
        return self.teams


# === Factory Method Implementation ===
class PersonFactory:
    @staticmethod
    def toPlayer(person, playerId, jerseyNumber, teamId, position, status="Active", marketValue=0.0):
        return Player(
            personId=person.personId,
            firstName=person.firstName,
            lastName=person.lastName,
            dateOfBirth=person.dateOfBirth,
            nationality=person.nationality,
            playerId=playerId,
            jerseyNumber=jerseyNumber,
            marketValue=marketValue,
            teamId=teamId,
            position=position,
            status=status
        )

    @staticmethod
    def toCoach(person, coachId, licenseLevel, teamId, role):
        return Coach(
            personId=person.personId,
            firstName=person.firstName,
            lastName=person.lastName,
            dateOfBirth=person.dateOfBirth,
            nationality=person.nationality,
            coachId=coachId,
            licenseLevel=licenseLevel,
            teamId=teamId,
            role=role
        )

# fun main

club = Club("C001", "FC Cakrawala", "2024-04-01", 1000000.0, "Liga Indonesia", "S001")

sponsor = Sponsor("SP001", "Universitas Cakrawala", "Adam Puspabuana", "080000000000", "sponsor@cakrawala.ac.id",
                  250000.0, "2024-01-01", "2025-01-01")
club.signSponsor(sponsor)

team = Team("T001", "Liga Universitas Indonesia", "Divisi Utama", "C001", "FC Cakrawala Muda")
club.teams.append(team)

# === Coaches lewat Factory Method ===
personCoach1 = Person("P001", "Lintang", "Atissalam", "1970-01-01", "Indonesia")
personCoach2 = Person("P002", "Hedy", "Pamungkas", "1970-01-01", "Indonesia")
headCoach = PersonFactory.toCoach(personCoach1, "HC001", "A", "T001", "Head Coach")
assistantCoach = PersonFactory.toCoach(personCoach2, "AC001", "B", "T001", "Assistant Coach")

# === Players lewat Factory Method ===
person1  = Person("P000001", "A", "B", "2006-01-01", "Indonesia")
person2  = Person("P000002", "A", "C", "2006-01-01", "Indonesia")
person3  = Person("P000003", "A", "D", "2006-01-01", "Indonesia")
person4  = Person("P000004", "A", "E", "2006-01-01", "Indonesia")
person5  = Person("P000005", "A", "F", "2006-01-01", "Indonesia")
person6  = Person("P000006", "A", "G", "2006-01-01", "Indonesia")
person7  = Person("P000007", "A", "H", "2006-01-01", "Indonesia")
person8  = Person("P000008", "A", "I", "2006-01-01", "Indonesia")
person9  = Person("P000009", "A", "J", "2006-01-01", "Indonesia")
person10 = Person("P000010", "A", "K", "2006-01-01", "Indonesia")
person11 = Person("P000011", "A", "L", "2006-01-01", "Indonesia")
person12 = Person("P000012", "A", "M", "2006-01-01", "Indonesia")
person13 = Person("P000013", "A", "N", "2006-01-01", "Indonesia")
person14 = Person("P000014", "A", "O", "2006-01-01", "Indonesia")
person15 = Person("P000015", "A", "P", "2006-01-01", "Indonesia")

player1  = PersonFactory.toPlayer(person1, "PL000001", 1,  "T001", "Striker", "Active")
player2  = PersonFactory.toPlayer(person2, "PL000002", 2,  "T001", "Striker", "Active")
player3  = PersonFactory.toPlayer(person3, "PL000003", 3,  "T001", "Striker", "Active")
player4  = PersonFactory.toPlayer(person4, "PL000004", 4,  "T001", "Striker", "Active")
player5  = PersonFactory.toPlayer(person5, "PL000005", 5,  "T001", "Striker", "Active")
player6  = PersonFactory.toPlayer(person6, "PL000006", 6,  "T001", "Striker", "Active")
player7  = PersonFactory.toPlayer(person7, "PL000007", 7,  "T001", "Striker", "Active")
player8  = PersonFactory.toPlayer(person8, "PL000008", 8,  "T001", "Striker", "Active")
player9  = PersonFactory.toPlayer(person9, "PL000009", 9,  "T001", "Striker", "Active")
player10 = PersonFactory.toPlayer(person10, "PL000010", 10, "T001", "Striker", "Active")
player11 = PersonFactory.toPlayer(person11, "PL000011", 11, "T001", "Striker", "Active")
player12 = PersonFactory.toPlayer(person12, "PL000012", 12, "T001", "Striker", "Active")
player13 = PersonFactory.toPlayer(person13, "PL000013", 13, "T001", "Striker", "Active")
player14 = PersonFactory.toPlayer(person14, "PL000014", 14, "T001", "Striker", "Injured")
player15 = PersonFactory.toPlayer(person15, "PL000015", 15, "T001", "Striker", "Loaned")

team.addPlayer(player1)
team.addPlayer(player2)
team.addPlayer(player3)
team.addPlayer(player4)
team.addPlayer(player5)
team.addPlayer(player6)
team.addPlayer(player7)
team.addPlayer(player8)
team.addPlayer(player9)
team.addPlayer(player10)
team.addPlayer(player11)
team.addPlayer(player12)
team.addPlayer(player13)
team.addPlayer(player14)
team.addPlayer(player15)


# === Output ===
print("Club:", club.name)
print("Team:", team.name)
print("Sponsor:", sponsor.name)
print("Coaches:", headCoach.getFullName(), "and", assistantCoach.getFullName())

print("\nPlayer Roster:")
print(f"{'No':<4} {'Name':<20} {'Position':<10} {'Status':<10}")
print("-" * 50)
for player in team.players:
    print(f"{player.jerseyNumber:<4} {player.getFullName():<20} {player.position:<10} {player.status:<10}")
