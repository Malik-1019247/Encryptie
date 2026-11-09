# Encryptie (Week 5 Opdracht)

Ik heb een Python applicatie gemaakt waarmee je tekst kunt encrypten en decrypten. Ik heb een eenvoudige GUI gemaakt met Tkinter en de encryptie gedaan met de Python library “cryptography”.

## Installeer instructies
- Clone deze repository
- voer dit commando in de terminal uit: `pip install -r requirements.txt`
- Start de app: `python main.py`

## Hoe werkt de encryptie-app?
- Vul je tekst en wachtwoord in.
- Klik op Versleutelen.
- Kopieer de versleutelde tekst en plak het in het invoerveld.
- Zorg ervoor dat je hetzelfde wachtwoord invoert en klik dan op "ontsleutelen".

Als je niks hebt ingevoerd krijg je een melding en ook als je een verkeerd wachtwoord of sleutel meegeeft.

## Keuze symmetrische en asymmetrische encryptie
Bij symmetrische encryptie wordt dezelfde geheime sleutel gebruikt om gegevens te versleutelen en weer te ontsleutelen. Een voorbeeld hiervan is AES. Symmetrische encryptie werkt snel en kan gebruikt worden om bijvoorbeeld teksten en bestanden te beveiligen. Wel moeten beide partijen toegang hebben tot dezelfde geheime sleutel. (What Is Symmetric Encryption?, n.d.)

Bij asymmetrische encryptie werkt het anders. Hierbij worden twee sleutels gebruikt: een publieke sleutel en een privésleutel. De publieke sleutel kan iedereen gebruiken, maar de privésleutel moet geheim blijven. Deze methode is handig om bijvoorbeeld veilig gegevens uit te wisselen, maar is minder snel wanneer je een groot aantal gegevens wilt versleutelen. (What Is Asymmetric Encryption?, n.d.)

Voor mijn opdracht heb ik gekozen voor symmetrische encryptie. De gebruiker moet namelijk zelf een wachtwoord kunnen invoeren om een tekst te versleutelen en deze later met hetzelfde wachtwoord weer te ontsleutelen.

## Waarom kies ik voor AES-256-GCM?
Voor het versleutelen gebruik ik AES-256-GCM. Dit heb ik gedaan met de AESGCM klasse uit de Python-library “cryptography”. AES is symmetrische encryptie en gebruikt een sleutel van 256 bits. De GCM-modus zorgt ervoor dat de gegevens versleuteld worden en gecontroleerd worden op of ze zijn aangepast. Als iemand de versleutelde tekst dus aanpast of een verkeerd wachtwoord invoert, werkt de ontsleuteling niet. (The cryptography developers, n.d.)

## Sleutelbeheer: wachtwoord, Scrypt, salt en nonce
De gebruiker voert eerst een wachtwoord in. Daarna gebruikt het programma Scrypt om het wachtwoord om te zetten in een sleutel van 32 bytes. Scrypt kost meer rekenkracht en geheugen waardoor het moeilijker is om veel verschillende wachtwoorden te proberen. Dit helpt tegen een poging tot brute force. (The cryptography developers, n.d.)

Elke keer als de tekst wordt versleuteld, maakt het programma een random salt van 16 bytes en een nonce van 12 bytes aan. Dan wordt de salt gebruikt bij Scrypt en de nonce bij AES-GCM.

Bij Scrypt gebruik ik als instelling n=2**14, r=8 en p=1. De salt zorgt ervoor dat hetzelfde wachtwoord niet elke keer dezelfde sleutel teruggeeft. De nonce zorgt ervoor dat er bij elke versleuteling een andere waarde wordt gebruikt. Bij AES-GCM is het belangrijk dat dezelfde nonce nooit opnieuw met dezelfde sleutel wordt gebruikt.

Als de tekst is versleuteld wordt de salt, nonce, versleutelde tekst en authenticatie tag achter elkaar gezet. Hiervan wordt een Base64 gemaakt. De salt en nonce zijn niet geheim maar het wachtwoord moet dat wel zijn. Daarom slaat het programma het wachtwoord niet op. (Key Management Cheat Sheet, n.d.)

Als gebruiker moet je er wel rekening mee houden dat je de tekst niet meer kan ontsleutelen als je het wachtwoord niet meer weet. Iemand die je versleutelde tekst heeft, zou ook je wachtwoord kunnen raden en het dan weer ontsleutelen. 

Zou je willen dat iemand jou tekst kan ontsleutelen? Dan zou je het wachtwoord moeten delen. Hiervoor heb ik zelf nog niks ontwikkeld. Je zou het dus moeten doen op een veilige manier.
## Kerckhoffs’ Principe
Volgens Kerckhoffs’ principe moet een cryptografisch systeem altijd veilig blijven. Zelfs al zou je weten hoe het werkt en de broncode hebben. Wel moet de geheime sleutel altijd geheim blijven.  Dit heb ik toegepast in mijn code. De beveiliging hangt vooral af van het wachtwoord en de encryptiemethode die wordt gebruikt. Je zou door te weten hoe de broncode werkt niet een versleutelde tekst kunnen ontsleutelen. Dit zou praktisch alleen mogelijk kunnen zijn als je het wachtwoord weet. Daarom moet de gebruiker er wel voor zorgen dat het een sterk wachtwoord is, zodat het niet makkelijk te raden is. (Kerckhoffs' Principle, n.d.)


## Bronnen

- The cryptography developers. (n.d.). Authenticated encryption — Cryptography 51.0.0-dev1 documentation. Retrieved November 1, 2026, from https://cryptography.io/en/latest/hazmat/primitives/aead/
- The cryptography developers. (n.d.). Key derivation functions. Cryptography. https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/
- Kerckhoffs' principle. (n.d.). Wikipedia. Retrieved November 1, 2026, from https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle
- Key Management Cheat Sheet. (n.d.). OWASP Cheat Sheet Series. Retrieved November 3, 2026, from https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html
- What is Asymmetric Encryption? (n.d.). IBM. Retrieved November 2, 2026, from https://www.ibm.com/think/topics/asymmetric-encryption
- What Is Symmetric Encryption? (n.d.). IBM. Retrieved November 2, 2026, from https://www.ibm.com/think/topics/symmetric-encryption
