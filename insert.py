from create import session, Studio, Anime

with open('data/studio.csv', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.split(',')
        studio = Studio(name=line[1])
        session.add(studio)
with open('data/anime.csv', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.split(',')
        anime = Anime(name=line[1], studio_id=int(line[2]), ep=int(line[3]))
        session.add(anime)
session.commit()
