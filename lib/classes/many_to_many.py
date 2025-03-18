class Article:
    all=[]
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5<=len(title)<=50:
            if  hasattr(self, "_title"):
                print("has title")
            else:
                self._title=title
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author=author
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine=magazine
        
        
class Author:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name)>0:
            if  hasattr(self, "_name"):
                print("has name")
            else:
                self._name=name

    def articles(self):
        return [article for article in Article.all if article.author==self]

    def magazines(self):
        return list(set(article.magazine for article in Article.all if article.author==self))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        articles=self.articles()
        if len(articles)==0:
            return None
        else:
            return list(set(article.magazine.category for article in articles))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2<=len(name)<=16:
            self._name=name
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category)>0:
            self._category=category

    def articles(self):
        return [article for article in Article.all if article.magazine==self]

    def contributors(self):
        return list(set(article.author for article in Article.all if article.magazine==self))

    def article_titles(self):
        articles=self.articles()
        if len(articles)==0:
            return None
        else:
            return [article.title for article in articles]

    def contributing_authors(self):
        count={}
        articles=self.articles()
        for article in articles:
            if article.author in count:
                count[article.author]+=1
            else:
                count[article.author]=1
        
        authorttwo=[author for author, num in count.items() if num >=2]
        if len(authorttwo)==0:
            return None
        else:
            return authorttwo
