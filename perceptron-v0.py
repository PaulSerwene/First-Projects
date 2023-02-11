Trainingsdaten = [
				[1, 0, 0, 0, 0, 0],
				[1, 0, 0, 0, 1, 0],
				[1, 0, 0, 1, 0, 0],
				[1, 1, 1, 1, 1, 0],
				[1, 0, 1, 0, 0, 0],
				[1, 1, 0, 0, 0, 0],
				[1, 1, 0, 1, 1, 0],
				[1, 0, 1, 1, 0, 0],
				[1, 1, 1, 0, 0, 0],
				[1, 0, 1, 0, 1, 1],
				[1, 1, 0, 1, 0, 0],
				[1, 0, 0, 1, 1, 1],
				[1, 1, 0, 0, 1, 0],
				[1, 0, 1, 1, 1, 1],
				[1, 1, 1, 0, 1, 1],
				[1, 1, 1, 1, 0, 0]
]

regel = [0, 0, 0, 0, 0]
alpha = 1
cyclen = 15

def training():
	esf = 0
	ex1 = 0
	ex2 = 0
	ex3 = 0
	ex4 = 0
	e = 0
	for j in range(cyclen):
		for i in range(len(Trainingsdaten)):
			esf = regel[0] * Trainingsdaten[i][0]
			ex1 = regel[1] * Trainingsdaten[i][1]
			ex2 = regel[2] * Trainingsdaten[i][2]
			ex3 = regel[3] * Trainingsdaten[i][3]
			ex4 = regel[4] * Trainingsdaten[i][4]

			if (esf + ex1 + ex2 +ex3 +ex4) >= 1:
				e = 1
			else:
				e = 0

			if e != Trainingsdaten[i][5]:
				if Trainingsdaten[i][5] == 1 and e == 0:
					regel[0] = regel[0] + alpha*Trainingsdaten[i][0]
					regel[1] = regel[1] + alpha*Trainingsdaten[i][1]
					regel[2] = regel[2] + alpha*Trainingsdaten[i][2]
					regel[3] = regel[3] + alpha*Trainingsdaten[i][3]
					regel[4] = regel[4] + alpha*Trainingsdaten[i][4]

				if Trainingsdaten[i][5] == 0 and e == 1:
					regel[0] = regel[0] - alpha*Trainingsdaten[i][0]
					regel[1] = regel[1] - alpha*Trainingsdaten[i][1]
					regel[2] = regel[2] - alpha*Trainingsdaten[i][2]
					regel[3] = regel[3] - alpha*Trainingsdaten[i][3]
					regel[4] = regel[4] - alpha*Trainingsdaten[i][4]


def groessteInListe(liste):
	g = liste[0]
	for i in liste:
		if i > g:
			g = i
	return g


def peeceptron(aufgabe):
	ue = groessteInListe(regel)
	if aufgabe[0] == 1 :
	 	esf = (regel[1])* 1 
	 	ue += -1
	else: 
	 	esf = (regel[1])* -1
	 	ue += 1
	if aufgabe[1] == 1 : 
		ex1 = (regel[2])* 1 
		ue += -1
	else:
		ex1 = (regel[2])* -1
		ue += 1
	if aufgabe[2] == 1 : 
		ex2 = (regel[3])* 1 
		ue += -1
	else: 
		ex2 = (regel[3])* -1
		ue += 1
	if aufgabe[3] == 1 : 
		ex3 = (regel[4])* 1 
		ue += -1
	else: 
		ex3 = (regel[4])* -1
		ue += 1

	if groessteInListe(regel)-4 == ue:
		return 0

	if (esf + ex1 + ex2 +ex3) >= ue:
		return 1
	else:
		return 0

training()
print(regel)
print(peeceptron([1, 1, 1, 1]))
