# pypolisen
> Python wrapper for `https://polisen.se/aktuellt/polisens-nyheter/`

```
Author     : Sebastian Karlsson <sebbekarlsson97@gmail.com>
Contributor: Jonas Björk <jonas.bjork@gmail.com>
Git repo   : https://github.com/sebbekarlsson/pypolisen
```

## Usage

### Fetching events / police notices

Use the `get_events()` method in `Client` to get the events. 
You can use three arguments to the method:

- `eventlocation` list that contains the city/cities you want events from. Could be:
`["Helsingborg"]`, `["Helsingorg", "Stockholm"]`. If no event location is set it will 
return events for all cities.
 
- `eventtype` list that contains the event type (see below for valid event types). 
Could be: `["Larm Inbrott", "Rån"]`. If no event type is set it will return events 
of all types. 

- `datetime` a string with the year, month or day you want events from. Could be: 
`2020`, `2020-08` and `2020-08-01`. If no date is set it will return all events for 
all dates available.

Example code:

```python
c = Client()
print(c.get_events(eventlocation=["Helsingborg"],
                eventtype=["Rån"],
                datetime="2020"))
```

### It can also be used through the command line

> Use the command `polisen`:

```bash
Usage: polisen <method> [--location city] [--type eventtype] [--date YYYY-MM-DD|YYYY-MM|YYYY]
Available methods: [events]
```

Example usage:

```bash
$ python bin.py events --location helsingborg --type Rattfylleri --date 2020-04-14
```

## Installing

To install either clone down the repository and run:

```bash
$ python setup.py install
```

Or using `pip`:

```bash
$ pip install pypolisen
```

## Event types

- Alkohollagen
- Anträffad död
- Anträffat gods
- Arbetsplatsolycka
- Bedrägeri
- Bombhot
- Brand
- Brand automatlarm
- Bråk
- Detonation
- Djur skadat/omhändertaget
- Ekobrott
- Farligt föremål, misstänkt
- Fjällräddning
- Fylleri/LOB
- Förfalskningsbrott
- Försvunnen person
- Gränskontroll
- HäleriInbrott
- Inbrott, försök
- Knivlagen
- Kontroll person/fordon
- Lagen om hundar och katter
- Larm Inbrott
- Larm Överfall
- Miljöbrott
- Missbruk av urkund
- Misshandel
- Misshandel, grov
- Mord/dråp
- Mord/dråp, försök
- Motorfordon, anträffat stulet
- Motorfordon, stöld
- Narkotikabrott
- Naturkatastrof
- Ofog barn/ungdom
- Ofredande/förargelse
- Olaga frihetsberövande
- Olaga hot
- Olaga intrång/hemfridsbrott
- Olovlig körning
- Ordningslagen
- Polisinsats/kommendering
- Rattfylleri
- Rån
- Rån väpnat
- Rån övrigt
- Rån, försök
- Räddningsinsats
- Sammanfattning dag
- Sammanfattning dygn
- Sammanfattning eftermiddag
- Sammanfattning förmiddag
- Sammanfattning helg
- Sammanfattning kväll
- Sammanfattning kväll och natt
- Sammanfattning natt
- Sammanfattning vecka
- Sedlighetsbrott
- Sjukdom/olycksfall
- Sjölagen
- Skadegörelse
- Skottlossning
- Skottlossning, misstänkt
- Spridning smittsamma kemikalier
- Stöld
- Stöld, försök
- Stöld, ringa
- Stöld/inbrott
- Tillfälligt obemannat
- Trafikbrott
- Trafikhinder
- Trafikkontroll
- Trafikolycka
- Trafikolycka, personskada
- Trafikolycka, singel
- Trafikolycka, smitning från
- Trafikolycka, vilt
- Uppdatering
- Utlänningslagen
- Vapenlagen
- Varningslarm/haveri
- Våld/hot mot tjänsteman
- Våldtäkt
- Våldtäkt, försök
- Vållande till kroppsskada
