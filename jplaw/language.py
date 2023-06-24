class Language():
    id: int
    code: str
    name: str
    def __init__(self, language_id:int, code:str, name:str):
        self.id = language_id
        self.code = code
        self.name = name