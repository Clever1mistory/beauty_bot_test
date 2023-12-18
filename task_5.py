from fastapi import FastAPI

app = FastAPI()

""" При поступлении входящего веб-хука на эндпоинт "/Datalore", будет вызвана функция process_webhook, 
    которая будет проверять поле 'function' в переданном JSON и выполнять соответствующие действия 
    в зависимости от значения этого поля. """


@app.post("/Datalore")
async def process_webhook(webhook: dict):
    function = webhook.get("function")

    if function == "function1":
        return {"message": "Выполняется функция 1"}
    elif function == "function2":
        return {"message": "Выполняется функция 2"}
    else:
        return {"message": "Неизвестная функция"}

