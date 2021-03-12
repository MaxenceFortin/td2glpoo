
import sys
from vue.member_vue import MemberVue
from vue.article_vue import ArticleVue
from exceptions import ResourceNotFound, Error, InvalidData


class AdminVue(MemberVue, ArticleVue):
    """
    Admin Vue
    Admin specific interfaces
    """

    def __init__(self, member_controller):
        super().__init__(member_controller)

    def help(self, commands):
        print()
        for command, description in commands.items():
            print("  * %s: '%s'" % (command, description))
        print()

    def ask_command(self, commands):

        command = input('command > ').lower().strip()
        while command not in commands.keys():
            print("Unknown command")
            command = input('command >').lower().strip()

        return command

    def admin_shell(self):

        commands = {
            "exit": "Quit the Shell",
            "add": "Add store member",
            "list": "List association members",
            "search": "Show member profile",
            "delete": "Delete a member",
            "update": "Update a member",
            "addArticle": "Add store article",
            "listArticle": "List association articles",
            "searchArticle": "Show article informations",
            "deleteArticle": "Delete an article",
            "updateArticle": "Update a article",
            "help": "Show this help"
        }

        self.help(commands)

        while True:
            try:
                command = self.ask_command(commands)
                if command == 'exit':
                    # Exit loop
                    break
                elif command == 'add':
                    user_type = 'unknown'
                    member = self.add_member(user_type)
                    self.show_member(member)
                elif command == 'list':
                    self.show_members()
                elif command == 'search':
                    member = self.search_member()
                    self.show_member(member)
                elif command == 'delete':
                    self.delete_member()
                elif command == 'update':
                    member = self.update_member()
                    self.show_member(member)
                elif command == 'help':
                    self.help(commands)
                elif command == 'addArticle':
                    article = self.add_article()
                    self.show_article(article)
                elif command == 'listArticle':
                    self.show_articles()
                elif command == 'searchArticle':
                    article = self.search_article()
                    self.show_member(article)
                elif command == 'deleteArticle':
                    self.delete_article()
                elif command == 'updateArticle':
                    article = self.update_article()
                    self.show_article(article)
                else:
                    print("Unknown command")
            except ResourceNotFound:
                self.error_message("Member/Article not found")
            except InvalidData as e:
                self.error_message(str(e))
            except Error as e:
                self.error_message("An error occurred (%s)" % str(e))
