class Movie:
    def __init__(self, id: int, title: str, year: int, description: str, rating: float,
                 ranking: int, review: str, img_url: str):
        self.id = id
        self.title = title
        self.year = year
        self.description = description
        self.rating = rating
        self.ranking = ranking
        self.review = review
        self.img_url = img_url
