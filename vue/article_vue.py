from vue.common import Common


class ArticleVue:
    """
    Article Vue
    Articles interface features
    """

    def __init__(self, article_controller):
        self._common = Common()
        self._article_controller = article_controller

    def add_article(self, article_type):
        # Show subscription formular
        data = {}
        print("Store user Subscription")
        print(article_type)
        print()
        data['name'] = self._common.ask_namearticle()
        data['description'] = self._common.ask_description()
        data['price'] = self._common.ask_price()
        return self._article_controller.create_article(data)

    def show_article(self, article: dict):
        print("Article information: ")
        print(article['name'].capitalize())
        print("description:", article['description'])

    def error_message(self, message: str):
        print("/!\\ %s" % message.upper())

    def succes_message(self, message: str = ""):
        print("Operation succeeded: %s" % message)

    def show_articles(self):

        articles = self._article_controller.list_articles()

        print("Members: ")
        for article in articles:
            print("* %s %s (%s)" % (article['name'].capitalize(),
                                    article['description'],
                                    article['price']))

    def search_article(self):
        name = self._common.ask_name('name')
        article = self._article_controller.search_article(name)
        return article

    def update_article(self):
        article = self.search_article()
        data = {}
        print("Update Article")
        print()
        data['name'] = self._common.ask_namearticle()
        data['description'] = self._common.ask_description(default=article['description'])
        data['price'] = self._common.ask_price(default=article['price'])
        print()
        return self._article_controller.update_member(article['id'], data)

    def delete_article(self):
        article = self.search_article()
        self._article_controller.delete_article(article['id'])
        self.succes_message()
