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

# fun main

club = Club("C001", "FC Cakrawala", "2024-04-01", 1000000.0, "Liga Indonesia", "S001")

sponsor = Sponsor("SP001", "Universitas Cakrawala", "Adam Puspabuana", "080000000000", "sponsor@cakrawala.ac.id",
                  250000.0, "2024-01-01", "2025-01-01")
club.signSponsor(sponsor)

team = Team("T001", "Liga Universitas Indonesia", "Divisi Utama", "C001", "FC Cakrawala Muda")
club.teams.append(team)

headCoach = Coach("P001", "Lintang", "Atissalam", "1970-01-01", "Indonesia", "HC001", "A", "T001", "Head Coach")
assistantCoach = Coach("P002", "Hedy", "Pamungkas", "1970-01-01", "Indonesia", "AC001", "B", "T001", "Assistant Coach")


player1  = Player("P000001", "A", "B", "2006-01-01", "Indonesia", "PL000001", 1, 0.0, "T001", "Striker", "Active")
player2  = Player("P000002", "A", "C", "2006-01-01", "Indonesia", "PL000002", 2, 0.0, "T001", "Striker", "Active")
player3  = Player("P000003", "A", "D", "2006-01-01", "Indonesia", "PL000003", 3, 0.0, "T001", "Striker", "Active")
player4  = Player("P000004", "A", "E", "2006-01-01", "Indonesia", "PL000004", 4, 0.0, "T001", "Striker", "Active")
player5  = Player("P000005", "A", "F", "2006-01-01", "Indonesia", "PL000005", 5, 0.0, "T001", "Striker", "Active")
player6  = Player("P000006", "A", "G", "2006-01-01", "Indonesia", "PL000006", 6, 0.0, "T001", "Striker", "Active")
player7  = Player("P000007", "A", "H", "2006-01-01", "Indonesia", "PL000007", 7, 0.0, "T001", "Striker", "Active")
player8  = Player("P000008", "A", "I", "2006-01-01", "Indonesia", "PL000008", 8, 0.0, "T001", "Striker", "Active")
player9  = Player("P000009", "A", "J", "2006-01-01", "Indonesia", "PL000009", 9, 0.0, "T001", "Striker", "Active")
player10 = Player("P000010", "A", "K", "2006-01-01", "Indonesia", "PL000010", 10, 0.0, "T001", "Striker", "Active")
player11 = Player("P000011", "A", "L", "2006-01-01", "Indonesia", "PL000011", 11, 0.0, "T001", "Striker", "Active")
player12 = Player("P000012", "A", "M", "2006-01-01", "Indonesia", "PL000012", 12, 0.0, "T001", "Striker", "Active")
player13 = Player("P000013", "A", "N", "2006-01-01", "Indonesia", "PL000013", 13, 0.0, "T001", "Striker", "Active")
player14 = Player("P000014", "A", "O", "2006-01-01", "Indonesia", "PL000014", 14, 0.0, "T001", "Striker", "Injured")
player15 = Player("P000015", "A", "P", "2006-01-01", "Indonesia", "PL000015", 15, 0.0, "T001", "Striker", "Loaned")

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

print("Club:", club.name)
print("Team:", team.name)
print("Sponsor:", sponsor.name)
print("Coaches:", headCoach.getFullName(), "and", assistantCoach.getFullName())
print("\nPlayer Roster:")
for player in team.players:
    print(f"{player.jerseyNumber:02} | {player.getFullName()} | {player.position} | {player.status}")
