from tomlkit import load, array, toml_file, _types

class UserConf:
    def __init__(self, path) -> None:
        self._conf = toml_file.TOMLFile(path)
        self._doc = self._conf.read()

    def get(self, id: str):
        ret = self._doc[id].unwrap()
        if type(ret) == list:
            try:
                ret = [tuple(row) for row in ret]
            except:
                pass
        return ret

    def set(self, id: str, data):
        self._doc[id] = data
        
        return self._doc[id] if self._conf.write(self._doc) == None else None

    def item_set(self, id: str, item_data: list|str, index: int=None) -> list:
        a: list = self.get(id)
        if index == None:
            a.append(item_data)
        else:
            a[index] = item_data
        
        ret = self.set(id, a)
        try:
            ret = [tuple(row) for row in ret]
        except:
            pass
        return ret
    
    def item_pop(self, id: str, index: int) -> list:
        a: list = self.get(id)
        a.pop(index)
        ret = self.set(id, a)
        try:
            ret = [tuple(row) for row in ret]
        except:
            pass
        return ret    

userconf = UserConf('./user-config.toml')
locations = userconf.get('locations')

print(userconf.get('title'))
new_title = userconf.set('title', 'TOML Test Example')
print(userconf.get('title'))
accts = userconf.get('accts')
print(accts, accts[0])
# accts = userconf.item_set('accts', [2, 2, 4])
# print(accts, accts[0])
# accts = userconf.item_pop('accts', -1)
# print(accts, accts[0])
# print(locations, locations[0])
# locations = userconf.item_set('locations', 6899)
print(locations, locations[0])
# locations = userconf.item_pop('locations', -1)
# print(locations, locations[0])


