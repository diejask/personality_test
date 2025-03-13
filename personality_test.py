''' This program is a personality test   '''
# authors: Sarah B., Diedan.S, Dieja S.
# date: 10.03.2025
# source: https://karrierebibel.de/persoenlichkeitstest/


### Initialization ###

number_of_questions = 10

answer = 0
macher_score = 0
zurueckhaltender_score = 0
traeumer_score = 0
realist_score = 0

number_of_questions = 10

macher_percentage = 0
zurueckhaltender_percentage = 0
traeumer_percentage = 0
realist_percentage = 0


#### Questions ####

## Question 1 ##
def question1():
 
 print("1. Sie treffen fremde Menschen: Wie verhalten Sie sich?\n")
 print(" Es fällt mir schwer, selber auf andere zuzugehen. (B)\n",
      "Ich suche jemanden, den ich kenne und plaudere mich warm. (C)\n",
      "Ich steige in ein Gespräch ein und finde sofort Anschluss. (A)\n",
     "Ich gehe unverkrampft auf fremde Menschen zu. (D)\n\n")


## Question 2 ## 
def question2():
 
 print("2. Wie gehen Sie mit Rückschlägen um?\n")
 print(" Aufstehen, Krone richten, weitergehen. (A)\n", 
      "Ich brauche länger, um darüber hinwegzukommen. (B)\n",
      "Das kommt darauf an, aber ich habe gute Freunde, die helfen. (C)\n",
      "Tiefpunkte gehören zum Leben. Wichtig ist, was man daraus lernt. (D)\n\n")

## Question 3 ##
def question3():
 
 print("3. Erwischen Sie sich häufiger beim Tagträumen?\n")
 print(" Nein, für so etwas habe ich keine Zeit! (D)\n", 
      "Ja – und stelle fest, wie viel Zeit dabei vergeht. (B)\n",
      "Es kommt vor. Dabei habe ich oft die besten Ideen. (C)\n",
      "Ich träume nicht, ich setze meine Ziele um! (A)\n\n")

## Question 4 ##
def question4(): 
 
 print("4. Ständig klingeln E-Mail-Postfach und Telefon: Wie reagieren Sie?")
 print(" Ich versuche, schnell auf alle Anfragen zu reagieren. (B)\n",
    "Ich überfliege die Mails und leite Telefonate an Kollegen weiter. (A)\n",
    "Ich arbeite konzentriert weiter und setze alles der Reihe nach um. (D)\n",
    "Ich nehme es, wie es kommt: erst Telefon, dann Mail. (C)\n\n")

## Question 5 ##
def question5():
 
 print("5. Haben Sie das Gefühl, sich für Ansichten rechtfertigen zu müssen?\n")
 print(" Nein. Wenn jemand ein Problem hat, soll er mich ansprechen. (A)\n",
      "Ich werde manchmal missverstanden und möchte das klären. (B)\n",
      "Das kann vorkommen, ich muss mich aber nicht rechtfertigen. (D)\n",
      "Man kann man mit mir über alles diskutieren. (C)\n\n")

## Question 6 ##
def question6():
 
 print("6. Wie gehen Sie mit Druck um?\n")
 print(" Irgendwie weiß ich mir immer zu helfen. (C)\n",
      "Kein Ding, ich behalte stets einen kühlen Kopf. (A)\n",
      "Das macht mich immer fix und fertig. (B)\n",
      "Von Zeit zu Zeit muss man da durch. (D)\n\n")

## Question 7 ## 
def question7():
 print("7. Wie gehen Sie mit Risiken und Unsicherheiten um?\n")
 print(" Meine Devise: „No risk, no fun!“ (A)\n",
      "Wenn man Risiken abwägt, sind es keine mehr. (D)\n",
      "Leichtsinniges Verhalten vermeide ich. (B)\n",
      "Unterschiedlich. Manche Situation war schon sehr riskant. (C)\n\n")

## Question 8 ##

def question8():
 print("8. Wie halten Sie es mit der Pünktlichkeit?\n")
 print(" Ich bin 30 Minuten vorher da. Dann hab ich genug Puffer. (B)\n",
      "10 Minuten reichen, um mir einen Überblick zu verschaffen. (D)\n",
      "Ich bin immer pünktlich. (A)\n",
      "Es kommt vor, dass ich mich verspäte. (C)\n\n")

## Question 9 ##

def question9():
 print("9. Wie überzeugt sind Sie von sich?\n")
 print(" Ich kenne meine Stärken und Schwächen. (D)\n",
      "Ich bin sehr gut in dem, was ich tue. (A)\n", 
      "Ich denke, ich muss noch viel lernen. (B)\n",
      "Ich komme gut an, kann also nicht verkehrt sein. (C)\n\n")

## Question 10 ##
def question10():
 print("10. Im Job wird hitzig gestritten. Was tun Sie?\n")
 print(" Ich trenne die Streithähne – bringt doch nichts! (A)\n",
      "Ich lenke mit etwas Humor vom Streit ab. (C)\n",
      "Ich erkläre den Streitern, dass sie am Thema vorbei diskutieren. (D)\n",
      "Ich suche Gemeinsamkeiten und vermittle. (B)\n\n")
 
question = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]



### Calculation ###

while i < len(question):
     question[i]()
     i += 1
     answer = input("Wählen Sie bitte A, B, C oder D: ")
     print("\n\n")
     
#The answer is converted to lowercase and compared with the letters a, b, c, d, 
#and a point is added to the corresponding personality based on the answer.
     if "a" == answer.lower() :
          macher_score += 1
     elif "b" == answer.lower() :
          zurueckhaltender_score += 1
     elif "c" == answer.lower() :
          traeumer_score += 1
     elif "d" == answer.lower() :
          realist_score += 1
     else: 
       print("\nSie haben ein ungültiges Zeichen eingegeben. Bitte geben sie A, B, C oder D ein. \n")      
       i -= 1                 # if user inputs invalid sign the question gets repeated

#Conversion of scores into percentage values
macher_percentage = (macher_score / number_of_questions) * 100
zurueckhaltender_percentage = (zurueckhaltender_score / number_of_questions) * 100
traeumer_percentage = (traeumer_score / number_of_questions) * 100
realist_percentage = (realist_score / number_of_questions) * 100