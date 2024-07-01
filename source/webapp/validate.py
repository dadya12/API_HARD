def article_validate(article):
    errors = {}
    if not article.title:
        errors["title"] = "Название обязательное поле"
    elif len(article.title) > 3:
        errors["title"] = "Длина поля не может быть больше чем 50"

    if not article.content:
        errors["content"] = "Контент обязательное поле"

    if not article.author:
        errors["author"] = "Автор обязательное поле"

    return errors