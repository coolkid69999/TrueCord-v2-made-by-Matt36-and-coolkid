class plugin():
    def __init__(self, name, source, developer, is_cog=True):
        self.source = source
        self.name = name
        self.developer = developer
        self.source = source
        self.is_cog = is_cog
        self.reveiws = []
        self.stars = self.get_stars(self.reveiws)
    
    def get_stars(reveiws):
        stars = 0
        for reveiw in reveiws:
            stars += reveiw.stars
        return stars / len(reveiws)
    

    def reveiw(self, title, description, stars):
        self.reveiws.append()

class Review():
    def __init__(self, title, description, stars):
        self.title = title
        self.description = description
        self.stars = stars
    
        if self.stars > 5:
            raise StarException

class StarException(Exception):
    pass


