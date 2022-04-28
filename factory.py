import dao as dao


class Factory:
    dao = dao.DAOFactory()
    dao = dao.get_dao()

    def get_all_anime(self):
        anime_list = []
        for anime in self.dao.get_all_anime():
            anime_list.append(anime)
        return anime_list

    def get_all_studios(self):
        studio_list = []
        for studio in self.dao.get_all_studios():
            studio_list.append(studio)
        return studio_list

    def get_anime_by_id(self, anime_id):
        return self.dao.get_anime_by_id(anime_id)

    def get_studio_by_id(self, studio_id):
        return self.dao.get_studio_by_id(studio_id)

    def commit(self):
        self.dao.commit()

    def update_anime(self, anime, id, name, studio_id, episodes):
        self.dao.update_anime(anime, id, name, studio_id, episodes)

    def update_studio(self, studio, id, name):
        self.dao.update_studio(studio, id, name)

    def add_anime(self, name, studio_id, episodes):
        self.dao.add_anime(name, studio_id, episodes)

    def add_studio(self, name):
        self.dao.add_studio(name)

    def delete_anime(self, anime_id):
        self.dao.delete_anime(anime_id)

    def delete_studio(self, studio_id):
        self.dao.delete_studio(studio_id)