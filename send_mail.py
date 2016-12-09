import Mail
import datetime

today = datetime.date.today().isoformat()
Mail.send("renzhentaxibaerde@csc271.adelphi.edu", today, today+".xlsx")
